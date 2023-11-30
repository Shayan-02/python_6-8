import sqlite3

connection = sqlite3.connect("./my-database.db")

cursor = connection.cursor()

sql = """
    CREATE TABLE IF NOT EXISTS Product (
        productId INTEGER ,
        productName VARCHAR (60),
        price INTEGER ,
        description VARCHAR (60)
    );
"""

cursor.execute(sql)

connection.commit()
connection.close()

# ORM => Object Relational Mapping
