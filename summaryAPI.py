import requests
from Config import HF_API_KEY
from colorama import Fore, Style, init

init(autoreset=True)

DEFAULT_MODEL = "google/pegasus-xsum"

def build_api_url(model_name):

    return f"https://router.huggingface.co/hf-inference/models/{model_name}"


def query(payload, model_name=DEFAULT_MODEL):
    api_url = build_api_url(model_name)
    headers = {
    "Authorization": f"Bearer {HF_API_KEY}",
    "Content-Type": "application/json"
    }
    try:
        response = requests.post(api_url,headers=headers,json=payload,timeout=30)
        print("Status Code:", response.status_code)
        if response.status_code != 200:
            print("Error Response:", response.text)
            return None
        return response.json()
    except Exception as e:
        print("Request Failed:", e)
        return None

def summarize_text(text,min_length,max_length,model_name=DEFAULT_MODEL):

    payload = { "inputs":text, 
               "parameters": {"min_length":min_length, "max_length": max_length }}
    
    print(Fore.BLUE + Style.BRIGHT + f"\m???? Performing AI summarization using model: {model_name}")

    result = query(payload,model_name=model_name)
    if isinstance(result,list) and result and "summary_text" in result[0]:
        return result[0]['summary_text']
    else:
        print(Fore.RED +" ❌ Error in summarization response:", result)
        return None
if __name__ == "__main__":
    print(Fore.YELLOW + Style.BRIGHT +'What your name:')
    username = input("Your name: ").strip()
    if not username:
        username = "User"
    print(Fore.GREEN + f" Welcome, {username}! Let's give your text some AI magic. ")

    print(Fore.YELLOW + Style.BRIGHT + "\n Please enter the text you want to summarize. ")
    usertext= input( "> ").strip()
    if not usertext:
        print(Fore.RED + " ❌ No text provided. Exiting")
    else:
        print(Fore.YELLOW + "\n Enter the model name you want to use (e.g, facebook/bart-large.cnn)")
        modelchoice = input('Enter the model name: ')
        if not modelchoice:
            modelchoice = DEFAULT_MODEL
        
        print(Fore.YELLOW + " \n Choose your summarization style:" )
        print("1. Standard Summary (Quick and Concise)")
        print("2. Enhanced Summary (More detailed and refined)")
        style_choice = input("Enter 1. or 2. ").strip()
        if style_choice == "2":
            min_length = 80
            max_length = 200
        else:
            min_length = 50
            max_length = 150
            print(Fore.BLUE + "Using standard summarization settings...")
            
        summary = summarize_text(usertext,min_length,max_length,model_name=modelchoice)
        if summary:
            print(Fore.GREEN + Style.BRIGHT + f"\n AI Summarizer Output for {username} ")
            print(Fore.GREEN + summary)
        else:
            print(Fore.RED + " ❌ Failed to generate summary.")




