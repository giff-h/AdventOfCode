
# coding: utf-8

# In[1]:

import re
import itertools


# In[43]:

input_file = open("input.txt")
data = [line.strip() for line in input_file.readlines()]
input_file.close()


# In[44]:

happysearch = re.compile("([a-z]+) would (gain|lose) ([0-9]+) happiness units by sitting next to ([a-z]+)\.", re.I)


# In[45]:

matches = [happysearch.match(line).groups() for line in data]


# In[46]:

names = set(list(zip(*matches))[0])


# In[73]:

fullperms = list(itertools.permutations(list(names), len(names)))


# In[74]:

perms = []
for p in fullperms:
    p = list(p)
    if not p[0] == "Alice":
        i = p.index("Alice")
        p = p[i:] + p[:i]
    if not p in perms:
        perms.append(p)


# In[77]:

happiness = {}


# In[78]:

for name1, gain, amt, name2 in matches:
    amt = int(amt)
    pair = ''.join(sorted([name1, name2]))
    if gain == 'lose':
        amt *= -1
    if pair in happiness:
        happiness[pair] += amt
    else:
        happiness[pair] = amt


# In[70]:

def tablehappywithoutself(people):
    table = people + people[:1]
    return sum([happiness[''.join(sorted(table[i:i+2]))] for i in range(len(people))])


# In[79]:

arrangements = [tablehappywithoutself(people) for people in perms]


# In[80]:

max(arrangements)


# In[81]:

def tablehappywithself(people):
    return sum([happiness[''.join(sorted(people[i:i+2]))] for i in range(len(people)-1)])


# In[82]:

selfarrangements = [tablehappywithself(people) for people in fullperms]


# In[83]:

max(selfarrangements)

