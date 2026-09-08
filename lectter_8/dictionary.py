phonebook = {'Anirach': '777-1111', 'Mickey': '777-2222', 'Donald': '777-3333'}

heroesdict = {} 
heroesdict['hulk'] = '888-1111'
heroesdict['Iron Man'] = '888-2222'
print(heroesdict.get('hulk','key not found')) 
print(heroesdict.get('Iron Man','key not found'))  # Output: 888-2222

for key, value in heroesdict.items():
    print(f"{key}: {value}")

print(heroesdict.keys())  # Output: dict_keys(['hulk', 'Iron Man'])
print(heroesdict.values())  # Output: dict_values(['888-1111', '888-2222'])

print(phonebook.get('Mickey', 'key not found'))  # Output: 777-2222
print(phonebook.get('Goofy', 'key not found'))  # Output: key not found
print(phonebook.keys())  # Output: dict_keys(['Anirach', 'Mickey', 'Donald'])
print(phonebook.values())  # Output: dict_values(['777-1111', '777-2222', '777-3333'])
print(phonebook.items())  # Output: dict_items([('Anirach', '777-1111'), ('Mickey', '777-2222'), ('Donald', '777-3333')])

phonebook.clear()
print('after clear')
print(phonebook)  # Output: {}
