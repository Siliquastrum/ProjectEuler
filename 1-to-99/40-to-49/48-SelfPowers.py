__date__ = "23 Nov 2022"
__answer__ = 9110846700

__problem__ = """
The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.
Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.
"""

# ---------------------------------------------------------


# Solution:
n = int(input())
tot = 0
for num in range(1, n+1):
    tot += pow(num, num, 10**10) # 3rd argument mod argument
res = int(str(tot)[-10:])
print(res)