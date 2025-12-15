# # You own a pizzeria named Olly’s Pizzas and want to create a Python program
# # to handle the customers and revenue. 
# # Create the following classes with the following methods:
# class InvalidToppings(Exception):
#     pass
# class InvalidCheese(Exception):
#     pass
# class Pizza:
    
    
#     def __init__(self, size , toppings, cheese):
#         self.size = size
#         self.toppings =  toppings
#         self.cheese= cheese
#         print(self.size , self.toppings, self.cheese)
#     def price(self):
#         self.bill = self.sizing = self.tops = self.chprice = 0
#         if self.size == "s":
#             self.sizing +=50
#         elif self.size=="m":
#             self.sizing+=100
#         else:
#             self.sizing +=200

#         for temp in self.toppings:
#             if temp not in ["brocolli" , "olives","mushrooms"]:
#                 self.tops += 70
#             else:
#                 self.tops+=50
        
#         self.chprice += 50 * len(self.cheese)
            
#         self.bill = self.sizing + self.tops + self.chprice
#         print(f"Cheese price {self.chprice} , Toppings {self.tops} , Size {self.sizing}")
#         print("The total bill is: ", self.bill)
#         return self.bill   

# class Order:
#     customerid = 0
#     def __init__(self, name):
#         self.name = name
#         self.customerid +=1
#     def order(self):
#         self.pizzas = []        
#         number = int(input("Ennter the nos. of pizzas u want to buy? "))
#         for i in range(number):
#             tops = []
#             cheese = []
#             size = input(f"Enter the size for pizza {i+1} : ")
#             ntoppings = int(input("Enter the nos of toppings u want to add? "))
   
#             for j in range(ntoppings):
#                while True:
#                    try :
#                         topping = input(f"Enter the [{j+1}] toppings for pizza {i+1} : ")
#                         if topping not in ['corn', 'tomato', 'onion','capsicum','mushroom', 'olives', 'broccoli']:
#                             raise InvalidToppings("Invalid Topping selected! ")
#                         else:
#                               tops.append(topping)
#                               break
#                    except InvalidToppings as e:
#                         print("Enter properly: ", e)                
#             ncheese = int(input("Enter the nos of cheese u want to add? "))
   
#             for k in range(ncheese):
#                while True:
#                    try :
#                         ch = input(f"Enter the [{k+1}]cheese for pizza {i+1}: ")
#                         if ch not in ["mozzarella", "feta", "cheddar"]:
#                             raise InvalidToppings("Invalid cheese selected! ")
                        
#                         else:
#                               cheese.append(ch)
#                               break
                        
#                    except InvalidToppings as e:
#                         print("Enter properly: ", e)


#             self.pizzas.append(Pizza(size, tops,cheese))

#     def bill(self):
#         self.total = 0
#         count = 1
#         for p in self.pizzas:
#             print("Pizza : ", count)
#             print("Size = ", p.size ," Toppings: ", p.toppings, " Cheese: ",p.cheese)
#             self.total += p.price()
#             count +=1
#         print("Total bill Amount: ", self.total)
# order1 = Order('Sarinah')
# order1.order()
# order1.bill()
                
                      

# # Writeaclass called WordPlay. It should have a constructor that 
# # holds a list of words. The user of the class should
# # pass the list of words through constructor, which user wants to 
# # use for the class. The class should have following methods:
            
# class WordPlay:
#     def __init__(self, words):
#         self.words  = words

#     def words_with_lenght(self , length):
#         self.words_length = []
#         for word in self.words:
#             if len(word) == length:
#                 self.words_length.append(word)
#         return self.words_length

#     def starts_with_char(self, char):
#         self.starts_with_ch = []
#         for i in self.words:
#             if i [0] == char:
#                 self.starts_with_ch.append([i])
#         return self.starts_with_ch
    
#     def ends_with_char(self, char):
#         self.ends_with_ch = []
#         for i in self.words:
#             if i[-1] == char:
#                 self.ends_with_ch.append([i])
#         return self.ends_with_ch
    
#     def palindrome(self):
#         palindromes = []
#         for x in self.words:
#             if x[::1] == x[::-1]:
#                 palindromes.append(x)
#         return palindromes
    
#     def only_s(self, s):
#         s = set(s)
#         list = []
#         for w in self.words:
#             wd = set(w)
#             if s==wd:
#                 list.append(w)
#         return list
    
#     def avoid_s(self, s):
#         s = set(s)
#         list = []
#         for w in self.words:
#             wd = set(w)
#             if wd.intersection(s) == set():
#                 list.append(w)
#         return list
# a = WordPlay(['apple', 'banana', 'find', 'dictionary', 'set', 'tuple', 'list',
#                 'malayalam', 'nayan', 'grind', 'apricot'])
# print(a.words_with_lenght(5))
# print(a.starts_with_char("a"))
# print(a.ends_with_char("d"))
# print(a.palindrome())
# print(a.only_s("ban"))
# print(a.avoid_s("amkd"))

#  Write a python program that has class store
#  which keeps record of code and price of each product.
#  Display a menu of all products to the user and prompt
#  him to enter the quantity of each item required. 
# generate a bill and display total amount.

# class Store:
#     def __init__(self):
#         self.products = {}
#         self.add_product()
#         self.bill()
#     def add_product(self):
#         n = int(input("How many products u want to add? "))
#         for i in range(n):
#             prodname= input("Enter product name or code: ")
#             cost = int(input("Enter the cost of the item: "))
#             self.products[prodname] = cost
#         print("The addded items are: ", self.products)
#     def bill(self):
#         self.bill = 0
#         print("Enter the quantity of each product: ")
#         for i,j in (self.products.items()):   
#             print(i,j)
#             quantity = int(input(f"Enter the quantity for product:{i}: "))
#             self.bill += self.products.get(i)*quantity
#         print("Your total bill is: ", self.bill)

# s1= Store()
# import math
# class Point:
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y
#         self.distance_from_origin()
#         self.reflect_x()

#     def distance_from_origin(self):
#         print(self.x , self.y)
#         distance = (self.x**2+self.y**2)**0.5 
#         print("The distance from the origin is: ", distance)
#     def translate_method(self,x1,y1):
#         print(self.x , self.y)
#         self.x += x1
#         self.y += y1
#         print(f"Translate method will be:  ({self.x},{ self.y })")
#     def reflect_x(self):
#         self.y  = -1 * self.y
#         print(f"Reflect method will be:  ({self.x},{ self.y })")
#     def distance_method(self, x1, y1):
#          distance = (((abs(self.x - x1))**2)+ ((abs(self.y - y1))**2))**0.5 
#          print("The distance between 2 points is: ", distance)

# point1 = Point(1, 2)
# point1.translate_method(1,1)
# point1.x = 2
# point1.y = -3
# print(point1.distance_method(3,4))