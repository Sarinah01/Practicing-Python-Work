# Starting with the imp topics:
print('Helloo');

list = [1, 'Sarinah', 'Helloooo', {1, 2, 3}, 78.5];

print(list[-1])
print(list[-2])
print('helloo')
list.append(34)
list.extend([23, 56])
list.insert(4,[15, 16])
list.insert(3, 78)
print(list);

# updating work
# update elemnt, or the whole list
list = [34, 56,"Sarinah has changed the list"]
# list[8]=0  index error 
list[2] =984
print(list);

# removing the elemnt from the list:
# /removes the first elemnt of the list first occurence one!
list = [56, 78,65,91, 56,78, 56]
list.remove(56)
# 1st occurence removed!
print(list)

# popping method
list.pop(2)
# list.pop(10) index error

# deleting using index or other will be from 
del list
list = [1]
print(list)

# iterating the list through for nd whilw loop
for ele in list:
 
 print(ele)
 
print('printing is over!')
list.extend([12,34,6167, 93])
list.sort()

# creating new list after being orted sorting
newlist = list.sort()
# here it only points to the original list does not clones
#  for tht do this
newlist1 = sorted(list)
list.reverse()

# copy will not change the original one 
num1 = [1,2,3]
num2 = num1.copy()
num1[0] =67
print(num1)
print(num2)
# this will give problem iin nested  copying
print(newlist)
print(type(newlist))
print(min(list))
print(max(list))
print(sum(list))

print('starting thewhile loop')
i=0
while i < len(list):
 print(list[i], end=' ,')
 i +=1
 
print('while loop ended!')

# Tuples: these are same as ht of list but these re immutable
# ordered but immutable
t = (34, 'Sarinah', 'helllo', [45, 67])
emptyTuple = ()
print(emptyTuple)
# indexes -2 is also possible
# slicing: syntax: tuple[start:end] end is exclusive
print(t[1:3])
print(t[:-3]) #then only one elemnt
print(t[-3:]) #from -3 to 0
print(t[:3]) # from 0 to 3

# adding of 2 tuples
t1= ('hiii','hiii', 123, 6723)
t += t1
print(t)

# unpackign of tuples:
fruitTuple= ('Mango', 'Orange', 'Apple', 'Lichi', 'Mango')
(onevar , twovar , threevar , fourvar, fivevar)= fruitTuple
print(onevar , twovar , threevar , fourvar , sep=" , " )

# iterating through loops:
i1 = 1
for fruity in fruitTuple:
    print(fruity)
print('for loop ended!')

while i < len(fruitTuple):
    print(fruitTuple[i])
print('while loop ended here')

# some operations
#  + - works as a contcatenation of the string
#  * - repetiitin
#  in , not in - to check the membership


# Tuple methods:
#  tuplename.count(whatever item to be searched) -- give stotal occurences
print(t1.count('hiii'))
print(fruitTuple.index('Mango')) #first occurence index
# other functions -- max() , min(), len()

# python sets:
# unorderd,uniindexed ,no dupliicates, mutables
s = {1 , 1,1, 'broo' , 2.3 , True} # true=1 is not printed, false=0, so will be printed in this case
print(s) 


# methods of set --  add , delete , update(adding multiple elemnts to the set)
# remove- keyeerror if element ot be remove is not found , remove(whatever obj)
# discard - also removes but no error if not element not found 
# pop  - remove and return random elemnt from set
# clear - remove all elemnts from the set 

# creating a set of square of numbers  
set_of_squares = {i**2 for i in range(6)}  
print(set_of_squares)  
  
# creating a set of cube of numbers  
set_of_cubes = {i**3 for i in range(6)}  
print(set_of_cubes)  

# Frozenset in Python
# A frozenset is an immutable version of a set, meaning we cannot add or remove elements from it once created.
# using the frozenset() function  
imm_set = frozenset(['one', 'two', 'three', 'four', 'five'])  
  
# printing results  
print(imm_set)  
print(type(imm_set))  

# creating a set  
vegetable_set = {'potato', 'eggplant', 'tomato', 'cabbage', 'broccoli'}  
# printing the set  
print("Given Set:", vegetable_set)  
  
# using the copy() method  
dummy_set = vegetable_set.copy()  
  
# printing the updated set    
print("Dummy Set:", dummy_set)

# creating a set  
state_set = {'New York', 'Delhi', 'Tokyo', 'Penang', 'Ontario'}  
# printing the set  
print("Given Set:", state_set)  
  
