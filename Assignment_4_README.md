<h1>Assignment 4</h1>
  
## Creative Scenario
My last job was as a researcher and manager of a secondhand bookshop, so I've chosen to make a Bookshop database, which will allow users to view the inventory, order a book, or add a new book to the inventory.
Each book needs to have an ID, Title, Author, Genre, Price, and stock status. For orders, we need an order ID, the book ID being ordered, the customer name, and the contact email.
The API should only allow a customer to order books that are in stock.

## The Code
### MySQL Database
has 2 tables: Inventory, and Orders

<img src="https://github.com/user-attachments/assets/5bfdad96-9a39-45c8-b64b-b8139bdb344b" alt="MySQL Bookshop Database" width="500"/>

### Back-end API setup
I have 5 endpoints, set up in [app.py](/app.py) with further code imported from [db_util.py](/db_util.py)
I defined functions for the different endpoints, to section out the code and cut down on repetition.
1. / - plain check endpoint, to see if API is running
2. /books - with GET method to view all available books
3. /order - with PUT method to request a book. Won't commit request if book is out of stock
4. /new_book - with POST method to add a new book to the inventory
5. /orders - another GET method, to view placed orders
I used exception handling, both for connection errors and also for other DB errors (like book not being In Stock)
<img src="https://github.com/user-attachments/assets/0f8c0f0f-1796-4baf-aad3-a5f3dc7d1b2a" alt="Different Exception uses" width="500"/>


### Client-side setup
I set up functions to:
- [X] get the inventory, and then to display it using Beautifultable (nicer formatting)
![image](https://github.com/user-attachments/assets/6aa9bc79-b2f8-4a91-af1f-39391c8ca45b)

- [X] get orders, use slicing to display only the most recent order
![image](https://github.com/user-attachments/assets/77bbf964-4729-499d-9753-f1479244924b)

- [X] try to place a new order - and show either that it was a success OR that the book isn't available to buy(using HTTP Response Codes set in db_util)

![image](https://github.com/user-attachments/assets/603ef542-d8ba-417b-a075-96861ada3574)

- [X] and finally one to add a new book

![image](https://github.com/user-attachments/assets/f734e895-6bcd-4955-baa9-28411da11e81)

- [X] Set up a looping run function, to call these earlier defined ones and act as a little bit of error handling for unexpected inputs


## Run Instructions
1. Set up the [config.py](/config.py) file, completing your values for the MySQL "HOST", "USER", and "PASSWORD"
2. Run [assignment_4_db_script.sql](/assignment_4_db_script.sql) in MySQL
3. Run [app.py](/app.py) in Python
4. Keep app.py running, open a second instance and run [main.py](/main.py)
5. Choose different options within the run function to browse the inventory, order a book, add a book, or exit.
6. Enjoy!


https://github.com/user-attachments/assets/1134d0c1-c488-40b8-b054-3e6872831dce

