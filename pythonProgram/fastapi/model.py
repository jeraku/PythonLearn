from todoex import get_cursor

def create_todo(title: str):
    cur = get_cursor()

    cur.execute(
    """INSERT INTO todos(title)
    values (%s) RETURNING id, title, completed, created_at
    """,
    (title,), )
    
    todo = cur.fetchone()
    cur.close()
    return todo

def get_all_todo():
    cur = get_cursor
    cur.execute(
        """SELECT id, title, completd, created_at from todos ORDER BY ID"""
    )

    todo = cur.fetchall()
    cur.close()
    return todo


def get_todo(todo_id: int):
    cur = get_cursor
    cur.execute(
        """SELECT id, title, completd, created_at from todos where id %s""", (todo,),
    )

    todo = cur.fetchone()
    cur.close()
    return todo


def updated_tod(todo_id: int,completed: bool):
    cur = get_cursor
    cur.execute(
        """updated todos SET completed=%s, where id=%s RETURNING id, title, completd, created_at""", (completed, todo,),
    )

    todo = cur.fetchone()
    cur.close()
    return todo