pizzas = ['Гавайская', 'Пепперони', '4 сыра']
for pizza in pizzas:
    print(pizza.title() + " - пицца, которую я люблю!")
print("Я действительно люблю пиццу!\n")

friend_pizzas = pizzas[:]
pizzas.append('Маргарита')
friend_pizzas.append('Мясная ассорти')


for pizza in pizzas:
    print(pizza.title() + " - пицца, которую я люблю!")
print("Я действительно люблю пиццу!\n")

for friend_pizza in friend_pizzas:
    print(friend_pizza.title() + " - пицца, которую любит моя подруга!")
print("Она действительно любит пиццу!")
