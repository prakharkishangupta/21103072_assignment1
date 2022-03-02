# Question 5

class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
    # Creating employee record
employee1 = Employee('Mehak',40000)
employee2 = Employee('Ashok',50000)
employee3 = Employee('Viren',60000)

   # Part <a> updating salary
employee1.salary = 70000
print(f"<a> The updated salary of {employee1.name} is {employee1.salary}")
# Part <b> deleting a record
print(f"<b> Record of Viren deleted", end='')
del employee3
print("\n")

    
