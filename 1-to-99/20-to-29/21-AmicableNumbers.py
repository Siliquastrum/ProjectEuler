__date__ = "14 Nov 2022"
__answer__ = 31626

__problem__ = """
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.
For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
Evaluate the sum of all the amicable numbers under 10000.
"""

# ---------------------------------------------------------


# Solution, this solution sometimes exceeds the time limit, sometimes not, idk why (in hackerrank):
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