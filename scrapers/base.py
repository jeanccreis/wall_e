# base_job_scraper.py
from abc import ABC, abstractmethod

class BaseScraper(ABC):
    def __init__(self, page):
        self.page = page

    @abstractmethod
    async def search_jobs(self):
        pass
