from dbconnection import run_select_query

query = "SELECT * FROM users;"
rows = run_select_query(query)

for row in rows:
    print(row)