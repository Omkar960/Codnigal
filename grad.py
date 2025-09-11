
mark = 1
while mark > 0:

 mark = int(input("Enter your mark: "))
 if mark < 40:
    print("You have failed")
    break
 elif mark >= 40 and mark <=80:
    print("You have passed")

 else:
    print("You have got the highest in the class")