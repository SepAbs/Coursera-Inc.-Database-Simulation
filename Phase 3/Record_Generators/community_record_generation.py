from faker import Faker

faker = Faker()

num_records = 500

# Generate SQL insert statements
sql_inserts = []
for community_id in range(1, num_records + 1):
    name = faker.catch_phrase()
    creation_date = faker.date_between(start_date='-5y', end_date='today')
    contents = faker.text(max_nb_chars=200)
    name = name.replace('\'', '\'\'')
    content = contents.replace('\'', '\'\'')

    sql_inserts.append(
        f"INSERT INTO community (community_id, name, creation_date, contents) VALUES " 
        f"({community_id}, '{name}', '{creation_date}', '{content}');"
    )

# Optionally, write the SQL statements to a file
with open('./community_inserts.sql', 'w') as file:
    for statement in sql_inserts:
        file.write(statement + "\n")
