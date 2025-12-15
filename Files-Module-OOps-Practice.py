# # 1]vWrite a function cust_data() to ask user to enter 
# # their names and age to store data in customer.txt file.
# def cust_data():
#     n = input("Enter the name:")
#     age = input("Enter the age:")
#     with open("customer.txt", "a+") as f:
#         f.write(f"Name: {n} \n")
#         f.write(f"Age: {age}\n")
#         print("----Printing the data----")
#         f.seek(0)
#         x= f.read()
#         print((x))
# cust_data()

# # 2]Write a function count_lines() to count and display the total number of
# #  lines from the file. Consider the following lines for the file– friends.txt.

# def count_lines():
#     with open("friends.txt") as f:
#         x = f.readlines()
#         print(x)
#         print(len(x))
    
#         f.seek(0)      
#         print("-----Output Of Readlines-----") 
#         for lines in f.readlines():
#             # in for each loop of this list \n gets converted to simple but \n gives new lines
#             print(lines)
#             print("Index - 0,1,2 values--",lines[0], lines[1], lines[2])
#         f.seek(0)
#         print("----Read Output----")
#         for ch in f.read():
#             # Reads and prints each character by character!
#             print(ch , " -- ",  end="")
#             print("Index - 0, values--",ch[0])
#         f.seek(0)
#         print("----Readline Output----")
        # for lines in f.readline():
        #     # Reads and prints each character by character but read only of one lineeee!
        #     print(lines)
        #     print("Index - 0, values--",lines[0])
#         f.seek(0)
#         print("----Output through looping through file obj----")
#         for lines in f:
#             # here it also reads line by line but same as readlines
#          
#             print(lines, " index value 0,1 ,2 -- ", lines[0], lines[1], lines[2])
# count_lines()

# def odd_lines():
#     with open("friends.txt") as f:
#         count=0
#         for lines in f:
#             if count%2==1:
#                 print(lines)
#             count+=1     
            
# odd_lines()

# def  read_lines_count_words():
    
#     with open("friends.txt") as f:
#         print("Nos.Of statements are: ", len(f.readlines()))    
#         count=0
#         f.seek(0)
#         for j in f:
#             for word in j.split():
#                 if word.isalpha() or word.isalnum():
#                     count+=1
#         print("Nos of words are: ", count)
# read_lines_count_words()

# # 3] checking with the write methods:
# with open("sample1.txt") as f:
#     x = f.read()
#     f.seek(0)
#     x1= f.readlines()
#     f.seek(0)
#     x2 =  f.readline()
# with open("output.txt", "w") as f1:
#     f1.write("-----Ouptut through write/read method----- \n")
#     f1.write(x.upper())
#     f1.write("-----Ouptut through write/readlines method-----\n")
#     f1.write(str(x1))
#     f1.write("-----Ouptut through write/readline method-----\n")
#     f1.write(x2.upper())
#     f1.write("---output of readlines---\n")
#     f1.writelines(x1)
#     f1.write("\n")

#     f1.write("Checking what's happening--")
#     f1.write("1234")
#     f1.write("5678")
#     # concluded: no new line is auto added when string is tyed inside!
#     # passing through read , readlines and readline it will start from where the cursor was and starts from where 
#     # cursor was and also the in between spaces through this methods used will be provided!

# 4] copies the content of file to another file:
# f1 = open("friends.txt")
# f2 = open("2.txt", 'w')
# for lines in f1.read():
#     f2.write(lines)
# print(f2.read())
# f1.close()
# f2.close()
# # 5] copiying 1line of file 1 and line 2 of file 2 alternatively!
# f = open("friends.txt")
# f1 = open("2.txt")
# f2  = open("3.txt",'w+')

# for lines in f:
#     f2.write(lines)
#     for lin2 in f1.readline():
#         f2.write(lin2) 
# f.close()
# f1.close()
# print(f2.read())

## 6] to count the nos.of lines:
# with open("friends.txt") as f:
#     for lines in f:
#         count+=1
# print("Total nos. of lines: ", count)

# #7] Search for a string te text file:
# n= input("Enter the string: ")
# count=0
# with open("friends.txt") as f:
#     for lines in f:
#         count+=1
#         if (n in lines.split()):
#             print("Word Found in this line : ", lines , "row = ", count)
#             for i in range(len(lines.split())):
#                 if lines.split()[i] == n:
#                     print("Found at column: ", i)

# def returnstr():
#     l=[]
#     seq = []
#     n = input("enter the string: ")
#     with open("example.txt") as f:
#         for lines in f:
#             # print(lines)
#             for ind, word in enumerate(lines.split()):
#                 print(ind, word)
#                 if n in word:
#                     l.append(word)
#                 print(l)
#         for ind, ch in enumerate(l):
#                 print(ind, ch)
#                 x= ch
#                 for i in range(len(x)):
#                     #  print(x[i])
#                      if x[i] in n and i not in seq:
#                           seq.append(i)
#         print(seq)
#         if len(seq) == len(n):
#              print(ch)
# returnstr()

