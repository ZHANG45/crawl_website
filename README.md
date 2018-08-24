# crawl_website

This is an example to use scrapy and python to crawl information from website https://twitter.com/TexasHumor/status/936415082782822401

## Usage
First you need to install scrapy, you can do it through

    pip install scrapy
    
Second run file, 

    open_quotes.py

This step will create two new files 'quotes.json' and 'Twitter-TexasHumor.html', and you can see the information crawled from the website.

Third, if you want to crawl data from other websites, you can change information

    url_former = 'https://twitter.com/xx/status/'
    data = [936415082782822401]

in file

    tutorial/spiders/quotes_spider.py
