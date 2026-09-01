def example_w_plus():
    # Open a file in write and read mode
    with open("example.txt", "w+") as file:
        # Write some content to the file
        file.write("This is an example of w+ mode.\n")
        file.write("You can read and write to the same file.\n")
        
        # Move the cursor to the beginning of the file
        file.seek(0)
        
        # Read the content of the file
        content = file.read()
        print("Content of the file:")
        print(content)