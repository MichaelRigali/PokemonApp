import requests
from bs4 import BeautifulSoup
import pandas as pd

searchterm = 'pokemon+first+edition+holo'

def get_data(searchterm):
    url = f'https://www.ebay.com/sch/i.html?_from=R40&_nkw={searchterm}&_sacat=0&LH_TitleDesc=0&LH_Auction=1&LH_PrefLoc=1&LH_Complete=1&LH_Sold=1&Graded=Yes&Language=English&Grade=10&rt=nc&Game=Pok%25C3%25A9mon%2520TCG&_dcat=183454'
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    return soup

def parse(soup):
    productslist = []
    results = soup.find_all('div', {'class': 's-item__info clearfix'})
    for item in results[2:]:
        product = {
            'title': item.find('span', {'role': 'heading'}).text,
            'price': item.find('span', {'class': 's-item__price'}).text.strip('$').replace(",", "")
        }
        if '10' in item.find('span', {'role': 'heading'}).text:
            productslist.append(product)
    return productslist

def output(productslist, searchterm):
    productsdf =  pd.DataFrame(productslist)
    productsdf.sort_values("price", axis=0, ascending=True,inplace=True, na_position='first')
    productsdf.to_csv(searchterm + 'output.csv', index=False)
    print('Saved to CSV')
    return

soup = get_data(searchterm)
productslist = parse(soup)
output(productslist, searchterm)