import colorama
from colorama import Fore, Style
from textblob import TextBlob
colorama.init()

print(Fore.CYAN,"👋 🎉 Welcome to sentiment spy!")
username = input(f"{Fore.MAGENTA}Please enter your name:" )

if not username:
    username = "Mystery Agent"
conversationhistroy = []

print(Fore.CYAN,"Hello",username)
print("Type a sentence and I will rate it based on it's postivity and polarity")
print(f"Type {Fore.YELLOW}'reset',{Fore.CYAN},{Fore.YELLOW}'history',{Fore.CYAN}",f"{Fore.YELLOW}'exit'{Fore.CYAN},to quit.{Style.RESET_ALL}\n")

while True:
    userinput = input(f"{Fore.GREEN}>> {Style.RESET_ALL}").strip()

    if not userinput:
        print(f"{Fore.RED} Please enter some text{Style.RESET_ALL}")
        continue

    elif userinput.lower() == "exit":
        print(f"\n{Fore.BLUE} Exiting Sentiment Spy. Farewell {username}! 🏁 {Style.RESET_ALL}")
        break
    elif userinput.lower() == "reset":
        conversationhistroy.clear()
        print(f"{Fore.CYAN} All conversation history cleared! {Style.RESET_ALL}")
        continue
    elif userinput.lower() == "history":
        if not conversationhistroy:
            print(f"{Fore.YELLOW} No conversation history {Style.RESET_ALL}")
        else:
            print(f"{Fore.CYAN} Conversation History {Style.RESET_ALL}")
            for idx, (text,polarity,sentiment_type,) in enumerate(conversationhistroy, start = 1):
                if sentiment_type == "Positive":
                    color = Fore.GREEN
                    emoji = "😊"
                elif sentiment_type == "Negative":
                    color = Fore.RED
                    emoji = "😥"
                else:
                    color = Fore.YELLOW
                    emoji = "😑"
                print(f"{idx}. {color}{emoji} {text} (Polarity: {polarity:.2f}, {sentiment_type}){Style.RESET_ALL}")


        continue

    polarity = TextBlob(userinput).sentiment.polarity
    if polarity > 0.25:
        sentiment_type = "Positive"
        color = Fore.GREEN
        emoji = "😊"
    elif polarity < -0.25:
        sentiment_type = "Negative"
        color = Fore.RED
        emoji = "😥" 
    else: 
        sentiment_type = "Neutral"
        color = Fore.YELLOW
        emoji = "😑"
    conversationhistroy.append((userinput,polarity,sentiment_type))
    print(f"{color}{emoji} {userinput} (Polarity: {polarity:.2f}, {sentiment_type}){Style.RESET_ALL}")

   
   