import random
from faker import Faker

faker = Faker()

num_records = 5000

# Assuming student_id and course_id ranges
student_id_range = (1, 2000)
course_id_range = (1, 499)

# Sets to keep track of unique credential IDs and student-course pairs
unique_credential_ids = set()
unique_student_course_pairs = set()

# Generate SQL insert statements
sql_inserts = []
for certificate_id in range(1, num_records + 1):
    name = faker.catch_phrase()
    related_student_id = random.randint(*student_id_range)
    related_course_id = random.randint(*course_id_range)
    student_course_pair = (related_student_id, related_course_id)

    # Ensure unique student-course pair
    while student_course_pair in unique_student_course_pairs:
        related_student_id = random.randint(*student_id_range)
        related_course_id = random.randint(*course_id_range)
        student_course_pair = (related_student_id, related_course_id)
    unique_student_course_pairs.add(student_course_pair)

    # Ensure unique credential ID
    credential_id = ''.join([str(random.randint(0, 9)) for _ in range(10)])  # 10-digit number
    while credential_id in unique_credential_ids:
        credential_id = ''.join([str(random.randint(0, 9)) for _ in range(10)])
    unique_credential_ids.add(credential_id)

    credential_url = f'https://coursera.com/certificates/{credential_id}'
    release_date = faker.date_between(start_date='-5y', end_date='today')
    expiry_date = faker.date_between(start_date='today', end_date='+5y')

    sql_inserts.append(
        f"INSERT INTO certificate (certificate_id, name, related_student_id, related_course_id, release_date, expiry_date, credential_id, credential_url) VALUES "
        f"({certificate_id}, '{name}', {related_student_id}, {related_course_id}, '{release_date}', '{expiry_date}', '{credential_id}', '{credential_url}');"
    )

# Write the SQL statements to a file
with open('./certificate_inserts.sql', 'w') as file:
    for statement in sql_inserts:
        file.write(statement + "\n")
