
# coding: utf-8

# In[1]:

graphics = False


# In[2]:

def main():
    with open("input.txt") as file:
        data = file.read().strip()
    if "\n" in data:
        data = data.split("\n")
    data = process_input(data)
    part1 = evalp1(data, graphics)
    print("Part 1:")
    print(part1[0])
    print("Part 2:")
    print(evalp2(data, part1[1], graphics))


# In[18]:

def process_input(inp):
    boss = {}
    for line in inp:
        line = line.split(": ")
        boss[line[0][:3].lower()] = int(line[1])
    return (boss['hit'], boss['dam'], boss['arm'])


# In[16]:

def evalp1(data, graphics):
    shop = {"Weapons": ((8,   4, 0),
                        (10,  5, 0),
                        (25,  6, 0),
                        (40,  7, 0),
                        (74,  8, 0)),
            "Armor":   ((13,  0, 1),
                        (31,  0, 2),
                        (53,  0, 3),
                        (75,  0, 4),
                        (102, 0, 5),
                        (0,   0, 0)),
            "Rings":   ((25,  1, 0),
                        (50,  2, 0),
                        (100, 3, 0),
                        (20,  0, 1),
                        (40,  0, 2),
                        (80,  0, 3),
                        (0,   0, 0))}
    cheapest = None
    hitpoints = 100
    for cost, damage, armor in combinations(shop):
        if cheapest and cost >= cheapest: continue
        if battle(data, (hitpoints, damage, armor)): cheapest = cost
    return (cheapest, shop)


# In[14]:

def evalp2(data, part1, graphics):
    expensive = None
    hitpoints = 100
    for cost, damage, armor in combinations(part1):
        if expensive and cost <= expensive: continue
        if not battle(data, (hitpoints, damage, armor)): expensive = cost
    return expensive


# In[6]:

def combinations(shop):
    for weapon in shop["Weapons"]:
        for armor in shop["Armor"]:
            for ring1 in shop["Rings"]:
                for ring2 in shop["Rings"]:
                    if not ring2 == (0, 0, 0) and ring1 == ring2: continue
                    for ring3 in shop["Rings"]:
                        if not ring3 == (0, 0, 0) and (ring1 == ring3 or ring2 == ring3): continue
                        yield tuple(map(sum, zip(weapon, armor, ring1, ring2, ring3)))


# In[7]:

def battle(boss, player):
    bh, bd, ba = boss
    ph, pd, pa = player
    playerturn = True
    while True:
        if playerturn:
            damage = pd-ba
            if damage < 1: damage = 1
            bh -= damage
            if bh <= 0: return True
        else:
            damage = bd-pa
            if damage < 1: damage = 1
            ph -= damage
            if ph <= 0: return False
        playerturn = not playerturn


# In[19]:

main()

