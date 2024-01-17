__date__ = "05 Nov 2022"
__answer__ = 906609

__problem__ = """
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
"""

# ---------------------------------------------------------


# Solution of the problem in one line
print(max([a*b for a in range(999, 99, -1) for b in range(a, 99, -1) if str(a*b) == str(a*b)[::-1]]))
# Answer = 906609


# ---------------------------------------------------------


# Main Solution: 
def ispal(x):
    return True if str(x) == str(x)[::-1] else False

lst = set(a*b for a in range(999, 99, -1) for b in range(a, 99, -1) if ispal(a*b))
N = int(input()) # maximum number
# 999*999 = 998001 for product of two 3-digit numbers or another number entry
# returns 906609 if the number 998001 is entered
mx = max(i for i in lst if i < N)
print(mx)


