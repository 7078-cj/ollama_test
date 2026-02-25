import ollama

client = ollama.Client(
    host="http://localhost:11434"
)


model = 'gemma3:4b'
prompt = 'hi'

response = client.generate(model=model, prompt=prompt)

print(response.response)