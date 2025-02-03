from flask import Flask, jsonify, request, send_from_directory
import os
import magic_json2  # Import deck generator

app = Flask(__name__)

@app.route('/generate_deck', methods=['POST'])
def generate_deck():
    data = request.json
    user_prompt = data.get("prompt", "")
    if not user_prompt:
        return jsonify({"error": "No prompt provided"}), 400

    magic_json2.generate_commander_deck(user_prompt)
    return jsonify({"message": "Deck generated successfully!"})

@app.route('/deck.json')
def get_deck():
    return send_from_directory(os.getcwd(), "deck.json")

@app.route('/')
def index():
    return send_from_directory(os.getcwd(), "index.html")

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000, debug=False, threaded=True)
