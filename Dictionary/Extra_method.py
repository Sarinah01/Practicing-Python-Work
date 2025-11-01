# -----------------------------------------------------------
# 📘 Dictionary Methods Demonstration
# Methods Covered: fromkeys(), setdefault(), keys(), values()
# -----------------------------------------------------------

# ------------------------------
# 1️⃣ fromkeys() Method
# ------------------------------
# Creates a new dictionary from a sequence of keys and assigns them a common value.
# Syntax: dict.fromkeys(keys, value)
# Returns → a new dictionary

# Example 1: Simple usage
keys = ['name', 'age', 'city']
new_dict = dict.fromkeys(keys, 'Unknown')
print("Example 1 - fromkeys() simple:", new_dict)
# Output: {'name': 'Unknown', 'age': 'Unknown', 'city': 'Unknown'}

# Example 2: Edge case with mutable default value
# ⚠️ If default value is mutable (like list), all keys share the same reference
keys = ['a', 'b']
d = dict.fromkeys(keys, [])
d['a'].append(1)
print("Example 2 - fromkeys() mutable edge case:", d)
# Output: {'a': [1], 'b': [1]} — both keys share same list!

# Use case:
# Quick initialization of dictionary with fixed keys.
default_config = dict.fromkeys(['theme', 'volume', 'brightness'], 'default')
print("Use case - default settings:", default_config)
print("\n")

# ------------------------------
# 2️⃣ setdefault() Method
# ------------------------------
# Returns the value for a key if it exists, else inserts it with the default value.
# Syntax: dict.setdefault(key, default)
# Returns → value of that key (existing or new)

dict_x = {'name': 'Alice', 'age': 25}

# Case 1: Existing key (no change)
age = dict_x.setdefault('age', 30)
print("Case 1 - setdefault() existing key:", age)
print("Dictionary:", dict_x)
# Output: 25 (no change, as 'age' already existed)

# Case 2: New key (added with default)
salary = dict_x.setdefault('salary', 50000)
print("Case 2 - setdefault() new key:", salary)
print("Dictionary after adding salary:", dict_x)
# Output: {'name': 'Alice', 'age': 25, 'salary': 50000}

print("\n")

# ------------------------------
# 3️⃣ keys() Method
# ------------------------------
# Returns a view object containing all keys in the dictionary.
# Syntax: dict.keys()
# Returns → dict_keys object (dynamic view)

dict_y = {'name': 'Bob', 'age': 28}
print("Initial keys:", dict_y.keys())

# Dynamic behavior → reflects changes
dict_y['city'] = 'Paris'
print("After adding 'city':", dict_y.keys())
# Output changes automatically
print("Converted to list:", list(dict_y.keys()))
print("\n")

# ------------------------------
# 4️⃣ values() Method
# ------------------------------
# Returns a view object containing all values.
# Syntax: dict.values()
# Returns → dict_values object (dynamic view)

print("Initial values:", dict_y.values())

# Dynamic behavior again
dict_y['country'] = 'France'
print("After adding 'country':", dict_y.values())
# Output updates dynamically as dictionary changes
print("Converted to list:", list(dict_y.values()))
print("\n")

# ------------------------------
# ✅ Summary
# ------------------------------
print("Quick Summary:")
print("""
fromkeys()   → Creates a dict from keys with same value.
setdefault() → Returns value if key exists, else adds it.
keys()       → Dynamic view of all keys.
values()     → Dynamic view of all values.
""")
