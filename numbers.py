import random 

def pick_random():
    balls = ['Red','Blue','Green']
    result = random.choice(balls)

    pro = balls.count('Red')/len(balls)
    print('Proability is: ',pro)


    if result == 'Red':

        return 'Red ball was picked'
    else:
        return "Red ball wasn't picked"

pick_random()