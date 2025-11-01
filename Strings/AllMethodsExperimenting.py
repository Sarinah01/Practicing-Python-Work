# help(str) #gives the documentation of string class
s = "helloo"
print(dir(s))

# Method 1: Capitalize -returns the 1st letter of the whole string as capital other all small
def capitalize_edge_cases():
    print("123hello".capitalize())    # Digits not affected → '123hello'
    print("".capitalize())            # Empty string → ''
    print("ßharp".capitalize())       # Special German char → 'Ss...' handled differently (Python 3)
    print(" hELLO".capitalize())      # Leading space → space remains, no capitalization
capitalize_edge_cases()

# caesfold methodd: aggressive case old for special unicode character like beta , gamma -- 
# .lower() method does not does this does not changes beta to small!
def casefold_edge_cases():
    print("Python".casefold())      # Normal lowercase → 'python'
    print("İstanbul".casefold())    # Turkish I handling → 'i̇stanbul'
    print("Straße".casefold())      # ß → ss
    print("".casefold())            # Empty string → ''
    print("12345".casefold())       # Numbers unaffected

casefold_edge_cases()
print("cvhjkUHJK".lower())#cvhjkuhjk
print("ßTRASSE".lower())#ßtrasse

# method 3: center(width, fillchar)
s ="helloo" # --helloo--
print(s.center(10, "-"))
def center_edge_cases():
    print("Hi".center(1))         # Width < len → 'Hi'
    print("Hi".center(2))         # Width == len → 'Hi'
    print("Hi".center(5, '*'))    # Odd padding → '**Hi*'
    print("".center(4, '-'))      # Empty string → '----'
    # print("Test".center(10, 'ab')) # ❌ Error: fillchar must be 1 character
center_edge_cases()
# method -4 count(string , begin , end):
#  counts how many times the passed string appear can be letter or word
text = "banana"
print("Normal cases:")
print(text.count("a"))           # 3
print(text.count("an"))          # 2
print(text.count("n", 2, 5))     # 1

print("\nEdge cases:")
print("Empty substring:", "abc".count(""))     # 4 (len+1)
print("Not found substring:", "abc".count("z"))  # 0
print("Case-sensitive:", "Banana".count("b"))    # 0

# method -5: Converts the string to bytes
# string.encode(encoding="utf-8", errors="strict")
def encode_example():
    text = "hello 😊"
    print("\nNormal cases:")
    print(text.encode("utf-8"))           # b'hello \xf0\x9f\x98\x8a'

    print("\nEdge cases:")
    # Unsupported encoding
    try:
        print(text.encode("unknown"))
    except LookupError as e:
        print("Unsupported encoding:", e)

    # Invalid characters handling
    print("Ignore errors:", text.encode("ascii", errors="ignore"))     # b'hello '
    print("Replace errors:", text.encode("ascii", errors="replace"))   # b'hello ?'
    print("Backslashreplace:", text.encode("ascii", errors="backslashreplace"))  # b'hello \\U0001f60a'
encode_example()


# 6-- endswithsuffix, begin , end) -- true/false 
def endswith_example():
    s = "hello.py"
    print("\nNormal cases:")
    print(s.endswith(".py"))                # True
    print(s.endswith(("jpg", "png")))       # False
    print(s.endswith("lo", 0, 5))           # True

    print("\nEdge cases:")
    print("Empty string:", "".endswith(""))          # True
    print("Empty suffix:", "abc".endswith(""))       # True
    print("Tuple match:", "pic.jpg".endswith(("jpg", "png")))  # True
    print("Start/End range:", "hello".endswith("lo", 1, 4))    # False (only checks 'ell')
endswith_example()

# method -7 :string.expandtabs(tabsize=8)
# replaces the /t with spaces mentioned in the tabsize
def expandtabs_example():
    text = "A\tB\tC"
    print("\nNormal cases:")
    print(text.expandtabs(4))   # 'A   B   C'
    print(text.expandtabs(2))   # 'A B C'

    print("\nEdge cases:")
    print("Negative tabsize:", text.expandtabs(-2))   # 'ABC' (no spaces)
    print("Large tabsize:", text.expandtabs(10))      # Big spacing between
    print("Mixed tabs:", "1\t12\t123\t1234".expandtabs(4))  
expandtabs_example()

# method -8 format(value1, value2)
# Insert values into placeholders {} in the string.
# returns - formatted string
def format_example():
    text = "My name is {} and I am {} years old.".format("Sarinah", 18)
    print(text)
    print("Name: {name}, Age: {age}".format(name="Sarinah", age=18))
