def simple_interest_calculator():
    principal = float(input("Enter the principal amount: "))
    rate = float(input("Enter the rate of interest: "))
    time = float(input("Enter the time (in years): "))
    simple_interest = (principal * rate * time) / 100
    print(f"The simple interest for the principal amount {principal}, rate of interest {rate} and time {time} years is: {simple_interest}")


if __name__ == "__main__":
    simple_interest_calculator()