import scrapy

class BHPhoto(scrapy.Spider):
    name = "bhbodies"  # Spider identifier for the project used for cmd line
    start_urls = ['https://www.bhphotovideo.com/c/search?ci=14876&fct=fct_bodies-kits_4016%7cbody-only&N=4232860786',
                  'https://www.bhphotovideo.com/c/search?ci=6222&fct=fct_brand_name%7ccanon%2bfct_bodies-kits_4016%7cbody-only&N=4288586280&',
                  'https://www.bhphotovideo.com/c/search?ci=16158&fct=fct_brand_name%7csony%2bfct_bodies-kits_4023%7cbody-only&N=4288586281&',
                  'https://www.bhphotovideo.com/c/search?ci=16158&fct=fct_bodies-kits_4023%7cbody-only%2bfct_brand_name%7cpanasonic&N=4288586281&']
    def parse(self, response):
        for item in response.css('div.items.full-width.list-view.elevn.c2 > div'):
            name_list = item.css('h3.bold.fourteen a span::text').extract()
            url = item.css('a.itemImg img::attr(src)').extract_first()
            price_list = item.css('span.price.bold.sixteen.c7::text').re('\S')

            if url != "" and name_list is not None and len(price_list) != 0:
                # Build JSON return output
                yield {
                    'itemName' : ' '.join(name_list),
                    'imageUrl' : url,
                    'price' : float(''.join(price_list).replace("$", "").replace(",", ""))
                }