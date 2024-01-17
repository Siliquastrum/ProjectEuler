__date__ = "15 Nov 2022"
__answer__ = 171

__problem__ = """
You are given the following information, but you may prefer to do some research for yourself.
1 Jan 1900 was a Monday.
    # https://en.wikipedia.org/wiki/Thirty_Days_Hath_September
    Thirty days has September,
    April, June and November.
    All the rest have thirty-one,
    Saving February alone,
    Which has twenty-eight, rain or shine.
    And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""

# ---------------------------------------------------------


# Solution:
month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
def isLeap(year) -> bool:
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                if year & 4000 == 0: return False
                return True
            return False
        return True

def newdate(date):
    y, m, d = date[0], date[1], date[2]
    if m <= 12 and d <= month[m]: return date
    if m != 2 and m != 12:
        return [y, m+1, d - month[m]]
    elif m == 12:
        return [y+1, 1, d - month[m]]
    else:
        if isLeap(y): 
            if d == 29: nd = 7
            else: nd = d - 29
            return [y, 3, nd]
        else: return [y, m+1, d - month[m]]

def counting(first:list, second:list):
    sundays = 0
    while not (first[0] == second[0] and first[1] == second[1]):
        if first[2] == 1: sundays += 1
        while first[2] <= month[first[1]]:
            first[2] += 7
        first = newdate(first)
    if first[2] == 1: sundays += 1 
    return sundays

# I spent a lot of time doing the function that finds sunday, but my functions were running very slow. 
# finally i had to look at the hackerrank forum and found this function which abdur_rakib_1508 did:
def day(date):
    # https://www.hackerrank.com/abdur_rakib_1508
    # https://www.hackerrank.com/contests/projecteuler/challenges/euler019/forum/comments/888030
    year = date[0]
    month = date[1]
    day = date[2]
    if month < 3:
        month += 12
        year -= 1
    cent = year // 100
    y = year % 100
    d = (y + (y // 4) + (cent // 4) - (2 * cent) + ((26 * (month + 1)) // 10) + day - 1) % 7
    return d


for _ in range(int(input())):
    start, end = [list(map(int, input().strip().split())), list(map(int, input().strip().split()))]
    d = day(start)
    if d != 0:
        start[2] += 7 - d
        start = newdate(start)
    print(counting(start, end))
