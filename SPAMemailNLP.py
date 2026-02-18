from transformers import pipeline
import torch
classifier = pipeline(
    "zero-shot-classification",
    model="facebook/bart-large-mnli"
)
LABELS = ["Spam", "Safe"]
def classify_message(message):
    result = classifier(message, LABELS)
    results = list(zip(result["labels"], result["scores"]))
    return sorted(results, key=lambda x: x[1], reverse=True)
def show_results(message, results):
    label, score = results[0]
    print("\n" + "=" * 60)
    print("Spam VS Safe Classifier")
    print("=" * 60)
    print(f"Message: {message}\n")
    print("Confidence scores:")
    for i, (lbl, scr) in enumerate(results, 1):
        print(f"{i}. {lbl}: {scr * 100:.1f}%")
    if label == "Spam":
        print("\n⚠️ Don't click suspicious links or share personal info!")
    else:
        print("\n✅ Looks safe, but always stay alert!")
    print("=" * 60)
def main():
    print("Spam VS Safe Message Classifier")
    print("Type 'exit' to quit\n")
    while True:
        msg = input("Enter message: ").strip()
        if msg.lower() == "exit":
            print("Goodbye!")
            break
        if not msg:
            print("Please enter a message.\n")
            continue

        results = classify_message(msg)
        show_results(msg, results)
if __name__ == "__main__":
    main()

