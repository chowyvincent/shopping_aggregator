import scrapy

class BestBuy(scrapy.Spider):
    name = "bestbuy"  # Spider identifier for the project used for cmd line
    start_urls = ['https://www.bestbuy.com/site/nikon/nikon-digital-slr/pcmcat155400050000.c?id=pcmcat155400050000']

    def parse(self, response):
        for item in response.css('div.list-item'):
            url = item.css('div.sku-title a::attr(href)').extract_first()
            name = item.css('div.sku-title a::text').extract_first()
            price_list = item.css('div.pb-hero-price.pb-purchase-price span::text').extract()

            if url != "" and name != "" and len(price_list) != 0:
                # Build JSON return output
                yield {
                    'item' : name,
                    'item_url' : "https://bestbuy.com" + url,
                    'price' : ''.join(price_list)
                }