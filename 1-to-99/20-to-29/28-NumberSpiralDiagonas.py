__date__ = "17 Nov 2022"
__answer__ = 669171001

__problem__ = """

Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

43 44 45 46 47 48 49 50
42 21 22 23 24 25 26
41 20  7  8  9 10 27
40 19  6  1  2 11 28
39 18  5  4  3 12 29
38 17 16 15 14 13 30
37 36 35 34 33 32 31

It can be verified that the sum of the numbers on the diagonals is 101.
What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
"""

# ---------------------------------------------------------


# Solution:

inps = [int(input()) for _ in range(int(input()))]
mx = max(inps)
way = [False, True, 3]
def changeWay(): 
    if way[0]:
        way[0] = False
    else:
        way[2] += 1
        way[0] = True
        if way[1]:
            way[1] = False
        else:
            way[1] = True

ans = {1:1, 3:25}
tot = 25
k = -1
for num in range(10, (mx**2)+2):
    k += 1
    if k == way[2]: 
        k = 0
        tot += num
        if (num-1)**0.5 in inps:
            tot -= 1
            ans[(num-1)**0.5] = tot

        changeWay()

for i in inps:
    print(ans[i])

