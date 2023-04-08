def print_file(infile):
    # Open the file for reading using with open()
    with open(infile, 'r') as file:
        # Read the contents of the file and store them in a variable
        file_contents = file.read()

    # Print the contents of the file to the console
    print(file_contents)
    