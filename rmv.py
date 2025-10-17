dic1 = {1:{'name': "Sara",'age':7} ,2:{'name': "Jeff",'age':5},3:{'name': "Sara",'age':7},4:{'name': "Jeff",'age':5}}
print (dic1.items())
result = {}

for key,value in dic1.items():

    if value not in result.values():
        result[key] = value

print(result)


