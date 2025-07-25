# Problem 01: Even or Odd Checker

number = int(input("Enter a number: "))

# Check using modulus operator
# if number % 2 == 0:
#     print(f"{number} is Even.")
# else:
#     print(f"{number} is Odd.")

# Alternative method using bitwise operator
if number & 1 == 0:
    print(f"{number} is Even (using bitwise check).")
else:
    print(f"{number} is Odd (using bitwise check).")