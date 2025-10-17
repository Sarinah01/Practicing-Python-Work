# Tuple Basics
# tpl = (10, 20, 30)

# Immutable → cannot be changed, added to, or removed from
# Ordered → preserves insertion order
# Holds references to objects in heap
# Can store mixed types: ints, strings, lists, etc.
# Faster and more memory-efficient than lists

# --------------------------------------------
# Creating Tuples

tpl = (1, 2, 3)
tpl2 = 1, 2, 3          # Parentheses optional
tpl3 = (10,)            # Single-element tuple → comma REQUIRED
tpl4 = tuple([4, 5, 6]) # From list
tpl5 = tuple("Hi")      # From iterable → ('H', 'i')

# Edge Cases:
# (10)  → not a tuple (just int)
# (10,) → valid tuple
# tuple() → empty tuple

# --------------------------------------------
# Accessing Elements

tpl = (10, 20, 30, 40)
print(tpl[0])    # 10
print(tpl[-1])   # 40
print(tpl[1:3])  # (20, 30)

# Supports slicing and negative indices
# IndexError if index out of range
# Slicing out of bounds → no error

# --------------------------------------------
# Immutability

tpl = (1, 2, 3)
# tpl[0] = 10    # TypeError: 'tuple' object does not support item assignment
# tpl.append(4)  # AttributeError: 'tuple' object has no attribute 'append'

# Mutable inside immutable:
tpl = ([1, 2], 3)
tpl[0].append(99)
print(tpl)  # ([1, 2, 99], 3)
# Inner list changed because list is mutable, tuple only locks the references.

# --------------------------------------------
# Tuple Methods (Only 2)

tpl = (1, 2, 2, 3, 2)
print(tpl.count(2))   # 3  → how many times '2' appears
print(tpl.index(3))   # 3 is at index 3

# Edge Cases:
# tpl.index(10) → ValueError if value not present
# tpl.count(10) → returns 0 (no error)

# --------------------------------------------
# Tuple Operations

a = (1, 2)
b = (3, 4)
print(a + b)      # (1, 2, 3, 4) → concatenation
print(a * 2)      # (1, 2, 1, 2) → repetition
print(2 in a)     # True
print(len(a))     # 2

# +, *, in, not in, len() supported
# append, remove, insert, pop not available

# --------------------------------------------
# Iteration & Unpacking

tpl = (10, 20, 30)
for i in tpl:
    print(i)

a, b, c = tpl
print(a, b, c)  # 10 20 30

# Extended Unpacking
tpl = (1, 2, 3, 4, 5)
x, *y, z = tpl
print(x, y, z)  # 1 [2, 3, 4] 5

# --------------------------------------------
# Tuple vs List (Quick Comparison)
# List → Mutable, many methods, slower, [] brackets
# Tuple → Immutable, only 2 methods, faster, () brackets

# --------------------------------------------
# Copying & References

tpl = (1, 2, [3, 4])
copy_tpl = tpl
copy_tpl[2].append(5)
print(tpl)  # (1, 2, [3, 4, 5])
# Same reference → inner list shared

# --------------------------------------------
# Conversion between list and tuple

lst = [1, 2, 3]
tpl = tuple(lst)
print(tpl)  # (1, 2, 3)

tpl = (4, 5, 6)
lst = list(tpl)
print(lst)  # [4, 5, 6]

# --------------------------------------------
# Tuple as Dictionary Key (hashable if all elements immutable)

point = (10, 20)
locations = {point: "Home"}  # Works
print(locations[(10, 20)])   # Home

# Not allowed if contains list (unhashable)
# bad = ([1, 2], 3)
# d = {bad: "Error"} → TypeError

# --------------------------------------------
# Tuple Memory Facts (Python 3.12+)

# Tuples are fixed-size arrays of object references stored on heap
# Each element reference ≈ 8 bytes (64-bit system)
# Tuple object itself ≈ 56 bytes overhead
# Immutable → allows internal caching and faster access

# --------------------------------------------
# Mini Project: Tuple Analyzer

tpl = (10, 20, 10, 30, 40, 10)

print("Tuple:", tpl)
print("Count of 10:", tpl.count(10))
print("Index of 30:", tpl.index(30))

# Slicing
print("Middle Elements:", tpl[1:4])

# Iterating with indices
for i, val in enumerate(tpl):
    print(f"Index {i}: {val}")

# Unpacking
a, b, *rest = tpl
print(f"a={a}, b={b}, rest={rest}")

# Converting tuple → list → tuple
tpl_list = list(tpl)
tpl_list.append(50)
tpl = tuple(tpl_list)
print("Modified Tuple:", tpl)
