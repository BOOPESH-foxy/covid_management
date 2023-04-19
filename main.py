from sqlalchemy import create_engine
import sqlalchemyDbconnect,adminPage
import pwinput
from os import  system
from sqlalchemy import create_engine,Table,VARCHAR, Column, Integer, String , MetaData,text
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.sql import schema
import utilClass as Uc
from startpage import startPage,user

engine = create_engine(sqlalchemyDbconnect.url)
session = sessionmaker(bind=engine)
Session = session()
metadata = MetaData() 
    
if __name__ == "__main__":
    sql = Uc(session)
    start_page = startPage(Session,metadata,engine=engine)
    start_Result:user = start_page.getData()
    system('clear')
    if(start_Result.userName != 0):
            if(start_Result.isStaff == 1):
                admin_page = adminPage(sql,start_Result)
                admin_page.page_start()
            else:
                pass
    else:
        print("Login failed")