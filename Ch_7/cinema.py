prompt = "\nУкажите ваш возраст:"

while True:
    age = int(input(prompt))
    if age < 3:
        print('Билет бесплатный')
    elif 3 <= age <= 12:
        print('Билет стоит $10.')
    elif 12 < age:
        print('Билет стоит $15.')
    break
