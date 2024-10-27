WITH TopInstructor AS (
    SELECT instructor_id
    FROM instructor
    ORDER BY rating DESC
    LIMIT 1
),
     WorstCourses AS (
         SELECT c.course_id, c.rating, rci.instructor_id
         FROM course c
                  JOIN rel_instructor_course rci ON c.course_id = rci.course_id
                  JOIN TopInstructor ti ON rci.instructor_id = ti.instructor_id
         ORDER BY c.rating ASC
         LIMIT 1
     )
SELECT u.first_name, u.last_name, i.instructor_id, wc.course_id, wc.rating
FROM "user" u
         JOIN instructor i ON u.user_id = i.instructor_id
         JOIN WorstCourses wc ON i.instructor_id = wc.instructor_id;
