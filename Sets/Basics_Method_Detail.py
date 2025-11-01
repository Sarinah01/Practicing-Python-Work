# -----------------------------------------------------------
# 📘 PYTHON SET METHODS – FULL GUIDE
# -----------------------------------------------------------
# Sets are unordered, mutable, and store UNIQUE elements.
# Methods covered:
# add(), clear(), copy(), discard(), remove(), pop(), update()
# union(), intersection(), difference(), symmetric_difference()
# intersection_update(), difference_update(), symmetric_difference_update()
# issubset(), issuperset(), isdisjoint()
# -----------------------------------------------------------

# -----------------------------------------------------------
# 1️⃣ add()
# -----------------------------------------------------------
# ✅ Purpose: Adds a single new element to the set.
# ✅ Syntax: set_name.add(element)
# ✅ Return: None
# ✅ Edge Case: If element already exists → no change
# -----------------------------------------------------------
fruits = {"apple", "banana", "mango"}
print("Before add:", fruits)
fruits.add("grapes")
print("After adding new element:", fruits)
fruits.add("apple")  # no change since already exists
print("Adding duplicate:", fruits)
print("\n")

# -----------------------------------------------------------
# 2️⃣ clear()
# -----------------------------------------------------------
# ✅ Purpose: Removes all elements from the set.
# ✅ Syntax: set_name.clear()
# ✅ Return: None
# -----------------------------------------------------------
games = {"football", "cricket", "chess"}
print("Before clear:", games)
games.clear()
print("After clear:", games)
print("\n")

# -----------------------------------------------------------
# 3️⃣ copy()
# -----------------------------------------------------------
# ✅ Purpose: Returns a shallow copy of the set.
# ✅ Syntax: set_name.copy()
# ✅ Return: New set (shallow copy)
# ✅ Edge Case: Changes in one won’t affect another.
# -----------------------------------------------------------
veggies = {"potato", "carrot", "broccoli"}
veggies_copy = veggies.copy()
veggies.add("tomato")
print("Original:", veggies)
print("Copy:", veggies_copy)
print("\n")

# -----------------------------------------------------------
# 4️⃣ discard()
# -----------------------------------------------------------
# ✅ Purpose: Removes an element if present; NO ERROR if missing.
# ✅ Syntax: set_name.discard(element)
# ✅ Return: None
# ✅ Edge Case: Safe to call even if item doesn’t exist.
# -----------------------------------------------------------
drinks = {"coffee", "tea", "juice"}
print("Before discard:", drinks)
drinks.discard("juice")
drinks.discard("milk")  # doesn’t raise an error
print("After discard:", drinks)
print("\n")

# -----------------------------------------------------------
# 5️⃣ remove()
# -----------------------------------------------------------
# ✅ Purpose: Removes an element.
# ✅ Syntax: set_name.remove(element)
# ✅ Return: None
# ✅ Edge Case: Raises KeyError if element not found.
# -----------------------------------------------------------
countries = {"India", "Japan", "USA"}
print("Before remove:", countries)
countries.remove("Japan")
print("After remove:", countries)
# countries.remove("Brazil")  # ❌ KeyError if uncommented
print("\n")

# -----------------------------------------------------------
# 6️⃣ pop()
# -----------------------------------------------------------
# ✅ Purpose: Removes & returns a RANDOM element.
# ✅ Syntax: set_name.pop()
# ✅ Return: Element removed
# ✅ Edge Case: Raises KeyError if set is empty.
# -----------------------------------------------------------
cities = {"Tokyo", "Paris", "London"}
print("Before pop:", cities)
removed = cities.pop()
print("Popped element:", removed)
print("After pop:", cities)
print("\n")

# -----------------------------------------------------------
# 7️⃣ update()
# -----------------------------------------------------------
# ✅ Purpose: Adds multiple elements (from iterable/set)
# ✅ Syntax: set_name.update(iterable1, iterable2, ...)
# ✅ Return: None
# ✅ Edge Case: Only unique elements are kept.
# -----------------------------------------------------------
set1 = {1, 2, 3}
set2 = {3, 4, 5}
set1.update(set2, [6, 7])
print("After update:", set1)
print("\n")

# -----------------------------------------------------------
# 8️⃣ union()
# -----------------------------------------------------------
# ✅ Purpose: Combines all unique elements.
# ✅ Syntax: set1.union(set2)
# ✅ Return: New set
# ✅ Edge Case: Doesn’t modify original sets.
# -----------------------------------------------------------
A = {1, 2, 3}
B = {3, 4, 5}
print("Union:", A.union(B))
print("Original A:", A)
print("\n")

# -----------------------------------------------------------
# 9️⃣ intersection()
# -----------------------------------------------------------
# ✅ Purpose: Returns common elements.
# ✅ Syntax: set1.intersection(set2)
# ✅ Return: New set
# ✅ Edge Case: Empty set if no common elements.
# -----------------------------------------------------------
print("Intersection:", A.intersection(B))
print("\n")

