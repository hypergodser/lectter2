# Initial sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7}

# Intersection Update: set1 will be updated to include elements present in both sets
set1 &= set2
print("After &= operation:", set1)  # Output: {4, 5}

# Resetting set1 to its original value
set1 = {1, 2, 3, 4, 5}

# Difference Update: set1 will be updated to remove elements also present in set2
set1 -= set2
print("After -= operation:", set1)  # Output: {1, 2, 3}

# Resetting set1 to its original value
set1 = {1, 2, 3, 4, 5}

# Symmetric Difference Update: set1 will be updated to keep elements in either set but not in both
set1 ^= set2
print("After ^= operation:", set1)  # Output: {1, 2, 3, 6, 7}