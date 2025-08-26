lowernumber = int(input("Enter a low number: "))
highnumber = int(input("Enter a high number: "))

print("Prime numbers between",lowernumber,"and",highnumber,"are: ")

for num in range(lowernumber,highnumber+1):
    if num > 1:
        for i in range (2,num):
            if(num%i) == 0:
                break
            else:
             print(num)
