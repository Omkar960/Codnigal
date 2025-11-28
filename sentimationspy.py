import colorama
from colorama import Fore, Style
from textblob import TextBlob
colorama.init()

print(Fore.CYAN,"👋 🎉 Welcome to sentiment spy!")
username = input(Fore.MAGENTA,"Please enter your name: ")

if not username:
    username = "Mystery Agent"
conversationhistroy = []

print(Fore.CYAN,"Hello",username)
print("Type a sentence and I will rate it based on it's postivity and polarity")
print(f"Type {Fore.YELLOW}'reset',{Fore.CYAN},{Fore.YELLOW}'history',{Fore.CYAN}",f"{Fore.YELLOW}'exit'{Fore.CYAN},to quit.{Style.RESET_ALL})