filename = 'guest.txt'

username = input("Как вас зовут?\n")

with open(filename, 'a') as file_object:
    file_object.write(username + "\n")


