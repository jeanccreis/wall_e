import logging
import asyncio
from scrapers.inter_scraper import InterScraper
from scrapers.stone_scraper import StoneScraper


# Configuração básica do logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def run_all_scrapers(browser):
    page1 = await browser.new_page()
    page2 = await browser.new_page()

    inter_scraper = InterScraper(page1)
    stone_scraper = StoneScraper(page2)

    logger.info("Iniciando scrapers simultaneamente...")

    tasks = [inter_scraper.search_jobs(), stone_scraper.search_jobs()]
    results = await asyncio.gather(*tasks)

    print(results)

    inter_jobs = results[0]
    stone_jobs = results[1]

    all_jobs = inter_jobs + stone_jobs

    logger.info(f"{len(inter_jobs)} vagas encontradas no InterScraper")
    logger.info(f"{len(stone_jobs)} vagas encontradas no StoneScraper")
    logger.info(f"Total de vagas encontradas: {len(all_jobs)}")

    return all_jobs
