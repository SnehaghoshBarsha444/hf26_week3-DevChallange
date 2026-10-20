import os
import requests
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
OLLAMA_URL = os.getenv("OLLAMA_URL", "http://localhost:11434/api/generate")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "gemma3:1b")

SYSTEM_PROMPT = """You are Steady, a practical planning assistant.
Turn a user's goal into a realistic, encouraging plan with small steps.
Be specific, avoid exaggerated claims, and never pretend tasks are completed.
Return:
1. A one-sentence summary
2. 3 to 7 numbered steps, each small and actionable
3. One likely obstacle and a practical workaround
Keep the answer concise and supportive."""

@app.get("/")
def home():
    return render_template("index.html")

@app.get("/api/health")
def health():
    return jsonify({"status": "ok", "model": OLLAMA_MODEL, "provider": "local Ollama"})

@app.post("/api/plan")
def create_plan():
    data = request.get_json(silent=True) or {}
    goal = str(data.get("goal", "")).strip()
    context = str(data.get("context", "")).strip()

    if not goal:
        return jsonify({"error": "Please enter a goal first."}), 400
    if len(goal) > 500 or len(context) > 1000:
        return jsonify({"error": "Goal must be under 500 characters and context under 1,000 characters."}), 400

    prompt = f"{SYSTEM_PROMPT}\n\nUser goal: {goal}\nContext or constraints: {context or 'None provided'}\n\nCreate the plan:"
    try:
        response = requests.post(
            OLLAMA_URL,
            json={"model": OLLAMA_MODEL, "prompt": prompt, "stream": False},
            timeout=120,
        )
        response.raise_for_status()
        result = response.json().get("response", "").strip()
        if not result:
            return jsonify({"error": "The local model returned an empty response. Try again."}), 502
        return jsonify({"plan": result, "model": OLLAMA_MODEL, "local": True})
    except requests.exceptions.ConnectionError:
        return jsonify({
            "error": "Could not connect to Ollama. Install and start Ollama, then pull the model shown in the README."
        }), 503
    except requests.exceptions.Timeout:
        return jsonify({"error": "The model took too long to respond. Try a smaller model or a shorter goal."}), 504
    except requests.exceptions.RequestException:
        return jsonify({"error": "The local AI request failed. Check that Ollama is running and the model is available."}), 502

if __name__ == "__main__":
    app.run(debug=os.getenv("FLASK_DEBUG", "false").lower() == "true", port=int(os.getenv("PORT", "5000")))
