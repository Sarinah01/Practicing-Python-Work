# 📘 Python Random Module — Complete Summary (All 22 Functions + Seed)
# The random module in Python is used to generate pseudo-random numbers.
# These numbers are not truly random; they are generated using a deterministic algorithm.

import random

# -----------------------------------------------
# 🧠 1️⃣ seed(a=None)
# Sets the seed value to produce the same random numbers each time (used for reproducibility)
random.seed(2)
print(random.random())  # 0.13436424411240122
print(random.random())  # 0.8474337369372327
# Edge Case: Using the same seed again produces identical random sequences.

# -----------------------------------------------
# 🧠 2️⃣ getstate()
# Returns the current internal state of the random number generator.
state = random.getstate()
print(type(state))  # <class 'tuple'>

# -----------------------------------------------
# 🧠 3️⃣ setstate(state)
# Restores the internal state (useful to continue a sequence later)
random.setstate(state)
print(random.random())  # continues sequence from where left off

# -----------------------------------------------
# 🧠 4️⃣ getrandbits(k)
# Returns a random integer with k random bits.
print(random.getrandbits(4))  # Example: 11 (binary 1011)
# Edge Case: k must be >= 0, else ValueError.

# -----------------------------------------------
# 🧠 5️⃣ randrange(start, stop[, step])
# Returns a random number from the range(start, stop, step)
print(random.randrange(1, 10, 2))  # Example: 3
# Edge Case: Raises ValueError if range is empty.

# -----------------------------------------------
# 🧠 6️⃣ randint(a, b)
# Returns a random integer N such that a <= N <= b
print(random.randint(1, 5))  # Example: 3
# Edge Case: If a == b, returns that number.

# -----------------------------------------------
# 🧠 7️⃣ choice(seq)
# Returns a random element from a non-empty sequence.
fruits = ['apple', 'banana', 'cherry']
print(random.choice(fruits))  # Example: 'banana'
# Edge Case: Raises IndexError if seq is empty.

# -----------------------------------------------
# 🧠 8️⃣ choices(population, weights=None, k=1)
# Returns a list with k randomly chosen elements (can repeat).
colors = ['red', 'green', 'blue']
print(random.choices(colors, k=4))  # Example: ['blue', 'red', 'blue', 'green']
# Edge Case: Returns [] if k=0.

# -----------------------------------------------
# 🧠 9️⃣ shuffle(x)
# Shuffles the sequence in place (no return value).
nums = [1, 2, 3, 4, 5]
random.shuffle(nums)
print(nums)  # Example: [3, 5, 2, 1, 4]
# Edge Case: Works only on mutable sequences (lists).

# -----------------------------------------------
# 🧠 🔟 sample(population, k)
# Returns a list of k unique elements chosen from the population.
letters = ['A', 'B', 'C', 'D']
print(random.sample(letters, 2))  # Example: ['C', 'A']
# Edge Case: Raises ValueError if k > len(population).

# -----------------------------------------------
# 🧠 1️⃣1️⃣ random()
# Returns a random float number between 0.0 (inclusive) and 1.0 (exclusive)
print(random.random())  # Example: 0.5324
# Edge Case: Always between [0.0, 1.0).

# -----------------------------------------------
# 🧠 1️⃣2️⃣ uniform(a, b)
# Returns a random float between a and b (a <= N <= b)
print(random.uniform(10, 20))  # Example: 13.456
# Edge Case: Works even if a > b (it swaps internally).

# -----------------------------------------------
# 🧠 1️⃣3️⃣ triangular(low, high, mode)
# Returns random float in range [low, high], mode is most likely value.
print(random.triangular(10, 20, 15))  # Example: 14.2
# Edge Case: If mode not specified, defaults to midpoint.

# -----------------------------------------------
# 🧠 1️⃣4️⃣ betavariate(alpha, beta)
# Returns random float from Beta distribution (between 0 and 1)
print(random.betavariate(2, 5))  # Example: 0.24
# Edge Case: alpha, beta must be > 0.

# -----------------------------------------------
# 🧠 1️⃣5️⃣ expovariate(lambd)
# Returns random float from Exponential distribution.
print(random.expovariate(1.5))  # Example: 0.43
# Edge Case: lambd must be > 0.

# -----------------------------------------------
# 🧠 1️⃣6️⃣ gammavariate(alpha, beta)
# Returns random float from Gamma distribution.
print(random.gammavariate(2, 2))  # Example: 3.7
# Edge Case: alpha, beta must be > 0.

# -----------------------------------------------
# 🧠 1️⃣7️⃣ gauss(mu, sigma)
# Returns random float from Gaussian distribution.
print(random.gauss(0, 1))  # Example: 0.347
# Edge Case: sigma must be > 0.

# -----------------------------------------------
# 🧠 1️⃣8️⃣ lognormvariate(mu, sigma)
# Returns random float from log-normal distribution.
print(random.lognormvariate(0, 1))  # Example: 2.13
# Edge Case: sigma must be > 0.

# -----------------------------------------------
# 🧠 1️⃣9️⃣ normalvariate(mu, sigma)
# Returns random float from normal (Gaussian) distribution.
print(random.normalvariate(0, 1))  # Example: -0.235
# Edge Case: sigma must be > 0.

# -----------------------------------------------
# 🧠 2️⃣0️⃣ vonmisesvariate(mu, kappa)
# Returns random float from Von Mises distribution (used for angles).
print(random.vonmisesvariate(0, 4))  # Example: 0.9
# Edge Case: kappa = 0 gives uniform distribution from 0 to 2π.

# -----------------------------------------------
# 🧠 2️⃣1️⃣ paretovariate(alpha)
# Returns random float from Pareto distribution.
print(random.paretovariate(3))  # Example: 1.12
# Edge Case: alpha must be > 0.

# -----------------------------------------------
# 🧠 2️⃣2️⃣ weibullvariate(alpha, beta)
# Returns random float from Weibull distribution.
print(random.weibullvariate(1, 1.5))  # Example: 0.88
# Edge Case: alpha, beta must be > 0.

# -----------------------------------------------
# ⚡ BONUS: Using getstate() & setstate() together
# You can "pause and resume" randomness.
s = random.getstate()
print(random.random())  # Random value
random.setstate(s)
print(random.random())  # Repeats same number as previous

# -----------------------------------------------
# ⚡ BONUS 2: SystemRandom
# Provides cryptographically secure random numbers (not affected by seed)
secure = random.SystemRandom()
print(secure.randint(1, 100))  # Example: 73
# Edge Case: Slower but safer, not deterministic.
