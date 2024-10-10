import json

nembers = [1,2,3,4,5,6,7]

filename = 'nember.json'
#new nember.json file and write[1,2,3,4,5,6,7]
with open(filename, 'w') as f:
    #json.dump()存数据
    json.dump(nembers, f)

with open(filename, 'r') as f:
    #json.load()取数据
    nembers = json.load(f)

print(nembers)