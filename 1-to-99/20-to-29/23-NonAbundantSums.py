__date__ = "16 Nov 2022"
__answer__ = 4179871

__problem__ = """
https://en.wikipedia.org/wiki/Abundant_number
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. 
For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.
A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.
As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. 
By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. 
However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.
Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
"""

# ---------------------------------------------------------


# Solution for HackerRank:
# i was a bit inspired by this solution: https://www.hackerrank.com/contests/projecteuler/challenges/euler023/forum/comments/964037
def sumfac(n):
    k = 1
    for i in range(2, int(int(n**0.5) + 1)):
        if n%i == 0:
            k += i
            y = n/i
            if i != y: k += y
    return k

m = [int(input()) for _ in range(int(input()))]
mx = max(m) if max(m) < 28123 else 28123
lst = [False, False]
for a in range(2, mx):
    if a < sumfac(a):
        lst.append(True)
    else: lst.append(False)

# this part is for hackerrank
for inp in m:
    if inp >= 28123: print("YES")
    else:
        for i in range(1, inp//2 + 1):
            if lst[inp - i] and lst[i]:
                print("YES")
                break
        else:
            print("NO")


# ---------------------------------------------------------


# Solution for projecteuler.net:
def sumfac(n):
    k = 1
    for i in range(2, int(int(n**0.5) + 1)):
        if n%i == 0:
            k += i
            y = n/i
            if i != y: k += y
    return k

lst = [False, False]
for a in range(2, 28124):
    if a < sumfac(a):
        lst.append(True)
    else: lst.append(False)

tot = 0
for num in range(1, 28124):
    for i in range(1, num//2 + 1):
        if lst[num - i] and lst[i]:
            break
    else:
        tot += num
print(tot)
