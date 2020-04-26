from bs4 import BeautifulSoup
import requests as requests
import pandas as pd

#URL = 'https://www.sec.gov/Archives/edgar/data/882835/000088283518000017/a180420q1earningsrelease.htm'

URL = 'https://en.wikipedia.org/wiki/List_of_largest_manufacturing_companies_by_revenue'

response = requests.get(URL)
soup = BeautifulSoup(response.text, 'html.parser')

#print(soup)

table = soup.find('table', {'class':'wikitable sortable plainrowheads'}).tbody

print(table)
