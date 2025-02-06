import openai
import os

def main():
    # Set your OpenAI API key.
    # Replace 'your_api_key_here' with your actual API key or set the OPENAI_API_KEY environment variable.
    openai.api_key = os.getenv("OPENAI_KEY", "your_api_key_here")
    
    # Prompt the user for input
    prompt = input("Enter your prompt: ").strip()
    if not prompt:
        print("No prompt provided. Exiting.")
        return

    try:
        # Create a chat completion request using the GPT-3.5 Turbo model
        response = openai.ChatCompletion.create(
            model="o3-mini",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ]
        )

        # Extract and print the assistant's reply from the API response.
        assistant_reply = response["choices"][0]["message"]["content"]
        print("\nResponse from OpenAI:")
        print(assistant_reply)
    except Exception as e:
        print("An error occurred while calling the OpenAI API:", e)

if __name__ == "__main__":
    main()

