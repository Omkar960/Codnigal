import requests
def get_trivia():
    url = "https://the-trivia-api.com/v2/questions"
    response = requests.get(url)
    if response.status_code == 200:
        trivia_json = response.json()
        if isinstance(trivia_json, list) and len(trivia_json) > 0:
            item = trivia_json[0]
        elif isinstance(trivia_json, dict):
            item = trivia_json
        else:
            return "Unexpected API response format"
        question = None
        answer = None
        q_field = item.get('question')
        if isinstance(q_field, dict):
            question = q_field.get('text')
        else:
            question = q_field
        answer = item.get('correctAnswer') or item.get('answer') or item.get('correct_answer')
        return f"{question} - {answer}"
    else:
        return "Failed to fetch trivia"  
def main():
    print("Welcome to Trivia")
    while True:
        userinput = input("Press enter to get new piece of trivia or 'q' to quit: ").strip().lower()
        if userinput in ("exit", "quit", "q"):
            print("Goodbye")
            break
        else:
            trivia =  get_trivia()
            print(trivia)
if __name__ == "__main__":
    main()