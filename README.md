# English to Kannada Translator

A minimal web app that translates English (or other languages) into Kannada using Flask and `deep-translator`.

Files added:
- [app.py](app.py) — Flask application
- [templates/index.html](templates/index.html) — UI template
- [static/style.css](static/style.css) — styles
- [requirements.txt](requirements.txt) — Python dependencies

Quick start

1. Create a virtual environment (recommended):

```powershell
python -m venv venv
venv\Scripts\Activate.ps1
```

2. Install dependencies:

```powershell
pip install -r requirements.txt
```

3. Run the app:

```powershell
python app.py
```

Open http://127.0.0.1:5000 in your browser.

Notes
- The app uses `deep-translator` which accesses online translation providers; network access is required.
- For production, run with a WSGI server and disable debug mode.
