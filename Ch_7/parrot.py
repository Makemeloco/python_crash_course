message = input("Tell me something, and I will repeat it back to you: ")
print(message)


name = input("Please enter your name: ")
print("Hello, " + name + "!")


prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "
name = input(prompt)
print("\nHello, " + name + "!")


prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
message = ""

while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print(message)
