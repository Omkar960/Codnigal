import random
length = int(input("How many characters: "))
list = ["a",'b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','x','w','y','z',]
list2 = [list.capitalize() for list in list]
list3 = ["1","2","3","4","5","6","7","8","9","10"]
list4 = list + list2 + list
password = []
for i in range(10):
    password += random.choice(list4)

print(password)

