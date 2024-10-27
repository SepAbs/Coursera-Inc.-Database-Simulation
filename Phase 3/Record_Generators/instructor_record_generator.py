import random
from faker import Faker

faker = Faker()

num_records = 800

# Generate SQL insert statements
sql_inserts = []
for instructor_id in range(2001, 2001 + num_records + 1):
    # Generating a random rating between 0 and 5, rounded to 2 decimal places
    rating = round(random.uniform(0, 5), 2)

    # Generating a random partner_organization_id (assuming a range)
    partner_organization_id = random.randint(1, 300)  # Adjust range as needed

    sql_inserts.append(
        f"INSERT INTO instructor (instructor_id, rating, partner_organization_id) VALUES ({instructor_id}, {rating}, {partner_organization_id});"
    )

# Optionally, write the SQL statements to a file
with open('./instructor_inserts.sql', 'w') as file:
    for statement in sql_inserts:
        file.write(statement + "\n")
