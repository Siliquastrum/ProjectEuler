__date__ = "16 Nov 2022"
__answer__ = 4782

__problem__ = """
The Fibonacci sequence is defined by the recurrence relation:
Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
Hence the first 12 terms will be:
F1 = 1
F2 = 1
F3 = 2
F4 = 3
F5 = 5
F6 = 8
F7 = 13
F8 = 21
F9 = 34
F10 = 55
F11 = 89
F12 = 144
The 12th term, F12, is the first term to contain three digits.
What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
"""

# ---------------------------------------------------------


# Solution for projecteuler.net:
fib = [1, 1]
mx = int(input())
while len(str(fib[-1])) != mx:
    fib.append(fib[-1] + fib[-2])
print(len(fib))


# ---------------------------------------------------------


# Solution for HackerRank:
fib = [1, 1]
inps = [int(input()) for _ in range(int(input()))]
mx = max(inps)
res = dict()
ln = len(str(fib[-1]))
while ln != mx:
    ln = len(str(fib[-1]))
    if ln in inps and not ln in res: res[ln] = len(fib)
    fib.append(fib[-1] + fib[-2])
for inp in inps:
    print(res[inp])