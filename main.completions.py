from openai import OpenAI
client = OpenAI()

model = "gpt-3.5-turbo-instruct"
prompt = "Write a tagline for an ice cream shop."

import sys
if len(sys.argv) > 1: prompt = sys.argv[1]

response = client.completions.create(
    model=model,
    prompt=prompt
)

print(f"User: {prompt}\n")
print(f"Assistant: {response.choices[0].text}")
