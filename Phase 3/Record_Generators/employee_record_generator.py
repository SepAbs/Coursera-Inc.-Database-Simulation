import random
from faker import Faker

faker = Faker()

# Define possible values for custom enumerated types
sex_types = ['Male', 'Female']
marital_statuses = ['Single', 'Married', 'Divorced']
departments = ['HR', 'Advertisement', 'Technical', 'Product', 'Support']  # Example departments
education_levels = ['Bachelors', 'Master', 'Phd']

num_records = 200

# Set to keep track of unique national IDs
unique_national_ids = set()

# Generate SQL insert statements
sql_inserts = []
for employee_id in range(2801, 2800 + num_records + 1):
    position_title = faker.job()
    salary = round(random.uniform(30000, 200000), 2)  # Random salary between 30k and 200k
    sex = random.choice(sex_types)
    marital_status = random.choice(marital_statuses)
    number_of_children = random.randint(0, 5)  # Random number of children between 0 and 5
    hire_date = faker.date_between(start_date='-10y', end_date='today')

    # Ensure unique national ID
    national_id = ''.join([str(random.randint(0, 9)) for _ in range(10)])  # 10-digit random number
    while national_id in unique_national_ids:
        national_id = ''.join([str(random.randint(0, 9)) for _ in range(10)])
    unique_national_ids.add(national_id)

    department_name = random.choice(departments)
    education = random.choice(education_levels)

    sql_inserts.append(
        f"INSERT INTO employee (employee_id, position_title, salary, sex, marital_status, number_of_children, hire_date, national_id, department_name, education) VALUES "
        f"({employee_id}, '{position_title}', {salary}, '{sex}', '{marital_status}', {number_of_children}, '{hire_date}', '{national_id}', '{department_name}', '{education}');"
    )

# Write the SQL statements to a file
with open('./employee_inserts.sql', 'w') as file:
    for statement in sql_inserts:
        file.write(statement + "\n")
