import requests
import json
import os
import re
import openai

# Set your OpenAI API Key here
SCRYFALL_API_URL = "https://api.scryfall.com/cards/named"

def ask_openai(prompt):
    """Ask OpenAI to generate a full Commander decklist."""
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response["choices"][0]["message"]["content"]

def fetch_card_data(card_name):
    """Fetch card details from Scryfall API."""
    response = requests.get(SCRYFALL_API_URL, params={"fuzzy": card_name})

    if response.status_code == 200:
        card_data = response.json()
        return {
            "name": card_data.get("name", card_name),
            "image": card_data.get("image_uris", {}).get("normal", "No image available"),
            "type": card_data.get("type_line", "Unknown"),
            "oracle_text": card_data.get("oracle_text", "No description available")
        }
    else:
        return {"name": card_name, "image": "No image available", "type": "Unknown", "oracle_text": "Unknown"}

def categorize_cards(deck_list):
    """Sort cards into categories."""
    categories = {
        "Creatures": [],
        "Instants": [],
        "Sorceries": [],
        "Artifacts": [],
        "Enchantments": [],
        "Planeswalkers": [],
        "Lands": []
    }

    for card in deck_list:
        card_type = card["type"].lower()
        if "creature" in card_type:
            categories["Creatures"].append(card)
        elif "instant" in card_type:
            categories["Instants"].append(card)
        elif "sorcery" in card_type:
            categories["Sorceries"].append(card)
        elif "artifact" in card_type:
            categories["Artifacts"].append(card)
        elif "enchantment" in card_type:
            categories["Enchantments"].append(card)
        elif "planeswalker" in card_type:
            categories["Planeswalkers"].append(card)
        elif "land" in card_type:
            categories["Lands"].append(card)

    return categories

def generate_commander_deck(user_prompt):
    """Generate a Commander deck using OpenAI."""
    print(f"🔄 Generating deck for prompt: {user_prompt}")

    response = ask_openai(user_prompt + " Please generate a full 100-card deck list.")

    deck_list = []
    card_count = 1

    for line in response.split("\n"):
        line = line.strip()
        if line:
            match = re.match(r'^(\d+)[xX]?\s*(.+)$', line)
            if match:
                quantity = int(match.group(1))
                card_name = match.group(2).strip()

                card_data = fetch_card_data(card_name)
                card_data["quantity"] = quantity
                card_data["number"] = card_count

                deck_list.append(card_data)
                card_count += 1

    # Ensure 100 cards are saved
    if len(deck_list) < 100:
        print(f"❌ Warning: Only {len(deck_list)} cards processed! Expected 100.")

    categories = categorize_cards(deck_list)

    deck_data = {
        "deck": deck_list,
        "categories": categories
    }

    json_path = os.path.join(os.getcwd(), "deck.json")
    with open(json_path, "w") as json_file:
        json.dump(deck_data, json_file, indent=4)

    print(f"✅ Deck saved to {json_path}!")

