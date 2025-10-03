n = int(input("Enter the number of the rows: "))
for rows in range(1, n+1):
    # for columns:
    for col in range(1,rows+1):
        print('*', end=' ')
    print()
    
# ****
# ****
# ****
# ****
print()

# *
# **
# ***
# ****
def rightTriangle(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(" * ",end=" ")
        print()
def pyramid(n):
    for i in range(1,n+1):
        for k in range(1,n-i+1):
            print("_", end=" ")
        for j in range(1,i+1):
            print(" * ",end=" ")
        print()
def invertedRightAngledTriangle(n):
    for i in range(1, n+1):
        for j in range(1,n-i+2):
            print(" * ", end=" ")
        print()
def LeftAlignedTriangle(n):
    for i in range(1, n+1):
        for j in range(1,n-i+1):
            print("_", end="")
        for k in range(1,i+1):
            print("*", end="")
        print()
def InvertedLeftAlignedTriangle(n):
    for i in range(1, n+1):
        for j in range(i-1,0,-1):
            print("_", end="")
        for k in range(1,n-i+2):
            print("*", end="")
        print()
def InvertedPyramid(n):
    for i in range(1, n+1):
        for k in range(1,i+1):
            print("_", end=" ")
        for j in range(1,n-i+2):
            print(" * ", end=" ")
       
        print()

def Diamond(n):
    for i in range(1, 2*n):
        if i <= n:  # upper half
            for k in range(n-i):
                print(" ", end=" ")   # spaces
            for j in range(2*i-1):
                print("*", end=" ")
        else:  # lower half
            for k in range(i-n):
                print(" ", end=" ")   # spaces
            for j in range(2*(2*n - i) - 1):
                print("*", end=" ")
        print()
def printX(n):
    total_rows = 2 * n - 1
    for i in range(1, total_rows + 1):
        for j in range(1, total_rows + 1):
            # left diagonal: starts at n and moves left
            if j == n - abs(n - i):
                print("*", end="")
            # right diagonal: starts at n and moves right
            elif j == n + abs(n - i):
                print("*", end="")
            else:
                print(" ", end="")
        print()
def printHollowDiamond(n):
    total_cols = 2*n - 1
    for i in range(1, 2*n):
        for j in range(1, total_cols+1):
            if i <= n:
                left = n - i + 1
                right = n + i - 1
            else:
                left = i - n + 1
                right = 3*n - i - 1

            if j == left or j == right:
                print("*", end='')
            else:
                print(" ", end='')
        print()

def printHollowX(n):
    for i in range(1, 2*n):
        for j in range(1, 2*n+1):
            if j == n - abs(n-i) or j == n + abs(n-i):
                print(" ", end=' ')
            else:
                 print("*", end=' ')
        print()

        
rightTriangle(n)
print()
invertedRightAngledTriangle(n)
print()
LeftAlignedTriangle(n)
print()
pyramid(n)
print()
InvertedLeftAlignedTriangle(n)
print()
InvertedPyramid(n)
print()
Diamond(n)
print()
printX(n)
print()
printHollowDiamond(n)
print()