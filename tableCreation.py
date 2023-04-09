from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker
import sqlalchemyDbconnect

engine = create_engine(sqlalchemyDbconnect.url)
session = sessionmaker(bind=engine)
Session = session()

Base = declarative_base()
class MyTable(Base):
    __tablename__ = 'Authentication'
    Id = Column(Integer, primary_key=True)
    name = Column(String(255))
    isStaff = Column(Integer)

Base.metadata.create_all(engine)

users = Session.query(MyTable).all()
for user in users:
    print(user.Id, user.name,)

class dbProcesses:
    
    def __init__(self,Id,name,isStaff) -> None:
        self.id = Id
        self.name = name
        self.isStaff = isStaff
    
    def inserInto(self):
        row = MyTable(Id = self.id,name=self.name, isStaff = self.isStaff)
        Session.add(row)
        self.commit()
        
    def checkUserstatus(self):
        onlyStaff = Session.query(MyTable).filter(MyTable.isStaff == 1).all()
        for staffs in active_employees:
            print(employee.name)
    
    def commit():
        Session.commit()