class Student:
    # Constructor to initialize name and marks
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    # Method to display student details
    def display(self):
        print("\n--- Student Details ---")
        print(f"Name  : {self.name}")
        print(f"Marks : {self.marks}")

# User se input lena
name_input = input("Enter student name: ")
marks_input = int(input("Enter marks: "))

# Object banana aur display method call karna
student1 = Student(name_input, marks_input)
student1.display()
