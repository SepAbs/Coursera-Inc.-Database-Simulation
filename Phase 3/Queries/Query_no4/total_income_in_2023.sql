SELECT sum(amount)
FROM transaction
WHERE date_of >= '2023-01-01'
AND date_of < '2024-01-01';
