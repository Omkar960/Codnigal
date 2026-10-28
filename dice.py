import random
six = 0

for i in range(10):
    a = random.randint(1,6)
    if a == 6:
        print('Six!')
        six += 1
    else:
        print('Not Six')

print('Odds of a 6', six/10)
        
