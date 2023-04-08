from sqlalchemy import create_engine
import mysql.connector
import sqlalchemyDbconnect as db

engine = create_engine(url = db.url)
conn = engine.connect()
result = conn.execute('SELECT * FROM Authentication')

for row in result:
    print(row)
conn.close()