def rectangl(A,B):
    return (A*2)+(B*2)
def squar(A):
    return(A*4)

print("Choose if you between sqaure or rectangle")
print("A, square")
print("B,rectangle")

choice = input("Select one: ")


if choice == "A":
    A = int(input("What's the length of one side:"))
    print(squar(A,))
elif choice == "B":
    A = int(input("What's the length of one side: "))
    B = int(input("What's the length of the other side: "))
    print(rectangl(A,B))

    