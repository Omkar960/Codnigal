from groq import generate_response
def bias():
    print("\n=== BIAS MITIGATION ACTIVITY === ")
    prompt = input("Enter a prompt to explore bias (e.g 'Describe the ideal doctor')").strip()
    if not prompt:
        print("Please enter a pormpt to run the activity.")
        return
    initalresponse = generate_response(prompt,temperature=0.3,max_tokens=1024)
    print(f"Initial AI Response: {initalresponse}")
    modifedpormpt = input("Modify the prompt to make it more neutral (e.g 'Describe the qualities of a doctor')").strip()
    if modifedpormpt:
        modifedresponse = generate_response(modifedpormpt,temperature=0.3,max_tokens=1024)
        print(f"\n Modied AI Response (Neutral): {modifedresponse}")
    else:
        print("No modified prompt entered. Skipping neutral response.")
def tokenlimit():
    print("\n === TOKEN LIMIT ACITVITY ===")
    longprompt = input("Enter a long prompt e.g a story or description").strip()
    if longprompt:
        longresponse = generate_response(longprompt,temperature=0.3,max_tokens=1024)
        priview = (longresponse[:500] + " ... ")if len(longresponse) > 500 else longresponse
        print(f"\n Response to Long Prompt: {priview}")
    else:
        print("No long prompt entered. Skipping long prompt response.")
    shortprompt = input("Now, condenser the prompt to eb more concise: ").strip()
    if shortprompt:
        shortresponse = generate_response(shortprompt,temperature=0.3,max_tokens=1024)
        print(f"Welcom to Codensed Prompt: {shortresponse}")
    else:
        print("No condensed prompt enetred. Skipping condensed prompt response.")
def runactivty():
    print("\n=== AI Learning Activity ===")
    print("Choose an actvity")
    print("1) Bias Mitigation")
    print("2) Token Limits")
    choice = input("> ").strip()
    if choice == "1":
        bias()
    elif choice == "2":
        tokenlimit()
    else:
        print("Invalid choice. Please choose 1 or 2")
if __name__ == "__main__":
    runactivty()

