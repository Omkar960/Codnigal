import requests
from Config import HF_API_KEY

Model_ID = "facebook/bart-large-mnli"
API_URL = f'https://router.huggingface.co/hf-inference/models/{Model_ID}'
HEADERS = {"Authorization:"f"Bearers{HF_API_KEY}"}
topics = ["Sports","Technology","Business","Politics","Health"]
def ask_hf(headline:str):
    payload = {"inputs": headline,"parameters":{"candidate_labels": topics}}
    r = requests.post(API_URL, headers=HEADERS,json=payload,timeout=30)
    if not r.ok:
        raise RuntimeError(f"HF error{r.status_code}:{r.text}")
    return r.json()

def best_topic(preds:list):
    best = max(preds, key = lambda x: x['score'])
    return best["label"], best["score"]
def bar(score: float) -> str:
    pct = score * 100
    blocks = int(pct//100)
    return "█" * blocks + "░" * (10 - blocks)
def show(headline: str, preds: list):
    top_label, top_score = best_topic(preds)
    print("\n" + "=" * 60)
    print("??? News Topic Classifiers")
    print("="* 60)
    print("Headline:",headline)
    print(f"Best topic: {top_label}")
    print(f"Confidence: {round(top_score*100,10)}% [{bar(top_score)}]")
    print("\nTop 3 guesses")
    top3 = sorted(preds, key = lambda x: x ["score"],reverse=True)[:3]
    for i, p in enumerate(top3, start=1):
        print(f"{i}. {p['label']:<11} {round(p['score']*100,1)}% [{bar(p['score'])}]")

    print("=" * 60)
def main():
    print("Welcome! Type a news headline and I'll guess the topic.")
    print("Topics",",".join(topics))
    print("Type 'exit' to stop.\n")
    while True:
        headline = input("Headline: ").strip()
        if headline.lower() == "exit":
            print("Bye!")
            break
        if not headline:
            print("Please type a headline.\n")
            continue
        try:
            preds = ask_hf(headline)
            if isinstance(preds,list) and preds and "label" in preds[0]:
                show(headline,preds)
            else:
                print("Oops! Unexpected reply:",preds)
        except Exception as e:
            print("\n⚠️ OOps! Something went wrong")
            print("Reason:", e)
            print("Tip: Check HF_API_KEY + internet.\n")
if __name__ == "__main__":
    main()