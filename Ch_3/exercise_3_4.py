guests = ['Tonya', 'Alisa', 'Samara', 'Ella', 'Stefany']

def invitations():
    for i in guests:
        print('Hello, ' + i + '! Come to my place for lunch on Wednesday at 14 o\'clock.')
    print('\n')

invitations()

print(guests[0] + ' will not be able to come.')

guests[0] = 'Aleksa'

invitations()

print('There will be more guests.')

guests.insert(0, 'Amy')
guests.insert(3, 'Rihanna')
guests.append('Ann')
invitations()

print('Only two guests are invited for lunch.')

while len(guests) > 2:
    last_guest = guests.pop()
    print('Sorry, ' + last_guest + '.')
print('\n')

for j in guests:
    print(j + ', see you later!')
print('\n')
print(len(guests))

while len(guests) > 0:
    del guests[0]

print(guests)
