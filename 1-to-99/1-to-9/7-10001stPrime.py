__date__ = "07 Nov 2022"
__answer__ = 104743

__problem__ = """
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10001st prime number?
"""

# ---------------------------------------------------------


# My Solution for HackerRank:
# https://www.hackerrank.com/contests/projecteuler/challenges/euler007/problem
prime = [0, 2, 3]
def isPrime(n):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0: return False
    return True

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    try: 
        print(prime[n])
    except:
        ln = len(prime)
        ind = ln - 1
        num = prime[ind]
        while ln <= n+1:
            num += 2
            if isPrime(num): 
                prime.append(num)
                ln += 1
        print(prime[n])
