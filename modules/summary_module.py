"""Summary Module - summarizes the conversation (customer email + reply) in about 50 words."""
from llm import ask


def summarize(e, reply):
    prompt = (f"Summarize this support conversation in about 50 words for a CRM note. Mention the customer, "
              f"the issue and the action promised.\n\nCustomer ({e['name']}): {e['email']}\n\nOur reply: {reply}")
    text = ask(prompt)
    return {"summary": text, "words": len(text.split())}
