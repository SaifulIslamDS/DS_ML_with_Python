class Animal:
    def sound(self):
        print("Animals make different sounds.")

class Dog(Animal):
    def sound(self):
        print("Dog barks!")


# Creating objects
a = Animal()
d = Dog()

# Calling methods
a.sound()  # From Animal class
d.sound()  # From Dog class
