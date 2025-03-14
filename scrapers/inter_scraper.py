# inter_scraper.py
from .base import BaseScraper
from config.selectors import INTER_SELECTORS
from . import formatters

class InterScraper(BaseScraper):
    async def search_jobs(self):
        await self.page.goto("https://carreiras.inter.co/carreiras?&q=")
   
        await self.page.wait_for_selector(INTER_SELECTORS["technology_button"])

        # Clica no elemento para buscar as vagas
        await self.page.click(INTER_SELECTORS["technology_button"])
        await self.page.click(INTER_SELECTORS["data_button"])

        await self.page.wait_for_selector(INTER_SELECTORS["vacancy_title"])
        elements = self.page.locator(INTER_SELECTORS["vacancy_title"])

        vacancy_list = await formatters.extract_text_list(elements)

        jobs = formatters.format_vacancies(vacancy_list, company="Inter")

        return jobs

