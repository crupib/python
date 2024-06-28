import openai
import os
def content_filter(prompt, generated_text):
   moderation_prompt = f"{{text:{generated_text}}} Moderation: Is this text safe for work and follows OpenAI's usage polices?"
   response = openai.Completion.create(
     engine="gpt-3.5-turbo-instruct",
     prompt=moderation_prompt,
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
generated_text = "This is an example of generated text."
if content_filter("What is the capital of France?", generated_text):
  print("The generated text is safe.")
else:
  print("The generated text is not safe.")
