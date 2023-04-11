from os import system, name
import time
import tableCreation
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class user():
    
    def __init__(self,userName,isAdmin,hospital_id=None,slotId=None,date=None) -> None:
        self.userName = userName
        self.isAdmin= isAdmin
        self.slotId = slotId
        self.hospitalId = hospital_id
        self.vaccinatedDate = date
            
class startPage():
    def __init__(self,Session):
        self.Session = Session
    
    def createUser(self,Id,name,password,isStaff):
        newUser = tableCreation.MyTable(id = Id,name = name,password = password,isStaff = isStaff)
        self.Session.add(newUser)
        self.Session.commit()
