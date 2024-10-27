import random
from faker import Faker

faker = Faker()

# Assuming you want to generate 100 financial_aid records
num_records = 1000

course_id_range = (1, 499)
student_id_range = (1, 2000)
employee_id_range = (2801, 3000)

# Generate SQL insert statements
sql_inserts = []
for _ in range(num_records):
    financial_aid_id = _ + 1
    course_id = random.randint(*course_id_range)
    student_id = random.randint(*student_id_range)
    relevant_employee_id = random.randint(*employee_id_range)
    aid_amount = round(random.uniform(100, 1000), 2)  # Random aid amount between 100 and 1000
    sending_date = faker.date_between(start_date='-1y', end_date='today')
    response_date = faker.date_between(start_date=sending_date, end_date='+30d')  # Response within 30 days after sending
    explanation_text_no1 = faker.text(max_nb_chars=200)
    explanation_text_no2 = faker.text(max_nb_chars=200)

    sql_inserts.append(
        f"INSERT INTO financial_aid (financial_aid_id, course_id, student_id, relevant_employee_id, aid_amount, sending_date, response_date, explanation_text_no1, explanation_text_no2) VALUES "
        f"({financial_aid_id}, {course_id}, {student_id}, {relevant_employee_id}, {aid_amount}, '{sending_date}', '{response_date}', '{explanation_text_no1}', '{explanation_text_no2}');"
    )

# Write the SQL statements to a file
with open('./financial_aid_inserts.sql', 'w') as file:
    for statement in sql_inserts:
        file.write(statement + "\n")
