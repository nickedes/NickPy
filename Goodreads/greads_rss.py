import feedparser
from random import randint

#give link of the rss feed of the user's liked quotes
url = "https://www.goodreads.com/quotes/list_rss/33276343-nikhil"
d = feedparser.parse(url)

x = randint(0,len(d['entries'])) #Inclusive

#prints all d quotes liked by user
#for count in range(len(d['entries'])):
#        print d.entries[count].description

#prints a random quote from the user's liked quotes
print  d.entries[x].description                       
                        
