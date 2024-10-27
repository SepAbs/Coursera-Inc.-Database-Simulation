import random
from faker import Faker

faker = Faker()

# Assuming you want to generate 100 request records
num_records = 1500

employee_id_range = (2801, 3000)
user_id_range = (1, 2800)  # Instructors & Students

# Generate SQL insert statements
sql_inserts = []
for request_id in range(1, num_records + 1):
    relevant_employee_id = random.randint(*employee_id_range)
    relevant_user_id = random.randint(*user_id_range)
    topic = faker.sentence()
    send_date = faker.date_between(start_date='-1y', end_date='today')
    response_date = faker.date_between(start_date=send_date, end_date='+30d')  # Response within 30 days after sending
    content = faker.text(max_nb_chars=200)

    sql_inserts.append(
        f"INSERT INTO request (request_id, relevant_employee_id, relevant_user_id, topic, send_date, response_date, content) VALUES "
        f"({request_id}, {relevant_employee_id}, {relevant_user_id}, '{topic}', '{send_date}', '{response_date}', '{content}');"
    )

# Write the SQL statements to a file
with open('./request_inserts.sql', 'w') as file:
    for statement in sql_inserts:
        file.write(statement + "\n")
