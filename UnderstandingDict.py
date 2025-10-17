# Dictionary Basics
# dict = {"key1": value1, "key2": value2}

# Mutable → can add, remove, and update elements
# Ordered (Python 3.7+) → preserves insertion order
# Keys must be hashable (immutable types like str, int, tuple)
# Values can be any type (mutable or immutable)
# Stored as hash table internally → fast lookup O(1) average

# --------------------------------------------
# Creating Dictionaries

# Using {}
d = {"a": 1, "b": 2, "c": 3}
print(d)  # {'a': 1, 'b': 2, 'c': 3}

# Using dict() constructor
d2 = dict(x=10, y=20)
print(d2)  # {'x': 10, 'y': 20}

# From list of tuples
d3 = dict([("name", "Alice"), ("age", 25)])
print(d3)

# Empty dict
d4 = {}
print(type(d4))  # <class 'dict'>

# Edge case: duplicate keys → last value wins
d = {"a": 1, "a": 100}
print(d)  # {'a': 100}

# --------------------------------------------
# Accessing Elements

d = {"a": 1, "b": 2, "c": 3}

# Using key
print(d["a"])  # 1
# KeyError if key does not exist
# print(d["z"])  # ❌ KeyError

# Using get() → returns None or default
print(d.get("b"))        # 2
print(d.get("z"))        # None
print(d.get("z", 0))     # 0

# --------------------------------------------
# Adding / Updating Elements

d["d"] = 4       # Add new key
d["a"] = 100     # Update existing key
print(d)  # {'a': 100, 'b': 2, 'c': 3, 'd': 4}

# update() → add multiple key-value pairs
d.update({"e": 5, "f": 6})
print(d)

# Edge cases:
# update() can take another dict, iterable of pairs, or keyword arguments

# --------------------------------------------
# Removing Elements

# pop(key) → removes key and returns value
val = d.pop("b")
print(val)  # 2
# KeyError if key not found

# pop(key, default) → returns default if key not found
val = d.pop("z", 0)
print(val)  # 0

# popitem() → removes last inserted key-value pair
kv = d.popitem()
print(kv)  # e.g., ('f', 6)
# KeyError if dict is empty

# del → delete key or entire dict
del d["a"]
# del d  → deletes entire dict

# clear() → remove all items
d.clear()
print(d)  # {}

# --------------------------------------------
# Dictionary Methods

d = {"a": 1, "b": 2, "c": 3}

# keys() → view of keys
print(d.keys())  # dict_keys(['a', 'b', 'c'])

# values() → view of values
print(d.values())  # dict_values([1, 2, 3])

# items() → view of (key, value) tuples
print(d.items())  # dict_items([('a',1),('b',2),('c',3)])

# setdefault(key, default) → returns value if key exists, else sets to default
val = d.setdefault("d", 4)
print(d)  # {'a':1,'b':2,'c':3,'d':4}

# copy() → shallow copy
d2 = d.copy()
d2["a"] = 999
print(d)   # original unchanged
print(d2)  # modified copy

# --------------------------------------------
# Iterating Dictionaries

for k in d:
    print(k, d[k])   # keys by default

for k, v in d.items():
    print(k, v)

# --------------------------------------------
# Dictionary Comprehensions

squares = {x: x*x for x in range(5)}
print(squares)  # {0:0,1:1,2:4,3:9,4:16}

# Conditional comprehension
even_squares = {x: x*x for x in range(6) if x%2==0}
print(even_squares)  # {0:0,2:4,4:16}

# --------------------------------------------
# Nested Dictionaries

students = {
    "Alice": {"age": 20, "grade": "A"},
    "Bob": {"age": 22, "grade": "B"}
}
print(students["Alice"]["grade"])  # A

# --------------------------------------------
# Memory and Hashability Notes

# Keys must be hashable (immutable types) → str, int, float, tuple
# Values can be anything
# Dicts are hash tables → fast access (O(1) avg)
# Internal structure stores key hash → memory slot
# Mutable keys (list, dict, set) not allowed → unhashable

# --------------------------------------------
# Mini Project: Word Frequency Counter

text = "python is easy and python is powerful"
words = text.split()

freq = {}
for word in words:
    freq[word] = freq.get(word, 0) + 1

print("Word frequency:", freq)

# Using dict comprehension
freq2 = {word: words.count(word) for word in set(words)}
print("Word frequency (dict comp):", freq2)
