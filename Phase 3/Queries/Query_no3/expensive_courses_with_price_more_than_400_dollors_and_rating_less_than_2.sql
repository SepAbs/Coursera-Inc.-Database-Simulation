SELECT c.name, c.price, c.rating FROM course c
WHERE c.price::numeric > 400.00 AND c.rating < 2;