import requests
import urllib3
import random
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
url1 = "https://uselessfacts.jsph.pl/random.json?language=en"
url2 = "https://opentdb.com/api.php?amount=1&category=18&type=boolean"
url3 = "https://history.muffinlabs.com/date"
url4 = "https://opentdb.com/api.php?amount=1&category=17&type=boolean"
url5 = "https://balldontlie.io/api/v1/players?search=lebron"
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
import requests

import requests

import requests
import random

def sports_facts():
    random_id = random.randint(1, 2000)
    url = f"https://api.balldontlie.io/v1/players/{random_id}"
    headers = {
        "Authorization": "7e03d30a-34b1-41e5-b88d-82623a35e4c7"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        dat = response.json()
        player = dat['data']
        name = f"{player['first_name']} {player['last_name']}"
        team = player['team']['full_name']
        pos = player['position'] if player['position'] else "N/A"
        print(f"ID:       {random_id}")
        print(f"Name:     {name}")
        print(f"Team:     {team}")
        print(f"Position: {pos}")
    elif response.status_code == 404:
        print(f"ID {random_id} (No player found). Try again!")
    else:
        print(f"Failed. Status: {response.status_code}")
while True:
    user_input = input("For General Fact: type 'g'. For Technology fact: type 't'. For History Fact: type 'h'. For Science Fact: type 's'.For Sport Fact: type 'sp' To quit: type q: ")
    if user_input.lower() == "g" or user_input.lower()== "general knowledge":
        general_facts()
    elif user_input.lower() == "t" or user_input.lower()== "technology":
        technology_facts()
    elif user_input.lower() == "h" or user_input.lower()== "history":
        history_facts()
    elif user_input.lower() == "s" or user_input.lower()== "science":
        science_facts()
    elif user_input.lower() == "sp" or user_input.lower()== "sport":
        sports_facts()
    elif user_input.lower()  == "q":
        break
        
