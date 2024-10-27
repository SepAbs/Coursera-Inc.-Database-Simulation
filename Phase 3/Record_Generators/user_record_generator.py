from faker import Faker
import random
import hashlib

fake = Faker()


# Helper function to hash passwords
def hash_password(psw):
    return hashlib.sha256(psw.encode('utf-8')).hexdigest()


# Generate SQL insert statements
sql_inserts = []
user_id = 1
unique_emails = set()
unique_phones = set()
unique_usernames = set()

for _ in range(3000):
    # Ensure unique username
    username = fake.user_name()
    while username in unique_usernames:
        username = fake.user_name()
    unique_usernames.add(username)

    password = hash_password(
        fake.password(length=12, special_chars=True, digits=True, upper_case=True, lower_case=True))
    registration_date = fake.date_between(start_date='-5y', end_date='today')
    region = fake.state()
    age = random.randint(18, 90)  # Assuming the age range is 18 to 90
    first_name = fake.first_name()
    last_name = fake.last_name()

    # Ensure unique email
    email = fake.ascii_free_email()
    while email in unique_emails:
        email = fake.ascii_free_email()
    unique_emails.add(email)

    # Ensure unique phone
    phone = fake.phone_number()[:10].replace("(", "").replace(")", "").replace(" ", "").replace("-", "")
    phone_formatted = f"{phone[:3]}-{phone[3:6]}-{phone[6:]}"
    while phone_formatted in unique_phones:
        phone = fake.phone_number()[:10].replace("(", "").replace(")", "").replace(" ", "").replace("-", "")
        phone_formatted = f"{phone[:3]}-{phone[3:6]}-{phone[6:]}"
    unique_phones.add(phone_formatted)

    sql_inserts.append(
        f"INSERT INTO \"user\" (user_id, username, password, registration_date, region, age, first_name, last_name, email, phone) VALUES "
        f"({user_id}, '{username}', '{password}', '{registration_date}', '{region}', {age}, '{first_name}', '{last_name}', '{email}', '{phone_formatted}');"
    )
    user_id += 1

# Write the SQL statements to a file
with open('user_inserts.sql', 'w') as file:
    for statement in sql_inserts:
        file.write(statement + "\n")
