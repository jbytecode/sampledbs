class Person:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def __str__(self):
        return f"{self.name} lives at {self.address}"
    


# Create a Person object
p = Person("John", "123 Main St")

# Print the object
print(p)  # John lives at 123 Main St


