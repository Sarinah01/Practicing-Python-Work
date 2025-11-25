n =  input("Enter the text: ")
u = l = d = space = special = 0
for i in n:
    if i.isupper(): u+=1
    if i.islower(): l +=1
    if i.isdigit(): d+=1
    if i.isspace(): space +=1
    if not i.isalnum(): special+=1
    
d= {"uppercase" : u , "lowercase" :l ,"digit":d,"space":space,"special":special}
d = dict(sorted(d.items(), key = lambda x : (x[1]) ,reverse=True))
print(d)
