__date__ = "08 Nov 2022"
__answer__ = 23514624000

__problem__ = """
The four adjacent digits in the 1000-digit number that have the greatest product are 9 × 9 × 8 × 9 = 5832.
73167176531330624919225119674426574742355349194934
96983520312774506326239578318016984801869478851843
..................................................
I didn't include them all here because there are too many numbers.
https://projecteuler.net/problem=8 for all numbers.
Find the thirteen adjacent digits in the 1000-digit number that have the greatest product. What is the value of this product?    
"""

# ---------------------------------------------------------


# # 1 # Solution 1:
def product(k: int, N):
    i = 0
    mx = 0
    while True:
        s = N[i : i + k]
        if len(s) < k: break
        if "0" in s:
            i += s.find("0") + 1
        else:
            mul = 1
            for l in s: mul *= int(l) 
            if  mul > mx: 
                mx = mul
            i += 1
    return mx
k = int(input()) # k = number of adjacent digits
N = input().strip() # number
print(product(k, N))