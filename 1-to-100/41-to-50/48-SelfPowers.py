__date__ = "23 Nov 2022"
__answer__ = 9110846700

__problem__ = """
The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.
Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.
"""

# ---------------------------------------------------------


# # 2 # Solution:
n = int(input())
tot = 0
for num in range(1, n+1):
    tot += pow(num, num, 10**10) # 3rd argument mod argument
res = int(str(tot)[-10:])
print(res)


# ---------------------------------------------------------


""" # 1 # Pseudo Solution (time limit exceeded):
n = int(input())
def f(maxn):
    num = 1
    tot = 0
    while num <= maxn:
        tot += pow(num, num)
        num += 1
    return tot
res = int(str(f(n))[-10:])
print(res)
"""