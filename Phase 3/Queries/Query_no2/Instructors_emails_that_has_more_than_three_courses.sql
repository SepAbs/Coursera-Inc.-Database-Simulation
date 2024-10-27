SELECT
    u.email,
    course_counts.course_count
FROM
    instructor ins
        JOIN
    (SELECT
         ric.instructor_id,
         COUNT(ric.course_id) AS course_count
     FROM
         rel_instructor_course ric
     GROUP BY
         ric.instructor_id
     HAVING
             COUNT(ric.course_id) > 3) AS course_counts
    ON ins.instructor_id = course_counts.instructor_id
        JOIN
    "user" u
    ON u.user_id = ins.instructor_id;
