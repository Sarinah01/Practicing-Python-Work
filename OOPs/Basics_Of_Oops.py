"""
🎯 PYTHON CLASSES COMPLETE GUIDE (With Examples & Edge Cases)

This file demonstrates:
✅ What is a Class and Object
✅ Constructor (__init__)
✅ Instance & Class Variables
✅ Instance Methods, Class Methods, Static Methods
✅ Encapsulation (Private variables)
✅ Inheritance
✅ Polymorphism
✅ Magic Methods (__str__, __repr__, __len__, __add__)
"""

# -----------------------------
# 1️⃣ BASIC CLASS & OBJECT
# -----------------------------
class Student:
    # Class variable → shared by all instances
    school_name = "Tech Academy"

    # Constructor (automatically called when object created)
    def __init__(self, name, marks):
        self.name = name               # instance variable
        self.marks = marks             # instance variable

    # Instance Method → works on object data
    def display(self):
        print(f"Student Name: {self.name}, Marks: {self.marks}")

    # Class Method → works on class data
    @classmethod
    def change_school(cls, new_name):
        cls.school_name = new_name

    # Static Method → doesn’t depend on class or object
    @staticmethod
    def is_pass(marks):
        return marks >= 33


# Create Object
s1 = Student("Alice", 85)
s2 = Student("Bob", 25)

s1.display()    # → Student Name: Alice, Marks: 85
print(Student.school_name)  # → Tech Academy

# Change class variable using class method
Student.change_school("Python Academy")
print(Student.school_name)  # → Python Academy

# Static Method Usage
print(Student.is_pass(40))  # → True
print(Student.is_pass(20))  # → False

# -----------------------------
# 2️⃣ ENCAPSULATION
# -----------------------------
class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance     # private variable (name mangling)

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("❌ Insufficient funds!")

    def show_balance(self):
        print(f"{self.owner}'s Balance: ₹{self.__balance}")

# Edge case: Direct access to __balance gives error
acc = Account("Sarinah", 5000)
acc.deposit(2000)
acc.withdraw(8000)  # Insufficient funds
acc.show_balance()

# print(acc.__balance)  # ❌ AttributeError (private)
print(acc._Account__balance)  # ✅ Accessed using name mangling

# -----------------------------
# 3️⃣ INHERITANCE
# -----------------------------
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Some sound"

class Dog(Animal):   # Dog inherits Animal
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

dog = Dog("Buddy")
cat = Cat("Whiskers")

print(dog.name, "→", dog.speak())   # → Buddy → Woof!
print(cat.name, "→", cat.speak())   # → Whiskers → Meow!

# -----------------------------
# 4️⃣ POLYMORPHISM
# -----------------------------
animals = [dog, cat]
for a in animals:
    print(f"{a.name} says: {a.speak()}")

# Same method name → different behaviors

# -----------------------------
# 5️⃣ MAGIC (DUNDER) METHODS
# -----------------------------
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"     # Used by print()

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"  # Developer representation

    def __add__(self, other):
        # Vector addition
        return Vector(self.x + other.x, self.y + other.y)

    def __len__(self):
        # Return length of vector (rounded)
        return int((self.x**2 + self.y**2) ** 0.5)

v1 = Vector(3, 4)
v2 = Vector(1, 2)
v3 = v1 + v2

print(v1)          # → (3, 4)
print(repr(v3))    # → Vector(4, 6)
print(len(v1))     # → 5 (since √(3²+4²)=5)

# Edge case: Adding incompatible type
try:
    print(v1 + 5)
except AttributeError as e:
    print("⚠️ Error:", e)

# -----------------------------
# 6️⃣ BUILT-IN CLASS METHODS DEMO
# -----------------------------
class Employee:
    company = "OpenAI"

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __str__(self):
        return f"{self.name} ({self.salary})"

    def __eq__(self, other):
        return self.salary == other.salary

    def __lt__(self, other):
        return self.salary < other.salary

e1 = Employee("A", 50000)
e2 = Employee("B", 60000)
e3 = Employee("C", 50000)

print(e1 == e3)   # True (equal salary)
print(e1 < e2)    # True (less salary)
print(sorted([e1, e2, e3], key=lambda e: e.salary))  # sort using attr

# -----------------------------
# 7️⃣ EDGE CASES
# -----------------------------
# - Calling class without __init__ args → TypeError
try:
    s3 = Student()
except TypeError as e:
    print("⚠️ Constructor Error:", e)

# - Accessing private variable directly → AttributeError
try:
    print(acc.__balance)
except AttributeError as e:
    print("⚠️ Private Access Error:", e)

# - Using isinstance() and issubclass()
print(isinstance(dog, Animal))   # True
print(issubclass(Dog, Animal))   # True

# -----------------------------
# ✅ SUMMARY
# -----------------------------
"""
CLASS CONCEPTS QUICK NOTES:

🔹 Class → Blueprint of object
🔹 Object → Instance of a class
🔹 __init__ → Constructor, auto-called
🔹 self → Reference to current object
🔹 Class variable → Shared among all objects
🔹 Instance variable → Unique to each object
🔹 @classmethod → Works with class data
🔹 @staticmethod → Independent of class/object
🔹 Encapsulation → Hide data using private vars
🔹 Inheritance → Reuse parent features
🔹 Polymorphism → Same method, diff behavior
🔹 Magic methods (__str__, __add__, etc.) → Operator overloading/custom behavior
"""
