"""Reply Module - writes a reply using the new email + similar past replies as examples (few-shot RAG)."""
from llm import ask

SYSTEM = ("You are a professional customer support executive for an e-commerce company called ShopSmart. "
          "Write clear, polite and helpful email replies.")


def generate(e, intent, examples):
    shots = "\n\n".join(f"Past email: {x['email']}\nPast reply: {x['reply']}" for x in examples)
    prompt = (f"Here are similar past conversations and how we replied:\n\n{shots}\n\n"
              f"New email from {e['name']}\nSubject: {e['subject']}\nEmail: {e['email']}\n"
              f"Detected intent: {intent['intent']} (urgency {intent['urgency']})\n\n"
              f"Write a reply to {e['name']} in the same helpful style. Start with 'Dear {e['name']},' "
              "and end with 'Regards,\\nShopSmart Customer Support'. Keep it under 120 words. "
              "Do not promise anything that is not in the past replies.")
    return ask(prompt, system=SYSTEM, temperature=0.4)
