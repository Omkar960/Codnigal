import requests
import urllib3
import random
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
url1 = "https://uselessfacts.jsph.pl/random.json?language=en"
url2 = "https://opentdb.com/api.php?amount=1&category=18&type=boolean"
url3 = "https://history.muffinlabs.com/date"
url4 = "https://opentdb.com/api.php?amount=1&category=17&type=boolean"
def general_facts():
    response = requests.get(url1,verify=False)
    if response.status_code == 200:
        generalfact = response.json()
        print(f"Did you know: {generalfact['text']}")
    else:
        print('Failed to fetch fact')
def technology_facts():
    response = requests.get(url2,verify=False)
    if response.status_code == 200:
        technology_fact = response.json()
        fact = technology_fact['results'][0]['question']
        fact = fact.replace('&quot;','"').replace("&039",'"')
        print(f"Did you know: {fact}")
    else:
        print("Failed to fetch fact")
def history_facts():
    response = requests.get(url3,verify=False)
    if response.status_code == 200:
        data = response.json()
        events = data['data']['Events']
        random_event = random.choice(events)
        print(f"Did you know in {random_event['year']}: {random_event['text']}")
    
    else:
        print("Failed to fetch fact")
def science_facts():

    response = requests.get(url4, verify=False, timeout=5)
    if response.status_code == 200:
        data = response.json()
            
        raw_fact = data['results'][0]['question']
            
        import html
        clean_fact = html.unescape(raw_fact)
            
        print(f" Science: {clean_fact}")
    else:
        print("Failed to fetch fact (Server error)")
    #For some reason it sometimes says fail to fetch and on other occasions it displays a fact.

while True:
    user_input = input("For General Fact: type 'g'. For Technology fact: type 't'. For History Fact: type 'h'. For Science Fact: type 's'. To quit: type q: ")
    if user_input.lower() == "g" or user_input.lower()== "general knowledge":
        general_facts()
    elif user_input.lower() == "t" or user_input.lower()== "technology":
        technology_facts()
    elif user_input.lower() == "h" or user_input.lower()== "history":
        history_facts()
    elif user_input.lower() == "s" or user_input.lower()== "science":
        science_facts()
    elif user_input.lower()  == "q":
        break
        
