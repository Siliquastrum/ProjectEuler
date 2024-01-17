__date__ = "09 Nov 2022"
__answer__ = 142913828922

__problem__ = """
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
"""

# ---------------------------------------------------------


# My Solution for HackerRank:
def isPrime(n):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0: return False
    return True

t = int(input().strip())
inputs = [int(input().strip()) for _ in range(t)]
mx = max(inputs)
numbers = [False, False] + [True for _ in range(2, mx + 1)]

k = 2
while ((k**2) <= (mx+1)):
    if isPrime(k):
        for ind in range(k*2, mx + 1, k):
            numbers[ind] = False
    k += 1

dic = dict()
tot = 0
for ind in range(mx + 1):
    if numbers[ind]:
        tot += ind
        dic[ind] = tot

for inp in inputs:
    while True:
        if isPrime(inp):
            break
        inp -= 1
    print(dic[inp])