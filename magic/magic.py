import os
import re
import json
import requests
import openai

# Set your OpenAI API key here (or via an environment variable)
SCRYFALL_API_URL = "https://api.scryfall.com/cards/named"
oaikey = os.environ.get('OPENAI_KEY', 'xxxxx')

def ask_openai(prompt):
    """Ask OpenAI for a 100-card Commander deck list based on the prompt."""
    openai.api_key = oaikey
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{
                "role": "user", 
                "content": prompt + " Please generate a full 100-card deck list with each line in the format '1x Card Name'."
            }]
        )
        return response["choices"][0]["message"]["content"]
    except Exception as e:
        print("Error calling OpenAI:", e)
        return ""

def normalize_card_name(card_name):
    """
    Normalize card names that contain "//" by ensuring there is exactly one space
    on each side of the "//". This returns the full normalized card name.
    """
    return re.sub(r'\s*//\s*', ' // ', card_name.strip())

def fetch_card_data(card_name):
    """
    Fetch card details from the Scryfall API.
    
    For cards with "//", normalize the full card name and first try an exact search.
    If that fails, fall back to a fuzzy search using the full normalized name.
    Then, check for image URLs in the top-level "image_uris" and if not found, in "card_faces".
    """
    normalized_name = normalize_card_name(card_name) if "//" in card_name else card_name.strip()

    # First, attempt an exact search using the full normalized name.
    params = {"exact": normalized_name}
    try:
        response = requests.get(SCRYFALL_API_URL, params=params)
        response.raise_for_status()
        card_data = response.json()
    except Exception as e:
        print(f"Exact search failed for '{normalized_name}': {e}")
        # Fall back to fuzzy search with the full normalized name.
        try:
            response = requests.get(SCRYFALL_API_URL, params={"fuzzy": normalized_name})
            response.raise_for_status()
            card_data = response.json()
        except Exception as e2:
            print(f"Fuzzy search failed for '{normalized_name}': {e2}")
            return {"name": normalized_name, "image": "", "type": "Unknown", "oracle_text": "Unknown"}
    
    # Try to get image URL from top-level image_uris.
    image_url = card_data.get("image_uris", {}).get("normal", "")
    # If not available, check for card_faces.
    if not image_url and "card_faces" in card_data:
        faces = card_data["card_faces"]
        if faces and "image_uris" in faces[0]:
            image_url = faces[0]["image_uris"].get("normal", "")
    
    return {
        "name": card_data.get("name", normalized_name),
        "image": image_url,
        "type": card_data.get("type_line", "Unknown"),
        "oracle_text": card_data.get("oracle_text", "No description available")
    }

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
    """Generate the commander deck, process each card from OpenAI's response,
    categorize the cards, and save the deck.json file.
    """
    print(f"Generating deck for prompt: {user_prompt}")
    openai_response = ask_openai(user_prompt)
    if not openai_response:
        print("No response received from OpenAI.")
        return

    deck_list = []
    card_number = 1  # Internal ordering (will not be displayed)

    # Process each nonempty line from the OpenAI response.
    for line in openai_response.splitlines():
        line = line.strip()
        if not line:
            continue
        # Expect lines of the format "1x Card Name" (or similar)
        match = re.match(r'^(\d+)[xX]?\s+(.+)$', line)
        if match:
            quantity = int(match.group(1))
            card_name = match.group(2).strip()
        else:
            # If no quantity is provided, assume 1 and use the full line as card name.
            quantity = 1
            card_name = line

        card_details = fetch_card_data(card_name)
        card_details["quantity"] = quantity
        card_details["number"] = card_number  # Stored for internal ordering only
        deck_list.append(card_details)
        card_number += 1

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
    prompt = input("Enter deck prompt: ")
    generate_commander_deck(prompt)
