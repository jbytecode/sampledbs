# Inheritance 


class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print("I am", self.name, "and I am", self.age, "years old")

# Inherit from the Human class
class Student(Human):
    def __init__(self, name, age, school):
        super().__init__(name, age)
        self.school = school

    def speak(self):
        super().speak()
        print("I go to", self.school)

    
# Create a Student object
s = Student("John", 15, "High School")

# Call the speak method
s.speak()  # I am John and I am 15 years old
           # I go to High School

