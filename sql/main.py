import sqlite3

conn = sqlite3.connect("mydb.db")
cur = conn.cursor()

sql = """
    create table if not exists persons (
    id integer primary key autoincrement not null,
    p_name varchar(20) not null,
    p_id integer not null,
    p_age integer not null
    )
"""

cur.execute(sql)
cur.close()