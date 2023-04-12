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
    
    def checkCredentials(self,name,password):
        pass
    
    def pageStart(self):
        
        login = int(input("[1] Login \n[2] Signup \nchoose [1-2]:"))
        system("clear")
        if(login == 1):
            name = str(input("Enter your user name:"))
            passwd = str(input("Enter your password:"))
            result = self.checkCredentials(name,passwd)
            return result
        elif(login == 2):
            while True:
                try:
                    new_name:str = input("Enter your user name:")
                    new_pass:str = input("Enter your password:")
                    self.create_user(new_name,new_pass)
                    print("Your account has been created \n redirecting you to slot booking page")
                    time.sleep(1)
                    return user(new_name,0)
                except Exception as e:
                    print("exeception",e)
                    retry:str = input("Do you want to try again [Y/n]:")
                    if(retry =='n'):
                        return user(0,0)
                    else:
                        system('clear')
                        pass