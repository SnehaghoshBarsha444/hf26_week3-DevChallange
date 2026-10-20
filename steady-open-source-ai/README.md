# Steady

**Small steps. Real progress.** Steady is a local-first AI planning assistant that turns a goal into small, actionable steps using an open-weight model running locally through Ollama.

## Why it exists

Large goals can feel hard to start. Steady helps users turn a goal and their constraints into a concise plan. The user stays in control and decides which suggestions to follow.

## Open-source AI at the core

Steady sends the user's goal to a model served by [Ollama](https://ollama.com/) on the same machine. The default model is `gemma3:1b`, an open-weight Gemma model. No hosted AI API key is required.

**Why local inference matters**
- Prompts can stay on the user's machine instead of being sent to a third-party AI API.
- The model can be changed through `OLLAMA_MODEL`.
- Users can run the prototype without paying per-request API fees, assuming compatible hardware and locally available software.
- Users can inspect and modify the application and its prompt.

Model availability and model-specific license terms can change. Review the current model card and license before redistributing weights or using the model commercially.

## Features

- Goal and optional context input.
- Local AI-generated plan with actionable steps.
- Clear connection and error states.
- Copy plan to clipboard.
- Input length validation.
- Lightweight Flask backend.
- Basic automated tests.

## Requirements

- Python 3.10+
- [Ollama](https://ollama.com/) installed and running
- A model supported by your hardware

## Run locally

### 1. Download a model

```bash
ollama pull gemma3:1b
```

If this model is not suitable for your device, choose another compatible Ollama model and update `OLLAMA_MODEL`.

### 2. Create an environment and install dependencies

```bash
python -m venv .venv
```

Linux/macOS:

```bash
source .venv/bin/activate
```

Windows PowerShell:

```powershell
.venv\\Scripts\\Activate.ps1
```

Install dependencies:

```bash
pip install -r requirements.txt
```

### 3. Configure and start

Copy `.env.example` to `.env` if you use an environment loader, or export the variables in your shell. Flask does not automatically load `.env` in this prototype, so set variables in your terminal or install and configure `python-dotenv`.

Default settings work without environment variables when Ollama uses its default URL and the model is `gemma3:1b`.

Start the application:

```bash
python app.py
```

Open http://127.0.0.1:5000.

## Run tests

```bash
pip install pytest
pytest -q
```

The AI endpoint requires Ollama to be running for a successful generation. The included tests cover the page, health endpoint, and input validation without requiring a model.

## API

`GET /api/health` reports the configured model and provider.

`POST /api/plan`

```json
{
  "goal": "Build a portfolio website in two weeks",
  "context": "I have 45 minutes each evening"
}
```

Returns a JSON object containing the generated plan and configured model, or a useful error message if local inference is unavailable.

## Privacy and limitations

- There is no user account or database in this MVP.
- The application does not intentionally store submitted goals.
- The browser makes a local request to Ollama to display model availability. This local endpoint may need CORS configuration in some environments; if the browser blocks it, the app still works and displays a generic local-AI status.
- Generated plans may be incomplete or inaccurate. Review them before acting.
- The app has not been security-audited and should not be exposed publicly without additional controls, authentication, rate limiting, and deployment hardening.

## Roadmap

- Save and check off plan steps locally.
- Add a selectable local model and improved model detection.
- Add a progress reflection flow.
- Add automated end-to-end tests.
- Add a privacy-focused export format.

## License

Choose and add a license before publishing. Do not imply that the repository is licensed until a license file is present.
