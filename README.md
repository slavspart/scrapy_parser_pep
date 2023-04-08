# Parser_pep

[Description](#description) /

[Launching](#launching) /

  

  

## Description

[Parser_pep](https://github.com/slavspart/scrapy_parser_pep) is a parser collecting information about Python Enhancement Guidelines (PEP).
It parses number, name and status of each PEP from Python's oficial website  'https://peps.python.org/' and save the data in 2 csv files:
- number, name, status of each PEP
- Summary on quantity of each status and total quantity of PEPs.
 
The project is developped on Scrapy framework basis.


## Launching

Bash

```
git clone git@github.com:slavspart/scrapy_parser_pep.git

pip install -r requirements.txt

cd scrapy_parser_pep/parser_pep

scrapy crawl pep
```

(c) [Svyatoslav Mikhaylov](https://github.com/slavspart)