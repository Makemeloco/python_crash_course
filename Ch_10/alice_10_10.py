filename = 'alice.txt'

try:
    with open(filename) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    msg = "Sorry, the file " + filename + " does not exist."
    print(msg)
else:
    # We count the number of occurrences of a word or expression.
    print(contents.count('cat'))
    print(contents.count('Alice'))
    print(contents.count('cards'))
    print(contents.count('the'))
