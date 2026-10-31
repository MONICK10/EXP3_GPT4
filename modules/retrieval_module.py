"""Retrieval Module - finds the most similar past emails and their replies.

Example: new email "My laptop screen is broken."
         -> most similar past email: "The phone I received has a cracked screen..." (similarity 0.58)
"""
import os

import pandas as pd

from semantic import SemanticIndex

PATH = os.path.join(os.path.dirname(__file__), "..", "data", "email_history.csv")


class Retriever:
    def __init__(self):
        self.df = pd.read_csv(PATH)
        self.index = SemanticIndex((self.df.subject + ". " + self.df.email).tolist())

    def similar(self, e, k=3):
        hits = self.index.search(f"{e['subject']}. {e['email']}", k)
        return [{"id": int(self.df.id[i]), "subject": self.df.subject[i], "email": self.df.email[i],
                 "intent": self.df.intent[i], "reply": self.df.reply[i], "score": s} for i, s in hits]
