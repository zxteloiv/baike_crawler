# coding: utf-8

import re, os
import scrapy
from baike.items import BaikeItem

class BaikeSpider(scrapy.Spider):
    name = "baike"
    allowed_domains = ["baike.baidu.com"]
    start_urls = (
        "http://baike.baidu.com/view/20069.html?fromTaglist",
        "http://baike.baidu.com/view/486340.htm",
        "http://baike.baidu.com/taglist?tag=%BE%B0%B5%E3",
        "http://baike.baidu.com/dili",
        "http://baike.baidu.com/shenghuo",
        "http://baike.baidu.com/wenhua",
        "http://baike.baidu.com/ziran",
        "http://baike.baidu.com/shehui"
    )

    def parse(self, response):
        # save data
        item = self.parse_page(response)
        if item is not None:
            yield item

        # follow links
        for link in response.xpath("//a[@href]"):
            href = link.xpath("@href").extract()[0]
            if not re.match('^http|^/', href):
                continue

            anchor = link.xpath("text()").extract()
            anchor_text = anchor[0].strip() if len(anchor) > 0 else ""

            url = response.urljoin(href)
            if any(x in url for x in ("/view/", '/subview/', 'taglist')):
                meta = {"anchor_text":anchor_text}
                yield scrapy.Request(url, callback=self.parse, meta=meta)

    def is_error(self, response):
        return len(response.body) < 10000 or response.status != 200

    def parse_page(self, response):
        urlparts = response.url.split('/')
        if 'view' in urlparts:
            itemid = re.search('(\d+).htm', urlparts[-1]).group(1) + ".htm"
            itemtype = 'view'
        elif 'subview' in urlparts:
            itemid = "_".join(re.search('(\d+)', x).group(1) for x in urlparts[-2:]) + ".htm"
            itemtype = 'subview'
        else:
            return None

        if self.is_error(response):
            savedir = self.settings.get("BAIKE_HTML_SAVE_DIR", default=".")
            with open(os.path.join(savedir, "log.err"), "a") as f:
                f.write("error\t" + response.url + "\n")
            return None

        item = BaikeItem()

        item['itemid'] = itemid
        item['itemtype'] = itemtype
        item['url'] = response.url
        item['anchor'] = response.meta.get("anchor_text")
        item['body'] = response.body

        return item
        
