class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f'Person(name={self.name}, age={self.age})'
    

people = [Person('John', 30), Person('Jane', 25), Person('Dave', 40)]

# Filter people older than 30
people_over_30 = list(filter(lambda p: p.age > 30, people))

print(people_over_30)  # Output: [Person(name=Dave, age=40)]


# Map names to their lengths
names = list(map(lambda p: len(p.name), people))

print(names)  # Output: [4, 4, 4]

# Sort people by age
people.sort(key=lambda p: p.age)

print(people)  # Output: [Person(name=Jane, age=25), Person(name=John, age=30), Person(name=Dave, age=40)]

# Sort people by name
people.sort(key=lambda p: p.name)

print(people)  # Output: [Person(name=Dave, age=40), Person(name=Jane, age=25), Person(name=John, age=30)]

