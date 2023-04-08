from sqlalchemy import create_engine
import mysql.connector

url = 'mysql+mysqlconnector://root:password@172.17.0.2:3306/mysql'
engine =  create_engine(url)
connection = engine.connect()
print(connection)