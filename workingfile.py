import requests
from bs4 import BeautifulSoup
import pandas as pd

def main():
    searchterm = 'pokemon+first+edition+holo'
    url = f'https://www.ebay.com/sch/i.html?_from=R40&_nkw={searchterm}&_sacat=0&LH_TitleDesc=0&LH_Auction=1&LH_PrefLoc=1&LH_Complete=1&LH_Sold=1&Graded=Yes&Language=English&Grade=10&rt=nc&Game=Pok%25C3%25A9mon%2520TCG&_dcat=183454'
    soup = get_data(url)
    products = parse(soup)
    export(products)

def get_data(url):
    r = requests.get(url)
    if r.status_code != 200:
        print('Failed to get data: ', r.status_code)
    else:
        soup = BeautifulSoup(r.text, 'html.parser')
        print(soup.title.text)
    return soup

def parse(soup):
    productlist = []
    results = soup.find_all('div', {'class': 's-item__info clearfix'})
    for item in results:
        products = {
            'title': item.find('span', {'role': 'heading'}).text,
            'price': item.find('span', {'class': 's-item__price'}).text.strip('$').replace(",", "")
        }
        productlist.append(products)
        #print(products)
    return productlist

def loadup(productlist):
    return

def export(productlist):
    productsdf = pd.DataFrame(productlist)
    productsdf.sort_values("price", axis=0, ascending=True,inplace=True, na_position='first')
    productsdf.to_csv('testoutput.csv', index=False)
    print('Saved to CSV')
    return


if __name__ == '__main__':
    main()
