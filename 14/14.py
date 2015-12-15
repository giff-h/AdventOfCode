
# coding: utf-8

# In[1]:

import re


# In[2]:

input_file = open("input.txt")
data = [line.strip() for line in input_file.readlines()]
input_file.close()


# In[3]:

parse = re.compile("([a-z]+) can fly ([0-9]+) km/s for ([0-9]+) second[s]?, but then must rest for ([0-9]+) second[s]?\.", re.I)


# In[4]:

speeds = [parse.match(line).groups() for line in data]


# In[22]:

reindeer = {name: [int(speed), int(time), int(rest)] for name, speed, time, rest in speeds}


# In[23]:

distances = []
max_time = 2503
for name, speed in reindeer.items():
    distance = 0
    time = 0
    while time < max_time:
        if (time + speed[1]) >= max_time:
            distance += (speed[0] * (max_time - time))
            break
        else:
            distance += (speed[0] * speed[1])
            time += (speed[1] + speed[2])
    distances.append(distance)


# In[24]:

print(max(distances))


# In[25]:

points = {name: 0 for name in reindeer.keys()}


# In[31]:

for name in reindeer.keys():
    reindeer[name][3:] = [0, False, 0]


# In[32]:

max_time = 2503
for i in range(1, max_time+1):
    ahead = ['', 0]
    for name, info in reindeer.items():
        speed, time, rest, distance, resting, last = info
        if resting:
            if last + rest == i:
                resting = False
                last = i
        else:
            distance += speed
            if last + time == i:
                resting = True
                last = i
        reindeer[name][3:] = [distance, resting, last]
        if distance > ahead[1]:
            ahead = [name, distance]
    points[ahead[0]] += 1


# In[35]:

print(max(points.values()))

