import requests

def get_card_image_url(card_name):
    # Construct the Scryfall API endpoint using fuzzy matching
    url = f"https://api.scryfall.com/cards/named?fuzzy={card_name}"
    response = requests.get(url)

    if response.status_code != 200:
        print("Error: Card not found or API request failed.")
        return None

    card_data = response.json()
    
    # Check if the card has a single face with image_uris
    if "image_uris" in card_data:
        # You can choose the size: small, normal, large, png, art_crop, border_crop
        return card_data["image_uris"].get("normal")
    # Check if it's a double-faced card with multiple card_faces
    elif "card_faces" in card_data:
        # For double-faced cards, get the image URL from the first face.
        if "image_uris" in card_data["card_faces"][0]:
            return card_data["card_faces"][0]["image_uris"].get("normal")
    
    print("Image URL not available for this card.")
    return None

def main():
    card_name = input("Enter a Magic card name: ").strip()
    image_url = get_card_image_url(card_name)
    if image_url:
        print("Image URL:", image_url)

if __name__ == "__main__":
    main()

