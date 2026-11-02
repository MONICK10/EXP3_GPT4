"""Summary Module - summarizes the conversation (customer email + reply) in about 50 words."""
import re

from llm import ask


def _clean(text):
    """Drop an opening line like 'Here is a 50-word summary:' and any wrapping quotes."""
    text = text.strip()
    first, sep, rest = text.partition("\n")
    if sep and first.rstrip().endswith(":") and len(first.split()) <= 20:
        text = rest.strip()
    text = re.sub(r"^here(?:'s| is)[^:]{0,80}:\s*", "", text, flags=re.I).strip()
    if len(text) > 1 and text[0] in '"“' and text[-1] in '"”':
        text = text[1:-1].strip()
    return text


def summarize(e, reply):
    prompt = (f"Summarize this support conversation in about 50 words for a CRM note. Mention the customer, "
              f"the issue and the action promised.\n"
              "Return only the summary text itself - no introduction line, no quotation marks.\n\n"
              f"Customer ({e['name']}): {e['email']}\n\nOur reply: {reply}")
    text = _clean(ask(prompt))
    return {"summary": text, "words": len(text.split())}
