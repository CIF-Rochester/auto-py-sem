# Open the file for reading using with open()
with open('example.txt', 'r') as file:
    # Read the contents of the file and store them in a variable
    file_contents = file.read()

# Print the contents of the file to the console
print(file_contents)
