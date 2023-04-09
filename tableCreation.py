from sqlalchemy import create_engine,Table,VARCHAR, Column, Integer, String , MetaData
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

Base.metadata.create_all(engine)
my_table = Table('Authentication', metadata) #, autoload=True, autoload_with=engine)
new_column = Column('password', VARCHAR(30))
alterTable = schema.AddColumn(my_table,new_column)
with engine.connect() as conn:
    conn.execute(alterTable)
users = Session.query(MyTable).all()
Session.commit()


# class dbProcesses:
    
#     def __init__(self) -> None:
#         pass
    
#     def inserInto(self,id,name,idStaff):
#         row = MyTable(Id = self.id,name=self.name, isStaff = self.isStaff)
#         Session.add(row)
#         self.commit()
        
#     def checkUserstatus(self,Id,password):
#         inputId = Id
#         password = password
#         onlyStaff = Session.query(MyTable).filter(MyTable.isStaff == 1).all()
#         for staffs in onlyStaff:
#             print(onlyStaff.Id)
        

#     def commit():
#         Session.commit()