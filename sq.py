start = int(input("Enter start value: "))
end = int(input("Enter end value: "))

number = 0
for i in range( start, end + 1):
    
    print(i*i)
    if i*i % 2 == 0:
        print("It's even")
    else:
        print("It's odd")
  






