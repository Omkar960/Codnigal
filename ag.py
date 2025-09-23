try:
 ae = int(input("Enter your age: "))
 if ae % 2 == 0:
  print("It's even")
 else:
  print("It's odd")
except ValueError as ex:
 print("There has been an error",ex)