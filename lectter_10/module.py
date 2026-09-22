import json

data = {"name" : "Alice", "age" : 25 }
json_string = json.dumps(data)
print(json_string)  # Output: {"name": "Alice", "age": 25}

parsed_data = json.loads(json_string)
print(parsed_data)  # Output: {'name': 'Alice', 'age': 25}
print(parsed_data["name"])  # Output: Alice
print(parsed_data["age"])  # Output: 25