import scrapy
from ..items import TargetproductItem

class TargetProductSpider(scrapy.Spider):
    name = 'target_spider'
    allowed_domains = ['www.target.com']
    start_urls = ['https://www.target.com/p/toddler-girls-shanel-fisherman-sandals-cat-jack/-/A-81204099?preselect=80859208']

    def parse(self, response):
        #Extract data using css selectors
        items = TargetproductItem()
        title = response.css('.h-margin-b-tiny.h-text-bold span::text')[0].extract()
        # price = response.css('.ceEMdT::text').extract()
        url = response.request.url
        price = '0'
        all_spec = response.xpath('//*[@id="specAndDescript"]')
        currency = 'USD'
        tcin = all_spec.xpath('//div/b[contains(text(),"TCIN")]/following-sibling::text()')[1].extract()
        upc = all_spec.xpath('//div/b[contains(text(),"UPC")]/following-sibling::text()')[1].extract()
        desc = all_spec.css('.h-margin-v-default::text')[0].extract()
        sizing = all_spec.xpath('//div/b[contains(text(),"Sizing")]/following-sibling::text()')[0].extract()
        care = all_spec.xpath('//div/b[contains(text(),"Care and Cleaning")]/following-sibling::text()')[0].extract()
        lining = all_spec.xpath('//div/b[contains(text(),"Lining Material")]/following-sibling::text()')[0].extract()
        insole = all_spec.xpath('//div/b[contains(text(),"Insole Material")]/following-sibling::text()')[0].extract()
        features = all_spec.xpath('//div/b[contains(text(),"Features")]/following-sibling::text()')[0].extract()
        upper = all_spec.xpath('//div/b[contains(text(),"Upper Shoe Material")]/following-sibling::text()')[0].extract()
        sole = all_spec.xpath('//div/b[contains(text(),"Sole Material")]/following-sibling::text()')[0].extract()
        heel = all_spec.xpath('//div/b[contains(text(),"Heel")]/following-sibling::text()')[0].extract()
        shoewidth = all_spec.xpath('//div/b[contains(text(),"Shoe Width")]/following-sibling::text()')[0].extract()
        footwear = all_spec.xpath('//div/b[contains(text(),"Footwear outsole details")]/following-sibling::text()')[0].extract()
        items['url'] = url
        items['tcin'] = tcin.strip()
        items['upc'] = upc.strip()
        items['price'] = price.strip()
        items['currency'] = currency
        items['title'] = title.strip()
        items['description'] = desc.strip()
        items['specs'] = {"Sizing": sizing.strip(), "Care and Cleaning": care.strip(), "Lining Material": lining.strip(), "Insole Material": insole.strip(), "Features": features.strip(), "Upper Shoe Material": upper.strip(), "Sole Material": sole.strip(), "Heel": heel.strip(), "Shoe Width": shoewidth.strip(), "Footwear outsole details": footwear.strip()}
        yield items