-- ___________________________________
-- 1

-- All items, ordered by price (lowest to highest).
-- select * from items order by price asc

-- Items with a price above 80 (80 included), ordered by price (highest to lowest).
-- SELECT * FROM items WHERE price >= 80 ORDER BY price DESC

-- The first 3 customers in alphabetical order of the first name (A-Z) – exclude the primary key column from the results.
-- SELECT first_name, last_name FROM customers ORDER BY first_name ASC LIMIT 3

-- All last names (no other columns!), in reverse alphabetical order (Z-A)
-- SELECT last_name FROM customers ORDER BY last_name DESC


-- ___________________________________
-- 2

-- SELECT * FROM customer

-- SELECT CONCAT (first_name, ' ', last_name)  AS full_name FROM customer

-- SELECT DISTINCT create_date FROM customer 

-- SELECT * FROM customer ORDER BY first_name DESC

-- SELECT film_id, title, description, release_year rental_rate FROM film 

-- SELECT address, phone FROM address WHERE district = 'Texas' 

-- SELECT * FROM film WHERE film_id IN (15, 150)

-- SELECT film_id, title, description, release_year, rental_rate FROM film WHERE title = 'Green Mile'

-- SELECT film_id, title, description, release_year, rental_rate, length FROM film WHERE title ILIKE 'gr%'

-- SELECT * FROM film ORDER BY rental_rate ASC LIMIT 10

-- SELECT * FROM film ORDER BY rental_rate ASC LIMIT 10 OFFSET 10

