"""
os_module_complete_demo.py
--------------------------
🔹 Purpose:
    Demonstrates the most useful and commonly used functions from Python's `os` module
    with examples, outputs, and edge cases.

🔹 What you’ll learn:
    1. File & directory handling
    2. Path and access operations
    3. System and environment handling
"""

import os

print("\n=================== 1️⃣ BASIC SYSTEM INFO ===================")

# os.name → gives the name of the operating system
print("Operating System name:", os.name)  # e.g., 'nt' (Windows), 'posix' (Linux/macOS)

# os.getcwd() → current working directory
print("Current Working Directory:", os.getcwd())

# os.environ → returns all environment variables (dict-like object)
print("Home Path:", os.environ.get("HOMEPATH", "Not Found"))  # using .get() for safety

# Edge Case: os.getcwd() after folder removal → FileNotFoundError
try:
    os.chdir("non_existent_folder")
except FileNotFoundError as e:
    print("Edge Case:", e)


print("\n=================== 2️⃣ DIRECTORY OPERATIONS ===================")

# os.mkdir() → create new directory
try:
    os.mkdir("test_dir")
    print("✅ Directory created successfully!")
except FileExistsError:
    print("⚠️ Directory already exists!")

# os.listdir() → list all files/folders in directory
print("Files & folders in current directory:", os.listdir())

# os.chdir() → change current working directory
print("Before change:", os.getcwd())
os.chdir("test_dir")
print("After change:", os.getcwd())

# os.rmdir() → remove an empty directory
os.chdir("..")  # move back before deleting
try:
    os.rmdir("test_dir")
    print("✅ Directory removed successfully!")
except OSError as e:
    print("Edge Case:", e)


print("\n=================== 3️⃣ FILE OPERATIONS ===================")

# Create a sample file
with open("sample.txt", "w") as f:
    f.write("Hello OS module!")

# os.rename() → rename file
try:
    os.rename("sample.txt", "renamed_sample.txt")
    print("✅ File renamed successfully!")
except FileNotFoundError as e:
    print("Edge Case:", e)

# os.remove() → delete a file
try:
    os.remove("renamed_sample.txt")
    print("✅ File deleted successfully!")
except FileNotFoundError:
    print("⚠️ File not found for deletion!")


print("\n=================== 4️⃣ ACCESS & PATH OPERATIONS ===================")

# os.path.exists() → check if path exists
print("Does sample.txt exist?", os.path.exists("sample.txt"))

# os.access() → check access permissions
file_path = "sample.txt"
print("Exist path:", os.access(file_path, os.F_OK))  # existence
print("Readable:", os.access(file_path, os.R_OK))   # read permission
print("Writable:", os.access(file_path, os.W_OK))   # write permission
print("Executable:", os.access(file_path, os.X_OK)) # execute permission

# Edge Case: checking invalid path
print("Invalid path check:", os.access("invalid_path.txt", os.F_OK))

# os.path.join() → combine paths safely
print("Joined Path:", os.path.join(os.getcwd(), "new_folder", "file.txt"))

# os.path.basename() & os.path.dirname()
path_example = r"C:\Users\Example\file.txt"
print("Basename:", os.path.basename(path_example))  # file.txt
print("Dirname:", os.path.dirname(path_example))    # C:\Users\Example


print("\n=================== 5️⃣ SYSTEM COMMANDS & ENVIRONMENT ===================")

# os.system() → executes a shell command
print("Running system command (dir / ls):")
os.system("dir" if os.name == "nt" else "ls")

# os.getenv() → get environment variable
print("PATH variable:", os.getenv("PATH")[:50], "...")

# os.putenv() → temporarily modify environment variable (won’t persist)
os.putenv("TEST_ENV", "123")
print("Temporary Env Variable TEST_ENV:", os.getenv("TEST_ENV"))

# Edge Case: non-existent variable
print("Unknown ENV var:", os.getenv("DOES_NOT_EXIST", "DefaultValue"))


print("\n=================== 6️⃣ PATH UTILITIES (os.path) ===================")

# os.path.abspath() → absolute path of file
print("Absolute path:", os.path.abspath("sample.txt"))

# os.path.isfile() → check if path is file
print("Is file:", os.path.isfile("sample.txt"))

# os.path.isdir() → check if path is directory
print("Is directory:", os.path.isdir("test_dir"))

# os.path.split() → split path into (head, tail)
print("Split Path:", os.path.split(path_example))

# os.path.splitext() → split filename and extension
print("Split Extension:", os.path.splitext(path_example))


print("\n=================== ✅ END OF OS MODULE DEMO ===================")
