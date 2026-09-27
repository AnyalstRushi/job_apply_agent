import asyncio
import os
from pathlib import Path

from browser_use import Agent, Browser, ChatGoogle
from dotenv import load_dotenv

load_dotenv()

PROFILE_FILE = Path(__file__).parent / "my_profile.txt"

JOB_TITLE = "Azure Data Engineer"
LOCATION = "Pune, Maharashtra, India"
JOB_SITE_URL = "https://in.indeed.com"
MAX_JOBS_TO_REVIEW = 2


def load_profile():
    if not PROFILE_FILE.exists():
        raise FileNotFoundError("my_profile.txt sapadla nahi.")

    profile = PROFILE_FILE.read_text(encoding="utf-8").strip()

    if not profile:
        raise ValueError("my_profile.txt rikami aahe.")

    return profile


async def main():
    if not os.getenv("GOOGLE_API_KEY"):
        raise EnvironmentError("GOOGLE_API_KEY .env file madhe sapadli nahi.")

    profile = load_profile()

    task = f"""
Open {JOB_SITE_URL} in a visible browser.
Search for "{JOB_TITLE}" jobs in "{LOCATION}".

Candidate profile:
---
{profile}
---

Review at most {MAX_JOBS_TO_REVIEW} relevant job listings.

For each reviewed job:
1. Open the full job description.
2. Compare it with the candidate profile.
3. Record job title, company, location, top required skills, and a short match reason.
4. Do NOT click Apply, Easy Apply, Submit, Sign In, or Create Account.
5. Do NOT fill any form.
6. Do NOT bypass CAPTCHA, OTP, login, payment, or website restrictions.

At the end, return a concise table with:
Job title | Company | Location | Match reason | Recommendation.
"""

    browser = Browser(headless=False)

    agent = Agent(
        task=task,
        llm=ChatGoogle(model="gemini-3-flash-preview"),
        browser=browser,
        flash_mode=True,
max_failures=2,
    )

    result = await agent.run(max_steps=6)

    print("\n================ JOB REVIEW SUMMARY ================\n")
    print(result)


if __name__ == "__main__":
    asyncio.run(main())
    