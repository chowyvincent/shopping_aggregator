import scrapy

class BHPhoto(scrapy.Spider):
    name = "bhlenses"  # Spider identifier for the project used for cmd line
    # NIKON
    # start_urls = ['https://www.bhphotovideo.com/c/buy/SLR-Lenses/ci/274/fct/fct_brand_name%7cnikon/N/4288584247']
    # for x in range(2, 7):
    #     link = 'https://www.bhphotovideo.com/c/buy/SLR-Lenses/ci/274/fct/fct_brand_name%7Cnikon/N/4288584247/pn/' + str(x)
    #     start_urls.append(link)
    # CANON
    # start_urls = []
    # start_urls.append('https://www.bhphotovideo.com/c/search?ci=274&fct=fct_brand_name%7ccanon&N=4288584247&')
    # for x in range(2, 5):
    #     link = 'https://www.bhphotovideo.com/c/buy/SLR-Camera-Lenses/ci/274/fct/fct_brand_name%7Ccanon/N/4288584247/pn/' + str(x)
    #     start_urls.append(link)
    #SONY
    # start_urls = []
    # start_urls.append('https://www.bhphotovideo.com/c/search?ci=17912&fct=fct_brand_name%7csony&N=4196380430')
    # for x in range(2, 4):
    #     link = 'https://www.bhphotovideo.com/c/buy/Mirrorless-Camera-Lenses/ci/17912/fct/fct_brand_name%7Csony/N/4196380430/pn/' + str(x)
    #     start_urls.append(link)
    # # PANASONIC
    start_urls = []
    start_urls.append('https://www.bhphotovideo.com/c/search?ci=17912&fct=fct_brand_name%7cpanasonic&N=4196380430')
    start_urls.append('https://www.bhphotovideo.com/c/buy/Mirrorless-Camera-Lenses/ci/17912/fct/fct_brand_name%7Cpanasonic/N/4196380430/pn/2')



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