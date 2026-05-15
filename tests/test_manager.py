import lazyllm

manager = lazyllm.LocalLLMManager()

response = manager.chat(
    backend="ollama", 
    model="phi3", # Using a tiny model for a fast test download
    messages=[{"role": "user", "content": "What is 2+2?"}]
)

print("\nResult:", response)