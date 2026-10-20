# Steady: Turn big goals into small steps with local open-source AI

> Draft for the Hacktoberfest 2026 DEV Challenge. Confirm the live challenge theme, official template, required tags, and submission deadline before publishing.

## The problem

A goal can be clear while the first step is not. Steady helps people turn a goal and their constraints into a short, practical action plan.

## What I built

Steady is a small web app with a Flask backend and a minimal browser interface. A user enters a goal and optional context. The app sends those details to a model running locally through Ollama and displays a concise plan.

## Why open-source AI?

The application uses a locally served open-weight model rather than a hosted AI API. This gives users more control over where their prompts are processed and lets them change the model without redesigning the application.

## How it works

1. The user enters a goal and optional constraints.
2. Flask validates the input.
3. The backend calls the local Ollama generation endpoint.
4. The result is returned to the browser for review and copying.

## Technology

- Python and Flask
- Ollama
- Gemma 3 1B by default, configurable
- HTML, CSS, and JavaScript
- Pytest for basic tests

## Run it locally

Install Python and Ollama, then run:

```bash
ollama pull gemma3:1b
pip install -r requirements.txt
python app.py
```

Open `http://127.0.0.1:5000`.

## What is next?

The next iteration could add local progress tracking, model selection, and a reflection flow that helps users revise their plans based on what actually happened.

## Links

- GitHub repository: TODO
- Demo: TODO
- Agent session: TODO (optional)

## Verification before publication

Replace this draft's placeholders with real links. Run the application and tests, capture screenshots, confirm the model/license details, and update this article to match the active challenge's official submission template and theme.
