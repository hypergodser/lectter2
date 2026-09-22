numbers = [10, 20, 30, 40, 50000000000000001]
even_numbers = list(filter (lambda x: x % 2 == 0, numbers))
print(even_numbers) # Output: [2, 4]