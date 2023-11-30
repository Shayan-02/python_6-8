import sqlite3

connection = sqlite3.connect("./my-database.db")

cursor = connection.cursor()

sql = """ 
    UPDATE Product SET productName="vuejs course edited" WHERE productId = 3
"""

cursor.execute(sql)

connection.commit()
connection.close()
