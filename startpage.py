from os import system, name
import time
from tableCreation import MyTable
from sqlalchemy import create_engine, select, Table, Column, Integer, String, MetaData
from sqlalchemy.orm import sessionmaker
import pwinput
import os

class user():
    
    def __init__(self,userName,isAdmin,hospital_id=None,slotId=None,date=None) -> None:
        self.userName = userName
        self.isAdmin= isAdmin
        self.slotId = slotId
        self.hospitalId = hospital_id
        self.vaccinatedDate = date
           
           
class startPage():
    
    def __init__(self,session,metadata,engine):
        self.Session = session
        self.metadata = metadata
        self.engine = engine
   
    def getData(self):
        os.system('clear')
        print("|\t\t\t COVID VACCINATION BOOKING \t\t\t|")
        Id = int(input("\nId : \t"))
        password = pwinput.pwinput(prompt="password : ",mask ="*")
        # dbProcess.dbProcesses.checkUserstatus(Id,password)
        
    def createUser(self,Id,name,password,isStaff):
        newUser = MyTable(id = Id,name = name,password = password,isStaff = isStaff)
        self.Session.add(newUser)
        self.Session.commit()
    
    def checkCredentials(self,name,password):
        select_Statement = select(MyTable).where(MyTable.name == name and MyTable.password == password)
        with self.engine.connect() as conn:
            result = conn.execute(select_Statement).fetchone()
        if result is not None:
            print(result.value)
            return 1
        else:
            print("User not found !")
            return 0
            
            
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
                    newName:str = input("Enter your user name   :")
                    newPassword:str = input("Enter your password    :")
                    self.create_user(newName,newPassword)
                    print("Your account has been created") 
                    time.sleep(1)
                    system('clear')
                    print("redirecting to slot booking page")
                    return user(newName,0)
                except Exception as e:
                    print("exeception",e)
                    retry:str = input("Do you want to try again [Y/n]:")
                    if(retry =='n' or retry == 'N'):
                        return user(0,0)
                    else:
                        system('clear')
                        pass
                    
object = startPage()
object.pageStart()