# Viva Notes – Ex 3 (Monick S, URK23CS1167)

Short answers. Example first, then the idea.

---

## Ex 3 – Email Assistant

**Q: Why use previous emails?**
Example: Old email "package arrived damaged" → old reply "we'll send a replacement". New email "laptop screen broken" → retrieved as similar → AI writes a reply in the same style.
Idea: This is **few-shot prompting** with retrieved examples. Replies stay consistent with company policy.

**Q: Tone module?** Same facts, rewritten Friendly / Formal / Empathetic. UI shows before vs after.

---

## Common to all 6 experiments

**Q: What is Ollama?**
Example: I type `ollama pull llama3.2`, then my app sends a prompt to `http://localhost:11434` and gets an answer. No internet.
Idea: Ollama runs LLMs on my own laptop. Free, offline, and data stays on my computer.

**Q: Which model did you use? Why not real GPT-4?**
Llama 3.2 (3B) by Meta, run through Ollama. GPT-4 needs a paid cloud API. Llama 3.2 does the same kind of work locally, so the "GPT-4" tasks run on a GPT-4-style model.

**Q: What is a prompt? What is prompt engineering?**
Example: "Write a blog" gives random output. "Write a 400-word informative blog on EVs for students, friendly tone, with Introduction and Conclusion" gives exactly what I want.
Idea: A prompt is the instruction. Prompt engineering means adding role, task, constraints and output format to get better answers.

**Q: Why do you ask the LLM for JSON?**
Example: I need `{"intent": "FAQ"}` so Python can read `data["intent"]`. Plain text like "I think it is FAQ" is hard to read in code.
Idea: JSON output is easy to parse. Ollama's `format: "json"` forces it. If parsing fails, my code uses a keyword fallback.

**Q: What is Flask?**
A small Python web framework. `@app.post("/api/chat")` makes a URL the web page can call. It connects the HTML page to my Python modules.

**Q: What is temperature?**
Example: temperature 0.1 → same answer every time (good for extraction). 0.7 → more creative (good for blogs).
Idea: It controls randomness.
