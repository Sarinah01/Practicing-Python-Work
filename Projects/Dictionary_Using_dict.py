print('''
      Given a list of elements, write a python program to perform grouping of similar elements, 
      as different key-value list in dictionary. 
      Print the dictionary sorted in descending order of frequency of the elements.
      ''')
l = eval(input("Enter the list: "))
d = {}
for i in l:
    if i not in d:
        d[i] = []
    d[i].append(i)
print(d)
d= dict(sorted(d.items(), key = lambda x:  len(x[1]), reverse = True))
print("The sorted list: ", d)
    
print('''
     create a Dictionary with Key as First Character and Value as list of words Starting 
     with that Character from above string. And print that dictionary by sorting it based
     on the number of elements in a list of values in descending order. 
      ''')
d1={}
for val in ['apple', 'apricot', 'banana']:
    key = val[0]   # first letter
    if key not in d1:
        d1[key] = []
    d1[key].append(val)

print(d1)

print("Change the values based on the key-as the word and how many times it appears:")
k=  ["apple" ,"mango" , "aa","aa","mm","mm"]
d= {}
for j in k:
    d[j] = d.get(j,0)+1
print(d)


    
