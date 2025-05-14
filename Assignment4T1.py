def read_file(filename):
    try:
        # Open and read the file
        with open(filename, 'r') as file:
            print("Reading file content:")
            # Read and print each line
            for line_number, line in enumerate(file, 1):
                print(f"Line {line_number}: {line.rstrip()}")
    except FileNotFoundError:
        # Handle the error if file does not exist
        print(f"Error: The file '{filename}' was not found.")

# Call the function with the filename
read_file('sample.txt')
