import sqlite3

connection = sqlite3.connect("./my-database.db")

cursor = connection.cursor()

sql = """
    INSERT INTO Product VALUES (4,'Django course',5000,'this is django course using python language');

"""

# sql = """
#     INSERT INTO Product VALUES (2,'kotlin course',3000,'this is kotlin course');
#     INSERT INTO Product VALUES (3,'vue course',4000,'this is vue course');
#
# """

# cursor.execute(sql)

cursor.executescript(sql)

connection.commit()

connection.close()
