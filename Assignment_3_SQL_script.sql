/* INTRODUCTION
See this branch's README.md for more information on why I chose this database topic, an EER, and scenarios for use case & further development.
*/
--------------------------------------------------------------------------------------------
CREATE DATABASE laboratory;
USE laboratory;

-- making the tables and adding information. Setting primary keys/foreign keys/constraints (with different methods) --

CREATE TABLE virus
(v_acronym VARCHAR(10) PRIMARY KEY,
v_name VARCHAR(250) NOT NULL
);
ALTER TABLE virus
add v_family VARCHAR (250);

INSERT INTO virus (v_acronym, v_name, v_family) VALUES
('AHS', 'African Horse Sickness Virus', 'orbivirus'),
('ASF', 'African Swine Fever Virus', 'asfivirus'),
('BTV', 'Bluetongue Virus', 'orbivirus'),
('EHDV', 'Epizootic Haemorrhagic Disease Virus', 'orbivirus'),
('GPV', 'Goatpox Virus', 'capripoxvirus'),
('LSDV', 'Lumpy Skin Disease Virus', 'capripoxvirus'),
('PPRV', 'Peste des Petits Ruminants Virus', 'morbilivirus'),
('SPV', 'Sheeppox Virus', 'capripoxvirus');

CREATE TABLE species
(sp_ID INT PRIMARY KEY,
sp_name VARCHAR(250) NOT NULL
);
INSERT INTO species (sp_ID, sp_name) VALUES
(1, 'Horse'),
(2, 'Cow'),
(3, 'Zebra'),
(4, 'Rhino'),
(5, 'Bison'),
(6, 'Goat'),
(7, 'Sheep'),
(8, 'Llama'),
(9, 'Pig'),
(10, 'Wild Boar');

CREATE TABLE samples
(s_ID INT primary KEY,
s_type VARCHAR(250)
);
INSERT INTO samples (s_ID, s_type) VALUES
(1, 'serum'),
(2, 'plasma'),
(3, 'EDTA'),
(4, 'spleen'),
(5, 'brain'),
(6, 'skin nodule'),
(7, 'ear flap'),
(8, 'swab');

CREATE TABLE tests
(t_ID INT PRIMARY KEY,
t_name VARCHAR(250),
t_type VARCHAR(250)
);
INSERT INTO tests (t_ID, t_name, t_type) VALUES
(1, 'antigen ELISA', 'serology'),
(2, 'antibody ELISA', 'serology'),
(3, 'PCR', 'molecular'),
(4, 'Virus Neutralisation Test', 'serology'),
(5, 'serotyping', 'molecular'),
(6, 'Virus Isolation', 'molecular'),
(7, 'lateral flow device', 'serology');

CREATE TABLE susceptible
(v_acronym VARCHAR(250),
sp_name VARCHAR(250),
FOREIGN KEY (v_acronym) REFERENCES virus(v_acronym)
);
INSERT INTO susceptible (v_acronym, sp_name) VALUES
('AHS', 'Horse'),
('AHS', 'Zebra'),
('ASF', 'Pig'),
('ASF', 'Wild Boar'),
('BTV', 'Cow'),
('BTV', 'Bison'),
('BTV', 'Sheep'),
('BTV', 'Goat'),
('BTV', 'Llama'),
('EHDV', 'Cow'),
('EHDV', 'Bison'),
('EHDV', 'Sheep'),
('EHDV', 'Goat'),
('EHDV', 'Llama'),
('LSDV', 'Cow'),
('LSDV', 'Bison'),
('SPV', 'Sheep'),
('GPV', 'Goat'),
('PPRV', 'Goat'),
('PPRV', 'Sheep');

