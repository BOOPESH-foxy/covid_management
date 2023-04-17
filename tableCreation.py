from sqlalchemy import create_engine,Table,VARCHAR, Column, Integer, String , MetaData,text
from sqlalchemy.orm import declarative_base, sessionmaker
import sqlalchemyDbconnect
from sqlalchemy.sql import schema

Base = declarative_base()
class MyTable(Base):
    __tablename__ = 'Authentication'
    Id = Column(Integer, primary_key=True)
    name = Column(String(255))
    isStaff = Column(Integer)
    password = Column(VARCHAR(30))

