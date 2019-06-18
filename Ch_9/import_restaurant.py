from restaurant import Restaurant

restaraunt = Restaurant('wokie chan', 'chinese')
restaraunt2 = Restaurant('vilanella', 'italian')
restaraunt3 = Restaurant('teremok', 'russian')
restaraunt.number_served = 7
print(restaraunt.number_served)
restaraunt.number_served = 367
print(restaraunt.number_served)
restaraunt.set_number_served(2333)
print(restaraunt.number_served)
restaraunt.increment_number_served(59)
print(restaraunt.number_served)

print("The restaraunt name is " + restaraunt.restaurant_name.title() + ".")
print("The cuisine type is " + restaraunt.cuisine_type + ".")
restaraunt.describe_restaurant()
restaraunt.open_restraunt()

restaraunt2.describe_restaurant()
restaraunt3.describe_restaurant()
