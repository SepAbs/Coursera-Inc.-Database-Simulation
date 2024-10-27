from faker import Faker
import random

faker = Faker()

num_records = 300

# Sets to track unique company names and websites
unique_company_names = set()
unique_websites = set()

# Generate SQL insert statements
sql_inserts = []
for _ in range(num_records):
    partner_id = _ + 1  # Assuming sequential IDs starting from 1

    # Ensure unique company name
    company_name = faker.company()
    while company_name in unique_company_names:
        company_name = faker.company()
    unique_company_names.add(company_name)
    company_name = company_name.replace("'", "''")  # Handle single quotes in company names

    # Ensure unique website
    website = faker.url()
    while website in unique_websites:
        website = faker.url()
    unique_websites.add(website)

    ceo = faker.name().replace("'", "''")  # Generate a random name
    region = faker.state()  # Generate a random state as region
    is_university = random.choice([True, False])  # Randomly choose if it's a university
    establishment_date = faker.date_between(start_date='-30y', end_date='today')  # Random date in the past 30 years

    sql_inserts.append(
        f"INSERT INTO partner_organization (partner_id, company_name, ceo, website, region, is_university, establishment_date) VALUES "
        f"({partner_id}, '{company_name}', '{ceo}', '{website}', '{region}', {is_university}, '{establishment_date}');"
    )

# Optionally, write the SQL statements to a file
with open('./partner_organization_inserts.sql', 'w') as file:
    for statement in sql_inserts:
        file.write(statement + "\n")
