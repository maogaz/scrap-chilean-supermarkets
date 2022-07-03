from datetime import date
import scrapy
from scrapy import Request


def extract_current_page_number(link: str):
    head, sep, page_number = link.partition("page=")
    try:
        return int(page_number)
    except:
        pass

def get_next_link(page_number: int):
    try:
        return f"https://www.jumbo.cl/despensa?page={page_number}"
    except:
        return ""


class Jumbo(scrapy.Spider):
    name = "jumbo"
    start_urls = [
        "https://www.jumbo.cl/despensa?page=1",
    ]

    def parse(self, response):
        shelf = response.css("div.shelf-wrapper")
        products = shelf.css("div.shelf-product-island")
        yield {"products": response}
        for product in products:
            url = product.css("a.shelf-product-title::attr(href)").get()
            #yield {"url": f"https://www.jumbo.cl{page}"}
            yield Request(url,callback=self.parse_page,meta={'url':url})
        try:
            next_page_link = get_next_link(
                extract_current_page_number(response.url) + 1
            )
            #yield response.follow(next_page_link, callback=self.parse)
        except TypeError:
            pass

    def parse_page(self, response):
        url = response.meta.get('url')
        shelf = response.css("div.product-info-wrapper")
        yield {
            "response": response,
            "sku": shelf.css("span.product-code::text").getall()[1],
            "name": shelf.css("h1.product-name::text").get(),
            "price": shelf.css("span.product-sigle-price-wrapper::text").get(),
            "extraction_date": str(date.today()),
            "url": url,
        }