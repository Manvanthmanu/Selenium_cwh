from bs4 import BeautifulSoup
import os
import pandas as pd

d= {'title':[], 'price':[],'link':[]}

for file in os.listdir('data'):
    try:

        with open(f'data/{file}') as f:
            html_doc = f.read()
        soup= BeautifulSoup(html_doc, 'html.parser')

        t= soup.find("h2")
        title = t.get_text()

        l = t.find("a")
        link = "https://www.amazon.de/" +l['href']

        price = soup.find('span',attrs={'class':'a-price-whole'}).get_text()
        d['title'].append(title)
        d['price'].append(price)
        d['link'].append(link)


        print(title , link , price)

    except Exception as e:
        print(e)


    # print(soup.prettify())

df = pd.DataFrame.from_dict(data=d)

df.to_csv('data.csv')