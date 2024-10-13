from flask import Flask, request

from db_util import get_all_inventory, request_book, book_add, get_all_orders

app = Flask(__name__)
#wanted a way to stop lists becoming out of order when using jsonify
app.json.sort_keys = False

# CHECK ENDPOINT
@app.route('/')
def index():
    return "Bookshop API is up!"

#Endpoint 1 - using GET to view all available books
@app.route('/books', methods=['GET'])
def get_books():
    inventory=get_all_inventory()
    return inventory
# http://127.0.0.1:5001/books

# Endpoint 2 - use PUT to Request a book
# -- I chose PUT because we don't want to order the book multiple times if the request was called repeatedly (which POST would)
@app.route('/order', methods=['PUT'])
def order_book():
    data = request.get_json()
    request_book(
        book_id=data['book_id'],
        cust_name=data['cust_name'],
        cust_email=data['cust_email']
    )
    return data

# Endpoint 3 - use POST to Add a new book
@app.route('/new_book', methods=['POST'])
def add_book():
    data = request.get_json()
    book_add(
        title=data['title'],
        author=data['author'],
        genre=data['genre'],
        price=data['price']
    )
    return data

# Endpoint 4 - using GET to access all placed orders
@app.route('/orders', methods=['GET'])
def get_orders():
    orders = get_all_orders()
    return orders
# http://127.0.0.1:5001/orders

# Run the app
if __name__ == '__main__':
    app.run(debug=True, port=5001)