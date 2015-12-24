
# coding: utf-8

# In[1]:

from erat import divisorGen


# In[2]:

graphics = False


# In[10]:

def main():
#    with open("input.txt") as file:
#        data = file.read().strip()
#    if "\n" in data:
#        data = data.split("\n")
#    data = process_input(data)
    data = 36000000
    part1 = evalp1(data, graphics)
    print("Part 1:")
    print(part1[0])
    print("Part 2:")
    print(evalp2(data, part1[1], graphics))


# In[ ]:

def process_input(inp):
    pass


# In[6]:

def evalp1(data, graphics):
    n = 2
    while 10*sum(divisorGen(n)) < data:
        n += 1
    return (n, None)


# In[9]:

def evalp2(data, part1, graphics):
    n = 2
    while 11*sum(i for i in divisorGen(n) if n / i < 50) < data:
        n += 1
    return n


# In[11]:

main()

