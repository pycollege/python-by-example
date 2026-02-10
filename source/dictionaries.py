# Create a dict
person = {"name": "Alice", "age": 30, "city": "Paris"}
print(person)

# Access by key
print(person["name"])

# Safe access with .get()
print(person.get("country", "unknown"))

# Add or update
person["email"] = "alice@example.com"
person["age"] = 31
print(person)

# Keys, values, items
print(person.keys())
print(person.values())
for k, v in person.items():
    print(k, v)
