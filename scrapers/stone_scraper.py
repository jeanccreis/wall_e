from .base import BaseScraper
from config.selectors import STONE_SELECTORS
from . import formatters


class StoneScraper(BaseScraper):
    async def search_jobs(self):
        await self.page.goto("https://jornada.stone.com.br/times/tecnologia?page=1#top")

        elements = self.page.locator(STONE_SELECTORS["engenharia_title"])

        element_with_text = elements.filter(has_text="Engenharia")

        first_element = element_with_text.first
        await first_element.click()

        await self.page.wait_for_selector(STONE_SELECTORS['vacancy_title'])

        buttons = self.page.locator(STONE_SELECTORS['link_list']).filter(has_text=STONE_SELECTORS['btn_vaga_detalhe'])
        count = await buttons.count()

        jobs_list = []

        for i in range(count):
            await buttons.nth(i).click()
            title = await self.page.locator(STONE_SELECTORS['title_page']).inner_text()
            url_vaga = self.page.url
            descricao_vaga = 'test'

            jobs_list = formatters.insert_jobs_list(jobs_list, 'Stone', title, str(descricao_vaga), url_vaga)
            await self.page.go_back()
        
        await self.page.close()
        return jobs_list
