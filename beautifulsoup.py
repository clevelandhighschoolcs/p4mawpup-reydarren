#
# BeautifulSoup Example For Web Scraping
#

# import libraries
import urllib2
from bs4 import BeautifulSoup
import time 
from twilio.rest import Client

account_sid = #Put Account Sid here.
auth_token = #Put Auth Token Here
twilio_phone_number = #Put Twilio phone number here
my_phone_number = #

# add prompt for frequency 
print("how often would you like this to run in seconds?")
frequency = raw_input("+" "frequency")

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
       body = "There has been a change!"
		client = Client(account_sid, auth_token)
		client.messages.create(
			body=body,
			to=my_phone_number,
			from_=twilio_phone_number
		)
        break
    time.sleep(frequency)# offer parameters 
    
    
 
 
 

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
