# Question 4

class Student:
    def __init__(self, student, roll_no):
        self.name = student
        self.roll_no = roll_no

    def __del__(self):
        print('Object destroyed')

     # Creating object
student1 = Student("Prakhar",21103072)
print('Object created')
     # Printing the assigned values
print(f"The name of the student is {student1.name} and SID is {student1.roll_no}.")
     # Deleting object
del student1
print("\n")
