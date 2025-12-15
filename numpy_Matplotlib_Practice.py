import numpy as np
from matplotlib import *
from matplotlib import pyplot as plt
from matplotlib import style
from mpl_toolkits import mplot3d  

a = np.array([1,2,30])  
print(np.sqrt(a))  
print(np.std(a))  
l =[1,23,3]
c = np.array(l)
print(c)
b = np.array([10,11,12])
print(np.vstack([a,b]))
print(np.hstack([a,b]))
a = np.array([[1,2,30],[10,15,4]])  
b = np.array([[10,11,12],[13,14,15]])
# concatenation:
print(np.concatenate([a , b] , axis = 0))#column wise 
print(np.concatenate([a,b], axis = 1))#row wise
# addition
print(a+b)#index wise addition take place

# numpy array intialization:
arr = np.empty((2,3), dtype = str)
print(arr)
arr= np.zeros((2,3), dtype=int)
print(arr)
arr= np.ones((1,3), dtype=float)
print(arr)

x = np.arange(0,10,1,float)
print(x)
print(np.linspace(10,20,5))#start, stop, how many numbers to display()
print(np.logspace(10,20,5))#creates on log space!
for x in np.nditer(x):
    print(x)

# printing the transpose:
print(a)
print(a.T)
x1= a.copy(order='F')
print(x1)

# non-zro
print(a)
print(np.nonzero(a))

a= [[1],[2]]
x3 = [[1,2]]
print(np.shape(a))
print(np.shape(b))


# Practicing matplotlib:
# simplr fgraph: 
# plt.plot([1,2,3],[4,5,6])
# plt.title("Line Graph: ")
# plt.ylabel("Yaxis")
# plt.xlabel("X-axis")
# plt.show()


# plt.plot([1,2,3,4,5],[1,4,9,16,25],'ro', linewidth=3,markersize=5)
# plt.axis([0,10,0,27])#takes control of the axis: (xmin ,xmax, ymin , ymax)
# # plt.axis('on') plt.axis('off') -- removes the axis:
# # plt.axis('equal')
# plt.show()

# # there are different
# # plotting with categorical variables:
# names = ["Sarinah", "sonia", "Diya"]
# marks = [90, 98, 89]

# plt.figure(figsize=(9,3))

# plt.subplot(131)
# plt.bar(names, marks)
# plt.title("Bar Chart")

# plt.subplot(132)
# plt.scatter(names, marks)
# plt.title("Scatter Chart")

# plt.suptitle("Categorical Plotting")

# x = [16, 8, 10]  
# y = [8, 16, 6]  
# x2 = [8, 15, 11]  
# y2 = [6, 15, 7]  
# plt.subplot(133)
# plt.grid(True,color='y')
# plt.legend()
# plt.plot(x,y,'m', label = "line one" ,  linewidth=2)
# plt.plot(x2,y2,'k',label="line-two",linewidth=2)
# plt.title("Epic Info")


# plt.title("Sin plot")
# plt.figure()
# x = np.linspace(0,10,1000)#start 0 end 10, 1000 evenly spaced
# ax=plt.axes()
# ax.plot(x,np.sin(x))

# y1 = np.sin(2 * np.pi * x)  
# y2 = 1.2 * np.sin(4 * np.pi * x)  
# fig, ax = plt.subplots(1, sharex=True)  
# ax.plot(x, y1, x, y2, color='black')  
# ax.fill_between(x, y1, y2, where=y2 >= y1, facecolor='blue', interpolate=True)  
# ax.fill_between(x, y1, y2, where=y2 <= y1, facecolor='red', interpolate=True)  
# ax.set_title('fill between where')  


# style.use('ggplot')  
# plt.figure()
# plt.axes()

# x = [5,8,10]  
# y = [12,16,6]  
  
# x2 = [6,9,11]  
# y2 = [7,15,7]  
  
  
# plt.bar(x, y, color = 'y', align='center')  
# plt.bar(x2, y2, color='c', align='center')  
  
# plt.title('Information')  
  
# plt.ylabel('Y axis')  
# plt.xlabel('X axis')  
# plt.tight_layout()
# plt.show()


# height = np.array([1,2,3,4,5])
# width  = np.array([7,8,9,10,11])

# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
# plt.title("Scatter 3D plot")

# ax.scatter3D(height, width, np.zeros_like(height))  # z = 0 for now
# # plt.show()
# data = [10,20,25,30,40,40,40,50,60,70]

# plt.hist(data, bins=5, color='skyblue')
# plt.show()

# import matplotlib.pyplot as plt

# maths = [87,90,92,45,56,33,78]
# science = [67,80,72,90,95,54,60]
# english = [55,65,75,85,70,66,59]

# plt.figure(figsize=(10,4))

# plt.subplot(1,3,1)
# plt.hist(maths, bins=5, color='red')
# plt.title("Maths")

# plt.subplot(1,3,2)
# plt.hist(science, bins=5, color='green')
# plt.title("Science")

# plt.subplot(1,3,3)
# plt.hist(english, bins=5, color='blue')
# plt.title("English")

# plt.suptitle("Students Marks Distribution")
# plt.show()


np.random.seed(0)  
x = np.random.standard_normal(100)  
y = np.random.standard_normal(100)  
z = np.random.standard_normal(100)  
  
# Create a 3D scatter plot  
fig = plt.figure()  
ax = fig.add_subplot(111, projection='3d')  
  
ax.scatter(x, y, z, c='r', marker='o')  
  
ax.set_xlabel('X Label')  
ax.set_ylabel('Y Label')  
ax.set_zlabel('Z Label')  
plt.show()     