# #control nd searching work using dict:
# def is_word_eligible(word, user_chars):

#     word_count = {}
#     for char in word:
#             if char in word_count:
#                 word_count[char] += 1
#             else:
#                 word_count[char] = 1
#     user_count = {}
#     for char in user_chars:
#             if char in user_count:
#                 user_count[char] += 1
#             else:
#                 user_count[char] = 1
#         # print(word_count,user_count)
#     for char, count in user_count.items():
#             if char not in word_count or word_count[char] < count:
#                 return False
#     return True
# def find_words_from_file(file_path, user_chars):
#     eligible_words = []
#     with open(file_path, 'r') as file:

#         for statement in file:
#             words = statement.split()
#         for word in words:
#         #print(word)
#             if is_word_eligible(word, user_chars):
#         #print(word)
#                 eligible_words.append(word)

#         return list(eligible_words)
# file_path = 'example.txt' 

# user_input = input("Enter a string of characters: ").lower()
# result = find_words_from_file(file_path, user_input)
# if result:
#     print("Output words will be:", ', '.join(result))
# else:
#     print("No matching words found.")

# # 11] Pager program:
# def pager():
#     n = input("Enetr the file name: ")
#     count = 0
#     with open(n) as f:
#         for lines in f:
#             if count<25:
#                 count+=1
#                 print(count, lines)
#             else:
#                 n1 = input("Do u want to continue:(yes/no): ")
#                 if n1.lower() == "yes":
#                     count=0
#                 else:
#                     print("----Exiting the system----")
#                     break
# pager()

# # 12] copying , vowels count and string reversing:
# with open("sample1.txt") as f:
#    x= f.read()[::-1]
#    print("Reversed the string: \n",x)
# with open("op.txt",'w+') as f1:
#    vowel =0
#    f1.write(x.upper())
#    f1.seek(0)
#    for ch in f1.read():
#       if (ch=='A' or ch=='E' or ch=='I' or ch=='O' or ch=='U'):
#          vowel+=1
#    print("Vowel count: ", vowel)
#    f1.seek(0)
#    print("Printing the second line: \n",f1.readlines()[1])
#    f1.seek(0)

#    print("The whole output : \n",f1.read())

# # 13] List of all the 4 letter words tht start and end with same letter:
# w= []
# with open("sample1.txt") as f:
#     for lines in f:
#         for word in lines.split():
#             if word[0]==word[-1] and len(word)==4:
#                 w.append(word)
# print(w)

# # 14] print only the word tht are starting from i and reverse order:
# with open("sample1.txt") as f:
#     for lines  in f:
#         for word in lines.split():
#             if word[0]=='I' or word[0]=='i':
#                 print(word , word[::-1])
#                 print(lines, lines[::-1])

# # 15] count words character and spaces:
# with open("sample1.txt") as f:
#     sp=w=0
#     c=0
    
#     for ch in f.read():
#         if not ch.isspace():
#             c+=1
#     f.seek(0)
#     for lines in f:
#         w += len(lines.split())
#         sp += len(lines.split())-1
# print("count  of characters: ", c , " space : ", sp ,  " word = ", w)
            
# # 16] file filtering when # symbol is there :
# with open("file1.txt") as f:
#     f2 = open("file2.txt","w")
#     l = 0
#     for lines in f:
#         l+=1
#         if '#' in lines:
#             for k in lines.split():
#                f2.write("".join(k+" "))
#             f2.write('\n')
# with open("friends.txt", "a") as f:
#     print("Some error occurred!", file=f)

# # Filtering from mail box and all tht!
# with open("mbox-short.txt","r") as f:
#     d={}
#     for lines in f:
#         if 'From ' in lines:
#         #     print(lines.split()[1])
#             d[lines.split()[1]] = d.get(lines.split()[1],0)+1
# x=  sorted(d.items(), key = lambda x: x[1], reverse = True)[0]
# print(d)
# print(x)

# # To check the frequency of the word:
# with open("python1.txt") as f:
#     d={}
#     for lines in f:
#         for i in lines.split():
#             d[i] = d.get(i,0)+1
# print(d)

# with open("friends.txt","rb") as f:
#     line = f.readline()
#     if line:
#         print(line.rstrip())

# with open("python1.txt") as f:
#     for lines in f:
#          print(str(lines.rstrip()))

# import os
# # def create():
# #     os.makedirs("Maindirectory", exist_ok=True)
# #     os.makedirs(os.path.join("Maindirectory", "Subdirectory"))
# def printing_directories():
#     print("Current Working Directories: ", os.getcwd())
#     files = os.listdir()
#     for file in files:
#         print(file)
# printing_directories()

# Write a python program to make a module named cal.py 
# which contain all the basic functions related to calculator
#  like addition, subtraction, multiplication, and division import that module in another file 
# and use that functions with number inputs given by user.

# import cal as c
# print(c.add(10,20))
# print(c.subtract(20,30))

