
# coding: utf-8

# In[2]:

from hashlib import md5


# In[10]:

data = b"yzbqklnj"


# In[18]:

i = 0
while True:
    m = md5()
    m.update(data + bytes(str(i), encoding="utf-8"))
    if m.hexdigest().startswith('00000'):
        break
    i += 1
print(i)


# In[19]:

i = 0
while True:
    m = md5()
    m.update(data + bytes(str(i), encoding="utf-8"))
    if m.hexdigest().startswith('000000'):
        break
    i += 1
print(i)

