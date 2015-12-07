
# coding: utf-8

# In[4]:

import re


# In[5]:

input_file = open("input.txt")
data = input_file.readlines()
input_file.close()


# In[8]:

lights = re.compile('(turn on|toggle|turn off) ([0-9]+,[0-9]+) through ([0-9]+,[0-9]+)')
lights.search("turn off 499,499 through 500,500").groups()


# In[13]:

lights = re.compile('(turn on|toggle|turn off) ([0-9]+,[0-9]+) through ([0-9]+,[0-9]+)')


# In[15]:

grid = [[False] * 1000 for i in range(1000)]
for inst in data:
    inst = lights.search(inst).groups()
    start = [int(i) for i in inst[1].split(',')]
    end = [int(i)+1 for i in inst[2].split(',')]
    if inst[0] == "turn on":
        y = [True] * (end[1] - start[1])
        for x in range(start[0], end[0]):
            grid[x][start[1]:end[1]] = y
    elif inst[0] == "turn off":
        y = [False] * (end[1] - start[1])
        for x in range(start[0], end[0]):
            grid[x][start[1]:end[1]] = y
    elif inst[0] == "toggle":
        for x in range(start[0], end[0]):
            for y in range(start[1], end[1]):
                grid[x][y] = not grid[x][y]
len([light for row in grid for light in row if light])


# In[17]:

grid = [[0] * 1000 for i in range(1000)]
for inst in data:
    inst = lights.search(inst).groups()
    start = [int(i) for i in inst[1].split(',')]
    end = [int(i)+1 for i in inst[2].split(',')]
    if inst[0] == "turn on":
        for x in range(start[0], end[0]):
            for y in range(start[1], end[1]):
                grid[x][y] += 1
    elif inst[0] == "turn off":
        for x in range(start[0], end[0]):
            for y in range(start[1], end[1]):
                grid[x][y] -= 1
                if grid[x][y] < 0:
                    grid[x][y] = 0
    elif inst[0] == "toggle":
        for x in range(start[0], end[0]):
            for y in range(start[1], end[1]):
                grid[x][y] += 2
sum(light for row in grid for light in row)

