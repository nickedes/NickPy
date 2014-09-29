from bs4 import BeautifulSoup
import requests
import os
import json

import decimal
def decimal_default(obj):
    if isinstance(obj, decimal.Decimal):
        return float(obj)
    raise TypeError

def get_quotes():
        count =0
        with open('quotes.json','w') as f1:
                
                for count in range(10):
                        url="https://www.goodreads.com/quotes/list/33276343?page="+str(count+1)
                        r = requests.get(url)
                        data = r.text
                        post = os.path.join('','quotes'+".json")
                        soup = BeautifulSoup(data)
                        results = soup.findAll('div', attrs={'class':'quoteText'})
                        for r in results:
                                with open(post, 'a') as f:
                                        x = r.findAll(text=True)
                                        json.dump(x, f, indent=1, default=decimal_default)   


get_quotes()
