
import scrapy
import json
from bigData.items import BigdataItem
class demo(scrapy.Spider):
    name="demo"

    def __init__(self):
        pass

    def start_requests(self):
        url = 'http://www.jscq.com.cn/dsf/gq/jygg/index.html'

        yield scrapy.Request(url=url, dont_filter=True, callback=self.parse)

    def parse(self, response):
        item = BigdataItem()
        res=response.xpath('//table/tr[@style="height:36px;"]')
        lis=[]
        for r in res:
            td=r.xpath("td")
            item["name"]=td[1].xpath('./a/@title').extract_first().strip()
            item["floorPrice"] = td[3].xpath("string(.)").extract_first().strip()
            item["type"] = td[2].xpath("string(.)").extract_first().strip()
            yield item
        # print(item)
        # print(res)

