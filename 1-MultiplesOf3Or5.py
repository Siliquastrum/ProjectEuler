__author__ = "Enes Bekdemir"
__date__ = "05 Nov 2022"

""" Problem
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
"""

# # 3 # Solution 1:
f = lambda a: a * (a + 1) // 2

def solution(n):
    n -= 1
    return 3 * f(n//3) + 5 * f(n//5) - 15 * f(n//15)
print(solution(int(input()))) # 1000 or another number entry
# returns 233168 if the number 1000 is entered





""" # 2 # Pseudo Solution
for a0 in range(int(input().strip())):
    x = 0
    for num in range(1, int(input().strip())):
        if num%3 == 0 or num%5 == 0: x += num 
    print(x)
""" 





""" # 1 # Pseudo Solution
for a0 in range(int(input().strip())):
    print(sum([num for num in range(1, int(input().strip())) if num%3 == 0 or num%5 == 0]))
""" 
    