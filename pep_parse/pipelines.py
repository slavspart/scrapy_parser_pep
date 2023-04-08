import csv
from pep_parse.settings import BASE_DIR
import datetime as dt


class PepParsePipeline:
    """Pipeline for creating status_summary"""

    def __init__(self):
        self.DATETIME_FORMAT = '%Y-%m-%d_%H-%M-%S'
        self.statuses = {}
        self.dup = []
        self.results_dir = BASE_DIR / 'results'

    def open_spider(self, spider):
        self.results_dir.mkdir(exist_ok=True)

    def process_item(self, item, spider):
        if item['status'] not in self.statuses.keys():
            self.statuses[item['status']] = 1
        else:
            self.statuses[item['status']] += 1
        return item

    def close_spider(self, spider):
        now = dt.datetime.now()
        now_formatted = now.strftime(self.DATETIME_FORMAT)
        file_name = f'status_summary_{now_formatted}.csv'
        file_path = self.results_dir / file_name
        total = 0
        results = []
        for s, q in self.statuses.items():
            results.append((s, q))
            total += q
        results.append(('Total', total))
        with open(file_path, 'w', encoding='utf-8') as f:
            writer = csv.writer(f, dialect='unix')
            writer.writerows(results)
