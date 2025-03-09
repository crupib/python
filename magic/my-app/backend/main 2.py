import os
import json
import openai
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

openai.api_key = os.getenv("OPENAI_KEY")

app = FastAPI()

origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # or ["*"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/save-deck")
async def save_deck(request: Request):
    deck_data = await request.json()

    # 1) Save deck_data to Deck.json
    with open("Deck.json", "w") as f:
        json.dump(deck_data, f, indent=2)

    # 2) Construct the prompt
    prompt_text = (
        "You are given a Magic: The Gathering deck in JSON format. "
        "Generate a card deck based on the distrobution in the Deck.json file, List 100 cards including the commander, also Generate a brief summary or analysis of this deck, returning a list of the cards and a summary. "
        "Deck data:\n\n"
        f"{json.dumps(deck_data, indent=2)}\n\n"
        "Return only the requested information."
    )

    # 3) Call the ChatCompletion API with GPT-4 (or gpt-3.5-turbo)
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt_text}],
            max_tokens=1200,
            temperature=0.1
        )
    except Exception as e:
        return {"error": f"OpenAI API call failed: {e}"}

    # 4) Extract the AI-generated text
    ai_output = response.choices[0].message["content"].strip()

    # 5) Save the AI output to prompt.txt
    with open("prompt.txt", "w") as f:
        f.write(ai_output)

    return {"message": "Deck saved successfully!", "ai_output": ai_output}
