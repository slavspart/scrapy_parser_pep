from pathlib import Path


BOT_NAME = "pep_parse"
SPIDER_MODULES = ["pep_parse.spiders"]
NEWSPIDER_MODULE = "pep_parse.spiders"

ROBOTSTXT_OBEY = False  # default True

REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"
FEEDS = {
    # 'pep__%(time)s.csv': {
    'results/pep_%(time)s.csv': {
        'format': 'csv',
        'fields': ['number', 'name', 'status'],
        # Хотел присвоить русские названия колонкам,
        # но pytest не дает это сделать
        # 'fields':
        # {'number': 'Номер', 'name': 'Название', 'status': 'Статус '},
        'overwrite': True
    },
}
ITEM_PIPELINES = {
    'pep_parse.pipelines.PepParsePipeline': 300,
}


LOG_FILE = 'file.log'

BASE_DIR = Path(__file__).parent.parent