# using the pop() method  
popped_item = state_set.pop()  
  
# printing the updated set  
print("Updated Set:", state_set)  
print("Popped Element:", popped_item)    

# given sets  
num_set_1 = {4, 7, 8, 11, 19}  
num_set_2 = {2, 5, 7, 8, 10}  
print("Set 1:", num_set_1)  
print("Set 2:", num_set_2)  
  
# using the update() method  
num_set_1.update(num_set_2)  
  
# printing the updated set  
print("Updated Set:", num_set_1)  

# Python Dictionaries
# A Python Dictionary is one of the built-in data types used to store data in 'key: value' pairs. The dictionary is an unordered, mutable and 
# indexed collection where each key is unique and maps to a value. 
# creating dictionaries  
dict_zero = {}     # empty dictionary  
dict_one = {"name": "Lucy", "age": 19, "city": "New Jersey"} # using {}  
dict_two = dict(name = "John", age = 21, city = "Havana")  # using dict()  
  
# printing the results  
print("Empty Dictionary:", dict_zero)  
print("Dictionary 1 (created using {}):", dict_one)  
print("Dictionary 2 (created using dict()):", dict_two) 
# accessing dictionary items using keys  
# print("Name:", dict_x["name"])  
# print("Age:", dict_x["age"])  
# accessing dictionary items using get()  
# print("Gender:", dict_x.get("gender"))  
# print("Profession:", dict_x.get("profession"))  

# removing items from the dictionary  
# del dict_x['age']     # using del  
# print("Updated Dictionary (Removed 'age'):", dict_x)  
  
# popped_value = dict_x.pop('gender')  # using pop()  
# print("Updated Dictionary (Removed 'gender'):", dict_x)  
# print("Popped Value:", popped_value)  

# popped_item = dict_x.popitem()  # using popitem()  
# print("Updated Dictionary (Removed last item):", dict_x)  
# print("Popped Item:", popped_item)  
  
# dict_x.clear()  # using clear()  
# print("Update Dictionary (Removed all items):", dict_x) 

# iterating through a dictionary using for loop  
# for key in dict_x:  
#   value = dict_x[key]  
#   print(key, "->", value)  
  
# simple example to check membership   
dict_y = {  
    'fruit': 'apple',  
    'vegetable': 'onion',  
    'dry-fruit': 'resins'  
}  
# using 'in' and 'not in' operators  
print("Is 'fruit' a member of 'dict_y'?:", 'fruit' in dict_y)  
print("Is 'beverage' a member of 'dict_y'?:", 'beverage' in dict_y)  
print("Is 'beverage' NOT a member of 'dict_y'?:", 'beverage' not in dict_y)  

# given dictionary  
dict_one = {'name': 'Sachin', 'age': 22}  
dict_two = {'salary': 69000, 'profession': 'software engineer'}  
print("Given Dictionary:", dict_one)  
  
# using the update() method  
dict_one.update(dict_two)  
  
print("Updated Dictionary:", dict_one)  

# python built in functions:
def welcomemessage():
    print("Hello, Welcome to this function!")

welcomemessage()
print(callable(welcomemessage))

# module:
# function to add two numbers  
def add(a, b):  
  return a + b  
  
# function to subtract two numbers  
def subtract(a, b):  
  return a - b  
  
# function to multiply two numbers  
def multiply(a, b):  
  return a * b  
# We have saved this file as calculator.py.
# importing the module  
# import calculator  
# total = calculator.add(num_1, num_2)  

# Exception Handling:
def divide(a, b):  
    if b == 0:  
        raise Exception(" Cannot divide by zero. ")  
    return a / b  
try:  
    result = divide(10, 0)  
except Exception as e:  
    print(" An error occurred: ", e)  
    
# File handling:
f = open("file.txt", "r")  
# "r" → Read (default, error if file doesn't exist)
# "w" → Write (creates new or overwrites existing file)
# "a" → Append (adds data at the end of the file)
# "x" → Create (error if file already exists)
# "b" → Binary mode (e.g., "rb", "wb")
# "t" → Text mode (default, e.g., "rt", "wt")

with open("file.txt", "r") as f:  
    content = f.read()      # To Read the entire file  
    line = f.readline()     # To Read one line  
    lines = f.readlines()   # To read all lines into a list  
    
import csv  
  
# opening the CSV file  
with open('companies.csv', newline='') as file:  
    # using the reader() function to read the content of the file  
    reader = csv.reader(file)  
  
    # printing each row of the table  
    for row in reader:  
        print(row)  