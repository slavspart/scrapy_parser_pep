import scrapy
from tqdm import tqdm

from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    STATUS_SELECTOR = '//dt[contains(., "Status")]/following::dd/abbr/text()'
    name = "pep"
    allowed_domains = ["peps.python.org"]
    start_urls = ['https://peps.python.org/', ]

    def parse(self, response):
        """Collect links and parse information"""
        """about number and name PEP for each PEP"""
        for row in tqdm(response.css('table.pep-zero-table>tbody>tr')):
            # getting all rows from tables with class pep-zero...
            item = PepParseItem()
            item['number'] = int(row.css('a::text')[0].get())
            item['name'] = row.css('a::text')[1].get()
            pep_link = row.css('a')[0]

            yield response.follow(
                pep_link,
                callback=self.parse_pep,
                meta={
                    'number': item['number'],
                    'name': item['name'],
                }
            )

    def parse_pep(self, response):
        """Collect status and return PepParseItem"""
        data = {
            'number': response.meta.get('number'),
            'name': response.meta.get('name'),
            'status': response.xpath(self.STATUS_SELECTOR)[0].get()
        }
        yield PepParseItem(data)
