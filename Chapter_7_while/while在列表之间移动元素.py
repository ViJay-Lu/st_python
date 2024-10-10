unconfirmed_users = ['vijay','yoyo','lilian']
confirmed_users = []

print(len(unconfirmed_users),len(confirmed_users))

while unconfirmed_users:
    confirmed_user = unconfirmed_users.pop()
    confirmed_users.append(confirmed_user)

print(len(unconfirmed_users),len(confirmed_users))
for confirmed_user in confirmed_users:
    print('confirmed_user is',confirmed_user.title())

