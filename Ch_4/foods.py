my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
for food in my_foods:
    print(food.title())
print("\n")

print("\nMy friend's favorite foods are:")
for friend_food in friend_foods:
    print(friend_food.title())

print('\nThe last three items in the list are:' + str(my_foods[-3:] ))
print('\nThe first three items in the list are:' + str(my_foods[:3] ))
