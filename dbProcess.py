from sqlalchemy import create_engine,Table,VARCHAR, Column, Integer, String , MetaData
from sqlalchemy.orm import declarative_base, sessionmaker
import sqlalchemyDbconnect
from sqlalchemy.sql import schema
import tableCreation
engine = create_engine(sqlalchemyDbconnect.url)
session = sessionmaker(bind=engine)
Session = session()

class dbProcesses:
    
    def __init__(self) -> None:
        self.userStatus = 0
    
    def inserInto(self,id,name,idStaff):
        row = tableCreation.MyTable(Id = self.id,name=self.name, isStaff = self.isStaff)
        Session.add(row)
        self.commit()
        
    def checkUserstatus(self,Id,password):
        inputId = Id
        password = password
        onlyStaff = Session.query(tableCreation.MyTable).filter(tableCreation.MyTable.isStaff == 1).all()
        for staffs in onlyStaff:
            print(onlyStaff.Id)
        for inputId in onlyStaff.Id:
            if onlyStaff.password == password and onlyStaff.isStaff == 1:
                self.userStatus = 1
    
        
        # sql_q= 'SELECT isadmin FROM Authentication where username like %s and passcode like %s'


    def commit():
        Session.commit()
        
dbProcesses.checkUserstatus('boo','NULL')