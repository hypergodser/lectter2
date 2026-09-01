# This program uses the for loop to read
# all of the values in the sales.txt file.

# Open the sales.txt file for reading using with statement.
with open('sales.txt', 'r') as sales_file:
    # Read all the lines from the file.
    for line in sales_file:
        # Convert line to a float.
        amount = float(line.strip())
        # Format and display the amount.
        print(format(amount, '.2f'))