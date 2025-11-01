#List Basics
# lst = [10, 20, 30]

# Mutable → can change, add, remove elements

# Holds references to objects in heap

# Dynamic size → grows automatically

# Can store mixed types: ints, strings, objects, lists, etc.

# Appending at the last only!
lst = [4,5,6,7]
lst.append("Hiii")
lst.append({1,2})
print(lst)
#[4, 5, 6, 7, 'Hiii', {1, 2}]
# here it was added as a whole
# lst.extend(iterable)

lst.extend("Hello")
lst.extend([3,4]) 
print(lst)
# here it will be added after iterating each thing in it
#[4, 5, 6, 7, 'Hiii', {1, 2}, 'H', 'e', 'l', 'l', 'o', 3, 4]

# inserting at specific index (index, value)
lst.insert(1,2)
print(lst)
# lst.insert(i, x)

# If i ≥ length → element added at end
# If i < 0 → counts from end, negative indices work ✅
# Never throws IndexError

# For removing the elemnt:
# 1] pop()
lst.pop() #removes last element
lst.pop(1)#removes at the index 
# IndexError → if index out of range OR list is empty

# 2] Remove -- removes the first occurence of thee value
lst.remove(4)
# ValueError → if value not in list

lst.clear() #removes all the elements of the list

# del element by index or entire list
# del lst[index] or del lst[start:end]--end :exclusive
# IndexError → if index out of range
lst = [1,2]
# del lst[5]  # IndexError

print(lst)
st = [1,2,3,4]
st[1:5] = []
print(st)
# No error for slices out of bounds → silently adjusts

# index -- search value
# index(value, [start], [end])
lst = [1,2,3,2,4]
lst.index(2)        # 1
lst.index(2,2)      # 3
# ValueError if value not in list

# count(value)

# Returns how many times a value appears
lst = [1,2,2,3,2]
lst.count(2)    # 3
# No error ever

# sort(key=None, reverse=False)
lst = [5,2,9,1]
lst.sort()                # [1,2,5,9]
lst.sort(reverse=True)    # [9,5,2,1]
# TypeError if incomparable data
lst.sort(key=str)   # convert all to string then sort
lst = [1,2,3]
lst.reverse()    # [3,2,1]
x = lst.reverse()  # x = None


# lst = [[1,2], [3,4]]
new_lst = lst.copy()
# Shallow → inner lists share same reference:
# new_lst[0][0] = 99
print(lst)  # [[99,2], [3,4]]

# new = lst → same reference 
# new = lst.copy() → new object 

