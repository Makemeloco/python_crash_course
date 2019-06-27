"""запрашиваю имя, вывожу приветствие, сохраняю приветствие в файл"""

filename = 'guest_book.txt'

while True:
    username = input("Enter your name:\n")
    if username == 'quit':
        break
    else:
        print("Hi, " + username.title() + "!\n")
        with open(filename, 'a') as file_object:
            file_object.write("Hi, " + username.title() + "!\n")
