for i in range(20):
    if i % 20 == 0:
        print("Buzz")
    elif i % 15 == 0:
        pass
    elif i % 5 == 0:
        print("Fizz")
    elif i % 3 == 0:
        print("Twist")
    else:
        print(i)