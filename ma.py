list1 = [1,2,3,4]
list2 = [2,3,4,5]
a = map(lambda x,y:x+y,list1, list2)
print(list(a))
number = [1,2,3,4]
def func(n):
 return(n**n)

b=map(func,number)
print(list(b))
