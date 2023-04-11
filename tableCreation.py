from sqlalchemy import create_engine,Table,VARCHAR, Column, Integer, String , MetaData,text
from sqlalchemy.orm import declarative_base, sessionmaker
import sqlalchemyDbconnect
from sqlalchemy.sql import schema

engine = create_engine(sqlalchemyDbconnect.url)
session = sessionmaker(bind=engine)
Session = session()
metadata = MetaData()

Base = declarative_base()
class MyTable(Base):
    __tablename__ = 'Authentication'
    Id = Column(Integer, primary_key=True)
    name = Column(String(255))
    isStaff = Column(Integer)
    password = Column(VARCHAR(30))
# metadata = MetaData()
# my_table = Table('Authentication', metadata,
#     Column('Id', Integer, primary_key=True),
#     Column('name', String(255)),
#     Column('isStaff',Integer)
# )

# new_column = Column('new_column', Integer)
# my_table = my_table.append_column(new_column)

# alter_query = text('ALTER TABLE Authentication ADD COLUMN password VARCHAR(30)')
# Session.execute(alter_query)