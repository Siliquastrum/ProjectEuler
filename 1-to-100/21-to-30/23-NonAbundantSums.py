__date__ = "15 Nov 2022"
__answer__ = None

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


# # 2 # Solution for HackerRank:
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


# # 3 # Solution for projecteuler.net:
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


# ---------------------------------------------------------


""" # 1 # Unfinished Solution:
start = dt.now()
def isPrime(n:int) -> bool:
    for i in range(2, int(n**0.5)+1):
        if n % i == 0: return False
    return True

prime = [False, False] + [True for _ in range(2, 28124)]

k = 2
while ((k**2) <= (28124)):
    if isPrime(k):
        for ind in range(k*2, 28124, k):
            prime[ind] = False
    k += 1

def factorization(n:int) -> dict:
    dic = {}
    ind = 0
    while n != 1:
        if prime[ind]:
            while n%ind == 0:
                n = n // ind
                if ind in dic: dic[ind] += 1
                else: dic[ind] = 1
            ind += 1
        else: ind += 1
    return dic

def whatis(num:int):
    factor = factorization(num)    
    tot = 1
    for k in factor:
        tot *= sum([k ** i for i in range(factor[k]+1)])
    tot -= num
    if tot == num: return "P"
    elif tot < num: return "D"
    else: return "A"

abundant = [False for _ in range(28124)]
for nm in range(6,28123):
    num = nm
    what = whatis(nm)
    if what == "A" and not abundant[nm]:
        while num < 28123:
            abundant[num] = True
            num += nm
    elif what == "P" and not abundant[nm]:
        num += nm
        while num < 28123:
            abundant[num] = True
            num += nm
"""

