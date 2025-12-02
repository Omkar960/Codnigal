import re,random
from colorama import Fore, init

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
def showhelp():
    print(f"{Fore.MAGENTA} \n I can")
    print(f"{Fore.GREEN} \n Suggest travel spots (say recommendation)")
    print(f"{Fore.GREEN} \n Offer packing tips(say packing)")
    print(f"{Fore.GREEN} \n Tell a joke (say joke)")
    print(f"{Fore.GREEN} \n Type exit or bye to end. \n")
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

