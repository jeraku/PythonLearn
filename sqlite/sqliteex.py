# PythonLearn
# <!-- pip install sqlite3 
# light weight
# no DB installation
# 10000 of record to hadle.
# trail purpose 100 user can use DB can go for SQLITE
# Mainly this can be used for lower trail applicaiton test

# Its like a file db
# -->

import sqlite3
conn= sqlite3.connect("./sqlite/Books.db")
cursor = conn.cursor()
cursor.execute(
    """
    create table if NOT EXISTS book(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    price REAL,
    published_year INTEGER
   )
"""
)

cursor.execute("""
insert into book (title, author, price, published_year) 
               values ('python','jegan',100,2005)
               """)
conn.commit

cursor.execute("""
insert into book (title, author, price, published_year) 
               values ('java','raj',200,2005)
               """)
books= cursor.execute("""
    select * from book
               """)
conn.commit

for book in books:
    print(book)

cursor.execute("""
    update book set price =105 where id =1
               """)
conn.commit
cursor.execute("""
    select * from book
               """)

book1 = cursor.fetchall()
for boo in book1:
    print(boo)

conn.close