format_example()

# method- 9: .format_map(whatecver dict passing)
def format_map_example():
    data = {"name": "Sarinah", "age": 18}
    print("Name: {name}, Age: {age}".format_map(data))
format_map_example()
# Missing key in dict → KeyError

# method-10: index(substring , start , end) 
# returns the index of first occurence else ValueError
def index_example():
    text = "Python programming"
    print(text.index("o"))       # 4
    print(text.index("gram"))    # 10
index_example()
# Substring not found → ValueError
# Empty substring → always returns 0
# Case-sensitive ("Python".index("p") → ValueError)


# method-11: string.isalnum()--returns boolean
# True if all characters are letters or digits (no spaces or symbols).
def isalnum_example():
    print("abc123".isalnum())   # True
    print("abc 123".isalnum())  # False (space)
    print("abc!".isalnum())     # False (symbol)
isalnum_example()
# Empty string → False
# Unicode letters/numbers allowed ("²".isalnum() → True)

# method -12 isalpha()--True if all characters are alphabetic (A–Z, a–z).
# string.isalpha()
def isalpha_example():
    print("Hello".isalpha())  # True
    print("Hello123".isalpha()) # False
isalpha_example()
# Empty string → False
# Works with Unicode alphabets (e.g., "é".isalpha() → True)

# method-13 string.isascii()
#  T/F returns and says whether the all chars are ASCII (0–127) → English letters, digits, symbols.
def isascii_example():
    print("Python".isascii())   # True
    print("😊".isascii())       # False
isascii_example()
# Emoji / foreign letters → False
# Empty string → True (special case)


# method-14:string.isdecimal()
# True if all characters are decimal digits (0–9 only).
def isdecimal_example():
    print("123".isdecimal())    # True
    print("²".isdecimal())      # False
isdecimal_example()
# "½" → False (fraction is numeric but not decimal)
# "٠١٢" (Arabic digits) → True (since they’re decimal category)
# Empty string → False

# method-15 string.isdigit()
# True if all chars are digits (includes superscript digits, etc.)
def isdigit_example():
    print("123".isdigit())    # True
    print("²".isdigit())      # True (superscript 2)
isdigit_example()

# method-16: string.find()
# Returns the lowest index of substring if found, else -1
def find_example():
    text = "python programming"
    print(text.find("pro"))       # 7
    print(text.find("xyz"))       # -1
    print(text.find("o", 5, 10))  # 9
find_example()
# Edge cases:
# substring not found → -1
# empty substring → returns 0
# case-sensitive

# method-17: string.isidentifier()
# True if valid Python identifier (letters, digits, underscore, not starting with digit)
def isidentifier_example():
    print("var_name".isidentifier())  # True
    print("123abc".isidentifier())    # False
    print("class".isidentifier())     # True (keyword but still valid identifier)
isidentifier_example()
# Edge cases:
# Empty string → False
# Special chars like '-' or ' ' → False

# method-18: string.islower()
# True if all alphabetic characters are lowercase and at least one is present
def islower_example():
    print("hello".islower())  # True
    print("Hello".islower())  # False
    print("123".islower())    # False (no letters)
islower_example()
# Edge cases:
# Empty string → False
# Non-alphabetic chars ignored

# method-19: string.isupper()
# True if all alphabetic characters are uppercase and at least one is present
def isupper_example():
    print("HELLO".isupper())  # True
    print("Hello".isupper())  # False
    print("123".isupper())    # False
isupper_example()
# Edge cases:
# Empty string → False

# method-20: string.isnumeric()
# True if all characters are numeric (includes decimals, superscripts, fractions)
def isnumeric_example():
    print("123".isnumeric())  # True
    print("½".isnumeric())    # True (fraction)
    print("²".isnumeric())    # True (superscript)
isnumeric_example()
# Edge cases:
# Empty string → False
# Roman numerals or alphabets → False

# method-21: string.isprintable()
# True if all characters are printable (no control chars)
def isprintable_example():
    print("Hello".isprintable())    # True
    print("Hello\nWorld".isprintable())  # False (newline not printable)
isprintable_example()
# Edge cases:
# Empty string → True

# method-22: string.isspace()
# True if string has only whitespace chars
def isspace_example():
    print("   ".isspace())    # True
    print("\n\t".isspace())   # True
    print(" a ".isspace())    # False
isspace_example()
# Edge cases:
# Empty string → False

