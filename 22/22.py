from copy import deepcopy


def check_types(*args):
    for arg, cls in args:
        if not isinstance(arg, cls):
            raise TypeError(arg)


class Boss:
    def __init__(self, hp, damage):
        self.hp = hp
        self.damage = damage
        check_types((self.hp, int), (self.damage, int))

    def __eq__(self, other):
        if not isinstance(other, Boss):
            return False
        return self.hp == other.hp and self.damage == other.damage

    def __str__(self):
        return ' '.join(["Boss",
                         "HP:", str(self.hp),
                         "Damage:", str(self.damage)])

    def __repr__(self):
        return "Boss(" + ', '.join(["hp=" + repr(self.hp),
                                    "damage=" + repr(self.damage)]) + ')'


class Player:
    def __init__(self, hp=50, mana=500):
        self.hp = hp
        self.mana = mana
        check_types((self.hp, int), (self.mana, int))

    def __eq__(self, other):
        if not isinstance(other, Player):
            return False
        return self.hp == other.hp and self.mana == other.mana

    def __str__(self):
        return ' '.join(["Player",
                         "HP:", str(self.hp),
                         "Mana:", str(self.mana)])

    def __repr__(self):
        return "Player(" + ', '.join(["hp=" + repr(self.hp),
                                      "mana=" + repr(self.mana)]) + ')'


class Spell:
    def __init__(self, name, cost):
        check_types((name, str), (cost, int))
        self.name = name
        self.cost = cost

    def __eq__(self, other):
        if not isinstance(other, Spell):
            return False
        return self.name == other.name

    def __str__(self):
        return " ".join([self.name,
                         "Cost:", str(self.cost)])

    def __repr__(self):
        return "Spell(" + ', '.join(["name=" + repr(self.name),
                                     "cost=" + repr(self.cost)]) + ')'


class EffectSpell(Spell):
    def __init__(self, spell):
        super().__init__(spell["name"], spell["cost"])
        self.timer = spell["timer"]
        self.damage = spell["damage"] if "damage" in spell else 0
        self.armor = spell["armor"] if "armor" in spell else 0
        self.mana = spell["mana"] if "mana" in spell else 0
        check_types((self.timer, int), (self.damage, int), (self.armor, int), (self.mana, int))

    def __str__(self):
        return ' '.join([super().__str__,
                         "Timer:", str(self.timer),
                         "Damage:", str(self.damage),
                         "Armor:", str(self.armor),
                         "Mana:", str(self.mana)])

    def __repr__(self):
        return "EffectSpell({" + ', '.join(("name=" + repr(self.name),
                                            "cost=" + repr(self.cost),
                                            "timer=" + repr(self.timer),
                                            "damage=" + repr(self.damage),
                                            "armor=" + repr(self.armor),
                                            "mana=" + repr(self.mana))) + '})'

    def stats(self):
        return self.damage, self.armor, self.mana


class InstantSpell(Spell):
    def __init__(self, spell):
        super().__init__(spell["name"], spell["cost"])
        self.damage = spell["damage"] if "damage" in spell else 0
        self.heal = spell["heal"] if "heal" in spell else 0
        check_types((self.damage, int), (self.heal, int))

    def __str__(self):
        return ' '.join([super().__str__,
                         "Damage:", str(self.damage),
                         "Heal:", str(self.heal)])

    def __repr__(self):
        return "InstantSpell({" + ', '.join(["name=" + repr(self.name),
                                             "cost=" + repr(self.cost),
                                             "damage=" + repr(self.damage),
                                             "heal=" + repr(self.heal)]) + '})'

    def stats(self):
        return self.damage, self.heal


