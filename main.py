import openai
import os
import sys


# Set the API key
openai.api_key = os.getenv('API_KEY')


# Use the ChatGPT model to generate text
model_engine = "text-davinci-003"
prompt = sys.argv[1]
completion = openai.Completion.create(engine=model_engine, prompt=prompt, max_tokens=1024, n=1,stop=None,temperature=0.7)
message = completion.choices[0].text
print(message)
