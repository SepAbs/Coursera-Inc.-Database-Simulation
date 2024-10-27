import random

num_records = 1000

# Define the range of IDs (adjust these based on your existing data)
instructor_id_range = (2001, 2800)  # Assuming 800 instructors
course_id_range = (1, 1000)

# Set to keep track of unique instructor-course pairs
pairings = set()

# Ensure every instructor is paired with at least one course
for instructor_id in range(*instructor_id_range):
    course_id = random.randint(*course_id_range)
    pairings.add((instructor_id, course_id))

# Generate additional random pairings if needed
while len(pairings) < num_records:
    instructor_id = random.randint(*instructor_id_range)
    course_id = random.randint(*course_id_range)
    pairings.add((instructor_id, course_id))

# Generate SQL insert statements
sql_inserts = [
    f"INSERT INTO rel_instructor_course (instructor_id, course_id) VALUES ({pair[0]}, {pair[1]});"
    for pair in pairings
]

# Write the SQL statements to a file
with open('./rel_instructor_course_inserts.sql', 'w') as file:
    for statement in sql_inserts:
        file.write(statement + "\n")
