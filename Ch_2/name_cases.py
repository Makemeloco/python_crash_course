# The program demonstrates work with strings.
name = 'Kate'
massage = 'Hello ' + name.title() + ' ' + name.upper() + ' ' + name.lower() + ', would you like to learn some Python today?'
print(massage)

famous_person = '\t\t\nкитайцы\t\n\n'
massage_2 = 'Наблюдательные ' + famous_person.lstrip()+ ' ' + famous_person.rstrip() + ' ' + famous_person.strip() + ' говорили: "вся вселенная помещается в чайнике".'
print(massage_2)
