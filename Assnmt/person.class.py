class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")


# object instantiation
p1 = Person("Alice", 25)

# Displaying details
p1.display()
