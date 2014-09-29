import requests 
from bs4 import BeautifulSoup
import os
from urllib import urlretrieve
import sys


def getPic(search):
    
    #replace spaces by %20 for searching    
        search = search.replace(" ","%20")
        url = "https://www.google.com/search?site=imghp&tbm=isch&source=hp&biw=1414&bih=709&q="+search+"&oq="+search
        
        folder="/images/"
        
        r = requests.get(url)
                
        data = r.text
        
        soup = BeautifulSoup(data)
        results = soup.findAll("img")
        count = 1
        for r in results :
                #print "%(src)s" % r 
                file_dest = r["src"].split("/")[-1]
                post = os.path.join(folder, str(count) + ".jpg")
                with open(post, 'w') as f:
                        if r["src"].lower().startswith("http"):
                                urllib.urlretrieve(r["src"], path)
                        else:
                                urlretrieve(urlparse.urlunparse(parsed), path)

getpic("f b g")
    
   
                                
   
