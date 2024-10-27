SELECT  u.first_name, u.last_name FROM student s
JOIN "user" u on u.user_id = s.student_id
JOIN coursera_plus cp on u.user_id = cp.user_id
JOIN certificate c on s.student_id = c.related_student_id
GROUP BY s.student_id, u.user_id
HAVING count(s.student_id) > 3;