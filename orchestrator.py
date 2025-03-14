import logging
from scrapers.inter_scraper import InterScraper
from scrapers.stone_scraper import StoneScraper

# Configuração básica do logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def run_all_scrapers(browser):
    scrapers = []

    page1 = await browser.new_page()
    scrapers.append(InterScraper(page1))

    page2 = await browser.new_page()
    scrapers.append(StoneScraper(page2))

    all_jobs = []
    for scraper in scrapers:
        logger.info(f"Iniciando o scraper: {scraper.__class__.__name__}")
        jobs = await scraper.search_jobs()
        all_jobs.extend(jobs)
        logger.info(f"{len(jobs)} vagas encontradas no {scraper.__class__.__name__}")
    
    logger.info(f"Total de vagas encontradas: {len(all_jobs)}")
    return all_jobs
