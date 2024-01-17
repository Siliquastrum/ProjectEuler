__date__ = "06 Nov 2022"
__answer__ = 232792560

__problem__ = """
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

# ---------------------------------------------------------


# Solution 1:
from collections import Counter
import math

def isPrime(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0: return False
    return True


def primeDiv(num): # prime factorizes the number "num"
    pr = []
    for n in [i for i in range(2, num + 1) if num%i==0 if isPrime(i)]:
        while num % n == 0 and num != 1:
            num = int(num / n)
            pr.append(n)
    return pr

def leastCommonMultiple(n): # n = largest number
    if n <= 2: return n
    dic = {}
    for primes in [primeDiv(i) for i in range(2, n + 1)]: # Lists the prime factors of each of the numbers 1 to n
        C = Counter(primes)
        for i in C:
            if i in dic:
                if C[i] > dic[i]: dic[i] = C[i]
            else: dic[i] = C[i]
    x = 1
    for i in [a**dic[a] for a in dic]: x *= i
    return int(x)
print(leastCommonMultiple(int(input()))) # 20 or another number entry
# returns 232792560 if the number 20 is entered