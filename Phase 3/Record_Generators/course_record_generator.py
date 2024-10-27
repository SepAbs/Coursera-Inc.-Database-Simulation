import random
from faker import Faker

faker = Faker()

num_records = 1000

# Generate SQL insert statements
sql_inserts = []
for course_id in range(1, num_records + 1):
    name = faker.catch_phrase()  # Using catchphrases as course names
    total_hour = round(random.uniform(1, 99), 2)  # Random hours between 1 and 99
    number_of_weeks = random.randint(1, 52)  # Random weeks between 1 and 52
    rating = round(random.uniform(0, 5), 2)  # Random rating between 0 and 5
    content = faker.text(max_nb_chars=200)  # Random text content
    amount = round(random.uniform(10, 1000), 2)  # Random amount between 10 and 1000

    sql_inserts.append(
        f"INSERT INTO course (course_id, name, total_hour, number_of_weeks, rating, content, price) VALUES "
        f"({course_id}, '{name}', {total_hour}, {number_of_weeks}, {rating}, '{content}', '{amount}');"
    )

# Write the SQL statements to a file
with open('./course_inserts.sql', 'w') as file:
    for statement in sql_inserts:
        file.write(statement + "\n")
