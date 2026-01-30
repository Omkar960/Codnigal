import requests
def get_random_jokes():
    url = "https://official-joke-api.appspot.com/random_joke"
    response = requests.get(url)
    if response.status_code == 200:
        print(f"Full JSON Response: {response.json()}")

        joke_data = response.json()
        return f"{joke_data['setup']} - {joke_data['punchline']}"
    else:
        return "Failed to return the joke"
def main():
    print("Welcome to the Random Joke Generatore")
    while True:
        user_input = input("Press Enter to get a new joke, or type 'q' to exit: ").strip().lower()
        if user_input in ("q","exit"):
            print("Goodbye")
            break
        joke = get_random_jokes()
        print(joke)
if __name__ == "__main__":
    main()