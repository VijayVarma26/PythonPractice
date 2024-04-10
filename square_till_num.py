def calulate_square(num):
    return num**2

def square_till_num(num):   
    return [calulate_square(i) for i in range(1, num+1)]

if __name__ == "__main__":
    try:
        num = int(input("Enter a number: "))
        print(f"The square of numbers till {num} is: {square_till_num(num)}")
    except ValueError:
        print("Invalid input, please enter only a number")
        
    