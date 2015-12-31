from copy import deepcopy

inp = """Hit Points: 55
Damage: 8"""


def battle(stage, playerturn, spell=None):
    if playerturn and stage["boss"]["part2"]:
        stage["player"]["hp"] -= 1
        if stage["player"]["hp"] == 0:
            return stage
    start = {"armor": 0, "damage": 0, "mana": 0}
    done = []
    for effect in stage["effects"].values():
        for key in start.keys():
            if key in effect:
                start[key] += effect[key]
        effect["timer"] -= 1
        if effect["timer"] == 0:
            done.append(effect["name"])
    for name in done:
        del stage["effects"][name]
    stage["player"]["mana"] += start["mana"]
    stage["boss"]["hp"] -= start["damage"]
    if stage["boss"]["hp"] <= 0:
        return stage

    if playerturn:
        if spell is None:
            raise Exception("No spell given when player's turn")
        stage["spent"] += spell["cost"]
        stage["player"]["mana"] -= spell["cost"]
        if "timer" in spell:
            stage["effects"][spell["name"]] = spell
        else:
            damage = spell["damage"] if "damage" in spell else 0
            heal = spell["heal"] if "heal" in spell else 0
            stage["player"]["hp"] += heal
            stage["boss"]["hp"] -= damage

    else:
        damage = stage["boss"]["damage"] - start["armor"]
        if damage < 1:
            damage = 1
        stage["player"]["hp"] -= damage

    return stage


def process_input():
    with open("input.txt") as file:
        data = file.read().splitlines()
    data = [line.split(": ") for line in data]
    data = dict([(line[0], int(line[1])) for line in data])
    boss = dict()
    boss["hp"] = data["Hit Points"]
    boss["damage"] = data["Damage"]
    boss["part2"] = False
    return boss


def evalp1(data):
    spells = {"Magic Missile": {"name": "Magic Missile", "cost": 53, "damage": 4},
              "Drain":         {"name": "Drain",         "cost": 73, "damage": 2, "heal": 2},
              "Shield":        {"name": "Shield",        "cost": 113, "timer": 6, "armor": 7},
              "Poison":        {"name": "Poison",        "cost": 173, "timer": 6, "damage": 3},
              "Recharge":      {"name": "Recharge",      "cost": 229, "timer": 5, "mana": 101}}

    boss = data
    player = {"hp": 50, "mana": 500}
    past_scenarios = []
    current_scenarios = [{"boss": boss, "player": player, "effects": {}, "spent": 0}]
    next_scenarios = []
    leastspent = None
    playerturn = True

    while True:
        for scenario in current_scenarios:
            if playerturn:
                for spell in spells.values():
                    in_effects = spell["name"] in scenario["effects"] and scenario["effects"][spell["name"]]["timer"] > 1
                    cant_cast = spell["cost"] > scenario["player"]["mana"]
                    if in_effects or cant_cast:
                        continue
                    outcome = battle(deepcopy(scenario), playerturn, deepcopy(spell))
                    if outcome["boss"]["hp"] <= 0:
                        if leastspent is None or outcome["spent"] < leastspent:
                            leastspent = outcome["spent"]
                    if (leastspent and leastspent < outcome["spent"]) or outcome["player"]["hp"] <= 0:
                        continue
                    if outcome not in next_scenarios + current_scenarios + past_scenarios:
                        next_scenarios.append(outcome)
            else:
                outcome = battle(deepcopy(scenario), playerturn)
                if outcome["boss"]["hp"] <= 0:
                    if leastspent is None or outcome["spent"] < leastspent:
                        leastspent = outcome["spent"]
                if (leastspent and leastspent < outcome["spent"]) or outcome["player"]["hp"] <= 0:
                    continue
                if outcome not in next_scenarios + current_scenarios + past_scenarios:
                    next_scenarios.append(outcome)
        if len(next_scenarios) == 0:
            return leastspent
        past_scenarios += current_scenarios
        current_scenarios = next_scenarios
        next_scenarios = []
        playerturn = not playerturn


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
