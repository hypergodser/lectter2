set1 = {1, 2, 3}
set2 = {3, 4, 5}

print("Union:", set1 | set2)  # Union of set1 and set2
print("Intersection:", set1 & set2)  # Intersection of set1 and set2
print("Difference (set1 - set2):", set1 - set2)  # Difference of set1 and set2
print("Difference (set2 - set1):", set2 - set1)  # Difference of set2 and set1
print("Symmetric Difference:", set1 ^ set2)  # Symmetric difference of set1 and set2
print("Is set1 a subset of set2?", set1 <= set2)  # Check if set1 is a subset of set2
print("Is set1 a superset of set2?", set1 >= set2)  # Check if set1 is a superset of set2
print("Are set1 and set2 disjoint?", set1.isdisjoint(set2))  # Check if set1 and set2 are disjoint
print("Length of set1:", len(set1))  # Length of set1
print("Length of set2:", len(set2))  # Length of set2
print("Is set1 empty?", len(set1) == 0)  # Check if set1 is empty
print("Is set2 empty?", len(set2) == 0)  # Check if set2 is empty
print("Does set1 contain 2?", 2 in set1)  # Check if set1 contains the element 2