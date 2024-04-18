# 
class Employee:
    def __init__(self, name, age, department):
        self.name = name
        self.age = age
        self.department = department

    def display_info(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Department:", self.salary)


# Creating an object of Employee class
emp1 = Employee("Vijay", 27, "IT")

# Accessing attributes and methods of the object
emp1.display_info()
