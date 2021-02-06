usernames = ('Rajib', 'Cindy', 'Kyle', 'Lary', 'Bill')

for user in usernames:
    if user == 'Lary':
        break
    print(user)


for user in usernames:
    if user == 'Cindy':
        print('Cindy will be skipped and next user will be printed out')
        continue
    print(user)
