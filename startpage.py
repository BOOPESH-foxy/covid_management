from os import system, name
import time

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
    
    def createUser(self,name,password):
        