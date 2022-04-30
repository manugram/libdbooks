from libdbooks import DBooks
from pprint import pp



db = DBooks()

def main():

    # Query for recent uploaded books
    r = db.get_recents_books()

    # Print the nomber of books return
    print(r.get('total'))

    # Query for search term, python in this example
    s = db.search_book('python')

    # Print total number of books found in query
    print('Total books:',s['total'])

    # Show books title and url...
    for x in s['books']:
        print(x['title'])
        print(x['url'])
        print('+' + '-----'*20 + '+')


    # Pretty print specific book details, as a formatted string, losing
    # dictionaries advantages
    d = db.get_book_details('1530051126')
    pp(d)



if __name__ == '__main__':
    main()

