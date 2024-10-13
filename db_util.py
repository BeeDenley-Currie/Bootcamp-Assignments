import mysql.connector
from config import USER, PASSWORD, HOST

class DbConnectionError(Exception):
    pass

def _connect_to_db(db_name):
    cnx = mysql.connector.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        auth_plugin='mysql_native_password',
        database=db_name
    )
    return cnx


# Endpoint 1 - using GET to view all available books in the bookshop
def get_all_inventory():
    inventory = []
    try:
        db_name = "bookshop"
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor()
        print("Connected to DB: %s" % db_name)

        query = "SELECT id, title, author, genre, price, stat FROM inventory WHERE stat = 'In Stock'"
        cur.execute(query)
        result = cur.fetchall()
        for item in result:
            inventory.append({
                'id': item[0],
                'title': item[1],
                'author': item[2],
                'genre': item[3],
                'price': item[4],
                'stat': item[5],
            })
        cur.close()
    # exception handling:
    except Exception:
        raise DbConnectionError("Failed to read data from DB")
    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")
    return inventory
# I could change this to view all books by removing the WHERE clause


# Endpoint 2 - use PUT to order a book
def request_book(book_id, cust_name, cust_email):
    # Find out if book is in stock - show error if not
    try:
        db_name = "bookshop"
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor(buffered=True)
        print("Connected to DB: %s" % db_name)

        query = "SELECT * FROM inventory WHERE id = %s AND stat = 'In Stock'".format(book_id)
        cur.execute(query, (book_id,))
        book = cur.fetchall()
        db_connection.commit()
        if not book:
            raise DbConnectionError("Book not available for purchase")
        # Update the book's status and add the customer to the orders table
        else:
            query2 = "UPDATE inventory SET stat = 'Out Of Stock' WHERE id = %s".format(book_id)
            cur.execute(query2, (book_id,))
            db_connection.commit()
            query3 = "INSERT INTO orders (book_id, cust_name, cust_email) VALUES (%s, %s, %s)".format(book_id, cust_name, cust_email)
            cur.execute(query3, (book_id, cust_name, cust_email))
            db_connection.commit()
            cur.close()
            print("Book ordered successfully")

    # exception handling:
    except Exception as err:
        print(f"Error: {err}")
        raise DbConnectionError("Failed to order book")
    finally:
        if db_connection:
            db_connection.close()
            print("Connection to DB closed")

# Endpoint 3 - use POST to Add a new book
def book_add(title, author, genre, price):
    try:
        db_name = "bookshop"
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor()
        print("Connected to DB: %s" % db_name)

        query = """INSERT INTO inventory (title, author, genre, price) VALUES (%s, %s, %s, %s)""".format(title, author, genre, price)
        cur.execute(query, (title, author, genre, price))
        db_connection.commit()
        print(f"{title} successfully added to inventory")
        cur.close()
    except Exception as e:
        print(f"Error: {e}")
        raise DbConnectionError("Failed to insert booking data into DB")
    finally:
        if db_connection:
            db_connection.close()
            print("Connection to DB closed")

# Endpoint 4 - using GET to access all placed orders
def get_all_orders():
    _orders = []
    try:
        db_name = "bookshop"
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor()
        print("Connected to DB: %s" % db_name)

        query = "SELECT id, book_id, cust_name, cust_email FROM orders"
        cur.execute(query)
        result = cur.fetchall()
        for item in result:
            _orders.append({
                'id': item[0],
                'book_id': item[1],
                'cust_name': item[2],
                'cust_email': item[3],
            })
        cur.close()
    # exception handling:
    except Exception:
        raise DbConnectionError("Failed to read data from DB")
    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")
    return _orders