class Stage:
    def __init__(self, player, boss, spells, spent, playerturn, part2):
        check_types((player, Player), (boss, Boss), (spells, dict), (spent, int), (playerturn, bool), (part2, bool))
        self.player = player
        self.boss = boss
        self.spells = spells
        self.spent = spent
        self.playerturn = playerturn
        self.turn = 0
        self.part2 = part2

    def __lt__(self, other):
        if not isinstance(other, Stage):
            return False
        return self.spent < other.spent

    def __eq__(self, other):
        if not isinstance(other, Stage):
            return False
        player = self.player == other.player
        boss = self.boss == other.boss
        spells = self.spells == other.spells
        spent = self.spent == other.spent
        playerturn = self.playerturn == other.playerturn
        turn = self.turn == other.turn
        return all([player, boss, spells, spent, playerturn, turn])

    def __str__(self):
        return ' '.join(("Player:", str(self.player),
                         "Boss: ", str(self.boss),
                         "Spells: ", str(self.spells),
                         "Spent: ", str(self.spent),
                         "Player's turn" if self.playerturn else "Boss's turn"))

    def __repr__(self):
        return "Stage(" + ', '.join(("player=" + repr(self.player),
                                     "boss=" + repr(self.boss),
                                     "spells=" + repr(self.spells),
                                     "spent=" + repr(self.spent),
                                     "playerturn=" + repr(self.playerturn))) + ')'

    def battle(self, spell=None):
        if self.part2 and self.playerturn:
            self.player.hp -= 1
            if self.player.hp == 0:
                return
        self.turn += 1
        damage, armor, mana = self.effects()
        self.player.mana += mana
        self.boss.hp -= damage
        if self.over():
            return
        if self.playerturn:
            if not spell:
                raise Exception("No spell passed when player's turn!")
            self.spent += spell.cost
            self.player.mana -= spell.cost
            if isinstance(spell, InstantSpell):
                damage, heal = spell.stats()
                self.player.hp += heal
                self.boss.hp -= damage
            else:
                self.spells[spell.name] = spell
        else:
            damage = self.boss.damage - armor
            if damage < 1:
                damage = 1
            self.player.hp -= damage
        self.playerturn = not self.playerturn

    def over(self):
        return self.player.hp <= 0 or self.boss.hp <= 0

    def won(self):
        return self.boss.hp <= 0 < self.player.hp

    def lost(self):
        return self.player.hp <= 0 < self.boss.hp

    def effects(self):
        ret = tuple(map(sum, zip(*[spell.stats() for spell in self.spells.values()])))
        if ret == tuple():
            return 0, 0, 0
        for spell in self.spells.values():
            spell.timer -= 1
        dead = [name for name, spell in self.spells.items() if spell.timer == 0]
        for name in dead:
            del self.spells[name]
        return ret


def process_input():
    with open("input.txt") as file:
        data = file.read().splitlines()
    boss = {}
    for line in data:
        line = line.split(": ")
        boss[line[0]] = int(line[1])
    boss["part2"] = False
    return boss


def evalp1(data):
    player = Player()
    boss = Boss(hp=data["Hit Points"], damage=data["Damage"])
    spells = (InstantSpell({"name": "Magic Missile", "cost": 53, "damage": 4}),
              InstantSpell({"name": "Drain", "cost": 73, "damage": 2, "heal": 2}),
              EffectSpell({"name": "Shield", "cost": 113, "timer": 6, "armor": 7}),
              EffectSpell({"name": "Poison", "cost": 173, "timer": 6, "damage": 3}),
              EffectSpell({"name": "Recharge", "cost": 229, "timer": 5, "mana": 101}))
    past_stages = []
    current_stages = [Stage(player, boss, dict(), 0, True, data["part2"])]
    next_stages = []
    won_battles = []
    # lost_battles = []
    spent = 1000

    def run_battle(least, battle, cast=None):
        battle.battle(cast)

        if battle.won():
            if least > battle.spent:
                least = battle.spent
            if battle not in won_battles:
                won_battles.append(battle)
        # elif battle.lost():
        #     if battle not in lost_battles:
        #         lost_battles.append(battle)
        elif not battle.over() and battle.spent < least:
            next_stages.append(battle)
        return least

    while True:
        for stage in current_stages:
            if stage.playerturn:
                for spell in spells:
                    if (spell.name in stage.spells and stage.spells[spell.name].timer > 1) or spell.cost > stage.player.mana:
                        continue
                    spent = run_battle(spent, deepcopy(stage), deepcopy(spell))
            else:
                spent = run_battle(spent, deepcopy(stage))
        if len(next_stages) == 0:
            print(spent == sorted(won_battles, key=lambda battle: battle.spent)[0].spent)
            break
        past_stages += current_stages
        current_stages = next_stages
        next_stages = []

    return spent


def evalp2(data):
    data["part2"] = True
    return evalp1(data)


def main():
    data = process_input()
    part1 = evalp1(data)
    print("Part 1:")
    print(part1)
    print("Part 2:")
    print(evalp2(data))

if __name__ == "__main__":
    main()
