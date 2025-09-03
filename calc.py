def add(P,Q):
    return P+Q
def subtract(P,Q):
    return P-Q
def mulitply(P,Q):
    return P*Q
def divide(P,Q):
    return P/Q
print("Select an operation")
print("A,add")
print("B,subtract")
print("C,mulitply")
print("D,divide")


choice = input("Select one: ")
P = int(input("Select 1st number: "))
Q = int(input("Select 2nd number: "))

if choice == "A":
    
    print(add(P,Q))
elif choice == "B":
    print(subtract(P,Q))
elif choice == "C":
    print(mulitply(P,Q))
elif choice == "D":
    print(divide(P,Q))
else:
    print("Invalid")