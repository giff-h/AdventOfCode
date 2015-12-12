
# coding: utf-8

# In[1]:

import json
import re


# In[51]:

input_file = open("input.json")
data = input_file.read()
input_file.close()


# In[11]:

num = re.compile('-?[0-9]+')


# In[24]:

print(sum(map(int, num.findall(data))))


# In[52]:

data = json.loads(data)


# In[50]:

def recsearch(obj):
    if type(obj) == list:
        it = range(len(obj))
    elif type(obj) == dict:
        if "red" in obj.values():
            return True
        it = obj.keys()
    to_del = []
    for i in it:
        if type(obj[i]) in [list, dict]:
            if recsearch(obj[i]):
                to_del.append(i)
    to_del.sort()
    to_del.reverse()
    for j in to_del:
        del obj[j]
    return False


# In[53]:

recsearch(data)


# In[56]:

print(sum(map(int, num.findall(str(data)))))

