
# coding: utf-8

# In[1]:

input_file = open("input.txt")
data = input_file.read()
input_file.close()


# In[14]:

print(data.count('(') - data.count(')'))


# In[21]:

i = 0
floor = 0
while True:
    c = data[i]
    if c == "(":
        floor += 1
    elif c == ")":
        floor -= 1
    i += 1
    if floor == -1:
        break
print(i)

