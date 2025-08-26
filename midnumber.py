number = int(input("Enter a number"))
t= number
numLen = 0

while t > 0:
    numLen += 1
    t = int(t/10)

if numLen >= 4:
    mid_pos1 = numLen // 2
    mid_pos2 = mid_pos1 - 1
    chk = 0
    midOne = midTwo = 0
    while number > 0:
        rem = number % 10
        if chk == mid_pos1:
            midOne = rem
        elif chk == mid_pos2:
            midTwo = rem
        number = int(number / 10)
        chk += 1
    prod = midOne * midTwo
    print("The product of the midpoints are", prod)
else:
    print("It's not a 4 digit number")


