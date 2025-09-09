def my_func(number):
    
    number = number ** 3
    return number

def my_number(number):
    if number%3 == 0:
        return my_func(number)
    else:
        return False
print(my_number(12))
print(my_number(6))