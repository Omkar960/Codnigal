dic1 = {"Codingal":2,"is":2,"the":3,"best":2}

print(str(dic1))
K = 2
res = 0
for key in dic1:
    if dic1[key] == K:
        res += 1
print("Result is ",str(res))

