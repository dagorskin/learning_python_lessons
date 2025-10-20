name = "Dmitri"
language = "Python"
message = "Bonjour, Dmitri! Would you like to start learning Python today?"
message_spaces = (
    " Bonjour, Dmitri!\nWould you like to start learning \t Python \t today? "
)
filename = "python_notes.txt"

# 2.3
print(message + "\n")

# 2.4
print(message.lower())
print(message.upper())
print(message.title() + "\n")

# 2.5 and 2.6
print(f'Bonjour, {name}! Would you like to start learning "{language}" today?\n')

# 2.7
print(message_spaces)
print(message_spaces.lstrip())
print(message_spaces.rstrip())
print(message_spaces.strip() + "\n")

# 2.8
print("Complete file name is:", filename)
print("Prefix name file is:", filename.removesuffix(".txt"))
print("File extension is:", filename.removeprefix("python_notes"), "\n")
