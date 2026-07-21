1 # Get the user's name, age, and income.
name = input('enter your name? ')
age = int(input('enter age? '))
income = float(input('enter income? '))
# Display the data.
print('Here is the infomation you entered:')
print('Name:', name)
print('Age:', age)
print('Income: ', format(income, '12,.2f'))