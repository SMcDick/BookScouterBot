# imported modules
import json
from sys import argv, exit
from json import loads
from urllib.request import urlopen

def checkPrices(isbn):

    # The site has three options: sell, buy, rent
    # After looking at how the page functions:
    url = ("https://api.bookscouter.com/v3/prices/sell/%s" % isbn)

    req = urlopen(url)
    
    # If the request failed, print error and why it failed, then close
    if req.code != 200:
        print("HTTP ERROR:", req.status_code)
        print("REASON:", req.reason)
        exit()
    
    # Continue if the request went through
    data = loads( req.read() )

    # This wiill print the entire dictionary in a readable format
    #print (json.dumps(data, ensure_ascii=False, indent=4, sort_keys=True))

    # The response is a dictionary
    data = data['data']
   
    print(data['Book']['Title'] + "-" + data['Book']['Isbn13'])

    for item in data['Prices']:
        if item['Price'] > 0:
            print(item['Vendor']['Name'] + " " + str(item['Price']))

if __name__=="__main__":

    # Read in the file of ISBN numbers
    with open('isbnList.txt', 'r') as isbnList:
        for isbn in isbnList:
            checkPrices(isbn)

