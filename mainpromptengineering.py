from groq import generate_response
def prompt_engineering_activity():
    print("Welcome to the AI Prompt Engineering Tutorial!")
    vagueprompt = input("Enter a vague prompt: ")
    print("\n AI's response to vague prompt")
    print(generate_response(vagueprompt))
    specificprompt = input("\n Now, make it more specific: ")
    print("\n AI's response to specific prompt: ")
    print(generate_response(specificprompt))
    contextualprompt = input("\n NOw, add context to your specific pormpt: ")
    print("\n AI's response to contextual prompt:")
    print(generate_response(contextualprompt))
    print("\n--- Reflection ---")
    print("1. How did the AI's response change when the prompt was made more specific")
    print("2. How did the AI's response improve with the added context?")
    print("3. Which prompt produced the relevant and tailored response? Why?")
if __name__ == "__main__":
    prompt_engineering_activity()