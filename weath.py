sunny = 0
rainy = 0
tuple = (0,1,0,1,0,1,1,)
for i in range(0,7):
    if tuple[1]==0:
        rainy +=1
    else:
        sunny +=1
if sunny>rainy:
    print("It's going to be sunny")
else:
    print("It's going to be rainy")
