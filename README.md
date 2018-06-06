# BookScouterBot

![Book Scouter Logo](bks_logo.svg "Title")

BookScouter.com is a book buyback aggregator which searches multiple websites to help you find the best price for your book. However, the price of the book you are trying to sell can fluctuate (e.g. a book that sells for $0 in January could sell for $23 in March). Manually typing in the ISBNs of all the books you want to sell is a tedious and time-consuming process.

To help simplify this process I have written a bot to automate the task for the user. The program uses the BookScouter API to search the ISBN of your books and find all the available prices. If the quoted price is greater than $0 it will add the book's title, ISBN and price to a dictionary of vendors. The results are then neatly printed to the console.
