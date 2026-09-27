from pathlib import Path

content = '''# Job Review Agent

## Project overview

This project is a local Python tool for reviewing job listings against a candidate profile. It runs on a Windows workstation, opens a visible browser, and uses the browser-use agent and a Google Gemini model to compare a listing with profile text and print a concise match summary.

The current implementation is intentionally limited to review and recommendation. It does not submit applications, fill forms, or bypass website restrictions.

## Features present in the current code

The repository currently implements the following behavior in `main.py`:

- loads a candidate profile from `my_profile.txt`
- validates that `GOOGLE_API_KEY` exists in a local `.env` file
- searches a configured job title and location on Indeed
- opens the site in a visible browser using Playwright
- reviews up to `MAX_JOBS_TO_REVIEW` relevant listings
- compares each listing to the profile text
- prints a final table with:
  - Job title
  - Company
  - Location
  - Match reason
  - Recommendation

The task prompt explicitly states the following restrictions:

- no Apply
- no Easy Apply
- no Submit
- no Sign In
- no Create Account
- no form filling
- no CAPTCHA bypass
- no OTP bypass
- no login, payment, or verification bypass

This is a review workflow, not an automated job application workflow.

## Technology stack

The repository currently declares and uses the following technologies:

- Python 3.11+ recommended
- `browser-use>=0.12.0`
- `playwright>=1.45`
- `python-dotenv>=1.0`
- Google Gemini model: `gemini-3-flash-preview`
- Playwright Chromium browser

## Windows setup commands

```powershell
cd Desktop\job_apply_agent
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python -m playwright install chromium
copy .env.example .env
```

Then add your API key to `.env`:

```env
GOOGLE_API_KEY=your_google_api_key_here
```

Create a local `my_profile.txt` with the candidate summary you want the agent to compare against the job descriptions.

## How to run the project

1. Ensure the virtual environment is activated.
2. Confirm `.env` contains a valid `GOOGLE_API_KEY`.
3. Confirm `my_profile.txt` exists and is not empty.
4. Review the constants near the top of `main.py`:

```python
JOB_TITLE = "Azure Data Engineer"
LOCATION = "Pune, Maharashtra, India"
JOB_SITE_URL = "https://in.indeed.com"
MAX_JOBS_TO_REVIEW = 2
```

5. Run:

```powershell
python main.py
```

The browser will open in visible mode and the agent will review the configured listings. The terminal will print the final summary table.

## Example output

```text
================ JOB REVIEW SUMMARY ================

Job title | Company | Location | Match reason | Recommendation
Azure Data Engineer | Example Company | Pune, Maharashtra, India | Strong match for data engineering responsibilities and cloud data platform work. | Consider for follow-up
```

This example is illustrative only. The actual result depends on the current listing content and the profile text in `my_profile.txt`.

## Safety limitations

This repository is intentionally constrained to safe, human-supervised review behavior.

- No automatic job application is performed.
- No Apply, Easy Apply, Submit, Sign In, CAPTCHA, OTP, or form filling is attempted.
- The workflow is bounded to reading listings and comparing them against the profile.
- The browser remains visible so the user can observe and intervene at any time.
- The project does not bypass login, payment, verification, or account restrictions.

## Known limitations

- The script currently targets a single site: Indeed.
- The search is set by static constants in `main.py` rather than a dynamic config file.
- The review count is fixed at two listings by `MAX_JOBS_TO_REVIEW`.
- The browser automation depends on the current behavior and stability of the external site.
- The model is `gemini-3-flash-preview`, which is a preview model and may vary in output quality.
- The project relies on a local profile file and therefore requires human-maintained profile text.

## Future roadmap

The following capabilities are planned and not yet implemented in the current codebase:

- broader job-board support beyond Indeed
- multi-role or multi-location search configuration
- structured profile parsing and scoring
- result export to CSV or JSON
- recurring scheduled review runs
- richer recommendation and ranking models

For architecture and support details, see the documentation in the `docs/` directory:

- [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md)
- [docs/SECURITY.md](docs/SECURITY.md)
- [docs/OPERATIONS.md](docs/OPERATIONS.md)
- [docs/ROADMAP.md](docs/ROADMAP.md)
'''
Path('README.md').write_text(content, encoding='utf-8')
