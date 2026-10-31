"""
Ex. No. 3 - Intelligent Email Assistant using Ollama
Monick S - URK23CS1167

Run:  python app.py    then open  http://localhost:5003
"""
from flask import Flask, jsonify, render_template, request

from llm import LLMError, status
from modules import input_module, intent_module, reply_module, save_module, summary_module, tone_module
from modules.retrieval_module import Retriever

app = Flask(__name__)
retriever = Retriever()

SAMPLES = [
    {"name": "John", "subject": "Delivery Delay", "email": "My package has not arrived yet. It was supposed to come 3 days ago."},
    {"name": "Fathima", "subject": "Laptop screen broken", "email": "My laptop screen is broken. I just opened the box today and there is a crack on the display."},
    {"name": "Kiran", "subject": "Refund pending", "email": "I returned the headphones 10 days back. When will I get my refund?"},
]


@app.errorhandler(LLMError)
def llm_error(e):
    return jsonify(error=str(e)), 503


@app.errorhandler(ValueError)
def bad_input(e):
    return jsonify(error=str(e)), 400


@app.get("/")
def home():
    return render_template("index.html", exp_no=3, title="MailMind AI – Intelligent Email Assistant",
                           samples=SAMPLES, tones=list(tone_module.TONES), n_history=len(retriever.df),
                           method=retriever.index.method)


@app.get("/api/status")
def api_status():
    return jsonify(status())


@app.post("/api/intent")
def api_intent():
    return jsonify(intent_module.detect(input_module.collect(request.get_json())))


@app.post("/api/retrieve")
def api_retrieve():
    return jsonify(similar=retriever.similar(input_module.collect(request.get_json())))


@app.post("/api/reply")
def api_reply():
    d = request.get_json()
    e = input_module.collect(d)
    return jsonify(reply=reply_module.generate(e, d["intent"], d["similar"]))


@app.post("/api/tone")
def api_tone():
    d = request.get_json()
    return jsonify(reply=tone_module.improve(d.get("reply", ""), d.get("tone")), tone=d.get("tone"))


@app.post("/api/summary")
def api_summary():
    d = request.get_json()
    return jsonify(summary_module.summarize(input_module.collect(d), d.get("reply", "")))


@app.post("/api/save")
def api_save():
    return jsonify(save_module.save(request.get_json()))


if __name__ == "__main__":
    app.run(port=5003, debug=False)
