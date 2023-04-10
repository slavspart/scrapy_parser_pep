import csv

import datetime as dt

from pep_parse.settings import BASE_DIR, DATETIME_FORMAT


class PepParsePipeline:
    """Pipeline for creating status_summary"""
    def __init__(self):
        self.RESULTS_DIR = BASE_DIR / 'results'
        self.FILE_NAME = 'status_summary_{}.csv'.format(
            dt.datetime.now().strftime(DATETIME_FORMAT))
        self.FILE_PATH = self.RESULTS_DIR / self.FILE_NAME
        self.statuses = {}
        self.dup = []

    def open_spider(self, spider):
        self.RESULTS_DIR.mkdir(exist_ok=True)

    def process_item(self, item, spider):
        if item['status'] not in self.statuses.keys():
            self.statuses[item['status']] = 1
        else:
            self.statuses[item['status']] += 1
        return item

    def close_spider(self, spider):
        total = 0
        results = []
        for s, q in self.statuses.items():
            results.append((s, q))
            total += q
        results.append(('Total', total))
        with open(self.FILE_PATH, 'w', encoding='utf-8') as f:
            writer = csv.writer(f, dialect='unix')
            writer.writerows(results)
