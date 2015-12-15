
# coding: utf-8

# In[2]:

import re
from functools import reduce


# In[3]:

input_file = open("input.txt")
data = [line.strip() for line in input_file.readlines()]
input_file.close()


# In[4]:

parse = re.compile("([a-z]+): capacity (-?[0-9]+), durability (-?[0-9]+), flavor (-?[0-9]+), texture (-?[0-9]+), calories (-?[0-9])+", re.I)


# In[12]:

ingredients_raw = [parse.match(line).groups() for line in data]
ingredients = [(int(capacity), int(durability), int(flavor), int(texture), int(calories)) for name, capacity, durability, flavor, texture, calories in ingredients_raw]


# In[13]:

ingredients


# In[17]:

max_score = [0, 0, 0, 0, 0]
for a in range(101):
    for b in range(101-a):
        for c in range(101-(a+b)):
            d = 100 - (a+b+c)
            properties = list(zip(*ingredients))[:4]
            properties = [a*prop[0] + b*prop[1] + c*prop[2] + d*prop[3] for prop in properties]
            zero = False
            if any(prop < 0 for prop in properties):
                continue
            score = reduce(lambda x,y: x*y, properties)
            if score > max_score[0]:
                max_score = [score, a, b, c, d]


# In[18]:

max_score


# In[19]:

max_score = [0, 0, 0, 0, 0]
for a in range(101):
    for b in range(101-a):
        for c in range(101-(a+b)):
            d = 100 - (a+b+c)
            properties = zip(*ingredients)
            properties = [a*prop[0] + b*prop[1] + c*prop[2] + d*prop[3] for prop in properties]
            properties, calories = properties[:4], properties[4]
            zero = False
            if any(prop < 0 for prop in properties):
                continue
            score = reduce(lambda x,y: x*y, properties)
            if calories == 500 and score > max_score[0]:
                max_score = [score, a, b, c, d]


# In[20]:

max_score

