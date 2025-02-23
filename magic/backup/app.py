import os
import re
import json
import requests
import openai
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Ensure the directory for card images exists.
STATIC_IMAGE_DIR = "static/cards"
os.makedirs(STATIC_IMAGE_DIR, exist_ok=True)

# Set your OpenAI API key.
openai.api_key = os.getenv("OPENAI_KEY", "your_api_key_here")

def get_card_image_url(card_name):
    """Fetch the card image URL from the Scryfall API."""
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
    # Delete any existing deck.json file.
    deck_json_path = os.path.join("static", "deck.json")
    if os.path.exists(deck_json_path):
        os.remove(deck_json_path)
        print("🗑 Removed existing deck.json file.")

    data = request.json
    prompt = data.get("prompt", "").strip()
    if not prompt:
        print("⚠️ No prompt provided!")
        return jsonify({"error": "No prompt provided"}), 400

    print(f"📢 Generating deck for prompt: {prompt}")
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    deck_text = response["choices"][0]["message"]["content"]
    print("✅ OpenAI response received.")
    print("🔍 OpenAI API Response:")
    print(deck_text)

    # --- Normalize and split raw text into deck lines and notes ---
    raw_lines = deck_text.split("\n")
    deck_lines = []
    notes_lines = []
    for line in raw_lines:
        # Remove any leading bullet markers (e.g., "- ") and ordering numbers (e.g., "60." or "72-76.")
        line = re.sub(r"^-+\s*", "", line)
        line = re.sub(r"^\d+(?:-\d+)?\.\s*", "", line)
        tline = line.strip()
        if not tline:
            continue
        # If the line contains a colon or begins with a number, treat as deck text.
        if re.match(r".*:\s*.*", tline) or re.match(r"^(?:(\d+)[xX]?\s+)?\S+", tline):
            deck_lines.append(tline)
        else:
            notes_lines.append(tline)
    notes_text = " ".join(notes_lines).strip()

    # --- Process deck lines into categories ---
    # For non-land categories we merge duplicates using a dictionary.
    # For any category whose name (case-insensitive) contains "land", we preserve each line (append to a list).
    categories = {}
    current_category = None
    deck_name = ""
    deck_details = ""
    deck_list = ""
    # Use a simple regex now: optional quantity then card name.
    card_line_regex = re.compile(r"^(?:(\d+)[xX]?\s+)?(.+)$")
    for line in deck_lines:
        header_match = re.match(r"^(.*):\s*(.*)$", line)
        if header_match:
            raw_category = header_match.group(1).strip()
            inline_text = header_match.group(2).strip()
            lower_header = raw_category.lower()
            if lower_header == "deck name":
                deck_name = inline_text
                print(f"📝 Found Deck Name: {deck_name}")
                continue
            if lower_header == "deck details":
                deck_details = inline_text
                print(f"📝 Found Deck Details: {deck_details}")
                continue
            if lower_header == "deck list":
                deck_list = inline_text
                print(f"📝 Found Deck List: {deck_list}")
                continue

            current_category = re.sub(r"\s*\(\d+\)$", "", raw_category)
            # For Lands, always use a list; for others, use a dictionary.
            if "land" in current_category.lower():
                if current_category not in categories:
                    categories[current_category] = []
            else:
                if current_category not in categories:
                    categories[current_category] = {}
            print(f"📂 New category detected: {current_category} from line: {repr(line)}")
            if inline_text:
                match = card_line_regex.match(inline_text)
                if match:
                    quantity = int(match.group(1)) if match.group(1) is not None else 1
                    card_name = match.group(2).strip()
                else:
                    quantity = 1
                    card_name = inline_text
                print(f"🃏 Processing inline card: {card_name} (x{quantity})")
                card_image = download_card_image(card_name)
                if "land" in current_category.lower():
                    categories[current_category].append({
                        "name": card_name,
                        "quantity": quantity,
                        "image": card_image
                    })
                else:
                    card_key = card_name.lower()
                    categories[current_category][card_key] = {
                        "name": card_name,
                        "quantity": quantity,
                        "image": card_image
                    }
            continue

        # Process as a card line.
        match = card_line_regex.match(line)
        if match:
            quantity = int(match.group(1)) if match.group(1) is not None else 1
            card_name = match.group(2).strip()
        else:
            notes_text += " " + line
            continue

        # Remove any accidental leading "x".
        card_name = re.sub(r"^[xX]\s*", "", card_name).strip()

        # Auto-assign "Commander" if no category is set and card name contains "(commander)".
        if current_category is None and "(commander)" in card_name.lower():
            current_category = "Commander"
            card_name = re.sub(r"\s*\(commander\)$", "", card_name, flags=re.IGNORECASE)
            if current_category not in categories:
                categories[current_category] = {}

        print(f"🃏 Processing card: {card_name} (x{quantity})")
        card_image = download_card_image(card_name)
        if current_category is None:
            print(f"⚠️ Error: No category found for {card_name}, skipping.")
            continue
        if "land" in current_category.lower():
            categories[current_category].append({
                "name": card_name,
                "quantity": quantity,
                "image": card_image
            })
        else:
            card_key = card_name.lower()
            if card_key in categories[current_category]:
                categories[current_category][card_key]["quantity"] += quantity
            else:
                categories[current_category][card_key] = {
                    "name": card_name,
                    "quantity": quantity,
                    "image": card_image
                }

    # For non-land categories, convert dictionaries to lists.
    for category, cards in categories.items():
        if category.lower().find("land") == -1:
            categories[category] = list(cards.values())

    # Compute overall total card count.
    overall_total = 0
    for cat, cards in categories.items():
        if cat.lower().find("land") != -1:
            overall_total += sum(card["quantity"] for card in cards)
        else:
            overall_total += len(cards)
    print(f"🔍 Deck card count before adjustments: {overall_total}")

    # Ensure a Commander is present.
    if not any(cat.lower() == "commander" for cat in categories):
        print("⚠️ Debug: No commander found in deck!")
        overall_total = 0

    # Adjust non-land categories only if overall total > 100.
    if overall_total > 100:
        excess = overall_total - 100
        print(f"Trimming deck (non-lands only): overall_total={overall_total}, excess={excess}")
        for cat in list(categories.keys()):
            if cat.lower().find("land") != -1 or cat.lower() == "commander":
                continue
            new_list = []
            for card in categories[cat]:
                if excess <= 0:
                    new_list.append(card)
                else:
                    excess -= 1
                    print(f"⚠️ Trimming card: {card['name']}")
            categories[cat] = new_list
            if excess <= 0:
                break
        overall_total = 100
    elif overall_total < 100:
        missing = 100 - overall_total
        print(f"Deck has less than 100 cards: {overall_total}. Adding {missing} filler land(s).")
        # Only add filler if no Lands category exists.
        lands_cat_key = None
        for cat in categories:
            if cat.lower().find("land") != -1:
                lands_cat_key = cat
                break
        if lands_cat_key is None:
            preferred_basic = "Plains"
            filler_land_image = download_card_image(preferred_basic)
            categories["Lands"] = [{
                "name": preferred_basic,
                "quantity": missing,
                "image": filler_land_image
            }]
            overall_total = 100
        else:
            print("Lands category exists; preserving exactly what the prompt returned.")
            overall_total = 100

    print(f"🔍 Final deck total is {overall_total}")

    deck_data = {"categories": categories, "total": overall_total}
    if deck_name:
        deck_data["deck_name"] = deck_name
    if deck_details:
        deck_data["deck_details"] = deck_details
    if deck_list:
        deck_data["deck_list"] = deck_list
    if notes_text:
        deck_data["notes"] = notes_text
    deck_data["raw_response"] = deck_text

    print("📄 Final Deck Data:")
    print(json.dumps(deck_data, indent=2))
    with open("static/deck.json", "w") as f:
        json.dump(deck_data, f)
    print("✅ Deck successfully saved!")
    return jsonify({"message": "Deck generated successfully.", "raw_response": deck_text})

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

