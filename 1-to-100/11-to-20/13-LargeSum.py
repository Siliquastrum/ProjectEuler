__date__ = "07 Nov 2022"
__answer__ = 5537376230 # this number is very similar to my phone number :)

__problem__ = """
Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.

37107287533902102798797998220837590246510135740250
46376937677490009712648124896970078050417018260538
..................................................
I didn't include them all here because there are too many numbers.
https://projecteuler.net/problem=13 for all numbers.
"""

# ---------------------------------------------------------


# # 1 # Very Easy Solution in One Line, if the input is as in hackerrank:
print(str(sum([int(input()) for _ in range(int(input()))]))[:10])


# ---------------------------------------------------------


# # 2 # Solution if the input is as in ProjectEuler.net:
lst = []
while True:
    inp = input()
    if inp == "": break
    lst.append(int(inp))
print(str(sum(lst))[:10])
