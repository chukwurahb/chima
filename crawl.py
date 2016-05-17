__author__ = 'sus'
import requests
from bs4 import BeautifulSoup

def naira_land_spider(max_pages):
    page=1
    while page <= max_pages:
        url='http://www.nairaland.com/'+str(page)
        source_code= requests.get(url)
        plain_text=source_code.text
        soup= BeautifulSoup(plain_text)
        for link in soup.findAll('a',{'rel':'noopener'}):
            href = link.get('href')
            print(href)
        page +=1

naira_land_spider(1)


