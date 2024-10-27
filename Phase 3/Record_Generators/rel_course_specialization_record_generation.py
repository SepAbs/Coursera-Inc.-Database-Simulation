import random

num_records = 1000

course_id_range = (1, 1000)  # Range of course IDs
specialization_id_range = (1, 300)  # Range of specialization IDs

# Generate unique pairings of course_id and specialization_id
pairings = set()

# Ensure every specialization_id is paired at least once
for specialization_id in range(*specialization_id_range):
    course_id = random.randint(*course_id_range)
    pairings.add((course_id, specialization_id))

# Generate additional random pairings if needed
while len(pairings) < num_records:
    course_id = random.randint(*course_id_range)
    specialization_id = random.randint(*specialization_id_range)
    pairings.add((course_id, specialization_id))

# Generate SQL insert statements
sql_inserts = [
    f"INSERT INTO rel_course_specialization (course_id, specialization_id) VALUES ({pair[0]}, {pair[1]});"
    for pair in pairings
]

# Write the SQL statements to a file
with open('./rel_course_specialization_inserts.sql', 'w') as file:
    for statement in sql_inserts:
        file.write(statement + "\n")
