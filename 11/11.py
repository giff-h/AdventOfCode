
# coding: utf-8

# In[12]:

old_pass = "hxbxwxba"


# In[15]:

password = old_pass


# In[1]:

def rule1(password):
    i = 0
    while i < (len(password) - 2):
        a = ord(password[i])
        b = ord(password[i+1])
        c = ord(password[i+2])
        if c - b == 1 and b - a == 1:
            return True
        i += 1
    return False


# In[2]:

def rule2(password):
    return not 'i' in password and not 'o' in password and not 'l' in password


# In[3]:

def rule3(password):
    double_count = 0
    i = 0
    while i < (len(password) - 1):
        if password[i] == password[i+1]:
            double_count += 1
            i += 2
        else:
            i += 1
    return double_count >= 2


# In[16]:

while True:
    if len(password) > 8:
        raise("error somewhere")
    begin = password[:-1]
    letter = ord(password[-1]) + 1
    if letter in [105, 108, 111]:
        letter += 1
    end = ''

    while letter == 123:
        end = 'a' + end
        letter = ord(begin[-1]) + 1
        if letter in [105, 108, 111]:
            letter += 1
        begin = begin[:-1]

    password = begin + chr(letter) + end
    
    if rule1(password) and rule2(password) and rule3(password):
        break

print(password)


# In[17]:

# again


# In[18]:

while True:
    if len(password) > 8:
        raise("error somewhere")
    begin = password[:-1]
    letter = ord(password[-1]) + 1
    if letter in [105, 108, 111]:
        letter += 1
    end = ''

    while letter == 123:
        end = 'a' + end
        letter = ord(begin[-1]) + 1
        if letter in [105, 108, 111]:
            letter += 1
        begin = begin[:-1]

    password = begin + chr(letter) + end
    
    if rule1(password) and rule2(password) and rule3(password):
        break

print(password)

