
# coding: utf-8

# In[1]:

graphics = False


# In[18]:

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


# In[10]:

def process_input(inp):
    return inp


# In[13]:

def evalp1(data, graphics):
    house = (0, 0)
    houses = [house]
    for d in data:
        house = step(house, d)
        if not house in houses:
            houses.append(house)
    return (len(houses), None)


# In[25]:

def evalp2(data, part1, graphics):
    santahouse = (0, 0)
    robothouse = (0, 0)
    houses = [santahouse]
    for i, d in enumerate(data):
        if i % 2:
            robothouse = step(robothouse, d)
            if not robothouse in houses:
                houses.append(robothouse)
        else:
            santahouse = step(santahouse, d)
            if not santahouse in houses:
                houses.append(santahouse)
    return len(houses)


# In[17]:

def step(house, direction):
    if direction == '>':
        return (house[0]+1, house[1])
    elif direction == '<':
        return (house[0]-1, house[1])
    elif direction == '^':
        return (house[0], house[1]+1)
    elif direction == 'v':
        return (house[0], house[1]-1)


# In[27]:

main()