# class Animal:
#     def __init__(self,arms , legs):
#         self.arms = arms
#         self.legs =legs
#     def limbs(self):
#         print(self.arms+self.legs)
# spider = (Animal(3,3))
# spider.limbs()

# def validate_age(age):
#     if not 18 <= age <= 120:
#         raise ValueError("Age must be between 18 and 120.")

# def get_user_info():
#     while True:
#         try:
#             age = int(input("Enter your age: "))
#             validate_age(age)
#             return age
#         except ValueError as e:
#             print("INSIDE EXCEPT:", e)   # <-- Statement 1
# try:
#     user_age = get_user_info()
#     print("Your age is valid:", user_age)   # --> Statement 2 (only if valid age)
# except ValueError:
#     print("OUTER EXCEPT: Some error")       # --> Statement 3 (rare)


# # raising the custoom exception :
# class InvalidAge(Exception):
#     pass
# class Person:
#     def __init__(self, name , age):
#         self.name = name
#         self.age = age
#     def valage(self):
#         if self.age<18 or self.age>120:
#             raise InvalidAge("Age should be greater than or equal to 18 and less than 120")
        
# def create_person_obj():
#     while True:
#         name = input("Enter your name: ")
#         age = int(input("ENter the age: "))

#         try:
#             person = Person(name,age)
#             person.valage()
#             print("Person added successfully!")
#             break
#         except InvalidAge as e:
#             print("Message: ", e)
# create_person_obj()


# # Student Management System:
# class Student:
#     students = []      # Class-level list to store ALL student objects

#     def __init__(self, name, roll, m1, m2):
#         self.name = name
#         self.roll = roll
#         self.m1 = m1
#         self.m2 = m2
#         Student.students.append(self)   # Add object automatically
#         print("const, " ,len(Student.students))
#     def accept(self):
#         name = input("Enter name: ")
#         roll = int(input("Enter roll number: "))
#         m1 = int(input("Enter marks 1: "))
#         m2 = int(input("Enter marks 2: "))
#         Student(name, roll, m1, m2)
#         print("Student added successfully!\n")
#         print("acc, " ,len(Student.students))
#     def display(self):
#         for i in Student.students:
#             print(" Name : ", i.name , " Roll nos: ", i.roll , " Marks 1 and 2  ", i.m1 ," " ,i.m2)
# temp = Student("Temporary",0,0,0)  
# while True:
    
#     print("\n------ MENU ------")
#     print("1. Add Student")
#     print("2. Display Students")
#     print("3. Search")
#     print("4. Delete")
#     print("5. Update")
#     print("6. Exit")

#     choice = input("Enter your choice: ")

#     match choice:
#         case "1":
#             print("Adding student...")
#             n = int(input("Enter how many nos. of students u Want to add? "))
#             for i in range(n):
#                 temp.accept()

#         case "2":
#             print("Displaying...")
#             temp.display()

#         case "3":
#             print("Searching...")
#             # search()

#         case "4":
#             print("Deleting...")
#             # delete()

#         case "5":
#             print("Updating...")
#             # update()

#         case "6":
#             print("Exiting program...")
#             break

#         case _:
#             print("Invalid choice! Please try again.")


# class Student:
#     students = []      
#     def __init__(self, name, roll, m1, m2):
#         self.name = name
#         self.roll = roll
#         self.m1 = m1
#         self.m2 = m2
#         Student.students.append(self)   
#     def accept(self):
#         name = input("Enter name: ")
#         roll = int(input("Enter roll number: "))
#         m1 = int(input("Enter marks 1: "))
#         m2 = int(input("Enter marks 2: "))
#         Student(name, roll, m1, m2)
#         print("Student added successfully!\n")

#     def display(self):
#         print("\n------ Student Records ------")
#         for s in Student.students:
#             print(f"Name: {s.name}, Roll: {s.roll}, Marks: {s.m1}, {s.m2}")
#         print()

#     def search(self):
#         r = int(input("Enter roll number to search: "))
#         for s in Student.students:
#             if s.roll == r:
#                 print(f"FOUND → Name: {s.name}, Roll: {s.roll}, Marks: {s.m1}, {s.m2}")
#                 return
#         print("Student not found!\n")

#     def delete(self):
#         r = int(input("Enter roll number to delete: "))
#         for s in Student.students:
#             if s.roll == r:
#                 Student.students.remove(s)
#                 print("Record deleted successfully!\n")
#                 return
#         print("Student not found!\n")

#     def update(self):
#         old = int(input("Enter old roll number: "))
#         new = int(input("Enter new roll number: "))
#         for s in Student.students:
#             if s.roll == old:
#                 s.roll = new
#                 print("Roll number updated!\n")
#                 return
#         print("Student not found!\n")



# obj = Student("temp", 0, 0, 0)   
# n = int(input("How many students you want to add? "))
# for i in range(n):
#     obj.accept()

# obj.display()
# obj.search()
# obj.update()
# obj.display()
# obj.delete()
# obj.display()

# 37 534 You own a pizzeria named Olly’s Pizzas and 
# want to create a Python program to handle the customers and revenue.
# Create the following classes with the following methods
