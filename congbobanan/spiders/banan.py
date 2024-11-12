import scrapy
from pathlib import Path


class ToaanSpider(scrapy.Spider):
    name = "banan"
    allowed_domains = ["congbobanan.toaan.gov.vn"]
    start_urls = [
        "https://congbobanan.toaan.gov.vn/2ta{}t1cvn/chi-tiet-ban-an".format(i)
        for i in range(1678910, 1, -1)
    ]

    custom_settings = {
        "FEED_FORMAT": "jsonlines",
        "FEED_URI": "output.jsonl",
        "CONCURRENT_REQUESTS": 256,
        "CONCURRENT_REQUESTS_PER_DOMAIN": 256,
        "CONCURRENT_REQUESTS_PER_IP": 256,
        "LOG_LEVEL": "INFO",
        # ignore retry
        "RETRY_ENABLED": False,
        "RETRY_TIMES": 0,
        "COOKIES_ENABLED": False,
        "JOBDIR": "jobdir",
    }

    def parse(self, response):
        title = response.css("title::text").get()
        if not title or title.strip() == "null":
            return
        item = {
            "url": response.url,
        }
        item_type = response.css(
            "#aspnetForm > section > div > div > div > div.col-xs-12.col-sm-5.col-md-4.col-lg-4 > div.search_left_pub.details_pub  > div > div > strong > label::text"
        ).get()
        if item_type == "Bản án số: ":
            item["type"] = "banan"
        if item_type == "Quyết định số: ":
            item["type"] = "quyetdinh"

        item_number, item_date = response.css(
            "#aspnetForm > section > div > div > div > div.col-xs-12.col-sm-5.col-md-4.col-lg-4 > div.search_left_pub.details_pub > div > div > strong > span::text"
        ).extract()

        item["id"] = item_number
        item["date"] = item_date

        item_table = response.css(".list-group-item")
        for row in item_table:
            key = row.css("label::text").get()
            value = row.css("span::text").get()
            if key and value:
                item[key] = value

        # pdf_url = response.url.replace("2ta", "5ta")
        # if "Loại án:" in item and item["Loại án:"].lower() == "hình sự":
        #     yield scrapy.Request(pdf_url, callback=self.parse_pdf)

        yield item

    def parse_pdf(self, response):
        filename = response.url.split("/")[-2] + ".pdf"
        output_dir = Path("output")
        # Path(filename).write_bytes(response.body)
        output_dir.mkdir(exist_ok=True)
        Path(output_dir / filename).write_bytes(response.body)

    def errback_httpbin(self, failure):
        with open("failed_urls.txt", "a") as f:
            f.write(failure.request.url + "\n")

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, callback=self.parse, errback=self.errback_httpbin)
