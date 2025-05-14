def write_and_append_to_file():
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
