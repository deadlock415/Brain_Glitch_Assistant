import ollama
from rich.console import Console
from rich.markdown import Markdown
from rich.panel import Panel

console = Console()

# Render title with Rich instead of pyfiglet
console.rule("[bold cyan]BRAIN GLITCH ASSISTANT🧠[/bold cyan]")
console.print("[bold magenta]OUTPUT-DRIVEN AI INSIGHT ENGINE[/bold magenta]\n")

# Step 1: List all available models
available_models = ollama.list()

console.print("[bold green]Available models:[/bold green]")
for i, model in enumerate(available_models['models']):
    console.print(f"[cyan]{i+1}.[/cyan] {model.model}")

# Step 3: Let user choose a model by number, with validation loop
while True:
    try:
        choice = int(console.input("\nChoose a model number: ")) - 1
        if 0 <= choice < len(available_models['models']):
            break
        else:
            console.print("[red]Invalid number. Please enter a number from the list above.[/red]")
    except ValueError:
        console.print("[red]Invalid input. Please enter a valid integer.[/red]")

selected_model = available_models['models'][choice]['model']
console.print(f"\n[bold yellow]Selected model:[/bold yellow] {selected_model}\n")

console.print("[bold]Welcome to Brain Glitch Assistant🧠[/bold]")
console.print("🔹 I'm your AI Insight Engine built on Output-Driven Architecture.")
console.print("💡 Start by telling me what you're working on and what you want to achieve.")
console.print("🔹 Example: I’m writing a book on startup life and want to finish the first draft in 10 days.\n")

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
# messages = []

message = "Introduce yourself"

# while message.lower() != "bye":
#     messages.append({'role': 'user', 'content': message})
#     response = ollama.chat(model=selected_model, messages=messages)
#     reply = response['message']['content']

#     console.print(Panel("[bold underline]Assistant Reply[/bold underline]", style="bright_blue"))
#     console.print(Markdown(reply), justify="left")
#     console.print("\n" + "-"*80 + "\n")

#     messages.append({'role': 'assistant', 'content': reply})
#     message = console.input("[bold green]You:[/bold green] ")

while message.lower() != "bye":
    messages.append({'role': 'user', 'content': message})
    
    console.print(Panel("[bold underline]Assistant Reply (Streaming)[/bold underline]", style="bright_blue"))
    streamed_reply = ""
    
    # Enable streaming in Ollama
    for chunk in ollama.chat(model=selected_model, messages=messages, stream=True):
        token = chunk['message']['content']
        streamed_reply += token
        console.print(token, end='', highlight=False, soft_wrap=True)  # Streaming line by line

    print()  # Final newline after stream completes
    messages.append({'role': 'assistant', 'content': streamed_reply})
    
    console.print("\n" + "-" * 80 + "\n")
    message = console.input("[bold green]You:[/bold green] ")
