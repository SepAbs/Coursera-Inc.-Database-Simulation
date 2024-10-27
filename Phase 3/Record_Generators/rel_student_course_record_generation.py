import random

# Define the number of records you want to generate
num_records = 2000

# Define the range of IDs (adjust these based on your existing data)
student_id_range = (1, 2000)  # Range of student IDs
course_id_range = (1, 1000)   # Range of course IDs

# Generate unique pairings of student_id and course_id
pairings = set()
while len(pairings) < num_records:
    student_id = random.randint(*student_id_range)
    course_id = random.randint(*course_id_range)
    pairings.add((student_id, course_id))

# Generate SQL insert statements
sql_inserts = [
    f"INSERT INTO rel_student_course (student_id, course_id) VALUES ({student_id}, {course_id});"
    for student_id, course_id in pairings
]

# Write the SQL statements to a file
with open('./rel_student_course_inserts.sql', 'w') as file:
    for statement in sql_inserts:
        file.write(statement + "\n")
