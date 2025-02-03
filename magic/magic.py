import os
import re
import json
import requests
import openai

# Set your OpenAI API key here (or use an environment variable)
SCRYFALL_API_URL = "https://api.scryfall.com/cards/named"

def ask_openai(prompt):
    """Ask OpenAI for a 100-card Commander deck list based on the prompt."""
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt + " Please generate a full 100-card deck list with each line in the format '1x Card Name'."}]
        )
        return response["choices"][0]["message"]["content"]
    except Exception as e:
        print("Error calling OpenAI:", e)
        return ""

def fetch_card_data(card_name):
    """Fetch card details from the Scryfall API."""
    try:
        response = requests.get(SCRYFALL_API_URL, params={"fuzzy": card_name})
        response.raise_for_status()
        card_data = response.json()
        return {
            "name": card_data.get("name", card_name),
            "image": card_data.get("image_uris", {}).get("normal", ""),
            "type": card_data.get("type_line", "Unknown"),
            "oracle_text": card_data.get("oracle_text", "No description available")
        }
    except Exception as e:
        print(f"Error fetching data for {card_name}: {e}")
        return {"name": card_name, "image": "", "type": "Unknown", "oracle_text": "Unknown"}

def categorize_cards(deck_list):
    """Sort cards into categories based on their type."""
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
        ctype = card["type"].lower()
        if "creature" in ctype:
            categories["Creatures"].append(card)
        elif "instant" in ctype:
            categories["Instants"].append(card)
        elif "sorcery" in ctype:
            categories["Sorceries"].append(card)
        elif "artifact" in ctype:
            categories["Artifacts"].append(card)
        elif "enchantment" in ctype:
            categories["Enchantments"].append(card)
        elif "planeswalker" in ctype:
            categories["Planeswalkers"].append(card)
        elif "land" in ctype:
            categories["Lands"].append(card)
    return categories

def generate_commander_deck(user_prompt):
    """Generate the commander deck, save the deck.json file with 100 cards and categorized sections."""
    print(f"Generating deck for prompt: {user_prompt}")
    openai_response = ask_openai(user_prompt)
    if not openai_response:
        print("No response received from OpenAI.")
        return

    deck_list = []
    card_number = 1  # Internal ordering (will not be shown on the website)

    # Process each nonempty line from the response.
    for line in openai_response.splitlines():
        line = line.strip()
        if not line:
            continue
        match = re.match(r'^(\d+)[xX]?\s+(.+)$', line)
        if match:
            quantity = int(match.group(1))
            card_name = match.group(2).strip()
            card_details = fetch_card_data(card_name)
            card_details["quantity"] = quantity
            card_details["number"] = card_number  # stored but not displayed
            deck_list.append(card_details)
            card_number += 1
        else:
            print(f"Skipping unrecognized line: {line}")

    if len(deck_list) < 100:
        print(f"Warning: Only {len(deck_list)} cards processed! Expected 100.")

    categorized = categorize_cards(deck_list)
    deck_data = {
        "deck": deck_list,
        "categories": categorized
    }
    json_path = os.path.join(os.getcwd(), "deck.json")
    with open(json_path, "w") as f:
        json.dump(deck_data, f, indent=4)
    print(f"Deck successfully saved to {json_path}.")

if __name__ == "__main__":
    # For testing, run: python magic_json2.py "Build a Sheoldred Commander deck"
    prompt = input("Enter deck prompt: ")
    generate_commander_deck(prompt)
