
# coding: utf-8

# In[24]:

input_file = open("input.txt")
data = [line.strip() for line in input_file.readlines()]
input_file.close()


# In[25]:

parsed_data = list(map(int, data))


# In[49]:

def combinations(rest, start=tuple(), result=150):
    if len(rest) == 1:
        if sum(start) + rest[0] == result:
            return [start + (rest[0],)]
        else:
            return [start + (-1,)]
    combos = []
    for i, n in enumerate(rest):
        if sum(start) + n == result:
            combos.append(start + (n,))
        elif sum(start) + n < result:
            combos += [combo for combo in combinations(rest[i+1:], start + (n,), result) if not -1 in combo]
    return combos


# In[50]:

combos = combinations(parsed_data[:])


# In[52]:

print(len(combos))


# In[58]:

save = min(map(len, combos))


# In[59]:

print(len([combo for combo in combos if len(combo) == save]))

