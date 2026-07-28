# (20) Python program demonstrating tuple functions/methods

t = (5, 3, 8, 6, 3,9,12,78)
print("Tuple:", t)
print("Length:", len(t))
print("Count of 3:", t.count(3))
print("Index of 8:", t.index(8))
print("Sorted tuple:", sorted(t))
print("Min:", min(t))
print("Max:", max(t))

# in python cmp() function is not allowed so we use comparison operator 

t2 = (5, 3, 8)
print("Comparison with (5, 3, 8):", t == t2)
print("Reversed:", tuple(reversed(t)))
