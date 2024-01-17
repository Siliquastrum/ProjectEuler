__date__ = "16 Nov 2022"
__answer__ = 2783915460

__problem__ = """
A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:
012   021   102   120   201   210
What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
"""

# ---------------------------------------------------------


# Solution for projecteuler.net:
from itertools import permutations as per
print(int("".join(list(per("0123456789"))[9999])))


# ---------------------------------------------------------


# Solution for HackerRank:
# https://www.hackerrank.com/surajcpp115?hr_r=1
# https://www.hackerrank.com/contests/projecteuler/challenges/euler024/forum/comments/947356
s = list("abcdefghijklm")
factorials = [1]
for i in range(1, 14):
    factorials.append(factorials[i-1] * i)
    
def per(arr, k, n = 13, ans = ""):
    if n == 1:
        ans += arr.pop(0)
        return ans
    index = k // factorials[n-1]
    if not k % factorials[n-1]:
        index -= 1
    ans += arr.pop(index)
    k -= factorials[n-1] * index
    return per(arr, k, n - 1, ans)
    
for _ in range(int(input())):
    N =  int(input())
    answer = per(s[:], N)
    print(answer)