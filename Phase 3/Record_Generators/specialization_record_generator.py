import random
from faker import Faker

faker = Faker()

num_records = 1000

student_id_range = (1, 2000)

# Generate SQL insert statements
sql_inserts = []
unique_credential_ids = set()

for specialization_id in range(1, num_records + 1):
    student_id = random.randint(*student_id_range)
    release_date = faker.date_between(start_date='-2y', end_date='today')
    expiry_date = faker.date_between(start_date='today', end_date='+2y')
    # Ensure unique credential ID
    credential_id = ''.join([str(random.randint(0, 9)) for _ in range(10)])  # 10-digit number
    while credential_id in unique_credential_ids:
        credential_id = ''.join([str(random.randint(0, 9)) for _ in range(10)])
    unique_credential_ids.add(credential_id)
    credential_url = f'https://coursera.com/specialization/{credential_id}'

    sql_inserts.append(
        f"INSERT INTO specialization (specialization_id, student_id, release_date, expiry_date, credential_id, credential_url) VALUES "
        f"({specialization_id}, {student_id}, '{release_date}', '{expiry_date}', '{credential_id}', '{credential_url}');"
    )

# Write the SQL statements to a file
with open('./specialization_inserts.sql', 'w') as file:
    for statement in sql_inserts:
        file.write(statement + "\n")
