from scrapers.inter_scraper import InterScraper
from scrapers.stone_scraper import StoneScraper

async def run_all_scrapers(browser):
    scrapers = []

    page1 = await browser.new_page()
    scrapers.append(InterScraper(page1))

    page2 = await browser.new_page()
    scrapers.append(StoneScraper(page2))

    all_jobs = []
    for scraper in scrapers:
        jobs = await scraper.search_jobs()
        all_jobs.extend(jobs)

    return all_jobs
