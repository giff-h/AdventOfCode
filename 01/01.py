
# coding: utf-8

# In[2]:

def main():
    with open("input.txt") as file:
        data = file.read()
    if "\n" in data:
        data = data.split("\n")
    data = process_input(data)
    part1 = evalp1(data)
    print("Part 1:")
    print(part1[0])
    print("Part 2:")
    print(evalp2(data, part1[1]))


# In[3]:

def process_input(inp):
    return inp


# In[4]:

def evalp1(data):
    floorup = '('
    floordown = ')'
    return (data.count(floorup) - data.count(floordown), {floorup: 1, floordown: -1})


# In[5]:

def evalp2(data, part1):
    floor = 0
    i = 0
    while floor >= 0:
        floor += part1[data[i]]
        i += 1
    return i


# In[6]:

main()

