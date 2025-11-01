# collections is a Python module that provides specialized container datatypes — better, faster, and more flexible versions of lists, tuples, and dictionaries.
"""
collections_module_complete_demo.py
-----------------------------------
🔹 Purpose:
    Demonstrates all major classes & methods of Python's `collections` module
    including usage, return values, and edge cases.

🔹 Classes covered:
    1. Counter
    2. defaultdict
    3. OrderedDict
    4. namedtuple
    5. deque
    6. ChainMap
"""

from collections import Counter, defaultdict, OrderedDict, namedtuple, deque, ChainMap

print("\n=================== 1️⃣ COUNTER ===================")

# Counter counts the frequency of hashable elements
c = Counter("banana")
print(c)  # Counter({'a': 3, 'n': 2, 'b': 1})

# Most common elements
print(c.most_common(2))  # [('a', 3), ('n', 2)]

# Returns elements repeated as per count
print(list(c.elements()))  # ['b', 'a', 'a', 'a', 'n', 'n']

# Update adds new counts
c.update("apple")
print(c)  # Counter({'a': 6, 'p': 2, 'n': 2, 'b': 1, 'l': 1, 'e': 1})

# Subtract reduces counts (can go negative)
c.subtract("apple")
print(c)  # Some counts may drop or go negative

# Edge case: empty Counter
empty_c = Counter()
print(empty_c.most_common())  # []

# Arithmetic operations between counters
c1 = Counter(a=2, b=1)
c2 = Counter(a=1, b=3)
print(c1 + c2)  # Counter({'a': 3, 'b': 4})
print(c1 - c2)  # Counter({'a': 1}) -> subtracts counts but removes negatives

# Intersection & union
print(c1 & c2)  # min counts
print(c1 | c2)  # max counts


print("\n=================== 2️⃣ DEFAULTDICT ===================")

# defaultdict auto-creates default values for missing keys
d = defaultdict(int)
d['apple'] += 1
print(d)  # {'apple': 1}

# Accessing missing key returns default (no KeyError)
print(d['banana'])  # 0

# Using list as default factory
d_list = defaultdict(list)
d_list['fruits'].append('apple')
print(d_list)  # {'fruits': ['apple']}

# Edge case: functionless defaultdict raises error
try:
    wrong = defaultdict()
except TypeError as e:
    print("Error:", e)


print("\n=================== 3️⃣ ORDEREDDICT ===================")

# OrderedDict remembers insertion order
od = OrderedDict()
od['a'] = 10
od['b'] = 20
od['c'] = 30
print(od)  # OrderedDict([('a', 10), ('b', 20), ('c', 30)])

# Move to end or beginning
od.move_to_end('a')
print(od)  # 'a' moved to end

od.move_to_end('c', last=False)
print(od)  # 'c' moved to start

# popitem removes last or first
od.popitem()  # removes last
print(od)

od.popitem(last=False)  # removes first
print(od)

# Edge case: Empty OrderedDict popitem() → KeyError
try:
    empty_od = OrderedDict()
    empty_od.popitem()
except KeyError as e:
    print("Edge Case:", e)


print("\n=================== 4️⃣ NAMEDTUPLE ===================")

# namedtuple creates class-like immutable tuples
Person = namedtuple('Person', ['name', 'age', 'city'])
p1 = Person('Sara', 18, 'Delhi')

print(p1.name)      # Sara
print(p1[1])        # 18
print(p1._asdict()) # {'name': 'Sara', 'age': 18, 'city': 'Delhi'}
print(p1._fields)   # ('name', 'age', 'city')

# Edge case: Immutable (cannot assign new value)
try:
    p1.age = 25
except AttributeError as e:
    print("Edge Case:", e)


print("\n=================== 5️⃣ DEQUE ===================")

# deque allows fast appends/pops from both ends
dq = deque([1, 2, 3])
dq.append(4)
dq.appendleft(0)
print(dq)  # deque([0, 1, 2, 3, 4])

# Remove elements
dq.pop()
dq.popleft()
print(dq)  # deque([1, 2, 3])

# Extend both ends
dq.extend([4, 5])
dq.extendleft([-1, -2])
print(dq)  # deque([-2, -1, 1, 2, 3, 4, 5])

# Rotate deque
dq.rotate(2)
print(dq)  # deque([4, 5, -2, -1, 1, 2, 3])

# Edge case: rotate negative value
dq.rotate(-1)
print(dq)  # deque([5, -2, -1, 1, 2, 3, 4])

# Clear all
dq.clear()
print(dq)  # deque([])


print("\n=================== 6️⃣ CHAINMAP ===================")

# ChainMap combines multiple dicts
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
dict3 = {'d': 5}

chain = ChainMap(dict1, dict2, dict3)
print(chain)  # ChainMap({'a': 1, 'b': 2}, {'b': 3, 'c': 4}, {'d': 5})

# Accessing keys
print(chain['b'])  # 2 (from first dict)
print(chain['c'])  # 4
print(chain['d'])  # 5

# All keys and values
print(list(chain.keys()))    # ['a', 'b', 'c', 'd']
print(list(chain.values()))  # [1, 2, 4, 5]

# Updating first mapping affects dict1
chain['a'] = 100
print(dict1)  # {'a': 100, 'b': 2}

# Edge case: Key not found
try:
    print(chain['z'])
except KeyError as e:
    print("Edge Case:", e)

# New child (temporary layer)
new_chain = chain.new_child({'x': 999})
print(new_chain['x'])  # 999 (top layer)
print(new_chain.maps)  # Shows chain hierarchy


print("\n=================== ✅ END OF COLLECTIONS MODULE DEMO ===================")
