import openai
import os
def generate_text(prompt, temperature):
  response = openai.Completion.create(
     engine="gpt-3.5-turbo-instruct",
     prompt=prompt,
     max_tokens=50,
     n=1,
     stop=None,
     temperature=temperature,
  )
  return response.choices[0].text.strip()
def collect_feedback():
  feedback = input("Please rate the response (1-5): ")
  return int(feedback)
def main():
  value = os.getenv('OPENAI_API_KEY')
  if value is None:
     print("The environment variable does not exist or has no value.")
  openai.api_key  = value
  prompt = "Write a brief introduction to machine learning."
  temperature = 0.7
  user_feedback = 0
  while user_feedback < 4:
    generated_text = generate_text(prompt, temperature)
    print("\nGenerated Text:")
    print(generated_text)
    user_feedback = collect_feedback()
    if user_feedback < 4:
      if user_feedback < 3:
        temperature += 0.1
      else:
        temperature -= 0.1
  print("Final Generated Text:")
  print(generated_text)
if __name__ == "__main__":
  main()  
