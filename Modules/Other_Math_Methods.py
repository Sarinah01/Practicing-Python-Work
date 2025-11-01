import math

print("--------- BASIC & ROOT FUNCTIONS ---------")

# sqrt(x): Returns square root (float)
print(math.sqrt(25))        # 5.0
# Edge: math.sqrt(-1) -> ValueError

# isqrt(x): Returns integer square root (no decimals, always floor)
print(math.isqrt(25))       # 5
print(math.isqrt(26))       # 5  (floor)
# Edge: math.isqrt(-1) -> ValueError

# cbrt(x): Returns cube root
print(math.cbrt(27))        # 3.0
print(math.cbrt(-8))        # -2.0

print("\n--------- COMBINATORICS ---------")

# comb(n, k): Returns number of ways to choose k items from n (nCk)
print(math.comb(5, 2))      # 10

# perm(n, k): Returns permutations (nPk)
print(math.perm(5, 2))      # 20

print("\n--------- TRIGONOMETRIC FUNCTIONS ---------")

# sin, cos, tan expect radians
print(math.sin(math.pi/2))  # 1.0
print(math.cos(math.pi))    # -1.0
print(math.tan(math.pi/4))  # 1.0

# asin, acos, atan (inverse trig functions)
print(math.asin(1))         # 1.5707963267948966 (π/2)
print(math.acos(0))         # 1.5707963267948966
print(math.atan(1))         # 0.7853981633974483 (π/4)

# atan2(y, x): Angle from x-axis to point (x, y)
print(math.atan2(1, 1))     # 0.7853981633974483 (π/4)

# asinh, acosh, atanh: Hyperbolic inverses
print(math.asinh(1))        # 0.881373587019543
print(math.acosh(2))        # 1.3169578969248166
print(math.atanh(0.5))      # 0.5493061443340548

print("\n--------- SIGN, DISTANCE & ERROR FUNCTIONS ---------")

# copysign(x, y): Returns x with the sign of y
print(math.copysign(5, -10))    # -5.0

# dist(p, q): Euclidean distance between two points
print(math.dist([1, 2], [4, 6]))   # 5.0

# erf(x): Error function used in statistics
print(math.erf(1))              # 0.8427007929497149

# erfc(x): Complementary error function (1 - erf(x))
print(math.erfc(1))             # 0.15729920705028513

print("\n--------- EXPONENTIALS & LOGS ---------")

# exp(x): Returns e^x
print(math.exp(2))              # 7.38905609893065

# expm1(x): e^x - 1 (more accurate for small x)
print(math.expm1(1e-5))         # 1.0000050000166668

# exp2(x): 2^x
print(math.exp2(3))             # 8.0

# log(x, base): Logarithm with base
print(math.log(8, 2))           # 3.0

# log10(x): Base 10 log
print(math.log10(1000))         # 3.0

# log1p(x): log(1+x) for small x — avoids precision loss
print(math.log1p(1e-9))         # 9.999999994736442e-10

print("\n--------- FLOAT & PRECISION UTILS ---------")

# frexp(x): Returns (mantissa, exponent) where x = m * 2**e
print(math.frexp(8))            # (0.5, 4)

# fsum(iterable): More accurate floating-point sum
print(math.fsum([0.1]*10))      # 1.0

# prod(iterable): Product of elements
print(math.prod([1, 2, 3, 4]))  # 24

# remainder(x, y): IEEE remainder (closest to 0)
print(math.remainder(10, 3))    # 1.0

# modf(x): Splits number into fractional & integer parts
print(math.modf(10.75))         # (0.75, 10.0)

# nextafter(x, y): Next floating-point number after x toward y
print(math.nextafter(1.0, 2.0)) # 1.0000000000000002

# ulp(x): Smallest difference between x and next representable float
print(math.ulp(1.0))            # 2.220446049250313e-16

# ldexp(x, i): Returns x * (2**i)
print(math.ldexp(2.0, 3))       # 16.0

print("\n--------- SPECIAL & CONSTANTS ---------")

# gamma(x): Gamma function (generalized factorial)
print(math.gamma(5))            # 24.0 (factorial(4))

# lgamma(x): Natural log of gamma(x)
print(math.lgamma(5))           # 3.1780538303479458

# hypot(x, y): sqrt(x² + y²)
print(math.hypot(3, 4))         # 5.0

# isclose(a, b): True if two floats are close
print(math.isclose(0.1+0.2, 0.3))  # True

# inf: Represents infinity
print(math.inf > 99999999)      # True

print("\n--------- CONSTANTS ---------")

print(math.pi)    # 3.141592653589793
print(math.e)     # 2.718281828459045
print(math.tau)   # 6.283185307179586 (2π)

print("\n--------- ROUNDING FUNCTIONS ---------")

# ceil(x): Rounds up
print(math.ceil(4.2))           # 5

# floor(x): Rounds down
print(math.floor(4.9))          # 4

# trunc(x): Truncates decimal part (towards 0)
print(math.trunc(-4.8))         # -4

# fabs(x): Absolute value (float)
print(math.fabs(-3.6))          # 3.6
