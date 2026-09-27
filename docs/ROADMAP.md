# Roadmap

## Current status

The repository is currently a local review-only workflow. It opens a visible browser, searches a configured role and location, and summarizes the match between job listings and a candidate profile.

## Status legend

- Current: implemented
- Planned: not yet implemented

## Near-term roadmap

### Current: review-only job matching

- Local Python workflow driven by `main.py`
- Google Gemini integration via `ChatGoogle`
- Browser automation via `browser-use` and Playwright
- Candidate-profile comparison against job listings
- Console summary output for candidate review

### Planned: broader configuration

- support for additional job boards beyond Indeed
- configurable search combinations by role, location, and category
- dynamic review limits and per-run configuration
- structured profile parsing for skills, experience, and education

### Planned: richer analysis output

- score-based job matching summaries
- CSV or JSON export of reviewed jobs
- clearer recommendation ranking and reasons
- optional notes for follow-up actions

### Planned: improved operational tooling

- repeatable scheduled review jobs
- logging and result persistence
- better failure handling and retry logic
- configuration through a dedicated settings file

## Out of scope for the current roadmap

These items are intentionally not part of the active implementation and should not be described as current capabilities:

- automatic application submission,
- sign-in or account automation,
- CAPTCHA or OTP solving,
- form filling or resume submission,
- any workflow that bypasses site restrictions.

## Strategic direction

The project is best positioned as a local, transparent review and decision-support tool rather than as an autonomous job application agent. That keeps the system aligned with the current browser automation, the user-controlled browsing session, and the explicit safety constraints in the code.
