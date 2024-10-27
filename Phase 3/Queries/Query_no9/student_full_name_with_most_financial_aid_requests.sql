WITH MostRequests AS (
    SELECT student_id, COUNT(*) AS request_count
    FROM financial_aid
    GROUP BY student_id
    ORDER BY COUNT(*) DESC
    LIMIT 1
)
SELECT u.first_name, u.last_name, mr.student_id, mr.request_count
FROM "user" u
         JOIN student s ON u.user_id = s.student_id
         JOIN MostRequests mr ON s.student_id = mr.student_id;
