
# coding: utf-8

# In[1]:

data = "1321131112"


# In[2]:

phrase = data


# In[3]:

for x in range(50):
    next_phrase = []
    i = 0
    while i < len(phrase):
        count = 1
        char = phrase[i]
        while i + 1 < len(phrase) and phrase[i+1] == char:
            count += 1
            i += 1
        else:
            i += 1
        next_phrase.append(str(count) + char)
    phrase = ''.join(next_phrase)


# In[4]:

len(phrase)

