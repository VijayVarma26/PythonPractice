def check_even_odd(num):
    return 'Even' if num%2 == 0 else 'Odd'

if __name__ == "__main__":
    try:
        num = int(input("Enter a number: "))
        print(f"The number {num} is {check_even_odd(num)}")
    except ValueError:
        print("Invalid input, please enter only a number")