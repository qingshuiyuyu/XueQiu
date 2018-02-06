# -*- coding: utf-8 -*-
import scrapy
import json
from XueQiu.items import XueqiuItem

class DiscoverSpider(scrapy.Spider):
    name = 'discover'
    allowed_domains = ['xueqiu.com']
    start_urls = ['https://www.xueqiu.com/']

    def parse(self, response):

        url = "https://xueqiu.com/cubes/discover/rank/cube/list.json?category=14&page=1&count=20"

        yield scrapy.Request(
            url=url,
            callback=self.parse_list
        )

    def parse_list(self,response):

        data = json.loads(response.body)

        infos = data.get("list")

        for info in infos:

            items = XueqiuItem()

            items["name"] = info.get("name")
            items["market"] = info.get("market")
            items["tags"] = '-'.join(info.get("tag"))
            items["description"] = info.get("description")
            items["income"] = info.get("total_gain")
            items["invesor"] = info.get("owner").get("screen_name")
            items["concernNum"] = info.get("follower_count")

            yield items




