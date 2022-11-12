__date__ = "12 Nov 2022"
__answer__ = 1366

__problem__ = """
2¹­­­⁵= 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
What is the sum of the digits of the number 2¹°°°?
"""

# ---------------------------------------------------------


# # 1 # Solution:
print(sum(map(int, str(input()))))


# ---------------------------------------------------------


# # 2 # Solution for HackerRank:
print(*[sum(map(int, str(pow(2, int(input()))))) for _ in range(int(input()))], sep="\n")