__date__ = "14 Nov 2022"
__answer__ = 31626

__problem__ = """
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.
For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
Evaluate the sum of all the amicable numbers under 10000.
"""

# ---------------------------------------------------------


# # 2 # Solution, this solution sometimes exceeds the time limit, sometimes not:
# always a valid solution in pypy 3
def isPrime(n:int) -> bool:
    for i in range(2, int(n**0.5)+1):
        if n % i == 0: return False
    return True

inputs = [int(input()) for _ in range(int(input()))]
mx = max(inputs)
prime = [False, False] + [True for _ in range(2, mx + 1)]
k = 2
while ((k**2) <= (mx+1)):
    if isPrime(k):
        for ind in range(k*2, mx + 1, k):
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

def d(num:int) -> int:
    dic = factorization(num)
    tot = 1
    for pr in dic:
        tot *= sum([pr ** i for i in range(dic[pr]+1)])
    return tot - num

tot = 504
sol = {}
for a in range(1000, mx+1):
    b = d(a)
    if b < mx or a in inputs:
        if d(b) == a and a!=b: tot += a
        if a in inputs: sol[a] = tot

for inp in inputs:
    if inp in sol: print(sol[inp])
    else: 
        if inp < 220: print(0)
        else: print(504)


# ---------------------------------------------------------


""" # 1 # Pseudo Solution  (only test 3 exceeded the time limit):
def isPrime(n:int) -> bool:
    for i in range(2, int(n**0.5)+1):
        if n % i == 0: return False
    return True

\""" sum of positive divisors

n = x^a * y^b * z^c   | x,y,z ∈ prime; a,b,c ∈ N

sum = (1 + x^1 + x^2 + ... + x^a) * (1 + y^1 + y^2 + ... + y^b) * (1 + z^1 + z^2 + ... + z^c)

\"""
prime = [2, 3, 5, 7, 11, 13, 17, 19]
def factorization(n:int) -> dict:
    dic = {}
    ind = 0
    while n != 1 and ind < len(prime):
        if n % prime[ind] == 0:
            n = n//prime[ind]
            if prime[ind] in dic: dic[prime[ind]] += 1
            else: dic[prime[ind]] = 1
        else:ind += 1
    if n != 1:
        for k in range(max(prime) + 2, n + 1, 2):
            if n == 1: break
            if isPrime(k):
                prime.append(k)
                while n%k == 0:
                    n = n//k
                    if k in dic: dic[k] += 1
                    else: dic[k] = 1
    return dic

def d(num:int) -> int:
    dic = factorization(num)
    tot = 1
    for pr in dic:
        tot *= sum([pr ** i for i in range(dic[pr]+1)])
    return tot - num

# this solution for the projecteuler.net
tot = 0
for a in range(5, int(input())+1):
    b = d(a)
    if d(b) == a and a!=b: tot += a
print(tot)

# this solution for the HackerRank:
inputs = [int(input()) for _ in range(int(input()))]
tot = 0
sol = {}
for a in range(5, max(inputs)+1):
    b = d(a)
    if d(b) == a and a!=b: tot += a
    if a in inputs: sol[a] = tot
print(*[sol[inp] for inp in inputs], sep="\n")
"""