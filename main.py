import asyncio
from playwright.async_api import async_playwright
from orchestrator import run_all_scrapers

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        all_jobs = await run_all_scrapers(browser)
        # TODO: Enviar para db e/ou planilha
        print("Total de vagas encontradas:", len(all_jobs))
        await browser.close()

if __name__ == "__main__":
    asyncio.run(main())
