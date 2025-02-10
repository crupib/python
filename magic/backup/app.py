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

# Set your OpenAI API key
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
        print(deck_text)  # Debug output

        categories = {}
        strategyText = ""
        collectStrategy = False
        current_category = None

        # Process each line from the OpenAI response.
        for line in deck_text.split("\n"):
            original_line = line  # for debugging
            line = line.strip()
            if not line:
                continue

            # Check if this line indicates strategy/notes.
            if re.match(r"^(deck strategy overview|strategy overview|strategy|notes|final)", line, re.I):
                collectStrategy = True
                parts = line.split(":", 1)
                if len(parts) > 1:
                    strategyText += parts[1].strip() + " "
                else:
                    strategyText += line + " "
                current_category = None  # Stop adding cards
                continue
            if collectStrategy:
                strategyText += line + " "
                continue

            # --- Header Detection ---
            # For your prompt, headers are like "Commander:" or "Creatures:".
            header_match = re.match(r"^(.*):\s*$", line)
            if header_match:
                raw_category = header_match.group(1).strip()
                # Remove any trailing count in parentheses so counts aren't duplicated.
                current_category = re.sub(r"\s*\(\d+\)$", "", raw_category)
                if current_category not in categories:
                    categories[current_category] = {}
                print(f"📂 New category detected: {current_category} from line: {repr(original_line)}")
                continue

            # --- Card Processing ---
            # Remove the leading index and dot if present.
            index_match = re.match(r"^\d+\.\s*(.*)$", line)
            if index_match:
                card_line = index_match.group(1)
            else:
                card_line = line

            # Now remove the quantity prefix (allowing an optional "x").
            qty_match = re.match(r"^(\d+)[x]?\s+(.*)$", card_line)
            if qty_match:
                quantity = int(qty_match.group(1))
                card_name = qty_match.group(2).strip()
            else:
                quantity = 1
                card_name = card_line.strip()

            print(f"🃏 Processing card: {card_name} (x{quantity})")
            card_image = download_card_image(card_name)
            if current_category is None:
                print(f"⚠️ Error: No category found for {card_name}, skipping.")
                continue
            # For lands, if already present, add quantity.
            if "land" in current_category.lower() and card_name in categories[current_category]:
                categories[current_category][card_name]["quantity"] += quantity
            else:
                categories[current_category][card_name] = {
                    "name": card_name,
                    "quantity": quantity,
                    "image": card_image
                }

        # Convert each category's cards from dict to list.
        for category, cards in categories.items():
            categories[category] = list(cards.values())

        # Compute overall total card count.
        overall_total = 0
        for cat, cards in categories.items():
            if "land" in cat.lower():
                overall_total += sum(card["quantity"] for card in cards)
            else:
                overall_total += len(cards)
        print(f"🔍 Deck card count before adjustments: {overall_total}")

        # ----- Ensure exactly one commander is present -----
        commander_found = False
        for cat in list(categories.keys()):
            if cat.lower() == "commander":
                commander_found = True
                if len(categories[cat]) != 1:
                    print(f"⚠️ Debug: Commander category has {len(categories[cat])} cards. Expected exactly 1 commander. Trimming to first entry.")
                    categories[cat] = categories[cat][:1]
                break
        if not commander_found:
            print("⚠️ Debug: No commander found in deck!")

        # ----- Adjust deck size to exactly 100 cards -----
        if overall_total > 100:
            excess = overall_total - 100
            print(f"Trimming deck: overall_total={overall_total}, excess={excess}")
            # First, try to trim from non-commander, non-land categories.
            for cat in list(categories.keys()):
                if cat.lower() in ["commander"] or "land" in cat.lower():
                    continue
                new_list = []
                for card in categories[cat]:
                    if excess <= 0:
                        new_list.append(card)
                    else:
                        # Each card in non-land counts as 1.
                        excess -= 1
                        print(f"⚠️ Trimming card: {card['name']}")
                        # Skip this card.
                categories[cat] = new_list
                if excess <= 0:
                    break
            # If excess still remains, trim from lands.
            if excess > 0:
                for cat in list(categories.keys()):
                    if "land" not in cat.lower():
                        continue
                    new_list = []
                    for card in categories[cat]:
                        if excess <= 0:
                            new_list.append(card)
                        else:
                            if card["quantity"] <= excess:
                                excess -= card["quantity"]
                                print(f"⚠️ Trimming entire land card: {card['name']} (x{card['quantity']})")
                                # Skip this card entirely.
                            else:
                                print(f"⚠️ Reducing quantity of land card: {card['name']} from {card['quantity']} by {excess}")
                                card["quantity"] -= excess
                                excess = 0
                                new_list.append(card)
                    categories[cat] = new_list
                    if excess <= 0:
                        break
            overall_total = 100  # Force overall total to 100 after trimming

        # If deck total is less than 100, add generic lands to fill the gap.
        if overall_total < 100:
            missing = 100 - overall_total
            print(f"Deck has less than 100 cards: {overall_total}. Adding {missing} generic land(s).")
            # Look for an existing land category.
            land_category = None
            for cat in categories.keys():
                if "land" in cat.lower():
                    land_category = cat
                    break
            if not land_category:
                land_category = "Lands"
                categories[land_category] = []
            # Try to find an existing generic land (using "Plains" as default).
            land_added = False
            for card in categories[land_category]:
                if card["name"].lower() == "plains":
                    card["quantity"] += missing
                    land_added = True
                    break
            if not land_added:
                categories[land_category].append({
                    "name": "Plains",
                    "quantity": missing,
                    "image": download_card_image("Plains")
                })
            overall_total = 100

        # Final check for overall total.
        final_total = 0
        for cat, cards in categories.items():
            if "land" in cat.lower():
                final_total += sum(card["quantity"] for card in cards)
            else:
                final_total += len(cards)
        if final_total != 100:
            print(f"⚠️ Debug: Final deck total is {final_total} instead of 100.")

        # Build final deck_data.
        deck_data = {"categories": categories, "total": final_total}
        if strategyText:
            deck_data["strategy"] = strategyText.strip()
        deck_data["raw_response"] = deck_text

        print("📄 Final Deck Data:")
        print(json.dumps(deck_data, indent=2))  # Debug output

        with open("static/deck.json", "w") as f:
            json.dump(deck_data, f)

        print("✅ Deck successfully saved!")
        return jsonify({"message": "Deck generated successfully.", "raw_response": deck_text})
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