# method-23: string.istitle()
# True if each word starts uppercase + rest lowercase
def istitle_example():
    print("Hello World".istitle())   # True
    print("Hello world".istitle())   # False
    print("HELLO WORLD".istitle())   # False
istitle_example()
# Edge cases:
# Empty string → False
# Words like "McDonald" → True (Python checks per word)

# method-24: string.lower()
# Converts all uppercase letters to lowercase
def lower_example():
    print("HELLO".lower())   # hello
    print("HeLLo123".lower()) # hello123
lower_example()
# Edge cases:
# No change for digits or special chars

# method-25: string.ljust()
# Left-aligns string in a field of given width, fills with spaces (or char)
def ljust_example():
    print("Hi".ljust(5, "_"))  # 'Hi___'
    print("Hello".ljust(3, "_")) # 'Hello' (no truncation)
ljust_example()
# Edge cases:
# Width < len(string) → unchanged
# Fillchar must be exactly 1 char

# method-26: string.join()
# Joins elements of iterable with string as separator
# "separator".join(iterable)

def join_example():
    print("-".join(["a", "b", "c"]))  # 'a-b-c'
    print("".join(["A", "B"]))        # 'AB'
join_example()
# Edge cases:
# Empty iterable → ''
# Iterable must contain only strings (not int)
# ''.join([]) → '' (empty string)

# Removes leading (left-side) characters. Default = spaces.
# Syntax: string.lstrip([chars])

# method-27: string.lstrip()
def lstrip_example():
    print("   hello  ".lstrip())        # 'hello  '
    print("@@@wow@@@".lstrip("@"))      # 'wow@@@'
lstrip_example()
# Edge cases:
# ''.lstrip() → '' (empty string)
# Only removes from left, not middle.
# 'abc'.lstrip('a') → 'bc'


# method-28
# Creates translation mapping for translate()
# Syntax: str.maketrans(dict | str1, str2, [str3])

def maketrans_translate_example():
    trans = str.maketrans({'a': '@', 'e': '3'})
    print("apple".translate(trans))  # '@ppl3'

    trans2 = str.maketrans("abc", "123")
    print("abc cab".translate(trans2))  # '123 312'
maketrans_translate_example()
# Edge cases:
# All keys and values must be strings of equal length if using 2 strings.
# Unsupported type → TypeError.

# 🧩 method-29: string.partition()
## Splits into a tuple of (before, separator, after)
# Syntax: string.partition(separator)

def partition_example():
    print("hello-world".partition('-'))  # ('hello', '-', 'world')
    print("python".partition('-'))       # ('python', '', '')
partition_example()
# Edge case:
# If separator not found → ('string', '', '')

# method-30: string.removeprefix()
# Removes given prefix if present.
# Syntax: string.removeprefix(prefix)

def removeprefix_example():
    print("unhappy".removeprefix("un"))  # 'happy'
    print("Unhappy".removeprefix("un"))  # 'Unhappy'
removeprefix_example()
# Edge case:
# Case-sensitive, no partial match removal.

# method-31: string.removesuffix()
# Removes given suffix if present.
# Syntax: string.removesuffix(suffix)

def removesuffix_example():
    print("data.txt".removesuffix(".txt"))  # 'data'
    print("file.txtx".removesuffix(".txt")) # 'file.txtx'
removesuffix_example()
# Edge case:
# Must match exact suffix.

# method-32
# Replaces old substring with new substring.
# Syntax: string.replace(old, new, [count])

def replace_example():
    print("hello world".replace("world", "bro"))   # 'hello bro'
    print("aaa".replace("a", "b", 2))              # 'bba'
replace_example()
# Edge cases:
# Empty old substring → inserts new between each char.
# "abc".replace("", "-") → '-a-b-c-'


# method-33:
# Returns highest index of substring, else -1
# Syntax: string.rfind(sub[, start[, end]])

def rfind_example():
    print("banana".rfind("a"))    # 5
    print("banana".rfind("z"))    # -1
rfind_example()
# Edge case:
# Doesn't raise error if not found.

# 34. rfind()
# Returns highest index of substring, else -1
# Syntax: string.rfind(sub[, start[, end]])
def rfind_example():
    print("banana".rfind("a"))    # 5
    print("banana".rfind("z"))    # -1
rfind_example()
# Edge case: Doesn't raise error if substring not found.

# --------------------------------------------------

# 35. rindex()
# Returns highest index of substring; raises ValueError if not found
# Syntax: string.rindex(sub[, start[, end]])
def rindex_example():
    print("banana".rindex("a"))   # 5
    # print("banana".rindex("z")) # ValueError if uncommented
