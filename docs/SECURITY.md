# Security

## Summary

This project is a local browser-assisted job review tool. It does not implement automated application submission, and it intentionally avoids login, OTP, CAPTCHA, and form-filling flows.

## Security principles

1. No automated application flow.
   - The script explicitly instructs the agent not to click Apply, Easy Apply, Submit, Sign In, or Create Account.
   - It does not fill forms or bypass login or verification steps.
2. Local secret handling.
   - The Google API key is expected in a local `.env` file.
   - The repository must not contain committed secrets or personal credentials.
3. Human control.
   - The browser is opened in visible mode to allow the user to observe the session.
   - The user decides whether a listing should be investigated further.
4. Respect for site protections.
   - The tool does not bypass CAPTCHA, OTP, payment, or account restrictions.
   - It does not attempt hidden or fraudulent automation.

## Data handling

The current implementation reads:

- `GOOGLE_API_KEY` from `.env`
- candidate summary text from `my_profile.txt`

The script then sends those values to the browser automation and LLM layer while evaluating a specific job search. No additional persistence or remote service layer is implemented in this repository.

## Threat model and risk areas

### Secret leakage

Risk: API keys or profile details could be committed to source control.

Controls:

- keep `.env` out of source control,
- use `.gitignore` to exclude local secrets,
- avoid storing personal details in documentation,
- review any generated logs before sharing output.

### Website abuse

Risk: the agent could be misused to bypass job-site protections.

Controls:

- the code explicitly forbids login, CAPTCHA, OTP, and form-filling operations,
- the browser is left visible to the user,
- the project is designed for review assistance rather than automated application.

### Operational misuse

Risk: a user could run a broad or repeated review loop against job sites without supervision.

Controls:

- the script currently limits review to `MAX_JOBS_TO_REVIEW = 2`,
- the browser is not headless,
- the user is expected to monitor the first runs closely.

## Required safety statements

The application must not:

- Apply
- Easy Apply
- Submit
- Sign In
- CAPTCHA
- OTP
- form filling
- login bypass
- payment bypass

These are explicitly forbidden in the task prompt and are considered non-goals for this repository.

## Recommended repository hygiene

- store `.env` locally only,
- do not commit credentials or personal profile content,
- keep browser sessions visible during testing,
- avoid screenshots or logs that capture personal data,
- validate `.gitignore` before sharing the project.
