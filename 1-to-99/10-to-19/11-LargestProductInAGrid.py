__date__ = "10 Nov 2022"
__answer__ = 70600674

__problem__ = """
In the 20×20 grid below, four numbers along a diagonal line have been marked in red.
08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
.. .. .. .. .. .. .. .. .. .. .. .. .. .. .. .. .. .. .. ..
I didn't include them all here because there are too many numbers.
https://projecteuler.net/problem=11 for all numbers.

The product of these numbers is 26 × 63 × 78 × 14 = 1788696.
What is the greatest product of four adjacent numbers in the same direction (up, down, left, right, or diagonally) in the 20×20 grid?
"""

# ---------------------------------------------------------


# Solution:
grid = []
for grid_i in range(20):
	grid_t = [int(grid_temp) for grid_temp in input().strip().split(' ')]
	grid.append(grid_t)

mult = [grid[k][i] * grid[k][i+1] * grid[k][i+2] * grid[k][i+3] for i in range(17) for k in range(20)] 
mult += [grid[l][s] * grid[l+1][s+1] * grid[l+2][s+2] * grid[l+3][s+3] for l in range(17) for s in range(17)]
mult += [grid[l][s+3] * grid[l+1][s+2] * grid[l+2][s+1] * grid[l+3][s] for l in range(17) for s in range(17)]
mult += [grid[t][b] * grid[t+1][b] * grid[t+2][b] * grid[t+3][b] for b in range(20) for t in range(17)] 
print(max(mult))
