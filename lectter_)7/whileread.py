with open ('example.txt', 'r') as infile:
    line = infile.readline()
    while line:
        print(line.strip())
        line = infile.readline()

       