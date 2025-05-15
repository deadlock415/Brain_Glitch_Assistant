import ollama

# Title and welcome
print("=" * 50)
print("BRAIN GLITCH ASSISTANT 🧠".center(50))
print("OUTPUT-DRIVEN AI INSIGHT ENGINE".center(50))
print("=" * 50)

# Step 1: List all available models
available_models = ollama.list()

print("\nAvailable models:")
for i, model in enumerate(available_models['models']):
    print(f"{i+1}. {model['model']}")

# Step 3: Let user choose a model by number, with validation loop
while True:
    try:
        choice = int(input("\nChoose a model number: ")) - 1
        if 0 <= choice < len(available_models['models']):
            break
        else:
            print("Invalid number. Please enter a number from the list above.")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

selected_model = available_models['models'][choice]['model']
print(f"\nSelected model: {selected_model}\n")

print("Welcome to Brain Glitch Assistant 🧠")
print("🔹 I'm your AI Insight Engine built on Output-Driven Architecture.")
print("💡 Start by telling me what you're working on and what you want to achieve.")
print("🔹 Example: I’m writing a book on startup life and want to finish the first draft in 10 days.\n")

# Step 4: Start chatting using the selected model
messages = [
    {'role': 'system', 'content': """You are Brain Glitch, an AI Insight Engine built on Output-Driven Architecture (ODA) principles.

Your core framework includes four insight dimensions:

✅ Do:
- Analyze the user's current situation and suggest clear, effective actions.
- Be specific and helpful based on the actual task at hand.

❌ Don’t:
- Warn the user against vague, broad, or non-impactful behaviors or approaches.
- Eliminate fluff and prevent misleading efforts.

🔄 Cause & Effect:
- Show the strategic, ethical, or logical consequence of an action or inaction.
- Help users understand “if this, then that” clarity.

📌 Clarity (Refactor):
- Improve framing, focus, or priority of a goal or plan.
- Offer better alternatives, simplify complexity, or increase alignment between input and output.

Rules:
- Always ask what the user is currently doing and what they want to achieve.
- Tailor insights; don’t give generic advice.
- Stay concise, but never sacrifice clarity.
- Use the insight format to deliver value in every response.

Format every output like this in short as Possible:
✅ Do:  
❌ Don’t:  
🔄 Cause & Effect:  
📌 Clarity:
"""}
]
message = ""
# message = "Introduce yourself"

while message.lower() != "bye":
    message = input("You: ")
    messages.append({'role': 'user', 'content': message})
    
    print("\nAssistant Reply (Streaming):")
    streamed_reply = ""
    
    for chunk in ollama.chat(model=selected_model, messages=messages, stream=True):
        token = chunk['message']['content']
        streamed_reply += token
        print(token, end='', flush=True)

    print()  # Final newline
    messages.append({'role': 'assistant', 'content': streamed_reply})
    
    print("\n" + "-" * 80 + "\n")
