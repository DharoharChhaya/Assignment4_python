Python File Handling Assignment
This repository contains solutions for Module 5: Files, Exceptions, and Errors in Python programming assignments.

Contents
This repository includes two Python programs demonstrating file handling operations:

Task 1: Read a File and Handle Errors - A program that reads a text file and handles file not found errors.
Task 2: Write and Append Data to a File - A program that writes and appends user input to a file, then displays the content.
Task 1: Read a File and Handle Errors
Problem Statement
Write a Python program that:

Opens and reads a text file named sample.txt.
Prints its content line by line.
Handles errors gracefully if the file does not exist.
Solution
Copydef read_file(filename):
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
Task 2: Write and Append Data to a File
Problem Statement
Write a Python program that:

Takes user input and writes it to a file named output.txt.
Appends additional data to the same file.
Reads and displays the final content of the file.
Solution
Copydef write_and_append_to_file():
    # Part 1: Write initial data to file
    initial_text = input("Enter text to write to the file: ")
    with open("output.txt", "w") as file:
        file.write(initial_text)
    print(f"Data successfully written to output.txt.")
    
    # Part 2: Append additional data to file
    additional_text = input("Enter additional text to append: ")
    with open("output.txt", "a") as file:
        file.write("\n" + additional_text)
    print("Data successfully appended.")
    
    # Part 3: Read and display final content
    print("\nFinal content of output.txt:")
    with open("output.txt", "r") as file:
        content = file.read()
        print(content)

# Run the function
write_and_append_to_file()
How to Run
Clone this repository to your local machine
Run each Python file using Python 3:
python task1_read_file.py
python task2_write_append_file.py
For Task 1, you may need to create a sample.txt file or test the error handling by running the program without the file
For Task 2, follow the prompts to enter text to write and append
Expected Output
Task 1
If the file exists:

Reading file content:
Line 1: This is a sample text file.
Line 2: It contains multiple lines.
If the file does not exist:

Error: The file 'sample.txt' was not found.
Task 2
Enter text to write to the file: Hello, Python!
Data successfully written to output.txt.
Enter additional text to append: Learning file handling in Python.
Data successfully appended.

Final content of output.txt:
Hello, Python!
Learning file handling in Python.
Learning Objectives
This assignment demonstrates understanding of:

File operations in Python (open, read, write, append)
Exception handling (try/except)
Working with user input
File handling best practices using context managers (with statement)
