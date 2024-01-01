from openai import OpenAI
client = OpenAI()

name="Math Tutor"
model="gpt-4-1106-preview"
instructions="You are a personal math tutor. Answer questions briefly, in a sentence or less."
prompt = "I need to solve the equation `3x + 11 = 14`. Can you help me?"

import sys
if len(sys.argv) > 1: prompt = sys.argv[1]

import json

def display(obj):
    print(json.dumps(obj, indent=2))
    
def show_json(obj):
    display(json.loads(obj.model_dump_json()))

assistant = client.beta.assistants.create(
    name=name,
    instructions=instructions,
    model=model,
)
# show_json(assistant)

thread = client.beta.threads.create()
# show_json(thread)

message = client.beta.threads.messages.create(
    thread_id=thread.id,
    role="user",
    content=prompt,
)
# show_json(message)

run = client.beta.threads.runs.create(
    thread_id=thread.id,
    assistant_id=assistant.id,
)
# show_json(run)

import time

def wait_on_run(run, thread):
    while run.status == "queued" or run.status == "in_progress":
        run = client.beta.threads.runs.retrieve(
            thread_id=thread.id,
            run_id=run.id,
        )
        time.sleep(0.5)
    return run

run = wait_on_run(run, thread)
# show_json(run)

messages = client.beta.threads.messages.list(thread_id=thread.id)
# show_json(messages)

print()
print(f"User: {prompt}\n")
print(f"Assistant: {messages.data[0].content[0].text.value}\n")
