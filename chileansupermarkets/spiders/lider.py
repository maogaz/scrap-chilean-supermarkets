from datetime import date
import scrapy


def return_lider_product_url(params: str) -> str:
    return f"https://www.lider.cl/supermercado/product{params}"


def return_lider_page(params: str) -> str:
    return f"https://www.lider.cl{params}"


def clean_id(product_id: str) -> str:
    clean_left = product_id.replace("(Ref: ", "")
    clean_right = clean_left.replace(")", "")
    return clean_right


class Lider(scrapy.Spider):
    name = "lider"
    start_urls = ["https://www.lider.cl/supermercado/category/"]

    def parse(self, response):
        product_list = response.css("div.grid-of-five.clearfix.box-products-list")
        for products in product_list:
            for product in products.css("div.box-product"):
                price = product.css("span.price-sell")
                brand = product.css("span.product-name::text").get()
                product_name = product.css(
                    "span.product-description.js-ellipsis::text"
                ).get()
                yield {
                    "name": product_name,
                    "sku": clean_id(
                        product.css("span.reference-code::text").get()
                    ),
                    "url": return_lider_product_url(
                        product.css("a.product-link::attr(href)").get()
                    ),
                    "price": price.css("b::text").get(),
                    "brand": brand,
                    "date": str(date.today()),
                }

        pagination_list = response.css("div.box-pagination.clearfix.hidden-xs")
        pages = []
        for pagination in pagination_list:
            page = pagination.css("a::attr(href)").getall()
            for i in page:
                pages.append(i)
        if len(pages) > 0:
            next_page = return_lider_page(pages[-1])
            try:
                yield response.follow(next_page, callback=self.parse)
            except TypeError:
                pass
