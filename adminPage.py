from os import system, name
from tabulate import tabulate
from startpage import user
import datetime
from datetime import date

class AdminPage:
    def __init__(self,db,user:user):
        self.db = db
        self.user = user
        self.hospitalName = ""
        self.hospitalId = 0
        self.applicants=[]
        self.applicant_selected=[]
        
    def find_hospital(self):
        self.db.cursor.execute("SELECT * FROM hospitals WHERE hospitalAdmin = %s",(self.user.userName,))
        myresult = self.db.cursor.fetchall()
        self.hospitalId=myresult[0][0]
        self.hospitalName=myresult[0][1]
        
    def view_slots(self):
        self.db.cursor.execute("SELECT * FROM %s_slots",(self.hospitalId,))
        mvResult = self.db.cursor.fetchall()
        mvResult.insert(0,["Slot id","Begining (HH:MM)","Ending (HH:MM)","Total Slots","Available Slots","Date"])
        print(tabulate(mvResult,showindex='always',headers='firstrow'))
        
    def pageStarup(self):
        self.find_hospital()
        print("Hello admin, {} of hospital {} (id {})".format(self.user.userName,self.hospitalName,self.hospitalId))
        admin_case = int(input("[1] Create/View Slots \n[2] Approve Slots \n[3] Record vaccination \nchoose [1-3]:"))
        system('clear')
        if(admin_case == 1):
            self.view_slots()
            create_bool = int(input("Do you want to add a new slot? [0-1]:"))
            while(create_bool):
                if(0):
                    break
                else:
                    system("clear")
                    self.create_slot()
                    if(int(input("Do you want to continue adding? [0-1]:"))==0):
                        break
                    else:
                        pass