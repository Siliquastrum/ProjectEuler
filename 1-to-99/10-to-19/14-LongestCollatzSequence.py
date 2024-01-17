__date__ = "11 Nov 2022"
__answer__ = 837799

__problem__ = """
The following iterative sequence is defined for the set of positive integers:
n → n/2 (n is even)
n → 3n + 1 (n is odd)
Using the rule above and starting with 13, we generate the following sequence:
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
Which starting number, under one million, produces the longest chain?
NOTE: Once the chain starts the terms are allowed to go above one million.
"""

# ---------------------------------------------------------


# Solution:
inps = [int(input()) for _ in range(int(input()))] # inputs
mx = max(inps) # maximum input

step = [1 for _ in range(mx + 1)] # each index of the list corresponds to a number, e.g: step[5] = How many steps do you take to get 1 from 5?

# this loop adds to the "step" list in how many steps all numbers up to the largest number entered will reach 1
for ind in range(2, mx+1): 
    cnt = 0
    cur = ind
    while cur >= ind: 
        if cur % 2 == 0:
            cnt += 1
            cur = cur//2
        else:
            cnt += 1
            cur = (3*cur) + 1
    step[ind] = cnt + step[cur]

""" This part is too slow, so i followed a different solution way below
for inp in inps:
    mxnum = 1
    mxval = 1
    for i in range(inp, 1, -1):
        if step[i]>mxval:
            mxval = step[i]
            mxnum = i
    print(mxnum)
"""

res = [1 for _ in range(mx + 1)]
mxnum = 1
mxval = 1
for i in range(2, mx+1):
    if step[i] >= mxval:
        mxval = step[i]
        mxnum = i
    res[i] = mxnum # e.g: i=5 => 3, The number that is less than 5 and has the most steps is 3
for inp in inps:
    print(res[inp])


