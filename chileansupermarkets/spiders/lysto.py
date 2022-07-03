from datetime import date

import scrapy
from scrapy import Request

def page_link(link: str):
    return f"https://www.lysto.cl{link}"

def clean_price(price: str):
    return price.replace("$","").replace(".","")


class Lysto(scrapy.Spider):
    name = "lysto"
    start_urls = [
        "https://www.lysto.cl/t/supermercado/",
    ]

    def parse(self, response):
        product_div = response.css(
            "div.container-fluid.mb-3.d-md-flex.justify-content-center"
        )
        product_container = product_div.css("div.col-md-12.col-lg-9")
        product_list = product_container.css("div.row")
        products = product_list.css("div.row-flex")
        for product in products:
            url = page_link(product.css("a.d-flex.flex-column.justify-content-between::attr(href)").get())
            yield Request(url,callback=self.parse_page,meta={'url':url})
        pagination = response.css("div.plp-pagination.d-none.d-lg-flex")
        next_page_button = pagination.css("li.next_page.page-item")
        try:
            next_page_link = page_link(
                next_page_button.css("a.page-link::attr(href)").get()
            )
            yield response.follow(next_page_link, callback=self.parse)
        except:
            pass

    def parse_page(self, response):
        url = response.meta.get('url')
        yield {
            "name": response.css("h1.mt-3.mt-md-0.text-center.text-md-left.product-details-title::text").get().strip(),
            "sku": response.css("div.text-center.text-md-left.add-to-cart-form-general-availability.variant-sku.text-uppercase::text").get().strip(),
            "url": url,
            "price": clean_price(response.css("span.price.selling::text").get().strip()),
            "brand": response.css("span.text-break::text").getall()[1].strip(),
            "date": str(date.today()),
        }