import os 

print(os.name)  # Output: 'posix' for Linux/Mac, 'nt' for Windows
print(os.getcwd())  # Output: Current working directory
os.chdir('/path/to/directory')  # Change current working directory