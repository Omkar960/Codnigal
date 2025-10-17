dic1 = {"Codingal": 1, "Is": 1, "The": 2, "Best": 2, "Ok": 3, "O": 3}
user = int(input("Which number do you want to check the frequency of (1-3): "))
repo = 0

for key in dic1:
    if dic1[key] == user:
        repo += 1
    else:
     pass

print(repo)

    
    