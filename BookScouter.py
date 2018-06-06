# imported modules
import json
from time import sleep
from sys import argv, exit
from json import loads
from urllib.request import urlopen
from urllib.error import URLError
from book import Book

buyers = {}

def checkPrices(isbn):

    # The site has three options: sell, buy, rent
    # After looking at how the page functions:
    url = ("https://api.bookscouter.com/v3/prices/sell/%s" % isbn)

    try:
        req = urlopen(url)
    
        # Continue if the request went through
        data = loads( req.read() )
    
        # This will print the entire dictionary in a readable format
        #print (json.dumps(data, ensure_ascii=False, indent=4, sort_keys=True))
    
        # The response is a dictionary
        data = data['data']
    
        # If the search doesn't find any results the Book field will be null.
        if data['Book'] is not None:
    
            # The results are always in decedning order of price so if the first isn't great than 0 none of them will be.
            if data['Prices'][0]['Price'] > 0:
            
                #print('---------------------------------') 
                #print(data['Book']['Title'] + "-" + data['Book']['Isbn13'])
    
                for item in data['Prices']:

                    if item['Price'] > 0:
                        #print(item['Vendor']['Name'] + " " + str(item['Price']))
                        
                        # Generate a book object to hold all the necessary information.
                        book = Book(data['Book']['Isbn13'], data['Book']['Title'], item['Price'])
                        
                        # If this is a new vendor then add them to the dictionary. Otherwise just append the book to the list.
                        if (item['Vendor']['Name'] in buyers): 
                            buyers[item['Vendor']['Name']].append(book)
                        else:
                            buyers[item['Vendor']['Name']] = []
                            buyers[item['Vendor']['Name']].append(book)

    # If there is an error print the URL, show error code and reason. 
    except URLError as e:
        print("This URL failed:", url)
        print("HTTP ERROR:", e.code)
        print("REASON:", e.reason)
        return

if __name__=="__main__":
    counter = 0
    # Read in the file of ISBN numbers
    with open('isbnList.txt', 'r') as isbnList:
        for isbn in isbnList:
            #if counter == 10:
            #    break
            checkPrices(isbn)
            sleep(5)
            #counter += 1
        
        totalPrice = 0

        for vendor, booksBought in buyers.items():
            print (vendor)
            for book in booksBought:
                print ("Book:", book.title, book.isbn, book.price),
                totalPrice += book.price
            
            print ("Total Price: " + str(totalPrice))
            totalPrice = 0
            print ("---------------------------------")

        print("Finished")

