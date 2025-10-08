# Define the sets
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# Compute union
union_set = A.union(B)

# Compute intersection
intersection_set = A.intersection(B)

# Compute differences
difference_A_B = A.difference(B)
difference_B_A = B.difference(A)

# Display the results
print("Set A:", A)
print("Set B:", B)
print("Union of A and B:", union_set)
print("Intersection of A and B:", intersection_set)
print("Difference A - B:", difference_A_B)
print("Difference B - A:", difference_B_A)
