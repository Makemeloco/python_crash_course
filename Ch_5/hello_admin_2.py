new_users = ['Tony', 'Lisa', 'Katie', 'Sonya', 'Klair']
current_users = ['Katie', 'Jane', 'admin', 'Dominic', 'Anna', 'Lisa', 'Mary']

for new_user in new_users:
    for current_user in current_users:
        if new_user.lower() == current_user.lower():
            print(new_user + ' name is already taken.')
        else:
            print(new_user + ' name is free.')
