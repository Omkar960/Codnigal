try:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter a number"))

    result = num1/num2
    print(result)
    print(result1)

except ZeroDivisionError:
    print("You can't divide a number by zero")
except ValueError:
    print("You didn't enter a integer")
except NameError as ex:
    print("The exception is",ex)

except:
    print("Some error has occured")
finally:
    print("I will run no matter what")
