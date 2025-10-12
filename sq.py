start = int(input("Enter start value: "))
end = int(input("Enter end value: "))


square_list = [i**2 for i in range(start, end + 1)]


print(square_list)
