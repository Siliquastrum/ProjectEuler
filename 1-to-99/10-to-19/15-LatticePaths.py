__date__ = "12 Nov 2022"
__answer__ = 137846528820

__problem__ = """
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
How many such routes are there through a 20×20 grid?
https://projecteuler.net/problem=15
"""

# ---------------------------------------------------------


# Solution for projecteuler.net:
from math import factorial as fac
n, m = list(map(int, input().strip().split()))
print(int((fac(n+m)//fac(n))//fac(m)))


# ---------------------------------------------------------


# Solution for HackerRank:
# from math import factorial as fac
for _ in range(int(input())):
    n, m = list(map(int, input().strip().split()))
    print(int(((fac(n+m)//fac(n))//(fac(m)))%((10**9) + 7)))