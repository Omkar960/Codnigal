import re,random
from colorama import Fore, init
import turtle

init(autoreset=True)

destination = {
    "beaches":["Bali","Maldives","Phoket"],
    "mountains":["Swiss Alps","Rocky Mountains","Himalayas"],
    "cities":["Tokyo","Paris","New York"]
}

jokes = [
    "Why don't programmers like nature? Too many bugs!",
    "Why did the computer go to the doctor? Because it had a virus!",
    "Why do travelers always feel warm? Because of all their hot spots!"
]
def telljoke():
    print(f"{Fore.YELLOW}Travelbot: {random.choice(jokes)}")

def draw():
    color = input(f"{Fore.GREEN}What's your favourite colour: ")
    turtle.fillcolor(color)
    choice = input(f"{Fore.GREEN}What do you want me to draw(circle,square or hexagon): ")
    if choice.lower() == "circle":
        turtle.begin_fill()
        turtle.circle(100)
        turtle.hideturtle()
        turtle.end_fill()
    elif choice.lower() == "square":
        turtle.fillcolor(color)
        turtle.begin_fill()
        for i in range(4):
            turtle.forward(150)
            turtle.right(90)
            turtle.hideturtle()
        turtle.end_fill()
            
    elif choice.lower() == "hexagon":
        turtle.fillcolor(color)
        turtle.begin_fill()
        for i in range(6):
            turtle.forward(150)
            turtle.right(60)
            turtle.hideturtle()
        turtle.end_fill()
    else:
        choice= input(f"{Fore.RED} Could you rephrase: ")
def weather():
    place = input(f"{Fore.GREEN}Where to: ")
    if place.lower() == "bali":
        print("It's approx 25 degrees on average and it's humid ")
    elif place.lower() == "maldives":
        print("It's approx 27 degrees on average and it's humid")
    elif place.lower() == "phoket":
        print("It's approx 27 degrees on average and it's humid")
    elif place.lower() == "new york":
        print("In the winter it's approx -7 degrees and quite chilly")

    elif place.lower() == "tokyo":
         print("In the winter it's approx 10 degrees and quite chilly")
      
    elif place.lower() == "paris":
         print("In the winter it's approx 6 degrees and quite chilly")

    elif place.lower() == "swiss alps":
        print("It's approx -5 degrees on average and it's humid")

    elif place.lower() == "himalayas":
        print("In the winter approx -40 degrees and it's chilly")

    elif place.lower == "rocky mountains":
         print("In the winter it's approx -11 degrees and quite chilly")

def price():
    place = input(f"{Fore.GREEN}Where to: ")
    days = int(input(f'{Fore.GREEN}How many day: '))
    nights = int(input(f"{Fore.GREEN}How many nights: "))
    hotel = int(input(f"{Fore.GREEN}How many stars is your hotel(1-5): "))
    daysprice = 0
    nightsprice = 0

    if place.capitalize() == "Tokyo" or place == "Paris" or place == "New York":
        ticketsprice = 2,000
    elif place.capitalize() == "Swiss Alps" or place == "Rocky Mountains" or place ==  "Himalayas":
        ticketsprice = 1,750
    elif place.capitalize() == "Bali" or place == "Maldives" or place == "Phoket":
        ticketsprice = 2,000
    else:
        place = input(f"{Fore.RED}Sorry,could you rephrase: ")
    if days == 1 or days == 2 or days == 3:
        daysprice = days * (100*hotel)
    elif days > 3 and days <= 7:
        daysprice = days * (90*hotel)
    elif days > 7 and days <= 15:
        daysprice = days * (80*hotel)
    elif days > 15:
        daysprice = days * (70*hotel)
    else:
        days = input(f"{Fore.RED}Could you rephrase: ")
    


    if nights == 1 or nights == 2 or nights == 3:
        nightsprice = days * (100*hotel)
    elif nights > 3 and nights <= 7:
        nightsprice = nights * (90*hotel)
    elif nights > 7 and nights <= 15:
        nightsprice = nights * (80*hotel)
    elif nights > 15:
        nightsprice = nights * (70*hotel)
    else:
        nights = input(f"{Fore.RED}Could you rephrase: ")
    
    ovrprice = daysprice + nightsprice
    print(f"{Fore.GREEN}Travelbot: Your total price is: £{ovrprice}")

def showhelp():
    print(f"{Fore.MAGENTA} \n I can")
    print(f"{Fore.GREEN} \n Suggest travel spots (say recommendation)")
    print(f"{Fore.GREEN} \n Offer packing tips(say packing)")
    print(f"{Fore.GREEN} \n Tell a joke (say joke)")
    print(f"{Fore.GREEN} \n Type exit or bye to end. \n")
    print(f"{Fore.GREEN}\n Type draw or paint for me to draw something of your choice: ")
    print(f"{Fore.GREEN}\n If you want me to find the price of your holiday,Type price or cost: ")
    print(f"{Fore.GREEN}\n If you want me to find the weather for your desired place Type weather or temperature: ")
def chat():
    print(f"{Fore.CYAN} Hello, I am a Travelbot!")

    name = input(f"{Fore.YELLOW} What's your name: ")
    print(f"{Fore.GREEN} nice to meet you {name}: ")
    showhelp()
    


    while True:
        userinput = input(f"{Fore.YELLOW} {name}")
        userinput = normalizeinput(userinput)

        if "recommend" in userinput or "suggest" in userinput:
            recommend()
        elif "pack" in userinput or "packing" in userinput:
            packingtips()
        elif "joke" in userinput or "funny" in userinput:
           telljoke()
        elif "recommend" in userinput:
            showhelp()
        elif "exit" in userinput or "bye" in userinput:
            print(f"{Fore.CYAN} Travelbot: Safe travels! Goodbye!")
            break
        elif "draw" in userinput or "paint" in userinput:
            draw()
        elif "price" in userinput or "cost" in userinput:
            price()
        elif "weather" in userinput or "temperature" in userinput:
            weather()
        else:
            print(f"{Fore.RED}Travelbot: Could you rephrase: ")
            
        
def normalizeinput(text):

    return re.sub(r"\s", "", text.strip().lower())
def recommend():
    print(f"{Fore.CYAN} Cities, mountains or beaches: ")

    preference = input(f"{Fore.YELLOW} You:")
    preference = normalizeinput(preference)

    if preference in destination:
        suggestion = random.choice(destination[preference])
        print(f"{Fore.GREEN} Travelbot: how about {suggestion}")
        print(f"{Fore.CYAN} Travelbot: do you like it?(yes/no)")

        answer = input(f"{Fore.YELLOW} You: ").lower()

        if answer == "yes":
            print(f"{Fore.GREEN} Travelbot: Awesome hope you enjoy it! ")
        elif answer == "no":
            print(f"{Fore.YELLOW} Travelbot: Let's try another: ")
            recommend()
        else:
            print(f"{Fore.YELLOW}I'll suggest another: ")
            recommend()
    else:
        print(f"{Fore.RED}Travelbot: I don't have that type of destination")
        showhelp()
def packingtips():
    print(f"{Fore.CYAN} Travelbot: Where to")
    location = normalizeinput(input(f"{Fore.YELLOW} You"))
    print(f"{Fore.CYAN} How many days")
    days = input(f"{Fore.YELLOW} You: ")
    print(f"{Fore.GREEN} Travelbot: Packing tips for {days} days and in {location}")
    print(f"{Fore.GREEN} Pack versatile clothes")
    print(f"{Fore.GREEN} Bring chargers/adaptors")
    print(f"{Fore.GREEN} Check the weather forecast")
            
if __name__ == "__main__":
    chat()

