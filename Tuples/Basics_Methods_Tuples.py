# Python Tuple Methods

# Tuples are immutable sequences in Python.
# Because they are immutable, they have only 2 built-in methods:
# 1. count() - counts occurrences of a value
# 2. index() - finds the first index of a value

# --------------------------
# 1️⃣ count() Method
# --------------------------
# Purpose: Count the number of times a specified element occurs in the tuple
# Syntax: tuple_name.count(item)
# Returns: int (number of occurrences)
# Works with nested tuples/lists
# Returns 0 if item is not present

# Example 1: Counting numbers
tuple_of_numbers = (1, 3, 4, 5, 2, 4, 6)
print("Tuple of numbers:", tuple_of_numbers)
print("Count of 4:", tuple_of_numbers.count(4))  # 2
print("Count of 7:", tuple_of_numbers.count(7))  # 0

# Example 2: Counting strings
tuple_of_countries = ('India', 'USA', 'France', 'USA', 'Germany', 'India')
print("\nTuple of countries:", tuple_of_countries)
print("Count of 'India':", tuple_of_countries.count('India'))  # 2

# Example 3: Counting nested tuples and lists
given_tuple = ((4, 5), 1, (4, 5), [4, 5], (2,), 4, 5)
print("\nGiven tuple with nested elements:", given_tuple)
print("Count of (4, 5):", given_tuple.count((4, 5)))  # 2
print("Count of [4, 5]:", given_tuple.count([4, 5]))  # 1

# --------------------------
# 2️⃣ index() Method
# --------------------------
# Purpose: Returns the first index of a specified element in the tuple
# Syntax: tuple_name.index(item[, start[, end]])
# Returns: int (index of first occurrence)
# Raises ValueError if item not found

# Example 1: Basic usage
tuple_of_fruits = ('orange', 'apple', 'banana', 'mango', 'apple', 'melon')
print("\nTuple of fruits:", tuple_of_fruits)
print("Index of first 'apple':", tuple_of_fruits.index('apple'))  # 1
print("Index of 'apple' after index 3:", tuple_of_fruits.index('apple', 3))  # 4

# Example 2: Element not found
tpl_1 = (1, 3, 4, 5, 6)
try:
    print("\nIndex of 8 in tpl_1:", tpl_1.index(8))
except ValueError as e:
    print("Error:", e)  # tuple.index(x): x not in tuple

# --------------------------
# Working with tuples and lists
# --------------------------
# Tuples are immutable, but you can convert them to a list to modify
tpl_2 = (1, 3, 5, 2)
lst_2 = list(tpl_2)
lst_2.append(4)
tpl_2 = tuple(lst_2)  # Convert back to tuple
print("\nModified tuple after converting to list and back:", tpl_2)  # (1, 3, 5, 2, 4)

# --------------------------
# Mutable elements inside tuples
# --------------------------
# Tuples themselves cannot be modified, but they can contain mutable elements like lists
tpl_3 = ([1, 3], 5)
tpl_3[0].append(2)  # Modify the list inside the tuple
print("\nTuple with mutable element modified:", tpl_3)  # ([1, 3, 2], 5)

# --------------------------
# Summary Table (printed)
# --------------------------
print("\nSummary of Tuple Methods:")
print("""
Method   | Purpose                          | Returns | Notes
-------- | -------------------------------- | ------- | -------------------------------
count    | Count occurrences of an element | int     | Works with nested tuples/lists
index    | Find first index of element     | int     | Optional start/end; raises ValueError if not found
""")

# --------------------------
# Key Points
# --------------------------
# 1. Tuples are immutable → cannot add/remove elements
# 2. Only count() and index() are available
# 3. To modify tuple data, convert to a list and back
# 4. Tuples can contain mutable objects like lists
