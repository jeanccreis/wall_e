import os
import asyncio
from playwright.async_api import async_playwright
from orchestrator import run_all_scrapers, run_form_fillers

from scrapers import formatters
from scrapers import db_handler

from dotenv import load_dotenv
from services.gemini_ai import GeminiChat

load_dotenv()

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        all_jobs = await run_all_scrapers(browser)
        df_all_jobs = formatters.format_data(all_jobs)
        db_handler.save_to_db(df_all_jobs)

        # Etapa 2 - IA identifica as vagas compativeis com perfis
        # TODO: Ler vagas do db
        # TODO: Importar classe IA
        chat = GeminiChat(api_key=os.getenv("API_KEY_GEMINI"))
        prompt = "Explique o que é DEEP LARNING de forma simples."
        resposta = chat.send_prompt(prompt)
        print(resposta)

        # TODO: Identificar vagas compativeis
        # TODO: marcar no banco as vagas compativeis

        await browser.close()

if __name__ == "__main__":
    asyncio.run(main())
