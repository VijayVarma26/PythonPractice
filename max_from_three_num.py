def find_highest(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

# Example usage:
num1 = 10
num2 = 25
num3 = 15

highest = find_highest(num1, num2, num3)
print("The highest of the three numbers is:", highest)
