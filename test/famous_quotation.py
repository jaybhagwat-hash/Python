""" Famous Quote: Find a quote from a famous person you admire . Print the 
quote and the name of its author . Your output should look something like the 
following, including the quotation marks:
 Albert Einstein once said, “A person who never made a 
mistake never tried anything new.” """

def quotation(name, quote):
    return str(name) + ' once said,' + '"' + quote + '"'

def main():
    name=input("Enter the famous persons name!\n")
    quote=input("Enter his quote")
    print(quotation(name,quote))

if __name__ == "__main__" : 
    main()