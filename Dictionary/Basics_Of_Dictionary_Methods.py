# Python Dictionaries - Quick Revision
# Date: 28 Apr 2025
# Read Time: ~9 min

# --------------------------------------
# 1️⃣ What is a Python Dictionary?
# --------------------------------------
# - Built-in data type that stores data in key: value pairs
# - Mutable: Can add, remove, or update items
# - Indexed: Access values using keys (keys act like indexes)
# - Unordered (before Python 3.7); ordered from Python 3.7+
# - Keys are unique
# - Values can be any type
# - Example:
D = {1: 'Learn', 2: 'Python', 3: 'from', 4: 'Tpoint', 5: 'Tech'}
print("Dictionary D:", D)

# --------------------------------------
# 2️⃣ Creating Dictionaries
# --------------------------------------
# Using {} or dict()
dict_zero = {}  # Empty dictionary
dict_one = {"name": "Lucy", "age": 19, "city": "New Jersey"}
dict_two = dict(name="John", age=21, city="Havana")
print("\nEmpty Dictionary:", dict_zero)
print("Dictionary using {}:", dict_one)
print("Dictionary using dict():", dict_two)

# --------------------------------------
# 3️⃣ Accessing Dictionary Items
# --------------------------------------
dict_x = {"name": "Sachin", "age": 18, "gender": "male", "profession": "student"}
print("\nAccess using key:", dict_x["name"])        # Sachin
print("Access using get():", dict_x.get("gender"))  # male

# --------------------------------------
# 4️⃣ Adding Items
# --------------------------------------
dict_x["country"] = "India"  # Add new key-value
print("\nAfter Adding 'country':", dict_x)

# --------------------------------------
# 5️⃣ Removing Items
# --------------------------------------
dict_x = {"name": "Sachin", "age": 18, "gender": "male", "profession": "student", "country": "India"}
print("\nOriginal Dictionary:", dict_x)

# Using del
del dict_x["age"]
print("After del 'age':", dict_x)

# Using pop()
popped_value = dict_x.pop("gender")
print("After pop 'gender':", dict_x)
print("Popped Value:", popped_value)

# Using popitem() - removes last inserted item
popped_item = dict_x.popitem()
print("After popitem():", dict_x)
print("Popped Item:", popped_item)

# Using clear() - remove all items
dict_x.clear()
print("After clear():", dict_x)

# --------------------------------------
# 6️⃣ Changing Items
# --------------------------------------
dict_x = {"name": "Sachin", "age": 18, "gender": "male", "profession": "student", "country": "India"}
dict_x["age"] = 20
dict_x["profession"] = "developer"
print("\nAfter Updating 'age' and 'profession':", dict_x)

# --------------------------------------
# 7️⃣ Iterating Through Dictionary
# --------------------------------------
dict_iter = {"Name": "Sachin", "Age": 18, "Gender": "Male", "Profession": "Student", "Country": "India"}
print("\nIterating through dict_iter:")
for key in dict_iter:
    print(key, "->", dict_iter[key])

# --------------------------------------
# 8️⃣ Length of a Dictionary
# --------------------------------------
employees_info = {
    "John": "Sr. Software Developer",
    "Irfan": "UI/UX Designer",
    "Lucy": "Human Resource Manager",
    "Peter": "Team Lead",
    "Johnson": "Business Developer"
}
print("\nEmployees Info:", employees_info)
print("Length of employees_info:", len(employees_info))  # 5

# --------------------------------------
# 9️⃣ Dictionary Membership Test
# --------------------------------------
dict_y = {'fruit': 'apple', 'vegetable': 'onion', 'dry-fruit': 'resins'}
print("\nIs 'fruit' in dict_y?", 'fruit' in dict_y)        # True
print("Is 'beverage' in dict_y?", 'beverage' in dict_y)    # False
print("Is 'beverage' NOT in dict_y?", 'beverage' not in dict_y)  # True

# --------------------------------------
# ✅ Summary Points for Quick Revision
# --------------------------------------
# - Dictionaries store data in key: value pairs
# - Mutable: add, update, delete items
# - Keys are unique and immutable
# - Access values via keys or get() method
# - Iteration is done through keys
# - len() gives number of key-value pairs
# - 'in' checks if key exists
# - Methods: del, pop, popitem, clear
