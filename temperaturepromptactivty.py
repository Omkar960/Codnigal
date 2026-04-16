from hf import generateresponse
import time
def temperatureprompotactivty():
    print("="*70)
    print("ADVANCED PROMPT ENGINEERING: TEMPERATURE + INSTRUCTIONS")
    print("="*70)
    print("\n PART 1: TEMPERATURE EXPLORATION")
    base = input("Enter a creative prompt: ").strip()
    for t,label in [(0.1,"LOW (0.1) - Deterministic"),(0.5,"MEDIUM (0.5) - Balanced"),(0.9,"HIGH (0.9) - Creative")]:
        print(f"\n----- {label} -----")
        print(generateresponse(base,temperature=t,max_tokens=512))
        time.sleep(1)
    print("\n PART 2: INSTRUCTION-BASED PROMPTS")
    topic  = input("Choose a topic (e.g,climate change, space exploration): ").strip()
    prompts = [ f"Summarize key facts about {topic} in 3-4 sentences",f"Explain {topic} as if I'm a 10-year old child",f"Create a fictional news headline from 2050 {topic}"]
    for i,p in enumerate(prompts,1):
        print(f"\n---- INSTRUCTION {i} ---\n{p}")
        print(generateresponse(p,temperature=0.7,max_tokens=512))
        time.sleep(1)
    print("\n PART 3: YOUR OWN INSTRUCTION PROMPT:")
    custom = input("Enter your instruction-based prompt: ").strip()
    try:
        temp = float(input("Set temperature (0.1 to 1.0)").strip())
        if not (0.1 <= temp <= 1.0): raise ValueError
    except ValueError:
        print("Invalid temperature. Using 0.7")
        temp =0.7
    print(f"\n ---- YOUR PROMPT @ TEMP {temp} ---- ")
    print(generateresponse(custom,temperature=temp,max_tokens=512))
    print("\n REFLECTION:")
    print("1) What changed when your prompts became more specific? ")
    print("2) What imporved when context was added?")
    print("3) Which prompt felt most useful and why? ")
    print("\n CHALLENGE: create a prompt chain:")
    print("Generate content -> rewrite wiht constraints -> create a sequel (try different temps).")
def pseudostream(text,delay=0.013):
    for ch in text:
        print(ch,end="",flush=True)
        time.sleep(delay)
    print()
def bonusstream():
    choice = input("\n BONUS: streaming-like output?(y/n)").lower().strip()
    if choice == "y":
        p = input("Enter a prompt: ").strip()
        out = generateresponse(p,temperature=0.5,max_tokens=512)
        print("\n Streaming-like response (not real streaming)")
        pseudostream(out)
if __name__ == "__main__":
    temperatureprompotactivty()
    bonusstream()