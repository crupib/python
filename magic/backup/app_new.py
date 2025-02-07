import os
import re
import openai
from flask import Flask, render_template, request

app = Flask(__name__)

# Set your OpenAI API key from the environment or fallback to a string.
openai.api_key = os.getenv("OPENAI_KEY", "your_api_key_here")

def parse_deck_text(deck_text):
    """
    Splits the provided deck text into sections.
    Each section is assumed to start with a header that begins with "■".
    """
    deck_text = deck_text.strip()
    # Split the text on lines starting with the bullet "■"
    parts = re.split(r'\n\s*■\s*', deck_text)
    sections = []
    for part in parts:
        part = part.strip()
        if not part:
            continue
        # Assume the first line is the section title.
        lines = part.splitlines()
        title = lines[0].strip()
        content = "\n".join(lines[1:]).strip()
        sections.append({"title": title, "content": content})
    return sections

@app.route("/", methods=["GET", "POST"])
def index():
    card_sections = None
    notes_sections = None
    error_message = None

    if request.method == "POST":
        prompt = request.form.get("prompt", "").strip()
        if not prompt:
            error_message = "No prompt provided. Please enter a prompt."
        else:
            try:
                # Call the OpenAI ChatCompletion API with your chosen model.
                response = openai.ChatCompletion.create(
                    model="o3-mini",  # Replace with your preferred model if needed.
                    messages=[
                        {"role": "system", "content": "You are a helpful assistant."},
                        {"role": "user", "content": prompt}
                    ]
                )
                deck_text = response["choices"][0]["message"]["content"]
                sections = parse_deck_text(deck_text)
                
                # Separate sections into card sections and notes/strategy.
                card_sections = []
                notes_sections = []
                for section in sections:
                    title_lower = section["title"].lower()
                    if "notes" in title_lower or "strategy" in title_lower:
                        notes_sections.append(section)
                    else:
                        card_sections.append(section)
            except Exception as e:
                error_message = f"An error occurred while calling the OpenAI API: {e}"

    return render_template("index.html",
                           card_sections=card_sections,
                           notes_sections=notes_sections,
                           error_message=error_message)

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=8000, debug=False)
