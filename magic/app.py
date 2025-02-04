from flask import Flask, jsonify, request, send_from_directory
import os
import magic

app = Flask(__name__)

@app.route('/generate_deck', methods=['POST'])
def generate_deck():
    data = request.get_json()
    user_prompt = data.get("prompt", "").strip()
    if not user_prompt:
        return jsonify({"error": "No prompt provided"}), 400

    magic.generate_commander_deck(user_prompt)
    return jsonify({"message": "Deck generated successfully!"})

@app.route('/deck.json')
def get_deck():
    json_path = os.path.join(os.getcwd(), "deck.json")
    if os.path.exists(json_path):
        return send_from_directory(os.getcwd(), "deck.json")
    else:
        return jsonify({"error": "Deck not found"}), 404

@app.route('/')
def index():
    return send_from_directory(os.getcwd(), "index.html")

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=8000, debug=True)
