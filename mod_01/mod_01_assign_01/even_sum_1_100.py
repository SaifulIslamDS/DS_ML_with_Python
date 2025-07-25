# Problem 03: Sum of Even Numbers from 1 to 100

total = 0

for number in range(2, 101, 2):  # Start at 2, go till 100, step by 2 (even numbers only)
    total += number

print("Sum of even numbers from 1 to 100 is:", total)
