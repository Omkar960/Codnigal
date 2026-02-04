import random
import html
import requests

EDUCATION_CATEGORY_ID = 15
api_url = f"https://opentdb.com/api.php?amount=10&category={EDUCATION_CATEGORY_ID}&type=multiple"

def get_question():
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        if data['response_code'] == 0 and data['results']:
            return data["results"]
    return None
def run_quiz():
    questions = get_question()
    if not questions:

        print("Failed to fetch educational questions")
        return
    
    score = 0
    print("Welcome to the Education Quiz")
    if EDUCATION_CATEGORY_ID == 9:
        print("General knowledge edition \n")
    elif EDUCATION_CATEGORY_ID == 10:
        print("Book knowledge edition")
    elif EDUCATION_CATEGORY_ID == 11:
        print("Movie knowledge edition \n")
    elif EDUCATION_CATEGORY_ID == 12:
        print("Music knowledge edition \n")
    elif EDUCATION_CATEGORY_ID == 13:
        print("Theatre knowledge edition \n")
    elif EDUCATION_CATEGORY_ID == 14:
        print("Youtube knowledge edition \n")
    elif EDUCATION_CATEGORY_ID == 15:
        print("Gaming knowledge edition \n")
    elif EDUCATION_CATEGORY_ID == 16:
        print("Card set knowledge edition \n")
    elif EDUCATION_CATEGORY_ID == 17:
        print("Science knowledge edition \n")
    elif EDUCATION_CATEGORY_ID == 18:
        print("Computer knowledge edition \n")
    elif EDUCATION_CATEGORY_ID == 19:
        print("Maths knowledge edition \n")
    elif EDUCATION_CATEGORY_ID == 20:
        print("Mythology knowledge edition \n")
    elif EDUCATION_CATEGORY_ID == 21:
        print("Sports knowledge edition \n")
    elif EDUCATION_CATEGORY_ID == 22:
        print("Geography knowledge edition \n")
    elif EDUCATION_CATEGORY_ID == 23:
        print("History knowledge edition \n")
    elif EDUCATION_CATEGORY_ID == 24:
        print("Politics knowledge edition \n")
    elif EDUCATION_CATEGORY_ID == 25:
        print("Art knowledge edition \n")
    elif EDUCATION_CATEGORY_ID == 26:
        print("TV knowledge edition \n")
    elif EDUCATION_CATEGORY_ID == 27:
        print("Animal knowledge edition \n")
    elif EDUCATION_CATEGORY_ID == 28:
        print("Train knowledge edition \n")
    elif EDUCATION_CATEGORY_ID == 29:
        print("Superhero knowledge edition \n")
    elif EDUCATION_CATEGORY_ID == 30:
        print("Technology knowledge edition \n")
    elif EDUCATION_CATEGORY_ID == 31:
        print("Anime knowledge edition \n")
    else:
        print("Disney knowledge edition \n")
    for i, q in enumerate(questions,1):
            questions = html.unescape(q["question"])
            correct = html.unescape(q["correct_answer"])
            incorrect = [html.unescape(a)for a in q["incorrect_answers"]]

            options = incorrect + [correct]
            random.shuffle(options)

            print(f"Questions {i}: {questions} ")
            for idx, option in enumerate(options,1):
                print(f"{idx}.{option}")
            while True:
                try:
                    choice = int(input("\n Your answer (1-4)"))
                    if 1<= choice <= 4:
                        break
                except ValueError:
                    pass
                print("Invalid input! Please enter 1-4")

            if options[choice-1] == correct:
                print("Correct \n")
                score += 1
            else:

                print(f"Wrong! The correct answer is: {correct}")
    print(f"Final score is: {score} out of {questions}")
    print(f"Percentage is: {score/len(questions)*100:.1f}%")
if __name__ == "__main__":
    run_quiz()
