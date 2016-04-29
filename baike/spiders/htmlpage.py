import scrapy
from baike.items import BaikeItem

class BaikeSpider(scrapy.Spider):
    name = "baike"
    allowed_domains = ["baike.baidu.com"]
    start_urls = (
        "http://baike.baidu.com/view/486340.htm",
        #"http://baike.baidu.com/dili",
        #"http://baike.baidu.com/shenghuo",
        #"http://baike.baidu.com/wenhua",
        #"http://baike.baidu.com/ziran",
        #"http://baike.baidu.com/shehui"
    )

    def parse(self, response):
        # save data
        if not self.is_error(response):
            item = self.parse_page(response)
            if item is not None:
                yield item

        # follow links
        """
        for link in response.xpath("//a[@href]"):
            anchor = link.xpath("text()").extract()[0].strip()
            href = link.xpath("@href").extract()[0]

            if not re.match('^http|^/', href):
                continue

            url = response.urljoin(href)
            meta = {"anchor_text":anchor}
            yield scrapy.Request(url, callback=self.parse, meta=meta)
        """

    def is_error(self, response):
        return len(response.body) < 25000 or response.status != 200

    def parse_page(self, response):
        urlparts = response.url.split('/')
        if 'view' in urlparts:
            itemid = urlparts[-1]
            itemtype = 'view'
        elif 'subview' in urlparts:
            itemid = "_".join(urlparts[-2:])
            itemtype = 'subview'
        else:
            return None

        item = BaikeItem()

        item['itemid'] = itemid
        item['itemtype'] = itemtype
        item['url'] = response.url
        item['anchor'] = response.meta.get("anchor_text")
        item['body'] = response.body

        return item
        
