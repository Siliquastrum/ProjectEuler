__date__ = "15 Nov 2022"
__answer__ = 871198282

__problem__ = """
https://projecteuler.net/problem=22
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.
For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.
What is the total of all the name scores in the file?
"""

# ---------------------------------------------------------


# Solution for HackerRank:
names = [" "] + sorted([input().strip().upper() for _ in range(int(input()))])
q = [input().strip().upper() for _ in range(int(input()))]
letter = "_ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def score(word):
    return sum([letter.find(l) for l in word])

for n in q:
    print(names.index(n) * score(n))


# ---------------------------------------------------------


# Solution for projecteuler.net:
with open("22-names.txt", "r") as f:
    names = sorted(f.read().strip('"').split('","'))

letter = "_ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def score(word):
    return sum([letter.find(l) for l in word])

tot = sum([(i+1)*score(word=word) for i,word in enumerate(names)])
print(tot)