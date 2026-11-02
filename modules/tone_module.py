"""Tone Module - rewrites the reply in a Friendly, Formal or Empathetic tone."""
from llm import ask

TONES = {
    "Friendly": "warm, cheerful and casual but still professional",
    "Formal": "formal, precise and corporate",
    "Empathetic": "very caring and understanding, acknowledging the customer's feelings first",
}


def improve(reply, tone):
    if tone not in TONES:
        raise ValueError("Tone must be Friendly, Formal or Empathetic.")
    prompt = (f"Rewrite this customer support email in a {TONES[tone]} tone. Keep all facts the same "
              f"and keep it under 130 words.\n"
              "Keep the customer's real name and every real detail exactly as written. "
              "Never replace anything with a placeholder such as [Customer] or [Date]. "
              "Do not add a 'Subject:' line. Start at 'Dear <name>,' and return only the email body.\n\n"
              f"{reply}")
    return ask(prompt, temperature=0.5)
