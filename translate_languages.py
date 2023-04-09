import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

text_to_translate = input("Enter Text to be translated into 1. French, 2. Spanish and 3. Portugese  : ")

translation_prompt=f"Translate this into 1. French, 2. Spanish and 3. Portugese :\n\n{text_to_translate}\n\n1.",


response = openai.Completion.create(
  model="text-davinci-003",
  prompt=translation_prompt,
  temperature=0.3,
  max_tokens=100,
  top_p=1.0,
  frequency_penalty=0.0,
  presence_penalty=0.0
)

print(f'1.{response["choices"][0]["text"]}')