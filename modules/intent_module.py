"""Intent Module - finds why the customer wrote the email.

Example: "My package has not arrived yet."  ->  Delivery Delay (urgency: Medium, sentiment: Negative)
"""
from llm import ask_json

INTENTS = ["Delivery Delay", "Damaged Product", "Refund Request", "Order Cancellation", "Payment Issue",
           "Account Issue", "Product Inquiry", "Complaint", "Return/Exchange", "Feedback"]


KEYWORDS = {
    "Delivery Delay": ["not arrived", "not received", "delay", "late", "transit", "where is"],
    "Damaged Product": ["damaged", "broken", "cracked", "missing", "torn"],
    "Refund Request": ["refund", "money back"],
    "Order Cancellation": ["cancel"],
    "Payment Issue": ["payment", "charged", "deducted", "coupon"],
    "Account Issue": ["log in", "login", "password", "account"],
    "Return/Exchange": ["return", "exchange", "wrong product"],
    "Feedback": ["thank", "great", "amazing", "excellent"],
    "Complaint": ["poor", "rude", "disappoint", "worst"],
}


def keyword_intent(text):
    """Backup rules if the LLM reply is not usable."""
    t = text.lower()
    for intent, words in KEYWORDS.items():
        if any(w in t for w in words):
            return intent
    return "Product Inquiry"


def detect(e):
    prompt = (f"Classify this customer email.\nSubject: {e['subject']}\nEmail: {e['email']}\n\n"
              f"Intent must be one of: {', '.join(INTENTS)}.\n"
              "Guidance:\n"
              "- Refund Request: the customer is chasing money back, even if they already returned the item.\n"
              "- Return/Exchange: the customer wants to START a return or swap, and has not asked about money.\n"
              "- Sentiment is about how the customer feels. A complaint or a chase-up is Negative or Neutral, "
              "never Positive. Only genuine praise is Positive.\n"
              'Return JSON: {"intent": "...", "urgency": "Low|Medium|High", '
              '"sentiment": "Positive|Neutral|Negative", "reason": "<one short sentence>"}')
    d = ask_json(prompt, default={}) or {}
    intent = d.get("intent", "")
    match = next((i for i in INTENTS if i.lower() == str(intent).lower()), None)
    return {"intent": match or keyword_intent(e["subject"] + " " + e["email"]),
            "urgency": d.get("urgency", "Medium"), "sentiment": d.get("sentiment", "Neutral"),
            "reason": d.get("reason", ""), "source": "LLM" if match else "fallback"}
