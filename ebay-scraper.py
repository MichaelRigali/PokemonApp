import requests
from bs4 import BeautifulSoup
import pandas as pd
from csv import reader

def getsearches(csvfile):
    searches = []
    with open(csvfile, 'r') as f:
        csv_reader = reader(f)
        for row in csv_reader:
            searches.append(row[0])
    return searches

def get_data(searchterm):
    url = f'https://www.ebay.com/sch/i.html?_from=R40&_nkw={searchterm}&_sacat=0&LH_TitleDesc=0&LH_Auction=1&LH_PrefLoc=1&LH_Complete=1&LH_Sold=1&Graded=Yes&Language=English&Grade=10&rt=nc&Game=Pok%25C3%25A9mon%2520TCG&_dcat=183454'
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    return soup

def parse(soup):
    productslist = []
    results = soup.find_all('div', {'class': 's-item__info clearfix'})
    for item in results:
        product = {
            'title': item.find('span', {'role': 'heading'}).text,
            'price': item.find('span', {'class': 's-item__price'}).text.strip('$').replace(",", "")
        }
        productslist.append(product)
    return productslist

def output(productslist, searchterm):
    productsdf =  pd.DataFrame(productslist)
    productsdf.sort_values("price", axis=0, ascending=True,inplace=True, na_position='first')
    productsdf.to_csv(searchterm + 'output.csv', index=False)
    print('Saved to CSV')
    return

for searchterm in getsearches('searches.csv'):
    soup = get_data(searchterm)
    productslist = parse(soup)
    output(productslist, searchterm)