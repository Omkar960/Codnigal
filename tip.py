def my_func(bill,percent):
    total = bill*(1+0.01*percent)
    total = round(total,2)
    print(f"The bill is £{total}")

my_func(154,20)


 
