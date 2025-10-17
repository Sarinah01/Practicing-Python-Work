# ===================================================
# Python File Handling Basics
# ===================================================

# File handling = reading/writing files stored on disk
# Steps:
# 1. Open the file
# 2. Perform operations (read/write)
# 3. Close the file

# ---------------------------
# 1️⃣ Opening a File
# ---------------------------

# Syntax: open(filename, mode)
# Modes:
# 'r'  → read (default) - file must exist
# 'w'  → write - overwrites if file exists
# 'a'  → append - adds at end
# 'x'  → create - fails if file exists
# 'b'  → binary mode
# 't'  → text mode (default)
# '+'  → read/write

# Example:
f = open("example.txt", "w")  # open file for writing
f.write("Hello World\n")
f.write("Python File Handling\n")
f.close()  # always close the file

# ---------------------------
# 2️⃣ Reading from a File
# ---------------------------

# Reopen in read mode
f = open("example.txt", "r")

# Read entire content
content = f.read()
print(content)
f.close()

# Read n characters
f = open("example.txt", "r")
print(f.read(5))   # reads first 5 characters
f.close()

# Read line by line
f = open("example.txt", "r")
print(f.readline())   # reads first line
print(f.readline())   # reads second line
f.close()

# Read all lines as list
f = open("example.txt", "r")
lines = f.readlines()   # returns list of lines
print(lines)
f.close()

# ---------------------------
# 3️⃣ Writing to a File
# ---------------------------

# Write mode ('w') → overwrites existing file
f = open("example.txt", "w")
f.write("New content\n")
f.close()

# Append mode ('a') → adds at end
f = open("example.txt", "a")
f.write("Appended line\n")
f.close()

# ---------------------------
# 4️⃣ Using 'with' Statement (Recommended)
# ---------------------------

# Automatically closes file after operation
with open("example.txt", "r") as f:
    content = f.read()
    print(content)

with open("example.txt", "a") as f:
    f.write("Using with statement\n")

# ---------------------------
# 5️⃣ File Pointer / seek()
# ---------------------------

# File pointer = current position in file
f = open("example.txt", "r")
print(f.read(5))  # reads first 5 characters
print(f.read(5))  # reads next 5 characters
f.seek(0)         # move pointer to beginning
print(f.read(5))  # reads first 5 characters again
f.close()

# ---------------------------
# 6️⃣ Tell() Method
# ---------------------------

# Returns current file pointer position
f = open("example.txt", "r")
print(f.read(5))
print(f.tell())   # prints pointer position
f.close()

# ---------------------------
# 7️⃣ Binary Files
# ---------------------------

# Reading/writing non-text files like images
# 'rb' = read binary, 'wb' = write binary
# Example: copy an image
# with open("source.jpg", "rb") as src:
#     data = src.read()
# with open("copy.jpg", "wb") as dst:
#     dst.write(data)

# ---------------------------
# 8️⃣ Mini Projects
# ---------------------------

# 1) Count number of lines in file
with open("example.txt", "r") as f:
    lines = f.readlines()
print("Number of lines:", len(lines))

# 2) Count words in file
with open("example.txt", "r") as f:
    content = f.read()
words = content.split()
print("Number of words:", len(words))

# 3) Copy content from one file to another
with open("example.txt", "r") as src, open("copy.txt", "w") as dst:
    dst.write(src.read())

# 4) Write user input to file
with open("user_input.txt", "w") as f:
    for i in range(3):
        text = input("Enter a line: ")
        f.write(text + "\n")

# ---------------------------
# 9️⃣ Edge Cases / Notes
# ---------------------------

# - 'r' mode → file must exist, else FileNotFoundError
# - 'w' mode → overwrites existing file
# - 'a' mode → pointer starts at end, creates file if not exists
# - Always close file or use 'with'
# - Reading after writing may require f.seek(0)
# - Binary mode needed for non-text files
