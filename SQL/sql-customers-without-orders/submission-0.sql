SELECT name
FROM customers
WHERE id NOT IN (
    SELECT DISTINCT customer_id
    FROM orders o, customers c
    WHERE c.id = o.customer_id
);