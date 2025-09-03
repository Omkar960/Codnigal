import math
def circum(A):
    return A * math.pi
def area(A):
    return (A ** 2) * math.pi

print("Select if you want to find the circumference or radius")
print("A, circumference")
print("B, area")
choice = input("Choose one: ")


if choice == "A":
    A = int(input("What's the diameter: "))
    print(circum(A))
else:
    A = int(input("What's the radius: "))
    print(area(A))
