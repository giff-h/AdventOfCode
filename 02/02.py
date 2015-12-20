
# coding: utf-8

# In[5]:

graphics = False


# In[20]:

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


# In[13]:

def process_input(inp):
    return [sorted(map(int, line.split('x'))) for line in inp]


# In[11]:

def evalp1(data, graphics):
    return (sum(wrapping(box) for box in data), None)


# In[17]:

def evalp2(data, part1, graphics):
    return sum(2*box[0] + 2*box[1] + box[0]*box[1]*box[2] for box in data)


# In[15]:

def wrapping(box):
    h, l, w = box
    return 3*h*l + 2*h*w + 2*l*w # 3hl because adding another for slack


# In[21]:

main()

