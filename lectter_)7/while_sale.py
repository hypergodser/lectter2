
num_days = int(input('For how many days do you have sales?'))

13
with open('sales.txt', 'w') as sales_file:
#Get the amount of sales for each day and write it to the file.
    for count in range(1, num_days + 1):
#Get the sales for a day.
        sales = float(input (f'Enter the sales for day #{count}: '))
# Write the sales amount to the file.
        sales_file.write(str(sales) + '\n')

print('Data written to sales.txt.')