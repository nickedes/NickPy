import urllib 
import mechanize 
from bs4 import BeautifulSoup
from urlparse import urlparse
import hashlib

def getPic(search):
    
    #replace spaces by %20 for searching    
    search = search.replace(" ","%20")
    try:
        browser = mechanize.Browser()
        browser.set_handle_robots(False)
        browser.addheaders = [('User-agent','Mozilla')]

        htmltext = browser.open("https://www.google.com/search?site=imghp&tbm=isch&source=hp&biw=1414&bih=709&q="+search+"&oq="+search)
        img_urls = []
        formatted_images = []
        soup = BeautifulSoup(htmltext)
        results = soup.findAll("a")
        for r in results:
            try:
                if "imgres?imgurl" in r['href']:
                    img_urls.append(r['href'])
            except:
                a=0
        for im in img_urls:
            refer_url = urlparse(str(im))
            image_f = refer_url.query.split("&")[0].replace("imgurl=","")
            formatted_images.append(image_f)
        
        return  formatted_images

    except:
        print "error"


print getPic("cars and music")   
