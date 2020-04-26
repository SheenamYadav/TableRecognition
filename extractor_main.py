import sys
from bs4 import BeautifulSoup
from html_table_extractor.extractor import Extractor
import requests as requests
import pandas as pd

#URL = 'https://en.wikipedia.org/wiki/List_of_largest_manufacturing_companies_by_revenue'
URL = 'https://www.sec.gov/Archives/edgar/data/882835/000088283518000017/a180420q1earningsrelease.htm'
response = requests.get(URL)

soup = BeautifulSoup(response.text, 'html.parser')

#table = soup.find('table',{'class':'wikitable sortable plainrowheads'})

tables = soup.findAll(lambda tag: tag.name=='table')

#rows = table.findAll(lambda tag: tag.name=='tr')

#table_div = soup.findAll(lambda tag: tag.name=='div')
#tables = table_div.findAll('table')




#print(len(table_div))
print(tables)


'''
extractor = Extractor(table)
extractor.parse()
print(extractor.return_list())
#print(extractor.parse())

extractor.write_to_csv(path=".")
'''
