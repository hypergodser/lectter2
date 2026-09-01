# This program reads all of the values in the sales.txt file.

# Open the sales.txt file for reading using with statement.
with open('sales.txt', 'r') as sales_file:
    # Read the first line from the file, but don't convert to a number yet.
    # We still need to test for an empty string.
    line = sales_file.readline()

    # Read until the empty string is return.
    while line != '':
        # Convert line to a float.
        amount = float(line.strip())
        # Format and display the amount.
        print(format(amount, '.2f'))
        # Read the next line.
        line = sales_file.readline()