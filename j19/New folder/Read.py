import sqlite3

connection = sqlite3.connect("./my-database.db")

cursor = connection.cursor()

# sql = """
#     SELECT * FROM Product WHERE productId = 8
# """

sql = """
    SELECT * FROM Product WHERE description LIKE "%python%"
"""

cursor.execute(sql)

for product in cursor:
    print(product)

connection.commit()
connection.close()
