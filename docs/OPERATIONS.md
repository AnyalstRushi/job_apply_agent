# Operations

## Purpose

This document describes the supported operational workflow for the current repository. The project is a local review assistant for comparing job listings with a candidate profile. It is not an end-to-end job application automation system.

## Runtime prerequisites

- Windows workstation
- Python 3.11 or newer recommended
- Internet access to browse job listings
- Google API key for the model used by `ChatGoogle`
- local browser support via Playwright Chromium

## Declared dependencies

The current repository declares the following dependencies in `requirements.txt`:

- `browser-use>=0.12.0`
- `playwright>=1.45`
- `python-dotenv>=1.0`

The application also uses the Google model string configured in `main.py`:

- `gemini-3-flash-preview`

## Initial setup on Windows

```powershell
cd Desktop\job_apply_agent
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python -m playwright install chromium
```

Then create a local `.env` file from the example and configure the API key:

```powershell
copy .env.example .env
```

Add the key:

```env
GOOGLE_API_KEY=your_google_api_key_here
```

## Profile and search configuration

The script reads a local profile from `my_profile.txt` and uses the following constants in `main.py`:

- `JOB_TITLE = "Azure Data Engineer"`
- `LOCATION = "Pune, Maharashtra, India"`
- `JOB_SITE_URL = "https://in.indeed.com"`
- `MAX_JOBS_TO_REVIEW = 2`

These values are user-editable and should be adjusted before running the review.

## Run the project

```powershell
python main.py
```

The browser opens in visible mode and the script reviews a limited number of job listings. The final output is a summary table in the console.

## Expected runtime flow

1. Validate that `GOOGLE_API_KEY` is present in `.env`.
2. Confirm `my_profile.txt` exists and is not empty.
3. Launch a visible browser session.
4. Search the configured job board using the configured title and location.
5. Review up to `MAX_JOBS_TO_REVIEW` relevant listings.
6. Compare each listing to the candidate profile.
7. Print a summary table:
   - Job title
   - Company
   - Location
   - Match reason
   - Recommendation

## Operational safety requirements

The application must not:

- Apply
- Easy Apply
- Submit
- Sign In
- CAPTCHA
- OTP
- form filling
- login bypass
- payment or verification bypass

The task prompt in `main.py` explicitly includes these restrictions and the script intentionally stops before any application flow.

## Monitoring and troubleshooting

- Watch the first run in the visible browser.
- Confirm the browser has Chromium available.
- Confirm the `.env` file is present and valid.
- Confirm the profile file is populated and not empty.
- Review the console output for matching quality and any upstream provider issues.

## Operational limits

The current project has no production deployment, scheduler, or persistent queue. It is designed as a manual local workflow for targeted job research rather than a fully managed service.

## Planned operational improvements

Planned but not yet implemented:

- configurable repeat runs,
- automatic result export,
- expanded job-site support,
- better comparison metrics and reporting,
- scheduling and orchestration for recurring review loops.
