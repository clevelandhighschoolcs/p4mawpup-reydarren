#
# BeautifulSoup Example For Web Scraping
#

# import libraries
import urllib2
from bs4 import BeautifulSoup
import time 



# specify the url
quote_page = 'http://www.bloomberg.com/quote/SPX:IND'

# query the website and return the html to the variable 'page'
page = urllib2.urlopen(quote_page)

# parse the html using beautiful soap and store in variable `soup`
soup = BeautifulSoup(page, 'html.parser')


# get the index price
price_box = soup.find('div', attrs={'class':'price'})
price = price_box.text
print price

while True:
    page = urllib2.urlopen(quote_page)
    soup = BeautifulSoup(page, 'html.parser')
    price_box = soup.find('div', attrs={'class':'price'})
    price_new = price_box.text
    print price_new
    if (str(price_new)) == (str(price)):
        print "There has not been a change"
        price = price_new
    else:
        print "There has been a change!"
        break
    time.sleep(5)
    
    
 
 
 

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
