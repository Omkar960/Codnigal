attendance = int(input("Enter student attendance"))
medcon = input("Does the student have a medical condition")

if medcon == "yes":
 
 print("Allowed")
else:

 if attendance >= 75:

  print("allowed")

 else:
  print("Not allowed")

 
