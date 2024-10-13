import requests
import json
from beautifultable import BeautifulTable

def get_inventory():
    result = requests.get(
        'http://127.0.0.1:5001/books',
        headers={'content-type': 'application/json'}
    )
    return result.json()

# using beautifultable means we will have a nicely formatted table
def display_inventory(inventory):
    table = BeautifulTable(maxwidth=4000) # setting maxwidth to a high value means don't need to worry about lines splitting
    table.columns.header = ['ID', 'Title', 'Author', 'Genre', 'Price', 'Status']
    for item in inventory:
        table.rows.append([item['id'], item['title'], item['author'], item['genre'], item['price'], item['stat']])
    print(table)

def get_orders():
    result = requests.get(
        'http://127.0.0.1:5001/orders',
        headers={'content-type': 'application/json'}
    )
    return result.json()

def show_recent_order(_orders):
    table = BeautifulTable(maxwidth=4000)
    table.columns.header = ['Order #', 'Book_ID', 'Customer', 'Customer Email']
    for item in _orders:
        table.rows.append([item['id'], item['book_id'], item['cust_name'], item['cust_email']])
    new_table = table.rows[-1:]
    return new_table

def new_order(book_id, cust_name, cust_email):
    _order = {
        "book_id": book_id,
        "cust_name": cust_name,
        "cust_email": cust_email}
    result = requests.put(
        'http://127.0.0.1:5001/order',
        headers={'content-type': 'application/json'},
        data=json.dumps(_order)
    )
    # using HTTP response codes to split logic out into success/not success
    if result.status_code == 200:
        print(f"Thank you for your order, {cust_name}")
        orders = get_orders()
        print()
        print(show_recent_order(orders))
    else:
        print(f"Failed to order book: error {result.status_code}")


def add_new_book(title, author, genre, price):
    new_book = {
        "title": title,
        "author": author,
        "genre": genre,
        "price": price,
    }
    result = requests.post(
        'http://127.0.0.1:5001/new_book',
        headers={'content-type': 'application/json'},
        data=json.dumps(new_book)
    )
    return result

def run():
    print("_______________________________")
    print("Welcome to My Bookshop!")
    print("_______________________________")
    print()
    choice = input("What would you like to Do? Add Stock [A], Browse [B], or Exit [E]: ").lower()
    if choice == ("b" or "browse"):
        stock = get_inventory()
        print('####### BOOKS FOR SALE #######')
        print()
        display_inventory(stock)
        print()
        buy = input("Would you like to order a book? Y/N: ").lower()
        if buy == "y":
            book_id = input("Book ID: ")
            cust_name = input("What is your name? ")
            cust_email = input("What is your contact email? ")
            new_order(book_id, cust_name, cust_email)
            run()
        elif buy == "n":
            run()
        else:
            print("\nHmm, I didn't understand that")
            run()
    elif choice == ("a" or "add" or "add book"):
        title = input("Title: ")
        author = input("Author: ")
        genre = input("Genre: ")
        price = float(input("Price: "))
        add_new_book(title, author, genre, price)
        stock = get_inventory()
        print('\n####### BOOKS FOR SALE #######')
        display_inventory(stock)
        print("\n")
        run()
    elif choice == ("e" or "exit"):
        print("\nOkay, bye!")
    else:
        print("\nHmm, I didn't understand that")
        run()

if __name__ == '__main__':
    run()