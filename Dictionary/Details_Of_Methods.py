# Python Dictionary Methods - Quick Revision

# --------------------------------------
# 1️⃣ get()
# --------------------------------------
# Returns the value for the given key if it exists, otherwise returns default (None if not specified)
# Syntax: dict_name.get(key, default)
# Return type: value corresponding to key or default
# Edge case: Does NOT raise KeyError
dict_one = {'name': 'Sachin', 'age': 22}
print("get('name'):", dict_one.get('name'))           # Sachin
print("get('salary'):", dict_one.get('salary', 'Not Found'))  # Not Found

# --------------------------------------
# 2️⃣ update()
# --------------------------------------
# Adds new items or updates existing key-value pairs from another dict/iterable
# Syntax: dict_name.update(other_dict)
# Return type: None (in-place update)
dict_two = {'salary': 69000, 'profession': 'software engineer'}
dict_one.update(dict_two)
print("\nAfter update:", dict_one)  

# --------------------------------------
# 3️⃣ copy()
# --------------------------------------
# Returns a shallow copy of the dictionary
# Syntax: new_dict = old_dict.copy()
# Return type: dict
# Edge case: Nested objects are not deep-copied
new_dict = dict_one.copy()
print("\nCopy of dict:", new_dict)

# --------------------------------------
# 4️⃣ pop()
# --------------------------------------
# Removes key and returns its value; can provide default to avoid KeyError
# Syntax: dict_name.pop(key, default)
# Return type: value of removed key
popped_value = dict_one.pop('age')
print("\nPopped 'age':", popped_value)
# dict_one.pop('nonexistent')  # Would raise KeyError
popped_default = dict_one.pop('nonexistent', 'Default Value')
print("Popped non-existent key with default:", popped_default)

# --------------------------------------
# 5️⃣ popitem()
# --------------------------------------
# Removes and returns the last inserted key-value pair as a tuple
# Syntax: dict_name.popitem()
# Return type: tuple (key, value)
popped_item = dict_one.popitem()
print("\nPopped last item:", popped_item)
# dict_one.clear()
# dict_one.popitem()  # KeyError if dict is empty

# --------------------------------------
# 6️⃣ clear()
# --------------------------------------
# Removes all items from dictionary
# Syntax: dict_name.clear()
# Return type: None
dict_one.clear()
print("\nAfter clear():", dict_one)

# --------------------------------------
# 7️⃣ keys()
# --------------------------------------
# Returns a view object of all keys
# Syntax: dict_name.keys()
# Return type: dict_keys
dict_one = {'name': 'Sachin', 'age': 22}
print("\nKeys:", dict_one.keys())

# --------------------------------------
# 8️⃣ fromkeys()
# --------------------------------------
# Creates a new dictionary with keys from sequence and values as default
# Syntax: dict.fromkeys(keys, value)
# Return type: dict
keys = ['first_name', 'last_name', 'job']
new_dict = dict.fromkeys(keys, 'Unknown')
print("\nFromKeys:", new_dict)

# --------------------------------------
# 9️⃣ items()
# --------------------------------------
# Returns a view object of key-value pairs as tuples
# Syntax: dict_name.items()
# Return type: dict_items
print("\nItems:", dict_one.items())

# --------------------------------------
# 10️⃣ setdefault()
# --------------------------------------
# Returns value if key exists, otherwise inserts key with default value
# Syntax: dict_name.setdefault(key, default)
# Return type: value of key
age = dict_one.setdefault('age', 25)        # returns existing 22
salary = dict_one.setdefault('salary', 69000)  # adds 'salary':69000
print("\nAge:", age)
print("Salary:", salary)
print("After setdefault:", dict_one)

# --------------------------------------
# 11️⃣ values()
# --------------------------------------
# Returns a view object of all values
# Syntax: dict_name.values()
# Return type: dict_values
print("\nValues:", dict_one.values())

# --------------------------------------
# 🔹 FAQs / Edge Cases
# --------------------------------------
# 1. get() vs []: get() returns default if key not found; [] raises KeyError
d = {'a': 1}
print("\nget('b'):", d.get('b'))  # None
# print(d['b'])  # KeyError

# 2. pop() vs popitem(): pop() removes specific key; popitem() removes last inserted
# 3. copy() creates shallow copy; nested mutable objects not deeply copied
original = {'a': [1, 2]}
shallow = original.copy()
shallow['a'].append(3)
print("\nShallow copy edge case:", original)  # {'a':[1,2,3]}

# 4. Keys must be immutable; lists/dictionaries cannot be keys
# 5. setdefault() on existing key does NOT change value; on missing key it adds the key
