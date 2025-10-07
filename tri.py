def hotel(days):
    return 140*days
def place(city):
    if "Charlotte" == city:
        return 183
    elif "Tampa" == city:
        return 220
    elif "Pittsburgh" == city:
        return 222
    elif "Los Angeles" == city:
        return 475
def rentcar(days):
    if days >= 7:
        return (days * 40) -50
        
    elif days >=3:
        return (days * 40) - 20
        
    else:
         return days * 40
def totalcost(city,days,spendingmoney ):
    return place(city) + hotel(days) + rentcar(days) + spendingmoney
print("Price of car rental",rentcar(6))
print("Price of plane",place("Los Angeles"))
print("Price of hotel",hotel(6))
print("Total cost of the trip is",totalcost("Los Angeles",7,500))
print(totalcost("Tampa",6,500))

    
