from huggingface_hub import InferenceClient
from datetime import datetime
from PIL import Image
from Config import HF_API_KEY

MODELS = [
    "ByteDance/SDXL-Lightning",
    "stabilityai/stable-diffusion-x1-base-1.0",
    "stabilityai/sdxl-turbo",
    "runawayml/stable-diffusion-v1.5"
]

cilent = InferenceClient(api_key=HF_API_KEY)

print(f"Primary model: {MODELS[:0]}")
print("Type 'quit' to exit\n")
while True:
    prompt = input("Enter prompt").strip()
    if prompt.lower in ["quit","exit","q"]:
        print("Bye")
        break
    if not prompt:
        continue

    print("Generating...")
    image = None

    for model in MODELS:
        try:
            image = cilent.text_to_image(prompt,model=model)
            break
        except Exception:
            print(f"Executing next...")
            continue
    if image:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"generated_{timestamp}.png"
        image.save(filename)
        print(f"✅ Saved: {filename}")
        image.show()
        print()
    else:
        print("Error: All models failed. Check your API ket.\n")
print("Goodbye!")