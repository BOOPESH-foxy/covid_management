from sqlalchemy import create_engine
import mysql.connector
import sqlalchemyDbconnect as db
import pwinput
import os
import tableCreation

class loginPage:
    def __init__(self) -> None:
        pass

    
    def getData(self):
        os.system('clear')
        print("|\t\t\t COVID VACCINATION BOOKING \t\t\t|")
        name = input("\nId : \t")
        password = pwinput.pwinput(prompt="password : ",mask ="*")
        tableCreation.dbProcesses.checkUserstatus(name,password)
    
    def pageSelection(self):
        pass
    
    
if __name__ == "__main__":
    mainObj = loginPage()
    mainObj.getData()
    