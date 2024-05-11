import openai
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

prompt = "What is the captial of Italy?"
response = test_chatgpt(prompt)
print(response)

