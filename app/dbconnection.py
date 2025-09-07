import psycopg2

# Define connection parameters
conn = psycopg2.connect(
    dbname="mydatabase",
    user="admin",
    password="admin",
    host="localhost",
    port="5432"
)

# Create a cursor and execute a query
cur = conn.cursor()
cur.execute("SELECT * FROM users;")
rows = cur.fetchall()

# Print results
for row in rows:
    print(row)

# Clean up
cur.close()
conn.close()