# -----------------------------------------------------------
# 🔟 difference()
# -----------------------------------------------------------
# ✅ Purpose: Returns elements in set1 but not in set2.
# ✅ Syntax: set1.difference(set2)
# ✅ Return: New set
# ✅ Edge Case: Empty set if no unique elements.
# -----------------------------------------------------------
print("Difference (A-B):", A.difference(B))
print("Difference (B-A):", B.difference(A))
print("\n")

# -----------------------------------------------------------
# 1️⃣1️⃣ symmetric_difference()
# -----------------------------------------------------------
# ✅ Purpose: Returns elements in either set but not both.
# ✅ Syntax: set1.symmetric_difference(set2)
# ✅ Return: New set
# -----------------------------------------------------------
print("Symmetric Difference:", A.symmetric_difference(B))
print("\n")

# -----------------------------------------------------------
# 1️⃣2️⃣ intersection_update()
# -----------------------------------------------------------
# ✅ Purpose: Updates set1 with common elements.
# ✅ Syntax: set1.intersection_update(set2)
# ✅ Return: None
# -----------------------------------------------------------
X = {2, 3, 4}
Y = {3, 4, 5}
X.intersection_update(Y)
print("After intersection_update:", X)
print("\n")

# -----------------------------------------------------------
# 1️⃣3️⃣ difference_update()
# -----------------------------------------------------------
# ✅ Purpose: Removes all elements found in another set.
# ✅ Syntax: set1.difference_update(set2)
# ✅ Return: None
# -----------------------------------------------------------
X = {1, 2, 3, 4}
Y = {3, 4, 5}
X.difference_update(Y)
print("After difference_update:", X)
print("\n")

# -----------------------------------------------------------
# 1️⃣4️⃣ symmetric_difference_update()
# -----------------------------------------------------------
# ✅ Purpose: Updates set with symmetric difference.
# ✅ Syntax: set1.symmetric_difference_update(set2)
# ✅ Return: None
# -----------------------------------------------------------
X = {1, 2, 3}
Y = {3, 4}
X.symmetric_difference_update(Y)
print("After symmetric_difference_update:", X)
print("\n")

# -----------------------------------------------------------
# 1️⃣5️⃣ issubset()
# -----------------------------------------------------------
# ✅ Purpose: Checks if all elements of one set are in another.
# ✅ Syntax: set1.issubset(set2)
# ✅ Return: True / False
# -----------------------------------------------------------
A = {1, 2}
B = {1, 2, 3}
print("A is subset of B:", A.issubset(B))
print("B is subset of A:", B.issubset(A))
print("\n")

# -----------------------------------------------------------
# 1️⃣6️⃣ issuperset()
# -----------------------------------------------------------
# ✅ Purpose: Checks if a set contains all elements of another.
# ✅ Syntax: set1.issuperset(set2)
# ✅ Return: True / False
# -----------------------------------------------------------
print("B is superset of A:", B.issuperset(A))
print("A is superset of B:", A.issuperset(B))
print("\n")

# -----------------------------------------------------------
# 1️⃣7️⃣ isdisjoint()
# -----------------------------------------------------------
# ✅ Purpose: Checks if sets have NO elements in common.
# ✅ Syntax: set1.isdisjoint(set2)
# ✅ Return: True / False
# -----------------------------------------------------------
A = {1, 2, 3}
B = {4, 5, 6}
C = {3, 7}
print("A and B disjoint:", A.isdisjoint(B))
print("A and C disjoint:", A.isdisjoint(C))
print("\n")

# -----------------------------------------------------------
# ✅ SUMMARY TABLE
# -----------------------------------------------------------
print("""
| Method Name                | Description                                      | Return Type  |
|----------------------------|--------------------------------------------------|--------------|
| add()                      | Adds single element                             | None         |
| clear()                    | Removes all elements                            | None         |
| copy()                     | Returns shallow copy                            | set          |
| discard()                  | Removes if exists, no error                     | None         |
| remove()                   | Removes, raises KeyError if not found           | None         |
| pop()                      | Removes and returns random element              | element      |
| update()                   | Adds from iterable(s)                           | None         |
| union()                    | Returns combined set                            | set          |
| intersection()             | Returns common elements                         | set          |
| difference()               | Returns elements not in others                  | set          |
| symmetric_difference()     | Returns elements in either but not both         | set          |
| intersection_update()      | Updates with common elements                    | None         |
| difference_update()        | Updates removing others’ elements               | None         |
| symmetric_difference_update() | Updates with symmetric difference           | None         |
| issubset()                 | Checks if subset                                | bool         |
| issuperset()               | Checks if superset                              | bool         |
| isdisjoint()               | Checks if no elements in common                 | bool         |
""")
