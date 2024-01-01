from openai import OpenAI
client = OpenAI()

model = "gpt-3.5-turbo"
prompt = "Where was it played?"

import sys
if len(sys.argv) > 1: prompt = sys.argv[1]

messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Who won the world series in 2020?"},
    {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
    {"role": "user", "content": prompt}
]

response = client.chat.completions.create(
    model=model,
    messages=messages
)

print()
for message in messages:
    print(f"{message['role']}: {message['content']}")
          
print()
# print(f"User: {prompt}\n")
print(f"Assistant: {response.choices[0].message.content}\n")
