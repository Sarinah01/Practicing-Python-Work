# Set Basics
# st = {10, 20, 30}

# Unordered → no defined index or position
# Mutable → can add or remove elements
# Unique elements only → duplicates auto removed
# Holds references to immutable objects (int, str, tuple, etc.)
# Sets cannot contain lists or other sets (unhashable types)

# --------------------------------------------
# Creating Sets

st = {1, 2, 3}
print(st)  # {1, 2, 3}

st2 = set([1, 2, 3, 2, 1])  # from iterable
print(st2)  # {1, 2, 3}

# Empty Set
st3 = set()
print(type(st3))  # <class 'set'>

# {} creates empty dictionary, not a set
# st4 = {} → type(st4) = dict

# Edge Case: duplicates removed automatically
st = {1, 2, 2, 3, 3}
print(st)  # {1, 2, 3}

# --------------------------------------------
# Accessing Elements

# No indexing or slicing allowed
# st[0] → TypeError
# Can only iterate or check membership

for val in st:
    print(val)

print(2 in st)   # True
print(5 not in st)  # True

# --------------------------------------------
# Adding Elements

st = {1, 2}
st.add(3)
print(st)  # {1, 2, 3}

# add() inserts single element
# If element already exists → no change, no error

# update() → add multiple elements (iterables)
st.update([4, 5, 6]) #{1, 2, 3, 4, 5, 6}
st.update({7, 8})
st.update("Hi")
print(st)
# All elements from iterables are added individually

# Edge Cases:
# add() with unhashable types → TypeError
# st.add([1, 2]) → ❌ TypeError: unhashable type: 'list'

# --------------------------------------------
# Removing Elements

st = {1, 2, 3, 4}

# remove(x) → deletes element, raises error if not present
st.remove(2)
print(st)  # {1, 3, 4}
# st.remove(9) → KeyError if not found

# discard(x) → deletes element if found, no error otherwise
st.discard(4)
st.discard(9)  # no error
print(st)

# pop() → removes random element (since unordered)
val = st.pop()
print("Removed:", val)
print("After pop:", st)
# KeyError if set is empty

# clear() → removes all elements
st.clear()
print(st)  # set()

# del st → deletes entire set
# Access after del st → NameError

# --------------------------------------------
# Set Operations (Mathematical)

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

# Union
print(A | B)           # {1,2,3,4,5,6}
print(A.union(B))      # same result

# Intersection
print(A & B)           # {3,4}
print(A.intersection(B))

# Difference
print(A - B)           # {1,2}
print(B - A)           # {5,6}

# Symmetric Difference → elements in A or B but not both
print(A ^ B)           # {1,2,5,6}
print(A.symmetric_difference(B))

# Update versions (modify in place)
A = {1, 2, 3}
B = {3, 4}
A.update(B)
print(A)               # {1,2,3,4}

A = {1, 2, 3}
A.intersection_update(B)
print(A)               # {3}

A = {1, 2, 3, 4}
A.difference_update({3, 4})
print(A)               # {1, 2}

A = {1, 2, 3, 4}
A.symmetric_difference_update({3, 4, 5})
print(A)               # {1,2,5}

# --------------------------------------------
# Subset, Superset, and Disjoint

A = {1, 2, 3}
B = {1, 2, 3, 4, 5}
C = {7, 8}

print(A.issubset(B))       # True
print(B.issuperset(A))     # True
print(A.isdisjoint(C))     # True (no common elements)

# --------------------------------------------
# Copying Sets

A = {1, 2, 3}
B = A.copy()
B.add(4)
print(A)  # {1, 2, 3}
print(B)  # {1, 2, 3, 4}

# Shallow copy → independent top-level set

# --------------------------------------------
# Frozen Set (Immutable Set)

A = frozenset([1, 2, 3])
# A.add(4) → AttributeError: 'frozenset' object has no attribute 'add'
print(A)

# Supports union, intersection, difference, etc.
B = frozenset([3, 4, 5])
print(A | B)   # frozenset({1, 2, 3, 4, 5})

# --------------------------------------------
# Set Comprehensions

squares = {x*x for x in range(6)}
print(squares)  # {0, 1, 4, 9, 16, 25}

# --------------------------------------------
# Memory and Performance Notes

# Sets store elements as hash table → O(1) average time for add, remove, lookup
# Each element’s hash() determines its bucket
# Random order because based on internal hash mapping
# Approx memory = overhead (56 bytes) + per element (72 bytes avg on 64-bit)

# --------------------------------------------
# Mini Project: Unique Word Extractor

text = "python is great and python is easy to learn and powerful"
words = text.split()
unique_words = set(words)

print("Unique words:", unique_words)
print("Total unique words:", len(unique_words))

# Add a new word
unique_words.add("developer")

# Remove a word safely
unique_words.discard("easy")

# Sort and display
print("Sorted:", sorted(unique_words))
