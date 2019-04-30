
a = 1
b = 2
print(a)
print(b)
a, b = b, a
print(a)
print(b)
=====================================================
l = ['David', 'Pythonista', '+1-514-555-1234']
people = [l, ['Guido', 'BDFL', 'unlisted']]

for (name, title, phone) in people:
    print(name, phone)
=====================================================

colors = ['red', 'blue', 'green', 'yellow']
print('Choose ' + ', '.join(colors[:-1]) + ' or ' + colors[-1] + '.')
=====================================================
navs = {}
for (portfolio, equity, position) in data:
    navs[portfolio] = (navs.get(portfolio, 0) + position * prices[equity])
=====================================================
equities = {}
for (portfolio, equity) in data:
    equities.setdefault(portfolio, []).append(equity)
=====================================================
Проверка на истинность значения
# делайте так:    # а не так:
if x:             if x == True:
    pass              pass
=====================================================
>>> items = 'zero one two three'.split()
>>> print items
['zero', 'one', 'two', 'three']
=====================================================
name = 'David'
messages = 3
text = ('Hello %s, you have %i messages'
        % (name, messages))
print text
=====================================================
values = {'name': name, 'messages': messages}
print ('Hello %(name)s, you have %(messages)i '
       'messages' % values)
=====================================================
Никогда!
from module import *
=====================================================

=====================================================
