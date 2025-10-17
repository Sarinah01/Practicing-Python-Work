# ===================================================
# Python Functions & Modules Basics
# ===================================================

# ---------------------------
# 1️⃣ Regular Functions (def)
# ---------------------------

# Syntax:
# def function_name(parameters):
#     """Optional docstring"""
#     statement(s)
#     return value (optional)

def add(a, b):
    """Add two numbers"""
    return a + b

print(add(5, 3))  # 8

def greet(name="User"):
    print(f"Hello, {name}!")

greet("Sarinah")  # Hello, Sarinah!
greet()           # Hello, User!

# Multiple return values
def operations(x, y):
    return x+y, x-y, x*y, x/y

print(operations(10, 2))  # (12, 8, 20, 5.0)

# Keyword arguments, positional arguments, default arguments
def describe_person(name, age=18, city="Unknown"):
    print(f"{name} is {age} years old from {city}.")

describe_person("Alice")
describe_person("Bob", city="Paris")

# Arbitrary number of arguments
def sum_all(*args):
    return sum(args)

print(sum_all(1,2,3,4,5))  # 15

# Arbitrary keyword arguments
def show_info(**kwargs):
    print(kwargs)

show_info(name="Alice", age=25)

# -----------------------------------
# 2️⃣ Lambda Functions (Anonymous)
# -----------------------------------

# Syntax: lambda arguments: expression
square = lambda x: x**2
print(square(5))  # 25

add = lambda a,b: a+b
print(add(3,4))   # 7

# Using with map()
nums = [1,2,3,4]
squared = list(map(lambda x: x**2, nums))
print(squared)  # [1,4,9,16]

# Using with filter()
even = list(filter(lambda x: x%2==0, nums))
print(even)  # [2,4]

# Using with sorted() key
words = ["apple", "banana", "kiwi"]
sorted_words = sorted(words, key=lambda x: len(x))
print(sorted_words)  # ['kiwi','apple','banana']

# Using with reduce()
from functools import reduce
sum_all = reduce(lambda x, y: x+y, nums)
print(sum_all)  # 10

# Mini project: Double even numbers
result = list(map(lambda x: x*2 if x%2==0 else x, nums))
print(result)  # [1,4,3,8]

# ---------------------------
# 3️⃣ Modules in Python
# ---------------------------

# Modules = pre-written Python files with useful functions, classes, variables

# 1) Math Module
import math

print(math.sqrt(16))      # 4.0
print(math.ceil(4.2))     # 5
print(math.floor(4.7))    # 4
print(math.factorial(5))  # 120
print(math.pi)            # 3.141592653589793

# 2) Random Module
import random

print(random.random())    # Random float [0,1)
print(random.randint(1,10))  # Random int [1,10]
lst = [1,2,3,4,5]
print(random.choice(lst))     # Random element
random.shuffle(lst)
print(lst)                    # Shuffled list

# 3) Time Module
import time

print(time.time())         # current epoch time
time.sleep(1)              # pause program for 1 second
print("Slept for 1 second")

# 4) OS Module
import os

print(os.name)             # OS type
print(os.getcwd())         # current working directory
# os.mkdir("test_folder")  # create folder (uncomment to run)
# os.remove("file.txt")    # remove file

# 5) Sys Module
import sys

print(sys.version)         # Python version
print(sys.path)            # list of paths Python searches for modules

# 6) Random + Functional Mini Project
# Guess the number game
number = random.randint(1,20)
guess = -1
while guess != number:
    guess = random.randint(1,20)
    print(f"Trying {guess}...")
print(f"Number {number} guessed correctly!")

# 7) Math Mini Project
# Area of circle function using math module
def circle_area(r):
    return math.pi * r**2

print(circle_area(5))  # 78.53981633974483

# 8) Time Mini Project
start = time.time()
for i in range(1000000):
    pass
end = time.time()
print("Time taken for loop:", end-start)

# 9) OS Mini Project
# List all Python files in current folder
files = [f for f in os.listdir() if f.endswith(".py")]
print("Python files in folder:", files)

