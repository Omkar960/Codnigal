L = [1,2,3,4,5,6,7,8,9,10]
print("Original list is",L)

count = 0

for i in L:
    count +=1 
avg=count/len(L)

print("Sum",count)
print("Avg",avg)
L.sort()
print("Smallest number is ",L[0])
print("Largest number is",L[-1])
