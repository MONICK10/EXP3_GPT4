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
              f"and keep it under 130 words. Return only the email.\n\n{reply}")
    return ask(prompt, temperature=0.5)
