import psycopg2

def run_select_query(query):
    try:
        conn = psycopg2.connect(
            dbname="mydatabase",
            user="admin",
            password="admin",
            host="localhost",
            port="5432"
        )
        cur = conn.cursor()
        cur.execute(query)
        results = cur.fetchall()
        cur.close()
        conn.close()
        return results
    except Exception as e:
        print(f"❌ Error: {e}")
        return []