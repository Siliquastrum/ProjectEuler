__date__ = "09 Nov 2022"
__answer__ = 142913828922

__problem__ = """
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
"""

# ---------------------------------------------------------


# # 3 # My Solution for HackerRank:
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


# ---------------------------------------------------------


""" # 2 # Pseudo Solution  (only test 7 exceeded the time limit):
def isPrime(n):
    for i in range(3, int(pow(n, 0.5))+1,):
        if n % i == 0: return False
    return True

primes = [2, 3]

t = int(input().strip())
inputs = [int(input().strip()) for _ in range(t)]

for i in range(5, max(inputs)+1, 2):
        if isPrime(i): primes.append(i)
        
for inp in inputs:
    n = inp
    ind = n
    while not ind in primes: ind -= 1
    print(sum(primes[:(primes.index(ind))+1]))

"""


# ---------------------------------------------------------


""" # 1 # This solution is too slow:
def isPrime(n):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0: return False
    return True
prime = [2] + [i for i in range(3, int(input())+1, 2) if isPrime(i)]
print(sum(prime))
"""