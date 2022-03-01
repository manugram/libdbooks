from libdbooks import DBooks
from pprint import pp



db = DBooks()

def main():

    # Query for recent uploaded books
    r = db.recent_books()

    # Print the nomber of books return
    print(r.get('total'))

    # Query for search term, gcc in this example
    s = db.search_book('asm')

    # Print total number of books found in query
    print('Total books:',s['total'])
    for x in s['books']:
        pp(x)
        print('+-------------------------+')


    # Pretty print specific book details, as a formatted string, losing
    # dictionaries advantages
    d = db.book_details('5606038334', indent=2)
    print(d)






if __name__ == '__main__':
    main()
