import random
from faker import Faker

faker = Faker()

num_records = 700
user_id_range = (1, 3000)

# Set to keep track of unique user IDs
unique_user_ids = set()

# Generate SQL insert statements
sql_inserts = []
for i in range(num_records):
    # Ensure unique user_id
    user_id = random.randint(*user_id_range)
    while user_id in unique_user_ids:
        user_id = random.randint(*user_id_range)
    unique_user_ids.add(user_id)

    activation_date = faker.date_between(start_date='-2y', end_date='today')
    valid_time = faker.date_time_between(start_date=activation_date, end_date="+1y")
    coursera_plus_id = i + 1  # Assuming sequential IDs starting from 1

    sql_inserts.append(
        f"INSERT INTO coursera_plus (user_id, activation_date, valid_time, coursera_plus_id) VALUES "
        f"({user_id}, '{activation_date}', '{valid_time}', {coursera_plus_id});"
    )

# Optionally, write the SQL statements to a file
with open('./coursera_plus_inserts.sql', 'w') as file:
    for statement in sql_inserts:
        file.write(statement + "\n")
