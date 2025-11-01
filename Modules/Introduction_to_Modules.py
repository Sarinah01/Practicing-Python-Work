# A module in Python is just a file that contains Python code — like functions, classes, or variables — which you can reuse in other programs.
import math

# ✅ BASIC MATH FUNCTIONS
print(math.sqrt(16))         # √16 → 4.0
print(math.pow(2, 3))        # 2³ → 8.0
print(math.floor(4.7))       # Floor → 4
print(math.ceil(4.2))        # Ceil → 5
print(math.trunc(4.9))       # Truncate → 4
print(math.fabs(-10))        # Absolute value → 10.0
print(math.factorial(5))     # 5! → 120
print(math.isqrt(25))        # Integer square root → 5

# ✅ LOGARITHMIC FUNCTIONS
print(math.log(100))         # Natural log (base e) → 4.605...
print(math.log10(1000))      # Log base 10 → 3.0
print(math.log2(8))          # Log base 2 → 3.0

# ✅ EXPONENTIAL FUNCTIONS
print(math.exp(2))           # e² → 7.389...
print(math.expm1(1))         # e¹ - 1 → 1.718...

# ✅ POWER & MOD FUNCTIONS
print(math.pow(3, 2))        # 3² → 9.0
print(math.fmod(10, 3))      # Remainder → 1.0
print(-10 % 3)       # 2 (Python’s % keeps divisor’s sign)
print(math.fmod(-10, 3))  # -1.0 (fmod keeps dividend’s sign)


# ✅ ANGLE / TRIGONOMETRY
print(math.degrees(math.pi)) # Convert radians → degrees → 180.0
print(math.radians(180))     # Convert degrees → radians → 3.1415...
print(math.sin(math.pi / 2)) # sin(90°) → 1.0
print(math.cos(0))           # cos(0°) → 1.0
print(math.tan(math.pi / 4)) # tan(45°) → 1.0

# ✅ HYPERBOLIC FUNCTIONS
print(math.sinh(1))          # sinh(1)
print(math.cosh(1))          # cosh(1)
print(math.tanh(1))          # tanh(1)

# ✅ COMPARISON & HELPERS
print(math.gcd(24, 36))      # Greatest common divisor → 12
print(math.lcm(4, 6))        # Least common multiple → 12
print(math.isfinite(10))     # True (finite number)
print(math.isinf(float('inf'))) # True
print(math.isnan(float('nan'))) # True

# ✅ CONSTANTS
print(math.pi)               # 3.141592653589793
print(math.e)                # 2.718281828459045
print(math.tau)              # 6.283185307179586 2π (approximately 6.283185307179586)
print(math.inf)              # Infinity
print(math.nan)              # Not a Number
