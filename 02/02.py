
# coding: utf-8

# In[14]:

from functools import reduce

input_file = open("input.txt")
data = input_file.readlines()
input_file.close()

split_data = [[int(i) for i in box.split('x')] for box in data]


# In[15]:

sum(2*dim[0]*dim[1] + 2*dim[0]*dim[2] + 2*dim[1]*dim[2] + min(dim[0]*dim[1],dim[0]*dim[2],dim[1]*dim[2]) for dim in split_data)


# In[17]:

sum(2*(sum(dim)-max(dim))+reduce(lambda x,y: x*y, dim) for dim in split_data)

