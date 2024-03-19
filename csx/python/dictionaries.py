# Create a dictionary
mydictionary = {
    "name": "Max",
    "age": 28,
    "city": "New York"
}

print(mydictionary)

# Creating a dictionary using a constructor
myotherdictionary = dict(name="Mary", age=27, city="Boston")

print(myotherdictionary)

# Iterating over dictionaries
for key, value in mydictionary.items():
    print(key, value)


# Accessing elements
print(mydictionary["name"])
print(mydictionary.get("age"))

# Adding elements
mydictionary["email"] = "max@server.com"
print(mydictionary)
