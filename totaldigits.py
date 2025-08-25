num = int(input("Enter a number: "))
dig = 0

while num > 0:
    num //= 10
    dig += 1

print("There is",dig,"digits in your number")