rindex_example()
# Edge case: Raises ValueError if substring not found.

# --------------------------------------------------

# 36. rjust()
# Right-aligns the string, padding with the specified fill character (default space)
# Syntax: string.rjust(width[, fillchar])
def rjust_example():
    print("hi".rjust(5, '*'))     # ***hi
    print("hi".rjust(2, '*'))     # hi
rjust_example()
# Edge case: If width <= len(string), returns original string.

# --------------------------------------------------

# 37. rpartition()
# Splits the string into a 3-part tuple (head, sep, tail) using the last occurrence of sep
# Syntax: string.rpartition(sep)
def rpartition_example():
    print("I love python".rpartition(" "))  # ('I love', ' ', 'python')
    print("python".rpartition("z"))         # ('', '', 'python')
rpartition_example()
# Edge case: Returns ('', '', string) if separator not found.

# --------------------------------------------------

# 38. rsplit()
# Splits from the right; optional maxsplit controls number of splits
# Syntax: string.rsplit(sep=None, maxsplit=-1)
def rsplit_example():
    print("a,b,c,d".rsplit(",", 1))  # ['a,b,c', 'd']
    print("a b c".rsplit())          # ['a', 'b', 'c']
rsplit_example()
# Edge case: If sep not found, returns [string].

# --------------------------------------------------

# 39. rstrip()
# Removes trailing spaces or specified characters
# Syntax: string.rstrip([chars])
def rstrip_example():
    print("hello   ".rstrip())       # 'hello'
    print("bananaaaa".rstrip("a"))   # 'banan'
rstrip_example()
# Edge case: Only trims from the right end.

# --------------------------------------------------

# 40. split()
# Splits the string at the specified separator
# Syntax: string.split(sep=None, maxsplit=-1)
def split_example():
    print("a,b,c".split(","))      # ['a', 'b', 'c']
    print("a b c".split())         # ['a', 'b', 'c']
split_example()
# Edge case: Default sep splits by any whitespace.

# --------------------------------------------------

# 41. splitlines()
# Splits at line breaks and keeps them if keepends=True
# Syntax: string.splitlines([keepends=False])
def splitlines_example():
    print("Hello\nWorld".splitlines())         # ['Hello', 'World']
    print("Hello\nWorld".splitlines(True))     # ['Hello\n', 'World']
splitlines_example()
# Edge case: Works with \n, \r, \r\n etc.

# --------------------------------------------------

# 42. startswith()
# Checks if string starts with the given prefix
# Syntax: string.startswith(prefix[, start[, end]])
def startswith_example():
    print("python".startswith("py"))   # True
    print("python".startswith("Py"))   # False
startswith_example()
# Edge case: Case-sensitive.

# --------------------------------------------------

# 43. strip()
# Removes leading and trailing whitespaces or specified chars
# Syntax: string.strip([chars])
def strip_example():
    print("   hi   ".strip())        # 'hi'
    print("...hello...".strip("."))  # 'hello'
strip_example()
# Edge case: Removes from both sides only.

# --------------------------------------------------

# 44. swapcase()
# Swaps case: uppercase ↔ lowercase
# Syntax: string.swapcase()
def swapcase_example():
    print("HeLLo WoRLD".swapcase())  # hEllO wOrld
swapcase_example()
# Edge case: Works with non-English alphabets too.

# --------------------------------------------------

# 45. title()
# Converts string to title case (first letter of each word capitalized)
# Syntax: string.title()
def title_example():
    print("hello world".title())        # Hello World
    print("heLLo woRLD".title())        # Hello World
title_example()
# Edge case: Handles words with apostrophes oddly ('they're' -> 'They'Re').

# --------------------------------------------------

# 46. translate()
# Replaces characters using a translation table
# Syntax: string.translate(table)
def translate_example():
    trans = str.maketrans("aeiou", "12345")
    print("apple".translate(trans))     # 1ppl2
translate_example()
# Edge case: Must use str.maketrans() to build translation table.

# --------------------------------------------------

# 47. upper()
# Converts all characters to uppercase
# Syntax: string.upper()
def upper_example():
    print("python".upper())             # PYTHON
upper_example()
# Edge case: Works only on alphabetic characters.

# --------------------------------------------------

# 48. zfill()
# Pads string on the left with zeros to reach given width
# Syntax: string.zfill(width)
def zfill_example():
    print("42".zfill(5))                # 00042
    print("-42".zfill(5))               # -0042
zfill_example()
# Edge case: Minus sign is preserved before zeros.


