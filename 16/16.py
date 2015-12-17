
# coding: utf-8

# In[1]:

import re


# In[2]:

input_file = open("input.txt")
data = [line.strip() for line in input_file.readlines()]
input_file.close()


# In[4]:

parse = re.compile("Sue ([0-9]+): ([a-z]+): ([0-9]+), ([a-z]+): ([0-9]+), ([a-z]+): ([0-9]+)")


# In[5]:

parsed_data = [parse.match(line).groups() for line in data]


# In[10]:

match = {"children": 3, "cats": 7, "samoyeds": 2, "pomeranians": 3, "akitas": 0, "vizslas": 0, "goldfish": 5, "trees": 3, "cars": 2, "perfumes": 1}


# In[11]:

for line in parsed_data:
    sue, id1, amt1, id2, amt2, id3, amt3 = line
    sue, amt1, amt2, amt3 = map(int, (sue, amt1, amt2, amt3))
    if match[id1] == amt1 and match[id2] == amt2 and match[id3] == amt3:
        print(sue)
        break


# In[17]:

for line in parsed_data:
    sue, id1, amt1, id2, amt2, id3, amt3 = line
    sue, amt1, amt2, amt3 = map(int, (sue, amt1, amt2, amt3))
    report = {id1: amt1, id2: amt2, id3: amt3}
    for name, amt in report.items():
        if name in ["cats", "trees"]:
            report[name] = range(0, amt)
        elif name in ["pomeranians", "goldfish"]:
            report[name] = range(amt+1, 100)
        else:
            report[name] = [amt]
    if match[id1] in report[id1] and match[id2] in report[id2] and match[id3] in report[id3]:
        print(sue)
        break

