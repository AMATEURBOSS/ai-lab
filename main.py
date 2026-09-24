import ollama

text = input("Paste text to summarize: ")

response = ollama.chat(
    model="qwen3:4b",
    messages=[{"role": "user", "content": f"Summarize this in English and Spanish:\n{text}"}],
)

print(response["message"]["content"])