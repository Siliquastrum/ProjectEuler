__date__ = "13 Nov 2022"
__answer__ = 21124

__problem__ = """
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
"""

# ---------------------------------------------------------


# Solution for HackerRank:
onedg = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
twodg = [["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", 
"Seventeen", "Eighteen", "Nineteen"],["Twenty", "Thirty", "Forty", "Fifty", "Sixty", 
"Seventy", "Eighty", "Ninety"]]
other = {0:"", 3:"Thousand", 6:"Million", 9:"Billion", 12:"Trillion"}

def tridigit(num:str): # this function analyzes the 3 digit number sent inside
    
    n3 = int(num[0])
    n2 = int(num[1])
    n1 = int(num[2])
    if n3 != 0:
        res = onedg[int(n3)] + " Hundred "
    else: res = ""
    if n2 == 1:
        res = res + twodg[0][n1]
    elif n2 == 0:
        res = res + onedg[n1]
    else:
        res = res + twodg[1][n2-2] + " " + onedg[n1]
    return res.strip()


for _ in range(int(input())):
    num = input().strip()
    if int(num) != 0:
        # I will separate the numbers by 3 digits
        ln = len(num)
        if ln%3 == 2: num = "0" + num
        elif ln%3 == 1: num = "00" + num
        ln = len(num)
        result = []
        for i in range(0, ln, 3):
            number = tridigit(num[i:i+3])
            res = (number + " " + other[abs(i-ln + 3)]).strip()
            if number != "": result.append(res)
        print(" ".join(result))
    else: print("Zero")


# ---------------------------------------------------------


# # 2 # Solution for projecteuler.net
onedg = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
twodg = [["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", 
"Seventeen", "Eighteen", "Nineteen"],["Twenty", "Thirty", "Forty", "Fifty", "Sixty", 
"Seventy", "Eighty", "Ninety"]]
other = {0:"", 3:"Thousand", 6:"Million", 9:"Billion", 12:"Trillion"}

def tridigitpe(num:str):
    n3 = int(num[0])
    n2 = int(num[1])
    n1 = int(num[2])

    if n3 != 0:
        res = onedg[int(n3)] + " Hundred "
    else: res = ""
    if n2 == 1:
        res = res + twodg[0][n1]
    elif n2 == 0:
        res = res + onedg[n1]
    else:
        res = res + twodg[1][n2-2] + " " + onedg[n1]
    if res[-8:-1].strip() != "Hundred":
        hund = res.find("Hundred") 
        if hund != -1:
            res = res[:hund+8].strip() + " and " + res[hund + 8:].strip()
    return res.strip()
numbers = []
for num in range(1, 1001):
    num = str(num)
    ln = len(num)
    if ln%3 == 2: num = "0" + num
    elif ln%3 == 1: num = "00" + num
    ln = len(num)
    result = []
    for i in range(0, ln, 3):
        number = tridigitpe(num[i:i+3])
        res = (number + " " + other[abs(i-ln + 3)]).strip()
        if number != "": result.append(res)
    numbers.append(" ".join(result))
sumleng = len("".join(["".join(x.split()) for x in numbers]))
print(sumleng)