#Example list
import numbers


numbers [4, 2, 9, 1, 5, 6]
#1. len(): Get the length of the list
length = len(numbers)
print(f"Length of the list: {length}") # Output: Length of the list: 6
#2. sum(): Calculate the sum of all elements in the list
total = sum(numbers)
print(f"Sum of all elements: {total}") # Output: Sum of all elements: 27

max_value = max(numbers)
print(f"Maximum value: {max_value}") 
min_value = min(numbers)
print(f"Minimum value: {min_value}") 

sorted_numbers = sorted(numbers)
print (f"Sorted list: {sorted_numbers}") # Output: Sorted list:
[1, 2, 4, 5, 6, 9]