import requests
import json

url = "https://randomuser.me/api/?results=5"

# Fetch data from API
response = requests.get(url)

# Check if request was successful
if response.status_code == 200:
    data = response.json()
    print("API Data Fetched Successfully!\n")

    # Print fetched data
    print(json.dumps(data, indent=4))

    # Process data (Extract only names and emails)
    users = []
    for user in data['results']:
        users.append({
            "name": f"{user['name']['first']} {user['name']['last']}",
            "email": user['email']
        })

# Save processed data to JSON
    with open("users.json", "w") as f:
        json.dump(users, f, indent=4)

    print("\nProcessed user data saved to users.json")

else:
    print(f"Error: Unable to fetch data (Status Code: {response.status_code})")

# Try Modifying:

# - Change API to fetch weather, news, or cryptocurrency prices.
# - Use query parameters to customize data.
# - Automate periodic API calls and logging.