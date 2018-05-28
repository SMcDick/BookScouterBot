class UpdateISBNList:

    if __name__=="__main__":

        try:
            isbnToDeleteFile = open ('isbnsToDelete.txt', 'r')
        except IOError:
            print ("Error: File isbnsToDelete.txt does not appear to exist.")
            exit()
       
        isbnsToDelete = {line.strip() for line in isbnToDeleteFile}  # makes a set of items to delete

        isbnToDeleteFile.close()

        for isbn in isbnsToDelete:
            isbn.strip()

        isbnListFile = open ('isbnList.txt', 'r')

        newISBNList = []

        linesDeleted = 0

        for isbn in isbnListFile:
            if isbn.strip() not in isbnsToDelete:
                newISBNList.append(isbn)
            else:
                linesDeleted += 1

        isbnListFile.close()

        updatedISBNList = open ('isbnList.txt', 'w')

        for isbn in newISBNList:
            updatedISBNList.write(isbn)
        
        updatedISBNList.close()

        print (str(linesDeleted) + ' Lines Delete')
