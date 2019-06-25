"""стандартный способ открыть файл и вывести его, данные в переменной"""

with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents.rstrip())

print(contents)

"""открываю файл, читаю и вывожу по строкам в цикле"""

filename = 'pi_digits.txt'

with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())

"""читаем файл и сохраняем список в переменную для использования снаружи with"""

filename = 'pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())

print(lines)


"""одна строка со всеми цифрами в ряд"""

filename = 'pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))


"""одна строка для файла с миллионом цифр числа пи"""

filename = 'pi_million_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()


print(pi_string[:52] + "...")
print(len(pi_string))

"""проверка, не встречается ли дата в первом миллионе цифр числа пи"""

birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")
