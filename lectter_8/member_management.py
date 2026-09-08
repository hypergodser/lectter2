fruits = {"apple", "banana", "cherry"}

# Adding an item
fruits.add("orange")
print(fruits)  # Output: {'apple', 'banana', 'cherry', 'orange'}

# Removing an item (raises KeyError if the item is not found)
fruits.remove("banana")
print(fruits)  # Output: {'apple', 'cherry', 'orange'}

# Discarding an item (removes the item if present, does nothing if not found)
fruits.discard("grape")
print(fruits)  # Output: {'apple', 'cherry', 'orange'} (no error raised)


removed_item = fruits.pop()
print(removed_item)
print(fruits)  
print(fruits)  