CREATE TABLE accept_test
(v_acronym VARCHAR(250),
s_ID INT,
t_ID INT,
FOREIGN KEY (v_acronym) REFERENCES virus(v_acronym),
FOREIGN KEY (s_ID) REFERENCES samples(s_ID),
CONSTRAINT FK_testaccept FOREIGN KEY (t_ID)
REFERENCES tests(t_ID)
);
INSERT INTO accept_test (v_acronym, s_ID, t_ID) VALUES
('ASF', 1, 3),
('ASF', 3, 3),
('ASF', 4, 3),
('ASF', 5, 3),
('ASF', 7, 3),
('ASF', 8, 3),
('ASF', 1, 7),
('ASF', 1, 1),
('ASF', 1, 2),
('ASF', 5, 1),
('ASF', 7, 1),
('ASF', 8, 1),
('ASF', 5, 2),
('ASF', 7, 2),
('ASF', 8, 2),
('ASF', 3, 6),
('AHS', 3, 3),
('AHS', 1, 2),
('AHS', 4, 3),
('AHS', 5, 3),
('AHS', 3, 6),
('AHS', 4, 6),
('BTV', 1, 2),
('BTV', 3, 3),
('BTV', 4, 3),
('BTV', 5, 3),
('BTV', 1, 4),
('BTV', 3, 5),
('BTV', 4, 5),
('BTV', 5, 5),
('BTV', 3, 6),
('BTV', 4, 6),
('BTV', 5, 6),
('EHDV', 1, 2),
('EHDV', 3, 3),
('EHDV', 3, 5),
('EHDV', 3, 6),
('EHDV', 1, 4),
('EHDV', 4, 3),
('EHDV', 4, 5),
('EHDV', 4, 6),
('EHDV', 5, 3),
('EHDV', 5, 5),
('EHDV', 5, 6),
('GPV', 3, 3),
('GPV', 1, 2),
('GPV', 8, 3),
('GPV', 3, 6),
('SPV', 3, 3),
('SPV', 1, 2),
('SPV', 8, 3),
('SPV', 3, 6),
('LSDV', 3, 3),
('LSDV', 1, 2),
('LSDV', 8, 3),
('LSDV', 3, 6),
('LSDV', 6, 3),
('LSDV', 6, 6),
('PPRV', 1, 2),
('PPRV', 3, 3),
('PPRV', 3, 6);

CREATE TABLE customers
(c_ID INT NOT NULL PRIMARY KEY,
c_name VARCHAR(250) NOT NULL,
country VARCHAR(250),
invoiceable ENUM("Y", "N") DEFAULT "Y"
);

INSERT INTO customers (c_ID, c_name, country, invoiceable) VALUES
(1, 'Ministry of Silly Walks', 'UKG', 'N'),
(2, 'Purple Pony Parties', 'UKG', 'Y'),
(3, 'Arrendelle Exotic Disease Unit', 'NOR', 'N'),
(4, 'Cod First Gills', 'UKG', 'Y'),
(5, 'Poorly Pet Parlour', 'UKG', 'Y'),
(6, 'VetsRUS', 'RUS', 'Y'),
(7, 'Animal Health Agency', 'UKG', 'N'),
(8, 'Livestock Export Ltd', 'UKG', 'Y'),
(9, 'Veterinaire Agence', 'FRA', 'N');

CREATE TABLE orders
(o_ID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
o_date DATE,
c_ID INT,
sp_ID INT,
v_acronym VARCHAR(250),
t_ID INT,
s_ID INT
);
ALTER TABLE orders
ADD FOREIGN KEY (c_ID) REFERENCES customers(c_ID),
ADD FOREIGN KEY (sp_ID) REFERENCES species(sp_ID),
ADD FOREIGN KEY (v_acronym) REFERENCES virus(v_acronym),
ADD FOREIGN KEY (t_ID) REFERENCES tests(t_ID),
ADD FOREIGN KEY (s_ID) REFERENCES samples(s_ID)
;
ALTER TABLE orders
ALTER o_date SET DEFAULT (CURDATE());
-- don't need to insert o_ID, this is automatically assigned. Moving forward the order date will be too! :) --

