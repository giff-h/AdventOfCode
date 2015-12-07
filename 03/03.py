
# coding: utf-8

# In[18]:

input_file = open("input.txt")
data = input_file.read()
input_file.close()


# In[19]:

x = 0
y = 0
grid = {(x, y)}
for d in data:
    if d == '>':
        y += 1
    elif d == '<':
        y -= 1
    elif d == 'v':
        x += 1
    elif d == '^':
        x -= 1
    grid.add((x, y))
print(len(grid))


# In[22]:

x = 0
y = 0
robotx = 0
roboty = 0
grids = [{(x, y)}, {(robotx, roboty)}]
for i in range(len(data)):
    d = data[i]
    if i % 2 == 0:
        if d == '>':
            y += 1
        elif d == '<':
            y -= 1
        elif d == 'v':
            x += 1
        elif d == '^':
            x -= 1
        grids[0].add((x, y))
    else:
        if d == '>':
            roboty += 1
        elif d == '<':
            roboty -= 1
        elif d == 'v':
            robotx += 1
        elif d == '^':
            robotx -= 1
        grids[1].add((robotx, roboty))
print(len(grids[0] | grids[1]))

