product1 = int(input("Enter the nos. of items u want to enter in this list: "))
product2 = int(input("Enter the nos.of list u want to enter in 2nd lsit: "))

def takeInput(d):
    d1={}
    for i in range(d):
        productname = input("Enter the name of the product: ")
        price = int(input("Enter the price of the product: "))
        d1[productname] = price
    return d1

p1 = takeInput(product1)
p2= takeInput(product2)
print("List of Product1: ",p1)
print("List of Product2: ",p2)
for (i,iv),(j,jv) in zip(p1.items(),p2.items()):
    if i == j:
        if iv >= jv:
            p2[j] = iv
        else:
            p1[i] = jv
p1.update(p2)
print("New Updated List: ",p1)


# 2nd Approach:
for key in p1:
    if key in p2:
        p2[key] = max(p1[key] , p2[key])
p1.update(p2)

        

