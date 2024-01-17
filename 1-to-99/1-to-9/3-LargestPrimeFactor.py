__date__ = "05 Nov 2022"
__answer__ = 6857

__problem__ = """
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
"""

# ---------------------------------------------------------


# Solution 1:
import math

def isPrime(n): # Finds whether n is prime or not.
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0: return False
    return True

def maxPrimeFactor(n):
    max = 1
    for i in range(1, int(math.sqrt(n))+1):
        if n%i == 0:
            if isPrime(n//i) and n//i > max:
                max = n//i
                break
            elif isPrime(i): max = i        
    return max
print(maxPrimeFactor(int(input()))) # 600851475143 or another number entry
# returns 6857 if the number 600851475143 is entered