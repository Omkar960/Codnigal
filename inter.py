set1 = {1,2,3,4}
set2 = {2,3,4,5,6}
print('Original sets:')
print(set1)
print(set2)
a = set1.intersection(set2)
b = set1.union(set2)
c = set1.difference(set2)
d = set2.difference(set1)
print(a)
print(b)
print(c)
print(d)