# Open the file for reading using with open()
with open('example.txt', 'r') as file:
    # Read the contents of the file and store them in a variable
    file_contents = file.read()

# Print the contents of the file to the console
print('Original contents of the file:')
print(file_contents)

# Open the file again for writing, this time appending some extra text
with open('example.txt', 'a') as file:
    file.write('\nThis is some extra text added to the file.')

# Open the file for reading again using with open()
with open('example.txt', 'r') as file:
    # Read the updated contents of the file and store them in a variable
    updated_contents = file.read()

# Print the updated contents of the file to the console
print('\nUpdated contents of the file:')
print(updated_contents)
