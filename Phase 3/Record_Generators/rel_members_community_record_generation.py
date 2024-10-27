import random

num_records = 1000
num_communities = 500

member_id_range = (1, 3000)  # Range of user IDs that are members

# Ensure every community has at least one member
pairings = {(random.randint(*member_id_range), community_id) for community_id in range(1, num_communities + 1)}

# Generate additional random pairings if needed
while len(pairings) < num_records:
    member_id = random.randint(*member_id_range)
    community_id = random.randint(1, num_communities)
    pairings.add((member_id, community_id))

# Generate SQL insert statements
sql_inserts = [
    f"INSERT INTO rel_community_members (member_id, community_id) VALUES ({member_id}, {community_id});"
    for member_id, community_id in pairings
]

# Write the SQL statements to a file
with open('./rel_members_community_inserts.sql', 'w') as file:
    for statement in sql_inserts:
        file.write(statement + "\n")