INSERT INTO orders (o_date, c_ID, sp_ID, v_acronym, t_ID, s_ID) VALUES
('2024-01-01', 9, 1, 'AHS', 5, 3),
('2024-01-19', 5, 5, 'BTV', 3, 3),
('2024-02-08', 7, 4, 'SPV', 3, 4),
('2024-02-09', 2, 3, 'EHDV', 2, 1),
('2024-02-21', 1, 8, 'BTV', 2, 2),
('2024-03-01', 4, 6, 'GPV', 3, 3),
('2024-03-04', 6, 1, 'AHS', 4, 1),
('2024-04-11', 3, 2, 'LSDV', 6, 6),
('2024-04-16', 8, 9, 'ASF', 7, 1),
('2024-05-30', 7, 10, 'ASF', 3, 7),
('2024-06-24', 5, 3, 'SPV', 7, 8),
('2024-07-04', 4, 4, 'AHS', 3, 5),
('2024-07-08', 2, 7, 'PPRV', 3, 8),
('2024-07-26', 8, 6, 'BTV', 4, 1),
('2024-08-29', 9, 5, 'SPV', 1, 1),
('2024-08-30', 6, 8, 'EHDV', 3, 4),
('2024-09-17', 3, 9, 'GPV', 2, 2),
('2024-09-20', 1, 2, 'LSDV', 4, 1);

/* Phew! Database all created! */

--------------------------------------------------------------------------------------------  
/*JOIN*/
-- using JOINS to create VIEWS to have human-readable information on what tests are accepted and requested orders
CREATE OR REPLACE VIEW vw_accept_test AS
	SELECT
		ac.v_acronym AS v_acronym,
        sa.s_type AS sample_type,
        te.t_name AS test_name,
        te.t_type AS test_type
	FROM accept_test AS ac
		INNER JOIN samples sa ON ac.s_ID = sa.s_ID
        INNER JOIN tests te ON ac.t_ID = te.t_ID;
SELECT * FROM vw_accept_test;

CREATE OR REPLACE VIEW vw_orders AS
	SELECT
		ord.o_ID AS order_ID,
        ord.o_date AS order_date,
        cu.c_name AS customer_name,
        cu.invoiceable AS invoiceable,
        sp.sp_name AS species_name,
        ord.v_acronym AS virus,
        te.t_name AS test_name,
        sa.s_type AS sample_type
	FROM orders ord 
    INNER JOIN customers cu ON ord.c_ID = cu.c_ID
    JOIN species sp ON ord.sp_ID = sp.sp_ID
    JOIN tests te ON ord.t_ID = te.t_ID
    JOIN samples sa ON ord.s_ID = sa.s_ID
ORDER BY order_ID DESC;
SELECT * FROM vw_orders;

-- as well as joins to create the view: let's see if we have sample types with no accepted tests?
SELECT sa.s_type
FROM samples sa
	LEFT JOIN accept_test ac ON sa.s_ID = ac.s_ID
    WHERE ac.s_ID IS NULL;
-- We do! Only 1. (Plasma)

-- Show ONLY orders which are requesting possible test/virus/sample combinations
SELECT vw_ord.order_ID, vw_ord.order_date, vw_ord.customer_name, vw_ord.invoiceable, vw_ord.species_name, vw_ord.virus, vw_ord.test_name, vw_ord.sample_type
FROM   vw_orders vw_ord
LEFT JOIN orders ord ON vw_ord.order_ID = ord.o_ID
WHERE EXISTS (SELECT *
                   FROM   accept_test ac
                   WHERE ord.v_acronym = ac.v_acronym AND ord.s_ID = ac.s_ID AND ord.t_ID = ac.t_ID);
	-- * could reverse this to see ONLY orders with impossible combinations, using "WHERE NOT EXISTS"

--------------------------------------------------------------------------------------------
/* STORED FUNCTION*/
-- The above query was useful, so I wanted a Stored Function to make sure that a new order meets testing/sampling requirements 
-- (i.e have they sent the right sample type for the test they've asked for & Virus we're looking for?)
-- This was definitely my folly - I spent so long trying to work out how I could compare across the tables, not have duplicate results, not throw up errors!
DELIMITER //
DROP FUNCTION IF EXISTS can_test_ord//
CREATE FUNCTION can_test_ord(o_ID INT)
RETURNS VARCHAR(12)
DETERMINISTIC
BEGIN
DECLARE o_status VARCHAR(12);
IF EXISTS 
		(SELECT DISTINCT 1 FROM vw_orders ord
		JOIN vw_accept_test ac ON ord.virus = ac.v_acronym 
		AND ord.test_name = ac.test_name
		AND ord.sample_type = ac.sample_type
        WHERE ord.order_ID = o_ID) 
