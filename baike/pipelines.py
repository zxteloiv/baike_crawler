# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
import os

class BaikePipeline(object):
    def __init__(self, savedir):
        self.savedir = savedir

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
                savedir=crawler.settings.get("BAIKE_HTML_SAVE_DIR", default=".")
                )

    def process_item(self, item, spider):
        filename = os.path.join(self.savedir, item['itemid'])

        meta = {'itemid':item['itemid'], 'itemtype':item['itemtype'],
                'url':item['url'], 'anchor':item['anchor']}

        with open(filename, 'wb') as f:
            f.write(json.dumps(meta) + "\n")
            f.write(item['body'])
            f.close()

