
# coding: utf-8

# In[2]:

import re


# In[4]:

input_file = open("input.txt")
data = input_file.readlines()
input_file.close()


# In[10]:

vowels = re.compile('[aoeui].*[aoeui].*[aoeui]')
def has_double(nice):
    for i in range(len(nice)-1):
        if nice[i] == nice[i+1]:
            return True
    return False
len([nice for nice in data if vowels.search(nice) and has_double(nice) and not 'ab' in nice and not 'cd' in nice and not 'pq' in nice and not 'xy' in nice])


# In[19]:

def is_nice(nice):
    dual_pair = False
    split_by_one = False
    for i in range(len(nice)-1):
        if nice.count(nice[i:i+2]) > 1:
            dual_pair = True
        if i < len(nice)-2 and nice[i] == nice[i+2]:
            split_by_one = True
    return dual_pair and split_by_one
len([nice for nice in data if is_nice(nice)])

