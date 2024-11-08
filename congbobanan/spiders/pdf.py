import scrapy
from pathlib import Path


class ToaanSpider(scrapy.Spider):
    name = "pdf"
    allowed_domains = ["congbobanan.toaan.gov.vn"]

    def start_requests(self):
        with open("banan.txt") as f:
            urls = f.read().splitlines()
        for url in urls:
            yield scrapy.Request(url, callback=self.parse, errback=self.errback_httpbin)

    custom_settings = {
        "CONCURRENT_REQUESTS": 128,
        "CONCURRENT_REQUESTS_PER_DOMAIN": 128,
        "CONCURRENT_REQUESTS_PER_IP": 128,
        "LOG_LEVEL": "INFO",
        # ignore retry
        "RETRY_ENABLED": False,
        "RETRY_TIMES": 0,
        "COOKIES_ENABLED": False,
        # TIME OUT 180
        "DOWNLOAD_TIMEOUT": 180,
    }

    def parse(self, response):
        filename = response.url.split("/")[-2] + ".pdf"
        output_dir = Path("output")
        # Path(filename).write_bytes(response.body)
        output_dir.mkdir(exist_ok=True)
        Path(output_dir / filename).write_bytes(response.body)

    def errback_httpbin(self, failure):
        with open("failed_urls.txt", "a") as f:
            f.write(failure.request.url + "\n")
