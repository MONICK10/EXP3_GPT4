"""Save Module - saves the reply, intent and timestamp to saved/saved_replies.csv."""
import csv
import os
from datetime import datetime

PATH = os.path.join(os.path.dirname(__file__), "..", "saved", "saved_replies.csv")
FIELDS = ["timestamp", "customer_name", "subject", "email", "intent", "tone", "reply", "summary"]


def save(d):
    os.makedirs(os.path.dirname(PATH), exist_ok=True)
    new = not os.path.exists(PATH)
    row = {"timestamp": datetime.now().strftime("%d-%m-%Y %H:%M:%S"), "customer_name": d.get("name", ""),
           "subject": d.get("subject", ""), "email": d.get("email", ""), "intent": d.get("intent", ""),
           "tone": d.get("tone", "Original"), "reply": d.get("reply", ""), "summary": d.get("summary", "")}
    with open(PATH, "a", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS)
        if new:
            w.writeheader()
        w.writerow(row)
    return {"saved": row, "file": os.path.abspath(PATH), "history": history()}


def history(n=5):
    if not os.path.exists(PATH):
        return []
    with open(PATH, encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    return rows[-n:][::-1]
