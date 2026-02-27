from huggingface_hub import InferenceClient
from datetime import datetime
from PIL import Image
from Config import HF_API_KEY

MODELS = [
    "ByteDance/SDXL-Lightning",
    "stabilityai/stable-diffusion-xl-base-1.0",
    "stabilityai/sdxl-turbo",
    "runwayml/stable-diffusion-v1.5"
]

cilent = InferenceClient(api_key=HF_API_KEY)
def generate_image_from_text():
    payload = {

    "inputs": prompt,

    "options": {"negative_prompt": "ugly, blurry", "guidance_scale": 7.5}

}
    last_err = None

print(f"Primary model: {MODELS[0]}")
print("Type 'quit' to exit\n")
while True:
    prompt = input("Enter prompt: ")
    if prompt.lower() in ["quit","exit","q"]:
        print("Bye")
        break
    if not prompt:
        continue
    user_input = input("Guidance Scale: enter 3-15: ")
    try:
        if not user_input.strip():
            scale = 7.5
        else:
            scale = float(user_input)
    except ValueError:
        print("That wasn't a number! Using default 7.5")
        scale = 7.5
    print("Generating...")
    image = None
    for model in MODELS:
        try:
            image = cilent.text_to_image(prompt,model=model,
            guidance_scale=scale,
            negative_prompt="ugly, blurry, distorted, grainy"
            )
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

