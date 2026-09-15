filename = input('Enter a filename: ')
try:
    infile = open(filename, 'r')
    content = infile.read()
    print(content)
    infile.close()
except IOError :
    print('An error occurred trying to read the file.')
    print('the file', filename)
print("End of program")