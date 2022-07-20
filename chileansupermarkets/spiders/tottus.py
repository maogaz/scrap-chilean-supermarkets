from datetime import date
import scrapy
import json
import base64
#from scrapy import Request
from scrapy_splash import SplashRequest

class Tottus(scrapy.Spider):
    name = "tottus"

    def start_requests(self):
        url = "https://www.santaisabel.cl/despensa"
        #url = "https://www.lider.cl/supermercado/category/"
        #yield SplashRequest(url=url, callback=self.parse, args={'wait': 2})
        #yield scrapy.Request(url=url, callback=self.parse)
        splash_args = {
            'html': 1,
            'png': 1
        }
        yield SplashRequest(url, self.parse, endpoint='render.json', args=splash_args)

    def parse(self, response):
        imgdata = base64.b64decode(response.data['png'])
        filename = 'some_image.png'
        with open(filename, 'wb') as f:
            f.write(imgdata)
        product_list = response.css("div.pre-header-container").getall()
        yield {
            "response": response.body,
            "response2": product_list,
        }