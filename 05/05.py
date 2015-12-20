
# coding: utf-8

# In[16]:

import re
vowels = re.compile("([aoeui].*){3}")


# In[1]:

graphics = False


# In[26]:

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


# In[4]:

def process_input(inp):
    return inp


# In[12]:

def evalp1(data, graphics):
    return (len(list(0 for word in data if p1rule1(word) and p1rule2(word) and p1rule3(word))), None)


# In[28]:

def evalp2(data, part1, graphics):
    return len(list(0 for word in data if p2rule1(word) and p2rule2(word)))


# In[19]:

def p1rule1(word):
    return vowels.search(word)


# In[6]:

def p1rule2(word):
    return any(word[i] == word[i+1] for i in range(len(word)-1))


# In[8]:

def p1rule3(word):
    return all(x not in word for x in ["ab", "cd", "pq", "xy"])


# In[24]:

def p2rule1(word):
    return any(word[i:i+2] in word[i+2:] for i in range(len(word)-3))


# In[23]:

def p2rule2(word):
    return any(word[i] == word[i+2] for i in range(len(word)-2))


# In[29]:

main()

