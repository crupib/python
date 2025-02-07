import os
import re
import json
import requests
import openai
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Ensure static/cards directory exists
STATIC_IMAGE_DIR = "static/cards"
os.makedirs(STATIC_IMAGE_DIR, exist_ok=True)

# Set OpenAI API key
openai.api_key = os.getenv("OPENAI_KEY", "your_api_key_here")

def get_card_image_url(card_name):
    """Fetch the card image URL from Scryfall API."""
    print(f"🔍 Fetching image URL for card: {card_name}...")

    url = f"https://api.scryfall.com/cards/named?fuzzy={card_name}"
    response = requests.get(url)

    if response.status_code != 200:
        print(f"⚠️ Error: Card '{card_name}' not found.")
        return None

    card_data = response.json()

    if "image_uris" in card_data:
        return card_data["image_uris"].get("normal")
    elif "card_faces" in card_data:
        return card_data["card_faces"][0]["image_uris"].get("normal")

    print(f"⚠️ No image found for {card_name}.")
    return None

def download_card_image(card_name):
    """Download and save the card image locally."""
    sanitized_name = re.sub(r'\W+', '_', card_name)
    local_image_path = os.path.join(STATIC_IMAGE_DIR, f"{sanitized_name}.jpg")

    if os.path.exists(local_image_path):
        print(f"✅ Image already exists for {card_name}, skipping download.")
        return f"/{local_image_path}"

    image_url = get_card_image_url(card_name)
    if not image_url:
        return None

    try:
        print(f"⬇️ Downloading image for {card_name}...")
        img_data = requests.get(image_url).content
        with open(local_image_path, 'wb') as img_file:
            img_file.write(img_data)
        print(f"✅ Image saved: {local_image_path}")
        return f"/{local_image_path}"
    except Exception as e:
        print(f"⚠️ Failed to download {card_name}: {e}")
        return None

@app.route("/")
def index():
    print("📢 Serving index.html...")
    return render_template("index.html")

@app.route("/generate_deck", methods=["POST"])
def generate_deck():
    data = request.json
    prompt = data.get("prompt", "").strip()
    if not prompt:
        print("⚠️ No prompt provided!")
        return jsonify({"error": "No prompt provided"}), 400

    try:
        print(f"📢 Generating deck for prompt: {prompt}")
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}]
        )
        deck_text = response["choices"][0]["message"]["content"]
        print("✅ OpenAI response received.")

        print("🔍 OpenAI API Response:")
        print(deck_text)  # Debugging

        categories = {}
        current_category = None

        for line in deck_text.split("\n"):
            line = line.strip()
            if not line:
                continue
            
            # Identify category headers, ensuring they are properly stored
            if line.endswith(":") or line.startswith("■"):
                current_category = line.replace(":", "").strip()  # Remove ":" if found
                if current_category not in categories:
                    categories[current_category] = {}
                print(f"📂 New category: {current_category}")
                continue
            
            print(f"🔍 Processing Line: {line}")  # Debugging

            # Match "1x Card Name" or "1. Card Name" formats
            match = re.match(r"(\d+)[x.]?\s+(.+)", line)  
            if match:
                quantity, card_name = int(match[1]), match[2]
                print(f"🃏 Processing card: {card_name} (x{quantity})")

                card_image = download_card_image(card_name)
                
                if current_category is None:
                    print(f"⚠️ Error: No category found for {card_name}, skipping.")
                    continue
                
                # Group lands with multiple copies
                if current_category == "Lands" and card_name in categories[current_category]:
                    categories[current_category][card_name]["quantity"] += quantity
                else:
                    categories[current_category][card_name] = {
                        "name": card_name,
                        "quantity": quantity,
                        "image": card_image
                    }
            else:
                print(f"⚠️ Skipping unrecognized line: {line}")

        # Convert categories to expected list format
        for category, cards in categories.items():
            categories[category] = list(cards.values())

        deck_data = {"categories": categories}
        print("📄 Final Deck Data:")
        print(json.dumps(deck_data, indent=2))  # Debugging

        with open("static/deck.json", "w") as f:
            json.dump(deck_data, f)

        print("✅ Deck successfully saved!")
        return jsonify({"message": "Deck generated successfully."})

    except Exception as e:
        print(f"⚠️ Error during deck generation: {e}")
        return jsonify({"error": f"Failed to generate deck: {e}"}), 500

@app.route("/deck.json")
def get_deck():
    try:
        print("📢 Serving deck.json...")
        with open("static/deck.json", "r") as f:
            return f.read(), 200, {'Content-Type': 'application/json'}
    except FileNotFoundError:
        print("⚠️ Error: Deck file not found.")
        return jsonify({"error": "Deck not found"}), 404

if __name__ == "__main__":
    print("🚀 Starting Flask Server on http://localhost:8000 🚀")
    app.run(host="0.0.0.0", port=8000, debug=True)

