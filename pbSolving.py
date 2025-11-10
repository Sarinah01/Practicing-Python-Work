print("-----PB -CH:4 -- Strings and List")
print("Write a Python program to check if a string is palindrome or not.")
n=input("Enter any String to check whether it is palindrome or not:")
if n == n[::-1]:
    print(n[::-1])
    print("Yes it's Palindrome")
else:
    print("Entered string is not palindrome!")
    
print("Write a Python program to Find length of a string in python.")
n=input("Enter the string to display it's length:")
count = 0
for c in n:
    count+=1
print("The length of the string is: ",count)

print("WriteaPythonprogramusing function to shift the decimal digits n places to the left, wrapping the extra digits around. If shift > the number of digits of n, then reverse the string.")
n= input("Enter the string")
r=""
s =int(input("Enter the number of shifts; [must be integer]"))
if s>len(n):
    print(n[::-1])
else: 
    
    result=n[s:] + n[:s]
    print(result)
    
print("Write a python program to check the password details:")
while True:
    upper = 0; lower = 0; digit = 0; sp = 0;space=0
    n= input("Enter the password!")
       
        
    for i, chr in enumerate(n):
            if chr.isupper():
                upper +=1
            if chr.islower():
                lower +=1
            if chr.isdigit():
                digit+=1
            if not chr.isalnum():
                sp +=1
            if chr.isspace():
                space +=1
                
    if(len(n)<8):
            print("Length should be greater than or equal to 8:");
            continue            
    if upper<2:
            print("Enter atleast 2 upper case")
            continue
    if lower<2:
                print("Enter atleast 2 lower case later")
                continue
    if digit<2:
                    print("Enter digit 2 atleast")
                    continue
    if sp<2:
                        print("Enter special chara -2")
                        continue
    if space >2 :
                            print("Enter space characters!")
                            continue
    else:
            print("Password is Valid!")
            break

print("Caeser Encryption:")
n=input("Enter the String: ")
shift= int(input("Enter the shift: "))
result = ""
for c in n:
    
    if c.isupper():
        if ord(c)+shift>=65 and ord(c)+shift<=90:
            print(result + chr(ord(c)+shift),end="")
        else:
            result += chr((ord(c)+shift)-90+65)
    elif c.islower():
        if ord(c)+shift>=97 and ord(c)+shift<=122:
            print(result + chr(ord(c)+shift),end="")
        else:
            result += chr((ord(c)+shift)-122+97)
    else:
        result +=c
            
