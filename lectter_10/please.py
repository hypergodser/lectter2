import requests

try:
    response = requests.get("https://jsonplaceholder.typicode.com/users/1", timeout=10)
    response.raise_for_status()

    user_data = response.json()
    print(user_data)
    print(f"User Name: {user_data['name']}")
    print(f"Name: {user_data['name']}, Email: {user_data.get('email', 'N/A')}, City: {user_data.get('address', {}).get('city', 'N/A')}")
    print(f"Company: {user_data.get('company', {}).get('name', 'N/A')}")
    print(f"Phone: {user_data.get('phone', 'N/A')}")
    print(f"Website: {user_data.get('website', 'N/A')}")
except requests.exceptions.RequestException as e:
    print(f"Failed to retrieve data: {e}")