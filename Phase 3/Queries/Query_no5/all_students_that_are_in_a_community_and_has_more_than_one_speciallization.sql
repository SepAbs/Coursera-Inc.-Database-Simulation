SELECT ud.*, sq.student_id, sq.specialization_count
FROM user_details ud
JOIN (
    SELECT s.student_id, COUNT(DISTINCT sp.specialization_id) AS specialization_count
    FROM students s
    JOIN rel_community_student rcs ON s.student_id = rcs.student_id
    JOIN specialization sp ON s.student_id = sp.student_id
    GROUP BY s.student_id
    HAVING COUNT(DISTINCT sp.specialization_id) > 2
) AS sq ON ud.student_id = sq.student_id;
