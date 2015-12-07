
# coding: utf-8

# In[38]:

input_file = open("input.txt")
data = [line.strip() for line in input_file.readlines()]
input_file.close()


# In[51]:

wires = {}
for line in data:
    logic, output = line.split(" -> ")
    logic = logic.split(' ')
    if len(logic) == 1:
        if logic[0].isnumeric():
            wires[output] = int(logic[0])
        else:
            wires[output] = logic[0]
    elif len(logic) == 2:
        wires[output] = logic
    elif len(logic) == 3:
        command = logic[1]
        if logic[0].isnumeric():
            left = int(logic[0])
        else:
            left = logic[0]
        if logic[2].isnumeric():
            right = int(logic[2])
        else:
            right = logic[2]
        wires[output] = [command, left, right]

while True:
    end = True
    for wire, logic in wires.items():
        try:
            if type(logic) == int:
                continue
            end = False
            if type(logic) == str:
                if type(wires[logic]) == int:
                    wires[wire] = wires[logic]
            elif len(logic) == 2:
                if type(logic[1]) == int:
                    wires[wire] = ~ logic[1]
                elif type(logic[1]) == str and type(wires[logic[1]]) == int:
                    wires[wire] = ~ wires[logic[1]]
            elif len(logic) == 3:
                if (type(logic[1]) == str and not type(wires[logic[1]]) == int) or (type(logic[2]) == str and not type(wires[logic[2]]) == int):
                    continue
                for i in (1, 2):
                    if type(logic[i]) == str:
                        logic[i] = wires[logic[i]]
                if logic[0] == 'AND':
                    wires[wire] = logic[1] & logic[2]
                elif logic[0] == 'OR':
                    wires[wire] = logic[1] | logic[2]
                elif logic[0] == 'LSHIFT':
                    wires[wire] = logic[1] << logic[2]
                elif logic[0] == 'RSHIFT':
                    wires[wire] = logic[1] >> logic[2]
        except:
            print(wire)
            raise
    if end:
        break
print(wires['a'])


# In[52]:

wires = {}
for line in data:
    logic, output = line.split(" -> ")
    logic = logic.split(' ')
    if len(logic) == 1:
        if logic[0].isnumeric():
            wires[output] = int(logic[0])
        else:
            wires[output] = logic[0]
    elif len(logic) == 2:
        wires[output] = logic
    elif len(logic) == 3:
        command = logic[1]
        if logic[0].isnumeric():
            left = int(logic[0])
        else:
            left = logic[0]
        if logic[2].isnumeric():
            right = int(logic[2])
        else:
            right = logic[2]
        wires[output] = [command, left, right]
wires['b'] = 16076
while True:
    end = True
    for wire, logic in wires.items():
        try:
            if type(logic) == int:
                continue
            end = False
            if type(logic) == str:
                if type(wires[logic]) == int:
                    wires[wire] = wires[logic]
            elif len(logic) == 2:
                if type(logic[1]) == int:
                    wires[wire] = ~ logic[1]
                elif type(logic[1]) == str and type(wires[logic[1]]) == int:
                    wires[wire] = ~ wires[logic[1]]
            elif len(logic) == 3:
                if (type(logic[1]) == str and not type(wires[logic[1]]) == int) or (type(logic[2]) == str and not type(wires[logic[2]]) == int):
                    continue
                for i in (1, 2):
                    if type(logic[i]) == str:
                        logic[i] = wires[logic[i]]
                if logic[0] == 'AND':
                    wires[wire] = logic[1] & logic[2]
                elif logic[0] == 'OR':
                    wires[wire] = logic[1] | logic[2]
                elif logic[0] == 'LSHIFT':
                    wires[wire] = logic[1] << logic[2]
                elif logic[0] == 'RSHIFT':
                    wires[wire] = logic[1] >> logic[2]
        except:
            print(wire)
            raise
    if end:
        break
print(wires['a'])


# In[71]:

wires = {}
for line in data:
    logic, output = line.split(" -> ")
    logic = logic.split(' ')
    if len(logic) == 1:
        if logic[0].isnumeric():
            wires[output] = int(logic[0])
        else:
            wires[output] = logic[0]
    elif len(logic) == 2:
        wires[output] = logic
    elif len(logic) == 3:
        command = logic[1]
        if logic[0].isnumeric():
            left = int(logic[0])
        else:
            left = logic[0]
        if logic[2].isnumeric():
            right = int(logic[2])
        else:
            right = logic[2]
        wires[output] = [command, left, right]
#wires['b'] = 19138
#wires['b'] = 16076
#wires['b'] = 2797
#wires['b'] = 14998
#wires['b'] = 44382
#wires['b'] = 4971
#wires['b'] = 58032
#wires['b'] = 64152
#wires['b'] = 40238
#wires['b'] = 38049
#wires['b'] = 7654
#wires['b'] = 13215
#wires['b'] = 59653
#wires['b'] = 13460
#wires['b'] = 57700
#wires['b'] = 22603
#wires['b'] = 18920
#wires['b'] = 1802
wires['b'] = 34935
while True:
    end = True
    for wire, logic in wires.items():
        try:
            if type(logic) == int:
                continue
            end = False
            if type(logic) == str:
                if type(wires[logic]) == int:
                    wires[wire] = wires[logic]
            elif len(logic) == 2:
                if type(logic[1]) == int:
                    wires[wire] = ~ logic[1]
                elif type(logic[1]) == str and type(wires[logic[1]]) == int:
                    wires[wire] = ~ wires[logic[1]]
            elif len(logic) == 3:
                if (type(logic[1]) == str and not type(wires[logic[1]]) == int) or (type(logic[2]) == str and not type(wires[logic[2]]) == int):
                    continue
                for i in (1, 2):
                    if type(logic[i]) == str:
                        logic[i] = wires[logic[i]]
                if logic[0] == 'AND':
                    wires[wire] = logic[1] & logic[2]
                elif logic[0] == 'OR':
                    wires[wire] = logic[1] | logic[2]
                elif logic[0] == 'LSHIFT':
                    wires[wire] = logic[1] << logic[2]
                elif logic[0] == 'RSHIFT':
                    wires[wire] = logic[1] >> logic[2]
        except:
            print(wire)
            raise
    if end:
        break
print(wires['a'])

