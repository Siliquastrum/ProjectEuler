__author__ = "Enes Bekdemir"
__date__ = "05 Nov 2022"

""" Problem
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
Answer: 906609
"""


# # 2 # Solution of the problem in one line
print(max([a*b for a in range(999, 99, -1) for b in range(a, 99, -1) if str(a*b) == str(a*b)[::-1]]))
# Answer = 906609





# # 6 # Main Solution: (It felt a bit strange to find after 5 different long solutions)
def ispal(x):
    return True if str(x) == str(x)[::-1] else False

lst = set(a*b for a in range(999, 99, -1) for b in range(a, 99, -1) if ispal(a*b))
N = int(input()) # maximum number
# 999*999 = 998001 for product of two 3-digit numbers or another number entry
# returns 906609 if the number 998001 is entered
mx = max(i for i in lst if i < N)
print(mx)




""" # 3 # Pseudo Solution (time limit exceeded)
# Largest palindrome made from the product of two 3-digit numbers which is less than N.
def lesspalindrome(N):
    for mult in sorted([a*b for a in range(999, 99, -1) for b in range(a, 99, -1) if str(a*b) == str(a*b)[::-1]])[::-1]:
        if mult <= N:
            return mult
# print(lesspalindrome(int(input())))
"""






""" # 4 # Pseudo Solution (time limit exceeded)
def ispal(x):
    return True if str(x) == str(x)[::-1] else False
N = int(input())
print(max(set(a*b for a in range(999, 99, -1) for b in range(a, 99, -1) if (ispal(a*b) and a*b<=N))))
"""





""" # 5 # Pseudo Solution (time limit exceeded)
def ispal(x):
    return True if str(x) == str(x)[::-1] else False

def lesspal(N):
    mx = 0
    for a in range(999, 99, -1):
        for b in range(a, 99, -1):
            if ispal(a*b):
                if mx < a*b <= N: mx = a*b
        if mx == N: break
    return mx
"""





""" # 1 # This function finds the largest palindrome smaller than the entered number, ie it solves a different problem
def palindrom(n):
    for i in range(n, 0, -1):
        if str(i) == str(i)[::-1]: return i

print(palindrom(int(input())))
"""