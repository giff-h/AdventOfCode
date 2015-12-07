
# coding: utf-8

# In[1]:

input_file = open("input.txt")
data = input_file.read()
input_file.close()


# In[14]:

print(data.count('(') - data.count(')'))

