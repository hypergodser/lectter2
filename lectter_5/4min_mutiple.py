def calculate_stats(numbers):
    total = sum(numbers)
    count = len(numbers)
    average = total / count if count > 0 else 0
    return total, count, average
numbers = [5, 10, 15, 20, 25]
total,count, average = calculate_stats(numbers)

print("Total:", total)
print("Count:", count) 
print("Average:", average)
