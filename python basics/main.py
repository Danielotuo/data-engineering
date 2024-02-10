"""
This module converts a JSON string into a Python dictionary and vice versa.
"""

import json

# JSON string
json_str = """
{
    "name": "Jack",
    "age": 29,
    "city": "Toronto",
    "country": "Canada"
}
"""

# Convert JSON string to Python dictionary
data = json.loads(json_str)

# Print the type of the data variable
print(type(data))

# Print the data dictionary
print(data)

data = {
    "name": "John",
    "age": 28,
    "city": "New York",
    "country": "USA"
}

# Convert Python dictionary to JSON string
json_str = json.dumps(data)

# Print the type of the json_str variable
print(type(json_str))

# Print the JSON string
print(json_str)
