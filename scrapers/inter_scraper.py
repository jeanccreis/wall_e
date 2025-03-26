# inter_scraper.py
from .base import BaseScraper
from config.selectors import INTER_SELECTORS
from . import formatters
import time

class InterScraper(BaseScraper):
    async def _click_job_filters(self):
        """Função auxiliar para clicar nos filtros de vaga"""
        await self.page.goto("https://carreiras.inter.co/carreiras?&q=")
        await self.page.wait_for_selector(INTER_SELECTORS["technology_button"])
        await self.page.click(INTER_SELECTORS["technology_button"])
        await self.page.click(INTER_SELECTORS["data_button"])

    async def _extract_items_from_third_ul(self):

        third_ul = self.page.locator('#content ul').nth(1)

        list_items = third_ul.locator('li')
        count = await list_items.count()

        items = []
        for i in range(count):
            item_text = await list_items.nth(i).inner_text()
            items.append(item_text)

        return items

    async def search_jobs(self):
        # Aplica os filtros de pesquisa
        await self._click_job_filters()

        await self.page.wait_for_selector(INTER_SELECTORS["vacancy_title"])
        elements = self.page.locator(INTER_SELECTORS["vacancy_title"])
        count = await elements.count()

        jobs_list = []
        for i in range(count):
            element = elements.nth(i)
            await element.click()

            title_element = await self.page.wait_for_selector(INTER_SELECTORS["title"])

            origem = "Inter"
            titulo_vaga = await title_element.text_content()
            descricao_vaga = await self._extract_items_from_third_ul()       
            url_vaga = self.page.url

            jobs_list = formatters.insert_jobs_list(jobs_list, origem, titulo_vaga, str(descricao_vaga), url_vaga)

            # Volta à página de resultados e aplica os filtros novamente
            await self.page.go_back()
            await self._click_job_filters()
            await self.page.wait_for_selector(INTER_SELECTORS["vacancy_title"])

        await self.page.close()
        return jobs_list

