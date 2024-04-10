# Take Input from Uswr and perform simple calculations

def addition():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    print("The sum of the two numbers is: ", num1 + num2)

def subtraction():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    print("The difference of the two numbers is: ", num1 - num2)

def multiplication():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    print("The product of the two numbers is: ", num1 * num2)

def division():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    try:
        print("The division of the two numbers is: ", num1 / num2)
    except ValueError:
        print("Division by zero is not allowed")
    
def main():
    while(input != 0):
        print("Enter 1 for addition")
        print("Enter 2 for subtraction")
        print("Enter 3 for multiplication")
        print("Enter 4 for division")
        print("Enter 0 to exit")
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid choice, please enter only a Number")
            continue
        if choice == 1:
            addition()
        elif choice == 2:
            subtraction()
        elif choice == 3:
            multiplication()
        elif choice == 4:
            division()
        elif choice == 0:
            print("Exiting the program")
            break
        else:
            print("Invalid choice, please enter a valid option (From Above Options)")

if __name__ == "__main__":
    main()