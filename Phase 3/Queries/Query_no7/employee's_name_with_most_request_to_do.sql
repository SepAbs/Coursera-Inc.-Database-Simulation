SELECT u.first_name, u.last_name, u.age, r.request_count
FROM "user" u
         JOIN employee e ON u.user_id = e.employee_id
         JOIN (
    SELECT relevant_employee_id, COUNT(*) as request_count
    FROM request
    GROUP BY relevant_employee_id
    ORDER BY COUNT(*) DESC
    LIMIT 1
) r ON e.employee_id = r.relevant_employee_id;
