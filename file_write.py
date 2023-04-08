# Open the file for reading using with open()
with open('example.txt', 'r') as file:
    # Read the contents of the file and store them in a variable
    file_contents = file.read()

# Print the contents of the file to the console
print('Original contents of the file:')
print(file_contents)

# Open the file for writing using with open()
with open('example.txt', 'w') as file:
    # Write some text to the file
    file.write('This is new text that will be written to the file.')

# Open the file for reading using with open()
with open('example.txt', 'r') as file:
    # Read the contents of the file and store them in a variable
    updated_contents = file.read()

# Print the updated contents of the file to the console
print('\nUpdated contents of the file:')
print(updated_contents)
