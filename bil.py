bill = int(input("Please enter the amount: "))
pay = int(input("Please enter the amount you would like to pay: "))


dueamount = bill - pay
while dueamount != 1:
  if dueamount == 0:
    print("You have paid enough")
    break
  elif dueamount > 0:
    print("You haven't paid enough")
    break
