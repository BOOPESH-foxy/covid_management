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