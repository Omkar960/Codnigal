a = {1,2,3,4}
b = {5,6,7,8}
d = zip(a,b)
print(list(d))
list = [10,20,30,40,50,60,70]
list2 = [100,200,300,400,500,600,700]
for x,y in zip(list,list2[::-1]):
 print(x,y)

e = ["reliance","infosys","tcs"]
f = [2543,2133,7000]
new_dict ={e:f for e,f in zip(e,f)}
print(new_dict)