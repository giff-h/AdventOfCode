
# coding: utf-8

# In[19]:

input_file = open("input.txt")
data = [line.strip() for line in input_file.readlines()]
input_file.close()


# In[18]:

# data = [".#.#.#", "...##.", "#....#", "..#...", "#.#..#", "####.."]


# In[3]:

def chr_to_bool(grid):
    return [[i == '#' for i in line] for line in grid]


# In[4]:

def bool_to_chr(grid):
    return [''.join('#' if i else '.' for i in line) for line in grid]


# In[25]:

def neighbors(grid, x, y):
    ymax = len(grid)
    xmax = list(set(len(row) for row in grid)) # verify all rows are equal in length
    if len(xmax) > 1:
        raise "Error: Grid not rectangular! " + str(xmax)
    xmax = xmax[0]
    xstart = (0 if x == 0 else x-1) # left side
    ystart = (0 if y == 0 else y-1) # top side
    xend = (xmax if x == xmax-1 else x+2) # right side ; +2 because range stops one short
    yend = (ymax if y == ymax-1 else y+2) # bottom side
    ret = []
    for ix in range(xstart, xend):
        for iy in range(ystart, yend):
            if ix == x and iy == y:
                continue
            ret.append(grid[iy][ix])
    return ret


# In[6]:

def switch(light, surround):
    if light:
        return surround.count(True) in (2, 3)
    else:
        return surround.count(True) == 3


# In[40]:

def step(grid, n=1, part2=False):
    stepped = [[switch(light, neighbors(grid, x, y)) for x, light in enumerate(row)] for y, row in enumerate(grid[:])]
    if part2:
        stepped[0][0] = True
        stepped[0][-1] = True
        stepped[-1][0] = True
        stepped[-1][-1] = True
    if n > 1:
        for i in range(n-1):
            stepped = step(stepped, 1, part2)
    return stepped


# In[38]:

lights = chr_to_bool(data)


# In[37]:

print(sum(row.count(True) for row in step(lights, 100)))


# In[50]:

lights[0][0] = True
lights[0][-1] = True
lights[-1][0] = True
lights[-1][-1] = True


# In[51]:

print(sum(row.count(True) for row in step(lights, 100, True)))

