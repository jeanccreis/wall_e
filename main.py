import asyncio
from playwright.async_api import async_playwright
from orchestrator import run_all_scrapers

from scrapers import formatters
from scrapers import db_handler

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        all_jobs = await run_all_scrapers(browser)
        df_all_jobs = formatters.format_data(all_jobs)
        db_handler.save_to_db(df_all_jobs)
        await browser.close()

if __name__ == "__main__":
    asyncio.run(main())
