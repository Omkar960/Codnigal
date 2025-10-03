import math

choice = input("Do you want to find a side or an angle,Y for side,N, for angle: ")

if choice == "Y":
    tri = input("Do you want S(sin),C(cos) or T(tan): ")
    sid = int(input("Enter side length: "))
    an = int(input("Enter angle :"))

    if tri == "S":
         a = sid/ math.sin(an)
         print(a)
    elif tri == "C":
        a = sid/ math.cos(an)
        print(a)
    else:
        a = sid/ math.tan(an)
        print(a)
elif choice == "N":
    tris = input("Do you want S(sin),C(cos) or T(tan): ")
    side = int(input("Enter your side"))
    sides = int(input("Enter your side"))

    if tris == "S":
        a = math.asin(side / sides)
        print(a*100)
    elif tris == "C":
        a = math.acos(side / sides)
        print(a*100)
    else:
        a = math.atan(side / sides)
        print(a*100)


