import scrapy

class BHPhoto(scrapy.Spider):
    name = "bhphoto"  # Spider identifier for the project used for cmd line
    start_urls = ['https://www.bhphotovideo.com/c/buy/DSLR-Digital-Cameras/ci/14876/N/4232860786']

    def parse(self, response):
        for item in response.css('div.items.full-width.list-view.elevn.c2 > div'):
            url = item.css('h3.bold.fourteen a::attr(href)').extract_first()
            name_list = item.css('h3.bold.fourteen a span::text').extract()
            price_list = item.css('span.price.bold.sixteen.c7::text').re('\S')

            if url != "" and name_list is not None and len(price_list) != 0:
                # Build JSON return output
                yield {
                    'item' : ' '.join(name_list),
                    'item_url' : url,
                    'price' : ''.join(price_list)
                }