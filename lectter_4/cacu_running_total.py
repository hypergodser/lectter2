max = 5 
total = 0.0 

print('This program calculates the sum of', max, 'numbers.')
for counter in range(max):
    number = float(input('Enter a number: '))
    total += number
print('The total is', total)
