import openai
import os
def test_chatgpt(prompt):
   response = openai.Completion.create(
     engine="gpt-3.5-turbo-instruct",
     prompt=prompt,
     max_tokens=50,
     n=1,
     stop=None,
     temperature=0.7,
   )
   message = response.choices[0].text.strip()
   return message

value = os.getenv('OPENAI_API_KEY')
if value is None:
    print("The environment variable does not exist or has no value.")
openai.api_key  = value
prompt = "What is the captial of Italy?"
response = test_chatgpt(prompt)
print(response)

