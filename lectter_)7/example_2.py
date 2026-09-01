def example_a_plus():
    # Open a file in append mode
    with open("example.txt", "a") as file:
        # Append some content to the file
        file.write("This is an example of a+ mode.\n")
        file.write("You can append and read from the same file.\n")
        
        # Move the cursor to the beginning of the file
        file.seek(0)
        
        # Read the content of the file
        content = file.read()
        print("Content of the file after appending:")
        print(content)