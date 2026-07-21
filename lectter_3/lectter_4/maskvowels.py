
input_string input("Enter a string: ")
# Initialize an empty string for the modified result

modified_string = ""

#Define a set of vowels
vowels = "aeiouAΕΙΟU"

# Use a for loop to iterate through the input string

for char in input_string:

# Convert character to uppercase

    upper_char = char.upper()

# Replace vowels with asterisks

    if upper_char in vowels:

     modified_string += "*"

    else:

        modified_string += upper_char


# Print the modified string

print("Modified string:", modified_string)