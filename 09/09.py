
# coding: utf-8

# In[53]:

from itertools import permutations

input_file = open("input.txt")
data = [line.strip() for line in input_file.readlines()]
input_file.close()


# In[54]:

cities = [line.split(' = ') for line in data]
distances = {''.join(sorted(line[0].split(' to '))): int(line[1]) for line in cities}
unique_cities = set()
for line in cities:
    city1, city2 = line[0].split(' to ')
    unique_cities.add(city1)
    unique_cities.add(city2)

travel = list(permutations(unique_cities, len(unique_cities)))
travel_lengths = [sum(distances[''.join(sorted(path[i:i+2]))] for i in range(len(path)-1)) for path in travel]


# In[55]:

print(min(travel_lengths))


# In[56]:

print(max(travel_lengths))

