import requests 

url =  "https://uselessfacts.jsph.pl/random.json?language=en"
url2 = "https://uselessfacts.jsph.pl/today.json?language=en"
def get_random_technology_fact():
    response = requests.get(url)
    if response.status_code == 200:
        fact_data = response.json()
        print(f"Did you know {fact_data['text']}")
    else:
        print("Failed to fetch fact")
def get_today_fact():
    response = requests.get(url2)
    if response.status_code == 200:
        facttoday_data = response.json()
        print(f"Today's facts is {facttoday_data['text']}")
while True:
    user_input = input("Press Enter to get random facts or press 'q' to quit or type 'today's fact':" )
    if user_input.lower()== "q":
        break
    elif user_input.lower() == "today's fact" or user_input.lower() == "todays fact":
        get_today_fact()
    get_random_technology_fact()


