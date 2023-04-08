import pymysql

connection = pymysql.connect(
    host="172.17.0.2",
    user="root",
    password="password",
    database="mysql",
)

cursor = connection.cursor()
cursor.execute("create table ")
cursor.execute("SELECT * FROM my_table")
result = cursor.fetchall()

print(result)

connection.close()