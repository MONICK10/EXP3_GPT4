"""Input Module - collects the customer name, subject and email body.

Example: {"name": "John", "subject": "Delivery Delay", "email": "My package has not arrived yet."}
"""


def collect(data):
    email = (data.get("email") or "").strip()
    if len(email) < 5:
        raise ValueError("Please paste the customer email.")
    return {"name": (data.get("name") or "Customer").strip(),
            "subject": (data.get("subject") or "(no subject)").strip(),
            "email": email}
