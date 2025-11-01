"""
🧠 Python sys Module — Complete Notes with Examples & Edge Cases
---------------------------------------------------------
📘 Overview:
The sys module provides access to variables, functions, and objects that interact directly with the Python interpreter.
It’s part of Python’s standard library — no installation needed.

Common uses:
✅ Work with command-line arguments
✅ Access interpreter info (version, platform, etc.)
✅ Manage standard input/output
✅ Control Python runtime (exit, recursion, etc.)
✅ Memory size of objects
✅ Module path control
"""

import sys

# ================================================================
# 1️⃣ System Information
# ================================================================

print("\n--- System Information ---")
print("Python Version:", sys.version)         # → Full version info
print("Platform:", sys.platform)              # → e.g., 'win32' or 'linux'
print("Executable Path:", sys.executable)     # → Path of python interpreter
print("Byteorder:", sys.byteorder)            # → 'little' (Intel) or 'big'

# Edge case: version check
if sys.version_info < (3, 8):
    print("⚠️ Python version is below 3.8")

# ================================================================
# 2️⃣ sys.argv — Command-Line Arguments
# ================================================================

"""
sys.argv → list of command-line arguments
sys.argv[0] is the filename
sys.argv[1:], etc., are additional arguments
"""

print("\n--- Command-Line Arguments ---")
print("Arguments List:", sys.argv)  # Run this in terminal for real args

# Example (Run in terminal):
# python script.py hello world
# Output: ['script.py', 'hello', 'world']

# Edge case: no arguments
if len(sys.argv) == 1:
    print("No additional arguments passed!")

# ================================================================
# 3️⃣ sys.path — Module Search Path
# ================================================================

"""
sys.path → List of directories Python searches for modules
You can modify it at runtime to add new paths
"""

print("\n--- Module Search Path ---")
print("Before:", sys.path[:2])  # print first 2 only

sys.path.append("D:/my_custom_modules")
print("After:", sys.path[-1])  # confirm new path added

# Edge Case → invalid path doesn’t break anything, just ignored

# ================================================================
# 4️⃣ sys.exit() — Exit from Python
# ================================================================

"""
Terminates program execution safely.
You can provide an exit status:
- 0 → success
- Non-zero → error
"""

print("\n--- sys.exit() Example ---")
try:
    if False:  # Change to True to test
        sys.exit("Exiting program manually!")  # raises SystemExit
except SystemExit as e:
    print("SystemExit Caught:", e)

# ================================================================
# 5️⃣ sys.stdin / sys.stdout / sys.stderr
# ================================================================

"""
These represent standard input/output/error streams.
You can redirect or read/write to them manually.
"""

print("\n--- I/O Streams ---")
sys.stdout.write("This is written using sys.stdout.write()\n")

# Edge case: redirect stdout temporarily
import io
temp = io.StringIO()
old_stdout = sys.stdout
sys.stdout = temp
print("This won’t appear in console directly.")
sys.stdout = old_stdout
print("Captured Output:", temp.getvalue().strip())

# ================================================================
# 6️⃣ sys.getsizeof() — Memory Usage
# ================================================================

"""
Returns memory size (in bytes) of an object.
"""

print("\n--- Memory Usage ---")
a = [1, 2, 3, 4, 5]
print("Size of list:", sys.getsizeof(a), "bytes")
print("Size of int:", sys.getsizeof(10), "bytes")

# Edge Case → empty structures
print("Empty dict:", sys.getsizeof({}))       # Minimum memory size

# ================================================================
# 7️⃣ sys.modules — Loaded Modules
# ================================================================

"""
A dictionary containing all loaded modules in current Python runtime.
You can inspect or remove from cache.
"""

print("\n--- Loaded Modules ---")
print("Total modules loaded:", len(sys.modules))

# Edge case: Removing a module
import math
print("math in sys.modules?", "math" in sys.modules)
del sys.modules["math"]
print("math removed:", "math" not in sys.modules)

# ================================================================
# 8️⃣ sys.getrecursionlimit() & sys.setrecursionlimit()
# ================================================================

"""
Used to get or set maximum recursion depth.
Default ≈ 1000.
Too high value → may crash program.
"""

print("\n--- Recursion Limit ---")
print("Current limit:", sys.getrecursionlimit())
sys.setrecursionlimit(2000)
print("Updated limit:", sys.getrecursionlimit())

# Edge case: setting too high may cause stack overflow
# sys.setrecursionlimit(10**6)  # ⚠️ Don’t try unless needed

# ================================================================
# 9️⃣ sys.maxsize & sys.float_info
# ================================================================

"""
sys.maxsize → largest integer Python can handle (related to platform)
sys.float_info → details about floating-point precision
"""

print("\n--- Max Sizes ---")
print("Max Int:", sys.maxsize)
print("Float Info:", sys.float_info.max)  # Maximum float representable

# ================================================================
# 🔟 sys.getdefaultencoding() & sys.getfilesystemencoding()
# ================================================================

"""
Return default encodings used by Python interpreter
"""

print("\n--- Encoding Info ---")
print("Default Encoding:", sys.getdefaultencoding())
print("Filesystem Encoding:", sys.getfilesystemencoding())

# ================================================================
# 🧾 Summary
# ================================================================
"""
✅ Most Commonly Used sys Module Functions:
1. sys.version / sys.platform / sys.executable
2. sys.argv → for command line args
3. sys.path → module search path
4. sys.exit() → safe exit
5. sys.getsizeof() → memory info
6. sys.getrecursionlimit() / setrecursionlimit()
7. sys.stdin / stdout / stderr → stream handling
8. sys.modules → check loaded modules

⚠️ Edge Cases:
- Running without arguments → argv = ['script.py']
- Redirecting stdout → may miss prints
- Too high recursion limit → crash
- Removing sys.modules item → re-import required
"""
