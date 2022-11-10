__date__ = "06 Nov 2022"
__answer__ = 25164150

__problem__ = """
The sum of the squares of the first ten natural numbers is,
    1²+2²+...+10²=385
The square of the sum of the first ten natural numbers is,
    (1+2+...+10)²=55²=3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is,
    3025 - 385 = 2640
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

# ---------------------------------------------------------


# I wanted to apply Carl Friedrich Gauss's sum formula,
# I searched if there was a formula for sum of squares and;
""" I found this formula:
                   n (n + 1) (2n + 1)
1² + 2² +...+ n² = ------------------
                           6
"""

# # 3 # Solution:
n = int(input())# 20 or another number entry
print(int(((n * (n + 1))/2)**2 - (n * (n + 1) * ((2 * n) + 1) / 6)))
# returns 25164150 if the number 100 is entered
# formulas save lives, thank you Gauss.


# ---------------------------------------------------------


""" # 1 # Very simple but Pseudo Solution (Time limit exceeded)
sqr = lambda x: x ** 2
N = int(input())
print(sqr(sum(range(N + 1))) - sum([sqr(i) for i in range(1, N + 1)]))
"""


# ---------------------------------------------------------


""" # 2 # Pseudo Solution (Time limit exceeded)
count = 0
total = 0
for i in range(1, int(input()) + 1):
    count += i
    total += i**2
print(count**2 - total)
"""