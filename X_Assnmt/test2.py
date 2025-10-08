# Define the Student class
class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

    # Method to display student details
    def display(self):
        print(f"Name: {self.name}")
        print(f"Roll No: {self.roll_no}")

# Create an object of Student
student1 = Student("John", 2)

# Display the student's details
student1.display()
