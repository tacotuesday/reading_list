# coding: utf-8
# Web scraping Zillow

# import request module
import requests
from bs4 import BeautifulSoup as Soup


header = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) '
                        'AppleWebKit/537.36 (KHTML, like Gecko) '
                        'Chrome/83.0.4103.97 Safari/537.36',
          'referer':'https://www.zillow.com/homes/for_sale/california,-md_rb/?searchQueryState=%7B%22pagination'
}

# Enter Zillow URL for the city of your preference
url = 'https://www.zillow.com/homes/for_sale/california,-md_rb'
html = requests.get(url=url,headers=header)
html.status_code
bsobj = Soup(html.content, 'lxml') #bsobj - Beautiful Soup Object
bsobj

# price list is a list variable that will contain

# the price information.
price_list = []

# loop through the price section of the data and extract

# the text and store it in the list.
for price in bsobj.findAll('div',{'class':'list-card-heading'}):
    print('price is: ',price.text.replace( 'bd','b|' ).replace('|s','|' ).replace('io','io|').strip().split('|')[:-1])
    price_list.append(price.text.replace('bd','b|').replace('|s','|').replace('o','o|').strip().split('|')[:-1])
print(price_list)

# address list is a list variable that will

# contain the address information.
address = []


# loop through the address section of the data

# and extract the text and store it in the list.
for adr in bsobj.findAll('div',{'class':'list-card-info'}):
    address.append(adr.a.text.strip())
    print(address)

import pandas as pd

# create a pandas data-frame to store the address

# and price information.
df = pd.DataFrame( price_list,columns = ['Price1','Price2','Price3','Price4'] )
df['Address'] = address

print(df)