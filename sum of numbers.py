number = int(input("Please enter in a number: "))
sum = 0
for i in range(number,0,-1):
    sum += i
print("The sum of all numbers from 1 to", number, "is", sum)