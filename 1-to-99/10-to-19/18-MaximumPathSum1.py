__date__ = "13 Nov 2022"
__answer__ = 1074

__problem__ = """
https://projecteuler.net/problem=18
By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

    3
   7 4
  2 4 6
 8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.
Find the maximum total from top to bottom of the triangle below:
NOTE: As there are only 16384 routes, it is possible to solve this problem by trying every route. However, Problem 67, is the same challenge with a triangle containing one-hundred rows; it cannot be solved by brute force, and requires a clever method! ;o)
"""

# ---------------------------------------------------------


# Solution:
n = int(input()) # number of row

rows = [list(map(int, input().strip().split())) for _ in range(n)]

# we will find the maximum sum by summing from bottom to top
for rw in range(n-2, -1, -1):
    for i in range(len(rows[rw])):
        rows[rw][i] += max(rows[rw+1][i],rows[rw+1][i+1])

print(rows[0][0])
