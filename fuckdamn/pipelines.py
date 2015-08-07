from scrapy import signals
import json
import codecs

class FuckdamnPipeline(object):

    def __init__(self):
        self.file = codecs.open('sweetheart.json', 'wb', encoding='utf-8')

    def process_item(self, item, spider):
        items=dict(item)
        for key in items:
            items[key]=items[key][0].strip()
        line = json.dumps(items, ensure_ascii=False) + "\n"
        self.file.write(line)
        return item

    def spider_closed(self, spider):
        self.file.close()
