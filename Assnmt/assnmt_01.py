def average(num1, num2):
    return (num1 + num2) / 2

# Calling the function with different values
print("Average of 10 and 20:", average(10, 20))
print("Average of 7.5 and 2.5:", average(7.5, 2.5))
print("Average of -5 and 5:", average(-5, 5))


# ----------------

def sort_strings(words):
    return sorted(words)

fruits = ["apple", "banana", "cherry", "kiwi", "grape"]
sorted_fruits = sort_strings(fruits)
print("Sorted list:", sorted_fruits)


# ----------------
def find_duplicates(lst):
    duplicates = []
    for item in lst:
        if lst.count(item) > 1 and item not in duplicates:
            duplicates.append(item)
    return duplicates

numbers = [1, 5, 6, 5, 1, 2, 3]
duplicates = find_duplicates(numbers)
print("Duplicate elements:", duplicates)
