import pymysql

connection = pymysql.connect(
    host="172.17.0.2",
    user="root",
    password="password",
    database="mysql",
)

cursor = connection.cursor()
result = cursor.fetchall()

connection.close()