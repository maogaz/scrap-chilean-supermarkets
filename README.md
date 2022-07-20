# Chilean Supermarket Web Scraping/Supermercados chilenos Web Scraping 🚀

This repository has the purpose of extract every product of the principal supermarkets in Chile. The supermarkets in this code are:

* Lider: https://www.lider.cl/supermercado/ ✅
* Jumbo: https://www.jumbo.cl/ 🛠
* Tottus: https://www.tottus.cl/ ⛔
* Unimarc: https://www.unimarc.cl/ ⛔
* Santa Isabel: https://www.santaisabel.cl/ ⛔
* A Cuenta: https://www.acuenta.cl/ ⛔
* Lysto: https://www.lysto.cl/ ✅


## Run the project:

To use this repo, you need first to install the libraries in the requeriments.txt. To do this you can use:

```
pip install -r requirements.txt
```

sources: [source 1](https://santandertrade.com/es/portal/analizar-mercados/chile/distribuir-un-producto) and [source 2](https://marketing4ecommerce.cl/top-los-supermercados-online-mas-populares-en-chile/)

Don't forget to activate your [virtual environment](https://uoa-eresearch.github.io/eresearch-cookbook/recipe/2014/11/26/python-virtual-env/) to work with this code:


- Mac/Linux:
```source venv/bin/activate ```

- Windows: 
```venv\Scripts\activate```

To create the virtual environment

```virtualenv venv```

Also you may need work with [docker](https://www.youtube.com/watch?v=CV_Uf3Dq-EU&ab_channel=PeladoNerd) to use [Splash](https://github.com/scrapinghub/splash) to use the [Scrapy-Splash](https://github.com/scrapy-plugins/scrapy-splash/tree/f5273b3a0ef15a9f6809d305a1dbe8f3efd12c5f) library. To do so, you need to run:

```docker run -p 8050:8050 scrapinghub/splash```

To work on port 8050. 