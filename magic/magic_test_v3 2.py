import openai
import os
import sys
import time
import threading
import readline  # Enables in-place editing in supported terminals

def spinner():
    """Displays a spinner while the API request is running."""
    while not stop_spinner:
        for cursor in "|/-\\":
            sys.stdout.write(f"\rProcessing {cursor}")
            sys.stdout.flush()
            time.sleep(0.1)

def generate_openai_response(prompt):
    """Send a prompt to OpenAI and return the response."""
    openai.api_key = os.getenv("OPENAI_KEY", "your_api_key_here")  # Replace with your API key
    
    global stop_spinner
    stop_spinner = False
    spinner_thread = threading.Thread(target=spinner)
    spinner_thread.start()
    
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",  # Specify the model you want to use
            messages=[
                {"role": "system", "content": "You are a Magic: The Gathering deck-building assistant. Provide deck suggestions, strategies, and card recommendations based on user input."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.0,
            top_p=0.0
        )
        return response["choices"][0]["message"]["content"].strip()
    except Exception as e:
        return f"Error: {e}"
    finally:
        stop_spinner = True
        spinner_thread.join()
        sys.stdout.write("\rDone!          \n")

def get_edited_input(initial_text=""):
    """Allows the user to edit their input in place."""
    readline.set_startup_hook(lambda: readline.insert_text(initial_text))
    try:
        return input("Edit your prompt: ")
    finally:
        readline.set_startup_hook(None)

if __name__ == "__main__":
    while True:
        user_prompt = input("Enter your deck-building request: ")
        
        while True:  # Loop allows multiple edits
            print("\nSubmitting your request...\n")
            result = generate_openai_response(user_prompt)
            print("\nMagic: The Gathering Deck Building Assistant Response:\n", result)
            
            # Ask if the user wants to edit the prompt and resubmit
            print("\nWould you like to edit and resubmit?")
            print(f"Current Prompt: \"{user_prompt}\"")
            edit_choice = input("Edit and resubmit? (y/n): ").strip().lower()
            
            if edit_choice == "y":
                user_prompt = get_edited_input(user_prompt)
            else:
                break  # Exit edit loop if user is satisfied
        
        # Ask if the user wants to enter another new request
        another = input("\nDo you want to enter another request? (y/n): ").strip().lower()
        if another != "y":
            print("Goodbye!")
            break

