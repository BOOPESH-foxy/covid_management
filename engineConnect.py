# connection to the sql container running on linux terminal using pymysql

import pymysql

connection = pymysql.connect(
    host="172.17.0.2",
    user="root",
    password="password",
    database="mysql",
)
