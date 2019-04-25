#! python3
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)
motorcycles.append('ducati')
print(motorcycles)


a = 1
b = 2
print(a)
print(b)
a, b = b, a
print(a)
print(b)

l = ['David', 'Pythonista', '+1-514-555-1234']
people = [l, ['Guido', 'BDFL', 'unlisted']]

for (name, title, phone) in people:
    print(name, phone)


colors = ['red', 'blue', 'green', 'yellow']
print('Choose ' + ', '.join(colors[:-1]) + ' or ' + colors[-1] + '.')
