def factorial(x):
    '''This is a recursive function to find the integer'''
    if x == 0 or x == 1:
        return 1
    else:
     return x*factorial(x-1)
    
print(factorial.__doc__)
print("Factorial of 2:",factorial(2))
print("Factorial of 5:",factorial(5))
print("Factorial of 6:",factorial(6))
print("Factorial of 10:",factorial(10))

