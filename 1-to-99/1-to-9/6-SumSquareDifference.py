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

"""
                   n (n + 1) (2n + 1)
1² + 2² +...+ n² = ------------------
                           6
"""

# Solution:
n = int(input())# 20 or another number entry
print(int(((n * (n + 1))/2)**2 - (n * (n + 1) * ((2 * n) + 1) / 6)))
# returns 25164150 if the number 100 is entered