from openai import OpenAI

client = OpenAI(
    api_key = 'ollama',
    base_url = 'http://localhost:11434/v1/'
)

response = client.chat.completions.create(
    model='deepseek-r1:1.5b',
    messages=[
        {"role":"system","content":"You are a helpful assistant."},
        {"role": "user", "content": "Hello!"}
    ],
    stream=True
)

for chunk in response:
    print(chunk.choices[0].delta.content, end="", flush=True)

