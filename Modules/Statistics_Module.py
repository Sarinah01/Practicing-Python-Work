"""
📊 Python Statistics Module — Complete Notes with Examples & Edge Cases
"""

import statistics
from statistics import NormalDist

# ================================================================
# 🧠 1️⃣ Classes in statistics module
# ================================================================

# --- StatisticsError ---
# Raised when invalid statistical operation (like empty data)
try:
    print(statistics.mean([]))   # ❌ Empty list
except statistics.StatisticsError as e:
    print("Error:", e)  # -> Error: mean requires at least one data point


# --- NormalDist Class ---
# Represents a Normal (Gaussian) Distribution
dist = NormalDist(mu=50, sigma=10)
print("\n--- NormalDist Class ---")
print("Mean:", dist.mean)        # 50.0
print("Std Dev:", dist.stdev)    # 10.0
print("PDF(50):", dist.pdf(50))  # → Probability density at x=50
print("CDF(60):", dist.cdf(60))  # → 0.8413 cumulative up to x=60
print("INV_CDF(0.95):", dist.inv_cdf(0.95))  # → Value at 95% confidence
print("Zscore(60):", dist.zscore(60))  # → (60-50)/10 = 1.0
print("Samples:", dist.samples(3))     # Random samples from distribution

# Edge Case → invalid sigma
try:
    invalid = NormalDist(mu=10, sigma=0)
except Exception as e:
    print("Error creating NormalDist:", e)

# ================================================================
# ⚙️ 2️⃣ Central Tendency
# ================================================================

print("\n--- Central Tendency ---")
data = [1, 2, 3, 4, 5, 6]

# Mean → average
print("Mean:", statistics.mean(data))        # 3.5
print("FMean:", statistics.fmean(data))      # faster mean (3.5)
print("Geometric Mean:", statistics.geometric_mean([1, 3, 9]))  # 3.0
print("Harmonic Mean:", statistics.harmonic_mean([40, 60]))     # 48.0

# Edge case: empty or invalid data
try:
    print(statistics.mean([]))
except statistics.StatisticsError as e:
    print("EdgeCase Mean:", e)

# ================================================================
# 📈 3️⃣ Median-related functions
# ================================================================

print("\n--- Median Functions ---")
even = [1, 2, 3, 4]
odd = [1, 2, 3]

print("Median (even):", statistics.median(even))      # (2+3)/2 = 2.5
print("Median (odd):", statistics.median(odd))        # 2
print("Median Low:", statistics.median_low(even))     # 2
print("Median High:", statistics.median_high(even))   # 3
print("Median Grouped:", statistics.median_grouped([1, 2, 2, 3]))  # ~2.25

# ================================================================
# 📊 4️⃣ Mode-related functions
# ================================================================

print("\n--- Mode Functions ---")
modes = [1, 1, 2, 3, 3, 3]
print("Mode:", statistics.mode(modes))      # → 3
print("Multimode:", statistics.multimode(modes))  # → [3]

# Edge Case – no unique mode
try:
    print(statistics.mode([1, 2, 3]))
except statistics.StatisticsError as e:
    print("EdgeCase Mode:", e)

# ================================================================
# 📏 5️⃣ Variance & Standard Deviation
# ================================================================

print("\n--- Variance & Std Dev ---")
values = [2, 4, 4, 4, 5, 5, 7, 9]
print("Variance:", statistics.variance(values))     # → 4.571
print("Stdev:", statistics.stdev(values))           # → 2.138
print("Pvariance:", statistics.pvariance(values))   # → 4.0 (population)
print("Pstdev:", statistics.pstdev(values))         # → 2.0

# Edge case – less than 2 values
try:
    print(statistics.variance([10]))
except statistics.StatisticsError as e:
    print("EdgeCase Variance:", e)

# ================================================================
# 🧩 6️⃣ Correlation, Covariance, Linear Regression
# ================================================================

print("\n--- Correlation & Regression ---")
x = [1, 2, 3, 4, 5]
y = [2, 4, 5, 4, 5]

print("Covariance:", statistics.covariance(x, y))        # → 1.5
print("Correlation:", statistics.correlation(x, y))      # → 0.832
print("Linear Regression:", statistics.linear_regression(x, y))
# → slope=0.8, intercept=1.9

# Edge Case – mismatched lengths
try:
    print(statistics.correlation([1, 2], [2]))
except statistics.StatisticsError as e:
    print("EdgeCase Correlation:", e)

# ================================================================
# 🧮 7️⃣ Other Distributional Functions (NormalDist)
# ================================================================

print("\n--- Normal Distribution Computations ---")
nd = NormalDist(mu=0, sigma=1)
print("PDF(0):", nd.pdf(0))      # → 0.3989
print("CDF(1.96):", nd.cdf(1.96))# → 0.975
print("Inv_CDF(0.975):", nd.inv_cdf(0.975))  # → 1.96

# ================================================================
# 🧾 Summary
# ================================================================
"""
✅ Most Common Interview / Project Functions:
1. mean(), median(), mode()
2. stdev(), variance()
3. correlation(), covariance()
4. geometric_mean(), harmonic_mean()
5. NormalDist(pdf, cdf, inv_cdf)
6. linear_regression()

⚠️ Edge Cases:
- Empty data → StatisticsError
- Single element → variance/stdev fail
- No unique mode → StatisticsError
- Mismatched lengths in correlation/regression
"""
