bool_list = [False, True, False]
any_true = any(bool_list)
print(f"Any true value in the list: {any_true}") # Output: Any true value in the list: True

all_true = all(bool_list)
print(f"All values are true in the list: {all_true}") # Output: All values are true in the list: False

string = "Hello, World!"
char_list = list(string)
print(f"list of characters: {char_list}") # Output: list of characters: ['H', 'e', 'l', 'l', 'o', ',', ' ', 'W', 'o', 'r', 'l', 'd', '!']

reversed_numbers = list(reversed(numbers))
print(f"Reversed list: {reversed_numbers}") # Output: Reversed list: [6, 5, 1, 9, 2, 4]

enumerated_numbers = list(enumerate(numbers))
print(f"Enumerated list: {enumerated_numbers}") # Output: Enumerated list: [(0, 4), (1, 2), (2, 9), (3, 1), (4, 5), (5, 6)]                 