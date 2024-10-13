CREATE DATABASE bookshop;
USE bookshop;

CREATE TABLE inventory (
    id SERIAL PRIMARY KEY, -- automatically adds next number, like auto increment
    title VARCHAR(250),
    author VARCHAR(250),
    genre VARCHAR(100),
    price DEC(65, 2),
    stat ENUM("In Stock","Out Of Stock") NOT NULL 
    -- ENUM will default to In Stock unless we state otherwise, 
	-- as NOT NULL makes it default to 1st value in ENUM list
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


CREATE TABLE orders (
    id SERIAL PRIMARY KEY,
    book_id INT REFERENCES inventory(id),
    cust_name VARCHAR(100),
    cust_email VARCHAR(100)
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO inventory (title, author, genre, price) VALUES
('Coding For Girls', 'CFG', 'Computing', 10.0),
('Herpetology: A PYTHON Guide', 'S. Nake', 'Computing', 9.99),
('SQL 2: A sequel to SQL', 'C. Quill', 'Computing', 20.00),
('Dragonriders of PERL', 'Anne McCatherty', 'Fantasy', 5.00),
('My Travels in JAVA', 'Coffie & Beann', 'Travel', 25.00);

SELECT * FROM inventory;
SELECT * FROM orders;