# ============================================================
# 📁 PYTHON FILE HANDLING — COMPLETE NOTES
# ============================================================

# --------------------------------------------
# 1️⃣ Opening a File
# Syntax: open(filename, mode)
# --------------------------------------------

# Modes:
# 'r'  - Read (default)
# 'w'  - Write (overwrites existing file)
# 'a'  - Append
# 'x'  - Create new file (error if exists)
# 'r+' - Read + Write
# 'w+' - Write + Read (overwrites)
# 'a+' - Append + Read
# Add 'b' for binary mode → 'rb', 'wb', etc.

# Example:
file = open("demo.txt", "w")     # Opens for writing
file.write("Hello, Python!\n")
file.write("File handling example.")
file.close()                     # Always close after work

# --------------------------------------------
# 2️⃣ Reading a File
# --------------------------------------------

# Using read()
f = open("demo.txt", "r")
print(f.read())                  # Reads whole content
f.close()

# Using readline()
f = open("demo.txt", "r")
print(f.readline())              # Reads one line
print(f.readline())              # Reads next line
f.close()

# Using readlines()
f = open("demo.txt", "r")
print(f.readlines())             # Returns list of lines
f.close()

# Edge case: reading non-existing file
try:
    f = open("nofile.txt", "r")
except FileNotFoundError:
    print("⚠️ File not found!")

# --------------------------------------------
# 3️⃣ Writing to a File
# --------------------------------------------

f = open("demo.txt", "w")        # Overwrites existing content
f.write("Overwritten text!\n")
f.close()

# Writing multiple lines
lines = ["Line1\n", "Line2\n", "Line3\n"]
f = open("demo.txt", "w")
f.writelines(lines)
f.close()

# --------------------------------------------
# 4️⃣ Appending Data
# --------------------------------------------

f = open("demo.txt", "a")
f.write("New line added!\n")
f.close()

# --------------------------------------------
# 5️⃣ Using 'with' for Auto-Closing
# --------------------------------------------

with open("demo.txt", "r") as f:
    content = f.read()
    print(content)
# File auto-closes even if error occurs

# --------------------------------------------
# 6️⃣ File Pointer Functions
# --------------------------------------------

with open("demo.txt", "r") as f:
    print(f.read(5))     # Reads first 5 characters
    print(f.tell())      # Shows current pointer position
    f.seek(0)            # Moves pointer back to start
    print(f.read())      # Reads full content again

# --------------------------------------------
# 7️⃣ File Existence Check
# --------------------------------------------

import os
if os.path.exists("demo.txt"):
    print("✅ File exists")
else:
    print("❌ File not found")

# --------------------------------------------
# 8️⃣ Deleting Files and Folders
# --------------------------------------------

import os
# os.remove("demo.txt")        # Deletes file
# os.rmdir("folder_name")      # Deletes empty folder

# Edge case:
try:
    os.remove("nofile.txt")
except FileNotFoundError:
    print("⚠️ Cannot delete — File doesn’t exist")

# --------------------------------------------
# 9️⃣ Working with Binary Files
# --------------------------------------------

# Copying image/video files
with open("image.jpg", "rb") as src:
    data = src.read()

with open("copy_image.jpg", "wb") as dest:
    dest.write(data)

# --------------------------------------------
# 🔟 Exception Handling in File Operations
# --------------------------------------------

try:
    with open("nofile.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("⚠️ File not found!")
except PermissionError:
    print("⚠️ Permission denied!")
finally:
    print("Operation complete ✅")

# --------------------------------------------
# 1️⃣1️⃣ Real-Life Example
# --------------------------------------------

def add_note(note):
    with open("notes.txt", "a") as f:
        f.write(note + "\n")

def read_notes():
    with open("notes.txt", "r") as f:
        return f.readlines()

add_note("Learn Python file handling")
add_note("Practice DSA daily")
print(read_notes())

# --------------------------------------------
# 1️⃣2️⃣ Summary Table (for quick revision)
# --------------------------------------------

# open("file", "mode")     → Opens file
# read()                   → Reads entire file
# readline()               → Reads single line
# readlines()              → Reads all lines as list
# write()                  → Writes string
# writelines()             → Writes list of strings
# close()                  → Closes file manually
# seek(pos)                → Moves pointer
# tell()                   → Shows pointer position
# os.path.exists()         → Check if file exists
# os.remove()              → Delete file
# with open(...) as f:     → Auto close (best practice)

# ============================================================
# ✅ END OF FILE HANDLING NOTES
# ============================================================
