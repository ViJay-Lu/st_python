
#eg1:
pets = ['dog','cat','monkey','snake','cat','fly','cat']

print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)

#eg2:
responses = {}
flag = True
while flag:
    name = input('What is your name?')
    response = input('Which mountain would you like to climb someday?')
    responses[name] = response

    repat = input('Would you like to let another person respond?("yes or no")')
    if repat == 'no':
        #break
        flag = False

for name,response in responses.items():
    print(name + ' would like to climb ' + response + '.')