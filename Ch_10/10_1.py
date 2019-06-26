"""стандартный способ открыть файл и вывести его, данные в переменной"""

with open('learning_python.txt') as file_object:
    contents = file_object.read()
    print(contents.rstrip())

print(contents)

"""открываю файл, читаю и вывожу по строкам в цикле"""

filename = 'learning_python.txt'

with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())

"""читаем файл и сохраняем список в переменную для использования снаружи with"""

filename = 'learning_python.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())

for line in lines:
    line = line.replace('файл', 'байт')
    print(line.rstrip())

print(lines)
