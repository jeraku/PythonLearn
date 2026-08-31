# CREATE TABLE todos (
#        id SERIAL PRIMARY KEY,
#     title VARCHAR(255) NOT NULL,
#     completed BOOLEAN DEFAULT FALSE,
#     created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
# )

# pip install psycopg2-binary
import psycopg2 
conn = psycopg2.connect(
    host= "localhost",
    database="todos",
    user = "admin",
    password= "qwerty123"
)

conn.autocommit =True # any query will be autocommitted
def get_cursor():
    return conn.cursor()
