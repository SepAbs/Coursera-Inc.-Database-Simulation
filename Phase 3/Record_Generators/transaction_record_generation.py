import random
from faker import Faker

faker = Faker()

num_records = 2000

user_id_range = (1, 3000)
coursera_plus_id_range = (1, 700)
course_id_range = (1, 499)

# Generate SQL insert statements
sql_inserts = []
for transaction_id in range(1, 701):
    user_id = random.randint(*user_id_range)
    date_of = faker.date_between(start_date='-2y', end_date='today')
    amount = round(random.uniform(10, 1000), 2)  # Random amount between 10 and 1000
    coursera_plus_id = transaction_id

    sql_inserts.append(
        f"INSERT INTO transaction (transaction_id, user_id, date_of, amount, coursera_plus_id) VALUES "
        f"({transaction_id}, {user_id}, '{date_of}', {amount}, {coursera_plus_id});"
    )

unique_user_course_pairs = set()

for transaction_id in range(701, num_records + 1):
    user_id = random.randint(*user_id_range)
    date_of = faker.date_between(start_date='-2y', end_date='today')
    amount = round(random.uniform(10, 1000), 2)  # Random amount between 10 and 1000
    course_id = random.randint(*course_id_range)
    user_course_pair = (user_id, course_id)

    # Ensure unique user_id and course_id pair
    while user_course_pair in unique_user_course_pairs:
        user_id = random.randint(*user_id_range)
        course_id = random.randint(*course_id_range)
        user_course_pair = (user_id, course_id)
    unique_user_course_pairs.add(user_course_pair)

    sql_inserts.append(
        f"INSERT INTO transaction (transaction_id, user_id, date_of, amount, course_id) VALUES "
        f"({transaction_id}, {user_id}, '{date_of}', {amount}, {course_id});"
    )
# Write the SQL statements to a file
with open('./transaction_inserts.sql', 'w') as file:
    for statement in sql_inserts:
        file.write(statement + "\n")
