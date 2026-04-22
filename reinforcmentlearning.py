from groq import generate_response
def reinforcemntlearnignactivity():
    print("\n==== REINFORCEMENT LEARNING ACTIVITY====")
    prompt = input("Enter a prompt for the AI mdoel (e.g 'Describe the lion')").strip()
    if not prompt:
        print("Please enter a prompt to run the acitivty.")
        return
    initialresponse = generate_response(prompt,temperature=0.3,max_tokens=1024)
    print(f"\n Initial AI Response: {initialresponse}")
    try:
        rating = int(input("Rate the response 1 (bad) to 5 (good):" ).strip())
        if rating < 1 or rating > 5:
            print("Invalid rating. Using 3")
            rating = 3
    except ValueError:
        rating = 3
    feedback = input("Provide feedback for improvement: ").strip()
    improvedresponse = f"{initialresponse} (Imporved wiht your feedback: {feedback})"
    print(f"\n Improved AI Response: {improvedresponse}")
    print("\n Reflection")
    print("1. How did the model's response improve with feedback")
    print("2. How does the reinforcement learning help AI to improve its performance over time?")
def rolebasedactivity():
    print("\n==== ROLSE-BASED PROMPTS ACTIVITY ====\n")
    category = input("Enter a category: ")
    item = input(f"Enter a specific {category} topic: ")
    if not category or not item:
        print("Please fill in both filed to run the activity.")
        return
    teacherprompt = f"You are a teacher. Explain {item} in simple terms"
    expertprompt = f"You are an expert in {category}. Explain {item} in a detailed technical manner."
    businessprompt = f"As a business leader, explain how {item} can impact your industry"
    peerprompt = f"Explain {item} in terms a college student would underrstand."
    teacherresponse = generate_response(teacherprompt,temperature=0.3,max_tokens=1024)
    expertresponse = generate_response(expertprompt,temperature=0.3,max_tokens=1024)
    businessresponse = generate_response(businessprompt,temperature=0.3,max_tokens=1024)
    peerresponse = generate_response(peerprompt,temperature=0.3,max_tokens=1024)
    print(f"\n----- Teacher's Perspective ----\n{teacherresponse}")
    print(f"\n---- Expert's Perspective ----\n{expertresponse}")
    print(f"\n---- Business Leader's Persepctive ----\n{businessresponse}")
    print(f"\n---- Peer Stduent's Perspective ----\n{peerresponse}")
    print("\n Reflection ")
    print("1. How did the AI's response differ between the teacher's and expert's perspectives?")
    print("2. How can role-based prompts help tailor AI responses for different contexts?")
def runactivity():
    print("\n=== AI Learning Activity ===")
    print("Choose an activity:")
    print("1) Reinforcement Learning")
    print("2) Role-Based Prompts")
    choice = input("> ").strip()
    if choice == "1":
        reinforcemntlearnignactivity()
    elif choice == "2":
        rolebasedactivity()
    else:
        print("Inavlid choice. Please choice 1 or 2.")
if __name__ == "__main__":
    runactivity()