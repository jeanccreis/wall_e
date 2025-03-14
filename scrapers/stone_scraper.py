from .base import BaseScraper
from config.selectors import STONE_SELECTORS
from utils import formatters

class StoneScraper(BaseScraper):
    async def search_jobs(self):
        await self.page.goto("https://jornada.stone.com.br/times/tecnologia?page=1#top")

        elements = self.page.locator(STONE_SELECTORS["engenharia_title"])

        element_with_text = elements.filter(has_text="Engenharia")

        first_element = element_with_text.first
        await first_element.click()
        await self.page.wait_for_selector(STONE_SELECTORS["vacancy_title"])

        elements = self.page.locator(STONE_SELECTORS["vacancy_title"])
        vacancy_list = await formatters.extrair_textos(elements)

        print("Stone:", "\n", vacancy_list)

        return vacancy_list
