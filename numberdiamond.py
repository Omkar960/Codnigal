rownumber = int(input("Enter the number of rows: "))

if rownumber % 2 == 0:
    halfDiam = int(rownumber/2)
else:
    halfDiam = int(rownumber/2)+1
space = halfDiam - 1

for i in range(1,halfDiam+1):

        for j in range(1,space+1):
             print(end=" ")
        space = space - 1
        num = 1
        for j in range(i*2-1):
             print(end=str(num))
             num += 1

        print()
space = 1


for i in range(1,halfDiam):

        for j in range(1,space+1):
             print(end=" ")
        space = space + 1
        num = 1
        for j in range(1,2*(halfDiam-i)):
             print(end=str(num))
             num += 1

        print()

         
        
         


             




