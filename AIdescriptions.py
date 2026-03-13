import base64
import requests
import os
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont
from config import HF_API_KEY
API_URL = "https://router.huggingface.co/v1/chat/completions"
HEADERS = {
    "Authorization": f"Bearer {HF_API_KEY}",
    "Content-Type": "application/json"
}
MODELS = [
    "Qwen/Qwen3-VL-8B-Instruct:together",
    "Qwen/Qwen3-VL-32B-Instruct:together",
    "Qwen/Qwen2.5-VL-32B-Instruct:together",
    "Qwen/Qwen2-VL-7B-Instruct:together",
]
def data_url(b: bytes) -> str:
    return "data:image/jpeg;base64," + base64.b64encode(b).decode("utf-8")
def extract_err(r: requests.Response) -> str:
    try:
        j = r.json()
        return j.get("error", {}).get("message", "Unknown API error")
    except Exception:
        return (r.text or "").strip() or r.reason or "Request failed"
def box(title: str, lines: list[str], icon: str):
    w = max(30, len(title) + 4, *[len(x) for x in lines])
    print("\n" + "┏" + "━" * (w + 2) + "┓")
    print(f"┃ {icon} {title.ljust(w - 2)} ┃")
    print("┣" + "━" * (w + 2) + "┫")
    for x in lines:
        print(f"┃ {x.ljust(w)} ┃")
    print("┗" + "━" * (w + 2) + "┛\n")
def add_caption_to_image(image_path, caption):
    img = Image.open(image_path)
    draw = ImageDraw.Draw(img)
    try:
        font = ImageFont.truetype("arial.ttf", 24)
    except:
        font = ImageFont.load_default()
    width, height = img.size
    text_bbox = draw.textbbox((0, 0), caption, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]
    x = (width - text_width) / 2
    y = height - text_height - 20
    draw.text((x, y), caption, font=font, fill="white")
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"captioned_{timestamp}.png"
    img.save(filename)
    print(f"✅ Saved: {filename}")
    try:
        img.show()
    except:
        print("⚠️ Could not open image viewer.")
def caption_single_image():
    image_source = input("🖼️ Enter image filename (default: test.jpg): ").strip() or "test.jpg"
    try:
        with open(image_source, "rb") as f:
            img_bytes = f.read()
    except Exception as e:
        box("File Error", [
            f"Couldn't load: {image_source}",
            f"Reason: {e}"
        ], "❌")
        return
    base = {
        "messages": [{
            "role": "user",
            "content": [
                {"type": "text", "text": "Give a short caption for this image."},
                {"type": "image_url", "image_url": {"url": data_url(img_bytes)}}
            ]
        }]
    }
    last = None
    for model in MODELS:
        payload = dict(base, model=model)
        try:
            r = requests.post(API_URL, headers=HEADERS, json=payload, timeout=120)
        except requests.RequestException as e:
            last = f"Request failed: {e}"
            continue
        if r.status_code != 200:
            last = extract_err(r)
            continue
        try:
            d = r.json()
        except Exception:
            last = "Non-JSON response received from the API"
            continue
        cap = (
            d.get("choices", [{}])[0]
            .get("message", {})
            .get("content", "")
            .strip()
        )
        if cap:
            box("Image Caption Generated", [
                f"🖼️ Image: {image_source}",
                "📝 Caption:",
                cap
            ], "🎉")
            add_caption_to_image(image_source, cap)
            return
        last = "No caption found."
    box("Caption Failed", [
        f"🖼️ Image: {image_source}",
        f"❌ Error: {last or 'Unknown error'}"
    ], "⚠️")
def main():
    caption_single_image()
if __name__ == "__main__":
    main()          