THEN SET o_status = "Possible";
ELSE SET o_status = "Impossible";
END IF;
RETURN (o_status);
END//
DELIMITER ;

-- Example Query to see which orders can't be fulfilled: 
SELECT *, can_test_ord(ord.order_ID) AS Can_test
FROM vw_orders ord
WHERE can_test_ord(ord.order_ID) = "Impossible"
ORDER BY order_ID;
-- again, could reverse using NOT or using different string comparison
    
--------------------------------------------------------------------------------------------   
/* IN-BUILT FUNCTIONS */
-- oh no! I've made a spelling mistake! Use REPLACE to correct the typo:
UPDATE virus
SET v_family = REPLACE(v_family, "morbilivirus", "morbillivirus");

SELECT * FROM virus;

-- Update Orders to give a "Date Due" column, depending on order type (Invoiceable or not), using subqueries, DATE_ADD, CASE, and logic.
ALTER TABLE orders ADD COLUMN due DATE;
UPDATE orders ord SET ord.due = CASE
	WHEN ord.c_ID IN 
		(SELECT cu.c_ID 
        FROM customers cu
        WHERE cu.invoiceable = "N")
		THEN date_add(ord.o_date, INTERVAL 3 DAY)
	WHEN ord.c_ID IN 
		(SELECT cu.c_ID 
        FROM customers cu
        WHERE cu.invoiceable = "Y")
		THEN date_add(ord.o_date, INTERVAL 5 DAY)
	END;

-- update vw_orders to include this extra column
CREATE OR REPLACE VIEW vw_orders AS
	SELECT
		ord.o_ID AS order_ID,
        ord.o_date AS order_date,
        ord.due AS order_due,
        cu.c_name AS customer_name,
        cu.invoiceable AS invoiceable,
        sp.sp_name AS species_name,
        ord.v_acronym AS virus,
        te.t_name AS test_name,
        sa.s_type AS sample_type
	FROM orders ord 
    INNER JOIN customers cu ON ord.c_ID = cu.c_ID
    JOIN species sp ON ord.sp_ID = sp.sp_ID
    JOIN tests te ON ord.t_ID = te.t_ID
    JOIN samples sa ON ord.s_ID = sa.s_ID
ORDER BY order_ID DESC;

-- Query to demonstrate the new values, using LIMIT so only last 5 orders shown:
SELECT * FROM vw_orders
ORDER BY order_ID DESC
LIMIT 5;

--------------------------------------------------------------------------------------------        
/* AGGREGATE FUNCTIONS*/
-- Count how many different species Susceptible for a Virus, in descending order
SELECT su.v_acronym, COUNT(su.sp_name) AS sp_count
FROM susceptible su
GROUP BY su.v_acronym
ORDER BY sp_count DESC;

-- MIN() to find which order is the oldest order for each customer in the UK only:
SELECT min(ord.o_date) AS order_date, cu.c_name AS Customer
FROM orders ord JOIN customers cu USING (c_ID)
WHERE cu.country = "UKG"
GROUP BY customer
ORDER BY order_date;

--------------------------------------------------------------------------------------------
-- DELETE Query. Deleting a no-longer acceptable test combination, and then checking it's gone using the view
DELETE FROM accept_test WHERE (v_acronym = "ASF" AND s_ID = 1 AND t_ID = 7);
SELECT * FROM vw_accept_test WHERE (v_acronym = "ASF" AND sample_type = "serum"); 
-- lateral flow device is gone!

--------------------------------------------------------------------------------------------
						-- THE END -- 
-------------------------------------------------------------------------------------------- 