# 
class Employee:
    def __init__(self, name, age, department):
        self.name = name
        self.age = age
        self.department = department

    # returns the string representation of the object. Gets called when we use print() function
    def __str__(self):
        return "Name: {}, Age: {}, Department: {}".format(self.name, self.age, self.department)
    
    # prints all the employee attributes
    def display_info(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Department:", self.department)


# Creating an object of Employee class
emp1 = Employee("Vijay", 27, "IT")


# Accessing attributes of the object
print(emp1.name)
print(emp1.age)
print(emp1.department)

# Accessing methods of the object
emp1.display_info()

# using __str__ method to display
print(emp1)