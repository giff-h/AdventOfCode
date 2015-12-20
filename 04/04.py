
# coding: utf-8

# In[1]:

from hashlib import md5


# In[2]:

graphics = False


# In[3]:

def main():
#    with open("input.txt") as file:
#        data = file.read().strip()
#    if "\n" in data:
#        data = data.split("\n")
#    data = process_input(data)
    data = "yzbqklnj"
    part1 = evalp1(data, graphics)
    print("Part 1:")
    print(part1[0])
    print("Part 2:")
    print(evalp2(data, part1[1], graphics))


# In[ ]:

def process_input(inp):
    pass


# In[4]:

def evalp1(data, graphics):
    i = 0
    while not md5(bytes(data + str(i), encoding="utf-8")).hexdigest().startswith("00000"):
        i += 1
    return (i, None)


# In[5]:

def evalp2(data, part1, graphics):
    i = 0
    while not md5(bytes(data + str(i), encoding="utf-8")).hexdigest().startswith("000000"):
        i += 1
    return i


# In[6]:

main()

