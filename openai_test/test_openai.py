#!/usr/bin/env python3

import os
from openai import OpenAI

def main():
    api_key = os.getenv("OPENAI_KEY")

    if not api_key:
        raise RuntimeError(
            "OPENAI_KEY environment variable is not set. "
            "Run: source ~/.bash_profile"
        )

    client = OpenAI(api_key=api_key)

    try:
        response = client.responses.create(
            model="gpt-5",
            input="Reply with exactly: API test successful"
        )

        print("Connection successful!")
        print("Response:")
        print(response.output_text)

    except Exception as e:
        print("API test failed:")
        print(e)

if __name__ == "__main__":
    main()
