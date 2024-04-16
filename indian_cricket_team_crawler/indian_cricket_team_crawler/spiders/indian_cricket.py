from scrapy.spiders import Rule, CrawlSpider
from scrapy.linkextractors import LinkExtractor
from pathlib import Path
import scrapy


class IndianCricketSpider(scrapy.Spider):
    name = "indian_cricket"
    allowed_domains = ["en.wikipedia.org"]
    custom_settings = {
        'DEPTH_LIMIT': 3,
        'MAX_PAGES': 300
    }

    def __init__(self, *args, **kwargs):
        super(IndianCricketSpider, self).__init__(*args, **kwargs)
        self.page_count = 0

    def start_requests(self):
        start_urls = ["https://en.wikipedia.org/wiki/India_national_cricket_team"]
        for url in start_urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        if self.page_count >= self.custom_settings.get('MAX_PAGES'):
            self.logger.info(f"Reached maximum pages limit ({self.custom_settings.get('MAX_PAGES')}). Stopping crawl.")
            return
        details = response.css("div.mw-content-ltr")
        page = response.url.split("/")[-1]
        dir = "C:/Users/swast/Desktop/MyProjects/python/Web_Crawler/indian_cricket_team_crawler/webpages"
        filename = f"webpage-{page}.html"
        file_path = Path(f'{dir}/{filename}')
        file_path.write_bytes(response.body)

        self.page_count += 1

        self.log(f"----------------------{response.url}----------------------")
        yield {
            # "content": "".join(list(filter(lambda x : x != "\n", details.css("div.mw-content-ltr p::text").getall()))),
            "title": response.css("span.mw-page-title-main::text").get(),
            "content": "".join(details.css("p::text").getall()).replace("\n", ""),
            "link": response.url,
            "filename": filename
        }
        for link in response.css("div.mw-content-ltr p a::attr(href)").extract()[:10]:
            if link.startswith("/wiki/") and ':' not in link:
                nextPage = response.urljoin(link)
                yield scrapy.Request(nextPage, callback=self.parse)