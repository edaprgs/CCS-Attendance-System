# COLLEGE OF COMPUTER STUDIES ATTENDANCE SYSTEM
# GROUP 12 - CLARIN, PARAGOSO, REPE
import tkinter
from tkinter import *
import customtkinter
from PIL import Image
import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as tkMessageBox
import sqlite3

customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("blue")

class AttendanceSystemApp(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("Student Attendance System")
        self.geometry("1310x715+0+0")
        self.resizable(False, False)    

# **************************************************************** DATABASE CONNECTION ****************************************************************#
        # ESTABLISH DATABASE CONNECTION
        self.conn = sqlite3.connect('attendancesystem.db')
        self.cursor = self.conn.cursor()

        # CREATE STUDENT TABLE
        create_student = '''CREATE TABLE IF NOT EXISTS student (
            "student_ID"	TEXT NOT NULL,
            "lastName"	TEXT NOT NULL,
            "firstName"	TEXT NOT NULL,
            "midName"	TEXT NOT NULL,
            "year_level"	TEXT NOT NULL,
            "course_code"	TEXT NOT NULL,
            PRIMARY KEY("student_ID"),
            FOREIGN KEY("course_code") REFERENCES "course"("course_code")
        )'''
        self.conn.execute(create_student)

        # CREATE EVENT TABLE
        create_event = '''CREATE TABLE IF NOT EXISTS events (
            "event_ID"	TEXT NOT NULL,
            "eventName"	TEXT NOT NULL,
            "startdate"	TEXT NOT NULL,
            "enddate"	TEXT NOT NULL,
            "school_year"	TEXT NOT NULL,
            "semester"	TEXT NOT NULL,
            PRIMARY KEY("event_ID")
        )'''
        self.conn.execute(create_event)

        # CREATE EVENT LOCATIONS TABLE
        create_eventlocation = '''CREATE TABLE IF NOT EXISTS event_locations (
            "event_ID"	TEXT NOT NULL,
            "eventLocation"	TEXT NOT NULL,
            PRIMARY KEY("event_ID"),
            FOREIGN KEY("event_ID") REFERENCES "event"("event_ID")
        )'''
        self.conn.execute(create_eventlocation)

        # CREATE COURSE TABLE
        create_course = '''CREATE TABLE IF NOT EXISTS course (
            "course_code"	TEXT NOT NULL,
            "courseName"	TEXT NOT NULL,
            PRIMARY KEY("course_code")
        )'''
        self.conn.execute(create_course)

        # CREATE ATTENDS TABLE
        create_attends = '''CREATE TABLE IF NOT EXISTS attends (
            "student_ID"	TEXT NOT NULL,
            "event_ID"	TEXT NOT NULL,
            "signin_datetime"	TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
            "signout_datetime"	TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
            PRIMARY KEY("student_ID","event_ID"),
            FOREIGN KEY("student_ID") REFERENCES "student"("student_ID"),
            FOREIGN KEY("event_ID") REFERENCES "event"("event_ID")
        )'''
        self.conn.execute(create_attends)
        self.conn.commit()

#**************************************************************** MAIN SCREEN ****************************************************************#
        # BACKGROUND 
        self.mainframe = tk.Frame(self,width=1000,height=1000,background="gray1")
        self.mainframe.pack(fill="both")
        self.bg_img = customtkinter.CTkImage(light_image=Image.open("C:\\Users\\User\\Desktop\\ATTENDANCE SYSTEM\\Wolf16.jpg"),size=(500,800))
        self.label1 = customtkinter.CTkLabel(master=self.mainframe,text= "",image=self.bg_img,anchor='e')
        self.label1.pack(fill="x")
        self.eventbtn = customtkinter.CTkButton(self.mainframe,text="EVENTS",text_color="white",font=("Tahoma",15),width=100,height=35,fg_color="gray5",hover_color="gray13",command=self.eventcom)
        self.eventbtn.place(x=50,y=30)
        self.studentbtn = customtkinter.CTkButton(self.mainframe,text="STUDENTS",text_color="white",font=("Tahoma",15),width=100,height=35,fg_color="gray5",hover_color="gray13",command=self.studentcom)
        self.studentbtn.place(x=170,y=30)
        self.coursebtn = customtkinter.CTkButton(self.mainframe,text="COURSE",text_color="white",font=("Tahoma",15),width=100,height=35,fg_color="gray5",hover_color="gray13",command=self.coursecom)
        self.coursebtn.place(x=290,y=30)
        self.label2 =customtkinter.CTkLabel(self.mainframe,text="Embrace the Digital Wave, Track Your Event Journey Today!",text_color="papaya whip",font=("Helvetica",30,"bold"))
        self.label2.place(x=55,y=120)
        self.label3 =customtkinter.CTkLabel(self.mainframe,text="College of Computer Studies Attendance System",text_color="white",font=("Helvetica",25,"bold"))
        self.label3.place(x=55,y=170)
        self.label4 =customtkinter.CTkLabel(self.mainframe,text="ATTENDANCE",text_color="lightgoldenrod3",font=("Rowdies",70,"bold"))
        self.label4.place(x=55,y=220)
        self.attendancebtn =customtkinter.CTkButton(self.mainframe,text="Record Now",text_color="black",font=("Arial",20,"bold"),fg_color="lightgoldenrod4",hover=True,hover_color= "lightgoldenrod3",corner_radius=10,width=205,height=50,command=self.eventcom)
        self.attendancebtn.place(x=55,y=335)

    def tablestyle(self):
        style = ttk.Style()
        style.configure("Treeview", background="light yellow2", fg="lightgoldenrod4", rowheight=35,
                        fieldbackground="lightgoldenrod4")
        style.configure("Treeview.Heading", font=('Calibri', 15, 'bold'), height=50)
        style.configure("Treeview", highlightthickness=0, bd=0, font=('Calibri', 14))
        style.layout("Treeview", [('Treeview.treearea', {'sticky': 'nswe'})])
        style.map("Treeview", background=[("selected", "lightgoldenrod4")])

    def eventcom(self):
        self.eventframe = tk.Frame(self.mainframe,width=1150,height=810,background="gray1")
        self.eventframe.place(x=65,y=100)
        self.tabview = customtkinter.CTkTabview(master=self.eventframe,width=900,height=555)
        self.tabview.place(x=0,y=20)
        self.tabview.configure(text_color="black",fg_color="light yellow",segmented_button_fg_color="lightgoldenrod3",segmented_button_selected_color="light yellow",segmented_button_unselected_color="lightgoldenrod3",segmented_button_unselected_hover_color="light yellow",segmented_button_selected_hover_color="light yellow")
        self.tabview.add("ADD EVENT")  
        self.tabview.add("EVENTS LIST") 
        self.tabview.set("EVENTS LIST") 

    # LABELS
        self.elabel1 =customtkinter.CTkLabel(self.tabview.tab("ADD EVENT"),text="EVENT INFORMATION:",text_color="black",font=("Helvetica",16,"bold"))
        self.elabel1.place(x=45,y=45)
        self.elabel2 =customtkinter.CTkLabel(self.tabview.tab("ADD EVENT"),text="EVENT ID:",text_color="black",font=("Helvetica",15))
        self.elabel2.place(x=45,y=120)
        self.elabel3 =customtkinter.CTkLabel(self.tabview.tab("ADD EVENT"),text="EVENT NAME:",text_color="black",font=("Helvetica",15))
        self.elabel3.place(x=45,y=205)
        self.elabel3 =customtkinter.CTkLabel(self.tabview.tab("ADD EVENT"),text="START DATE:",text_color="black",font=("Helvetica",15))
        self.elabel3.place(x=45,y=295)
        self.elabel4 =customtkinter.CTkLabel(self.tabview.tab("ADD EVENT"),text="SCHOOL YEAR:",text_color="black",font=("Helvetica",15))
        self.elabel4.place(x=535,y=120)
        self.elabel5 =customtkinter.CTkLabel(self.tabview.tab("ADD EVENT"),text="END DATE:",text_color="black",font=("Helvetica",15))
        self.elabel5.place(x=45,y=380)
        self.elabel6 =customtkinter.CTkLabel(self.tabview.tab("ADD EVENT"),text="SEMESTER:",text_color="black",font=("Helvetica",15))
        self.elabel6.place(x=535,y=205)

    # ENTRIES
        self.eIDentry = customtkinter.CTkEntry(self.tabview.tab("ADD EVENT"),placeholder_text="e.g. EVENT ID",placeholder_text_color="lightgoldenrod4",border_color="lightgoldenrod2",fg_color="lightgoldenrod2",width=295,height=35)
        self.eIDentry.place(x=180,y=120)
        self.eNameentry = customtkinter.CTkEntry(self.tabview.tab("ADD EVENT"),placeholder_text="e.g. EVENT NAME",placeholder_text_color="lightgoldenrod4",border_color="lightgoldenrod2",fg_color="lightgoldenrod2",width=295,height=35)
        self.eNameentry.place(x=180,y=205)
        self.monthOM1_var = tkinter.StringVar(value="Month")
        self.monthOM1 = customtkinter.CTkOptionMenu(self.tabview.tab("ADD EVENT"),variable=self.monthOM1_var,values=["01","02","03","04","05","06","07","08","09","10","11","12"],text_color="black",dynamic_resizing=TRUE,width=90,fg_color="lightgoldenrod2",button_color="lightgoldenrod4",button_hover_color="lightgoldenrod4",dropdown_fg_color="lightgoldenrod2",dropdown_hover_color="lightgoldenrod3")
        self.monthOM1.place(x=180,y=295)
        self.dayOM1_var = tkinter.StringVar(value="Day")
        self.dayOM1 = customtkinter.CTkOptionMenu(self.tabview.tab("ADD EVENT"),variable=self.dayOM1_var,values=["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30"],text_color="black",dynamic_resizing=FALSE,width=75,fg_color="lightgoldenrod2",button_color="lightgoldenrod4",button_hover_color="lightgoldenrod4",dropdown_fg_color="lightgoldenrod2",dropdown_hover_color="lightgoldenrod3")
        self.dayOM1.place(x=295,y=295)
        self.yearOM1_var = tkinter.StringVar(value="Year")
        self.yearOM1 = customtkinter.CTkOptionMenu(self.tabview.tab("ADD EVENT"),variable=self.yearOM1_var,values=["2023","2024","2025","2026","2027","2028","2029","2030"],text_color="black",dynamic_resizing=TRUE,width=85,fg_color="lightgoldenrod2",button_color="lightgoldenrod4",button_hover_color="lightgoldenrod4",dropdown_fg_color="lightgoldenrod2",dropdown_hover_color="lightgoldenrod3")
        self.yearOM1.place(x=390,y=295)
        self.monthOM2_var = tkinter.StringVar(value="Month")
        self.monthOM2 = customtkinter.CTkOptionMenu(self.tabview.tab("ADD EVENT"),variable=self.monthOM2_var,values=["01","02","03","04","05","06","07","08","09","10","11","12"],text_color="black",dynamic_resizing=TRUE,width=90,fg_color="lightgoldenrod2",button_color="lightgoldenrod4",button_hover_color="lightgoldenrod4",dropdown_fg_color="lightgoldenrod2",dropdown_hover_color="lightgoldenrod3")
        self.monthOM2.place(x=180,y=380)
        self.dayOM2_var = tkinter.StringVar(value="Day")
        self.dayOM2 = customtkinter.CTkOptionMenu(self.tabview.tab("ADD EVENT"),variable=self.dayOM2_var,values=["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30"],text_color="black",dynamic_resizing=FALSE,width=75,fg_color="lightgoldenrod2",button_color="lightgoldenrod4",button_hover_color="lightgoldenrod4",dropdown_fg_color="lightgoldenrod2",dropdown_hover_color="lightgoldenrod3")
        self.dayOM2.place(x=295,y=380)
        self.yearOM2_var = tkinter.StringVar(value="Year")
        self.yearOM2 = customtkinter.CTkOptionMenu(self.tabview.tab("ADD EVENT"),variable=self.yearOM2_var,values=["2022","2023","2024","2025","2026","2027","2028","2029","2030"],text_color="black",dynamic_resizing=TRUE,width=85,fg_color="lightgoldenrod2",button_color="lightgoldenrod4",button_hover_color="lightgoldenrod4",dropdown_fg_color="lightgoldenrod2",dropdown_hover_color="lightgoldenrod3")
        self.yearOM2.place(x=390,y=380)
        self.schoolyearOM_var = tkinter.StringVar(value="Select")
        self.schoolyearOM = customtkinter.CTkOptionMenu(self.tabview.tab("ADD EVENT"),variable=self.schoolyearOM_var,values=["2022-2023","2023-2024","2024-2025","2025-2026","2026-2027","2027-2028","2028-2029","2029-2030","2030-2031"],text_color="black",dynamic_resizing=FALSE,width=160,fg_color="lightgoldenrod2",button_color="lightgoldenrod4",button_hover_color="lightgoldenrod4",dropdown_fg_color="lightgoldenrod2",dropdown_hover_color="lightgoldenrod3")
        self.schoolyearOM.place(x=680,y=120)
        self.semesterOM_var = tkinter.StringVar(value="Select")
        self.semesterOM = customtkinter.CTkOptionMenu(self.tabview.tab("ADD EVENT"),variable=self.semesterOM_var,values=["1ST SEMESTER","2ND SEMESTER"],text_color="black",dynamic_resizing=TRUE,width=160,fg_color="lightgoldenrod2",button_color="lightgoldenrod4",button_hover_color="lightgoldenrod4",dropdown_fg_color="lightgoldenrod2",dropdown_hover_color="lightgoldenrod3")
        self.semesterOM.place(x=680,y=205)
    # SAVE BUTTON
        self.esavebtn = customtkinter.CTkButton(self.tabview.tab("ADD EVENT"),text="ADD EVENT",font=("Helvetica",14),text_color="black",fg_color="lightgoldenrod2",border_width=2,hover=True,hover_color= "lightgoldenrod1",corner_radius=10,border_color= "lightgoldenrod2",width=100,height=35,command=self.add_event)
        self.esavebtn.place(x=640,y=295)

    #**************************************************************** EVENTS LIST TABVIEW ****************************************************************#
        self.elabel7 =customtkinter.CTkLabel(self.tabview.tab("EVENTS LIST"),text="EVENTS LIST:",text_color="black",font=("Helvetica",16,"bold"))
        self.elabel7.place(x=50,y=45)
    # SEARCH
        self.elabel8 =customtkinter.CTkLabel(self.tabview.tab("EVENTS LIST"),text="SEARCH:",text_color="black",font=("Helvetica",13))
        self.elabel8.place(x=610,y=45)
        self.esearchentry = customtkinter.CTkEntry(self.tabview.tab("EVENTS LIST"),placeholder_text="e.g. DEVCON",placeholder_text_color="lightgoldenrod4",border_color="lightgoldenrod2",fg_color="lightgoldenrod2",width=160,height=35)
        self.esearchentry.place(x=680,y=45)
    # TABLE
        self.tablestyle()
        self.table_frame = tk.Frame(self.tabview.tab("EVENTS LIST"),bg="white")
        self.table_frame.place(x=55,y=125,width=1000,height=360)
        self.y_scroll = customtkinter.CTkScrollbar(self.table_frame,orientation=VERTICAL,button_color="lightgoldenrod4",button_hover_color="lightgoldenrod3")
        self.y_scroll.pack(side=RIGHT,fill=Y)
        self.etable = ttk.Treeview(self.table_frame,yscrollcommand=self.y_scroll.set)
        self.y_scroll.configure(command=self.etable.yview)
        self.etable["columns"] = ("EVENT ID","EVENT NAME","START DATE","END DATE","SCHOOL YEAR","SEMESTER")
        self.etable.column("#0", width=0, stretch=NO)  
        self.etable.column("EVENT ID", width=100,anchor=CENTER)
        self.etable.column("EVENT NAME", width=200,anchor=CENTER)
        self.etable.column("START DATE", width=150,anchor=CENTER)
        self.etable.column("END DATE", width=150,anchor=CENTER)
        self.etable.column("SCHOOL YEAR", width=150,anchor=CENTER)
        self.etable.column("SEMESTER", width=150,anchor=CENTER)
        self.etable.heading("EVENT ID", text="EVENT ID")
        self.etable.heading("EVENT NAME", text="EVENT NAME")
        self.etable.heading("START DATE", text="START DATE")
        self.etable.heading("END DATE", text="END DATE")
        self.etable.heading("SCHOOL YEAR", text="SCHOOL YEAR")
        self.etable.heading("SEMESTER", text="SEMESTER")
        self.etable.insert("", tk.END, text="1", values=("DEVCON","DEVCON SUMMIT", "JUNE 26,2023","June 26,2023","2023-2024","1ST SEMESTER"))
        self.etable.insert("", tk.END, text="2", values=("PALAKASAN","FOUNDATION DAY", "JUNE 26,2023","June 27,2023","2023-2024","1ST SEMESTER"))
        self.etable.pack(fill=BOTH,expand=True)
    # BUTTONS
        self.eviewbtn = customtkinter.CTkButton(self.tabview.tab("EVENTS LIST"),text="VIEW ATTENDANCE",font=("Helvetica",14),text_color="black",fg_color="lightgoldenrod2",border_width=2,hover= True,hover_color= "lightgoldenrod1",corner_radius=10,border_color= "lightgoldenrod2",width=100,height=35)
        self.eviewbtn.place(x=45,y=405)
        self.eeditbtn = customtkinter.CTkButton(self.tabview.tab("EVENTS LIST"),text="EDIT EVENT",font=("Helvetica",14),text_color="black",fg_color="lightgoldenrod2",border_width=2,hover= True,hover_color= "lightgoldenrod1",corner_radius=10,border_color= "lightgoldenrod2",width=100,height=35)
        self.eeditbtn.place(x=625,y=405)
        self.edeletebtn = customtkinter.CTkButton(self.tabview.tab("EVENTS LIST"),text="delete event",font=("Helvetica",14),text_color="white",fg_color="red2",border_width=2,hover= True,hover_color= "red",corner_radius=10,border_color= "red2",width=100,height=35)
        self.edeletebtn.place(x=745,y=405)

    def clear_event_inputs(self):
        self.eIDentry.delete(0, END)
        self.eNameentry.delete(0, END)
        self.monthOM1_var.set('Month')
        self.dayOM1_var.set('Day')
        self.yearOM1_var.set('Year')
        self.monthOM2_var.set('Month')
        self.dayOM2_var.set('Day')
        self.yearOM2_var.set('Year')
        self.schoolyearOM_var.set('Select')
        self.semesterOM_var.set('Select')

    def add_event(self):
        conn = sqlite3.connect('attendancesystem.db')
        cursor = conn.cursor()
    # get the student info from the input fields
        eventID = self.eIDentry.get().upper()
        eventName = self.eNameentry.get().upper()
        month1 = str(self.monthOM1_var.get())
        day1 = str(self.dayOM1_var.get())
        year1 = str(self.yearOM1_var.get())
        start_date = month1 + "/" + day1 + "/" + year1
        month2 = str(self.monthOM2_var.get())
        day2 = str(self.dayOM2_var.get())
        year2 = str(self.yearOM2_var.get())
        end_date = month2 + "/" + day2 + "/" + year2
        school_year = str(self.schoolyearOM_var.get())
        semester = str(self.semesterOM_var.get())
    # input in database
        # Print the values for debugging
        print("Event ID:", eventID)
        print("Event Name:", eventName)
        print("Start Date:", start_date)
        print("End Date:", end_date)
        print("School Year:", school_year)
        print("Semester:", semester)
        if eventID=='' or eventName=='' or start_date=='' or end_date=='' or school_year=='' or semester=='': tkMessageBox.showwarning("Warning","Please fill the empty field!") 
        else:
            if self.event_exists(cursor, eventID):
                tkMessageBox.showerror("Error", "The event already exists!")
            else:
                data_insert_query = '''INSERT INTO events (event_ID,eventName,startdate,enddate,school_year,semester) VALUES (?,?,?,?,?,?)'''
                data_insert_tuple = (eventID,eventName,start_date,end_date,school_year,semester)
                cursor.execute(data_insert_query,data_insert_tuple)
                conn.commit()
                tkMessageBox.showinfo("Message","Event information added successfully")
        conn.close()
        self.clear_event_inputs()

    # Check if an event with the same ID already exists in the database
    def event_exists(self ,cursor, eventID):
        conn = sqlite3.connect('attendancesystem.db')
        cursor = conn.cursor()
        query = '''SELECT * FROM events WHERE event_ID = ?'''
        cursor.execute(query, (eventID,))
        conn.commit()
        if cursor.fetchone():
            return True
        conn.close()
        return False

    

    #**************************************************************** ADD STUDENT TABVIEW ****************************************************************#
    def studentcom(self):
        self.studentframe = tk.Frame(self.mainframe,width=1150,height=810,background="gray1")
        self.studentframe.place(x=65,y=100)
        self.tabview = customtkinter.CTkTabview(master=self.studentframe,width=900,height=560)
        self.tabview.place(x=0,y=20)
        self.tabview.configure(text_color="black",fg_color="light yellow",segmented_button_fg_color="lightgoldenrod3",segmented_button_selected_color="light yellow",segmented_button_unselected_color="lightgoldenrod3",segmented_button_unselected_hover_color="light yellow",segmented_button_selected_hover_color="light yellow")
        self.tabview.add("ADD STUDENT")  
        self.tabview.add("STUDENTS LIST") 
        self.tabview.set("STUDENTS LIST") 
    # LABELS
        self.slabel1 =customtkinter.CTkLabel(self.tabview.tab("ADD STUDENT"),text="STUDENT INFORMATION:",text_color="black",font=("Helvetica",16,"bold"))
        self.slabel1.place(x=45,y=45)
        self.slabel2 =customtkinter.CTkLabel(self.tabview.tab("ADD STUDENT"),text="LAST NAME:",text_color="black",font=("Helvetica",15))
        self.slabel2.place(x=45,y=120)
        self.slabel3 =customtkinter.CTkLabel(self.tabview.tab("ADD STUDENT"),text="FIRST NAME:",text_color="black",font=("Helvetica",15))
        self.slabel3.place(x=45,y=205)
        self.slabel3 =customtkinter.CTkLabel(self.tabview.tab("ADD STUDENT"),text="MIDDLE NAME:",text_color="black",font=("Helvetica",15))
        self.slabel3.place(x=45,y=295)
        self.slabel4 =customtkinter.CTkLabel(self.tabview.tab("ADD STUDENT"),text="STUDENT ID:",text_color="black",font=("Helvetica",15))
        self.slabel4.place(x=480,y=120)
        self.slabel5 =customtkinter.CTkLabel(self.tabview.tab("ADD STUDENT"),text="COURSE:",text_color="black",font=("Helvetica",15))
        self.slabel5.place(x=480,y=205)
        self.slabel6 =customtkinter.CTkLabel(self.tabview.tab("ADD STUDENT"),text="YEAR LEVEL:",text_color="black",font=("Helvetica",15))
        self.slabel6.place(x=480,y=295)
    # VARIABLES
        self.scourse_var = customtkinter.StringVar(value="Select")
        self.syearlevel_var = customtkinter.StringVar(value="Select")
    # ENTRIES
        self.slNameent = customtkinter.CTkEntry(self.tabview.tab("ADD STUDENT"),placeholder_text="e.g. PARAGOSO",placeholder_text_color="lightgoldenrod4",border_color="lightgoldenrod2",fg_color="lightgoldenrod2",width=230,height=35)
        self.slNameent.place(x=180,y=120)
        self.sfNameent = customtkinter.CTkEntry(self.tabview.tab("ADD STUDENT"),placeholder_text="e.g. EDA GRACE",placeholder_text_color="lightgoldenrod4",border_color="lightgoldenrod2",fg_color="lightgoldenrod2",width=230,height=35)
        self.sfNameent.place(x=180,y=205)
        self.smNameent = customtkinter.CTkEntry(self.tabview.tab("ADD STUDENT"),placeholder_text="e.g. JUTBA",placeholder_text_color="lightgoldenrod4",border_color="lightgoldenrod2",fg_color="lightgoldenrod2",width=230,height=35)
        self.smNameent.place(x=180,y=295)
        self.sIDent = customtkinter.CTkEntry(self.tabview.tab("ADD STUDENT"),placeholder_text="e.g. 2021-1574",placeholder_text_color="lightgoldenrod4",border_color="lightgoldenrod2",fg_color="lightgoldenrod2",width=230,height=35)
        self.sIDent.place(x=610,y=120)
        self.scourseOM = customtkinter.CTkOptionMenu(self.tabview.tab("ADD STUDENT"),variable=self.scourse_var,values=["BSCS","BSIT","BSCA","BSIS"],text_color="black",dynamic_resizing=TRUE,width=230,fg_color="lightgoldenrod2",button_color="lightgoldenrod4",button_hover_color="lightgoldenrod4",dropdown_fg_color="lightgoldenrod2",dropdown_hover_color="lightgoldenrod3")
        self.scourseOM.place(x=610,y=205)
        self.syearlevelOM = customtkinter.CTkOptionMenu(self.tabview.tab("ADD STUDENT"),variable=self.syearlevel_var,values=["1ST YEAR","2ND YEAR","3RD YEAR","4TH YEAR"],text_color="black",dynamic_resizing=TRUE,width=230,fg_color="lightgoldenrod2",button_color="lightgoldenrod4",button_hover_color="lightgoldenrod4",dropdown_fg_color="lightgoldenrod2",dropdown_hover_color="lightgoldenrod3")
        self.syearlevelOM.place(x=610,y=295)
    # SAVE BUTTON
        self.ssavebtn = customtkinter.CTkButton(self.tabview.tab("ADD STUDENT"),text="ADD STUDENT",font=("Helvetica",14),text_color="black",fg_color="lightgoldenrod2",border_width=2,hover=True,hover_color= "lightgoldenrod1",corner_radius=10,border_color= "lightgoldenrod2",width=100,height=35)
        self.ssavebtn.place(x=400,y=390)

    #**************************************************************** STUDENTS LIST TABVIEW ****************************************************************#
        self.elabel7 =customtkinter.CTkLabel(self.tabview.tab("STUDENTS LIST"),text="STUDENTS LIST:",text_color="black",font=("Helvetica",16,"bold"))
        self.elabel7.place(x=45,y=45)
    # SEARCH
        self.elabel8 =customtkinter.CTkLabel(self.tabview.tab("STUDENTS LIST"),text="SEARCH:",text_color="black",font=("Helvetica",13))
        self.elabel8.place(x=610,y=45)
        self.ssearchentry = customtkinter.CTkEntry(self.tabview.tab("STUDENTS LIST"),placeholder_text="e.g. 2021-1574",placeholder_text_color="lightgoldenrod4",border_color="lightgoldenrod2",fg_color="lightgoldenrod2",width=160,height=35)
        self.ssearchentry.place(x=680,y=45)
    # TABLE
        self.tablestyle()
        self.table_frame = tk.Frame(self.tabview.tab("STUDENTS LIST"),bg="white")
        self.table_frame.place(x=55,y=125,width=1000,height=360)
        self.y_scroll = customtkinter.CTkScrollbar(self.table_frame,orientation=VERTICAL,button_color="lightgoldenrod4",button_hover_color="lightgoldenrod3")
        self.y_scroll.pack(side=RIGHT,fill=Y)
        self.stable = ttk.Treeview(self.table_frame,yscrollcommand=self.y_scroll.set)
        self.y_scroll.configure(command=self.stable.yview)
        self.stable["columns"] = ("STUDENT ID","LAST NAME","FIRST NAME","MIDDLE NAME","COURSE","YEAR LEVEL")
        self.stable.column("#0", width=0, stretch=NO)  
        self.stable.column("STUDENT ID", width=120,anchor=CENTER)
        self.stable.column("LAST NAME", width=200,anchor=CENTER)
        self.stable.column("FIRST NAME", width=200,anchor=CENTER)
        self.stable.column("MIDDLE NAME", width=200,anchor=CENTER)
        self.stable.column("COURSE", width=130,anchor=CENTER)
        self.stable.column("YEAR LEVEL", width=130,anchor=CENTER)
        self.stable.heading("STUDENT ID", text="STUDENT ID")
        self.stable.heading("LAST NAME", text="LAST NAME")
        self.stable.heading("FIRST NAME", text="FIRST NAME")
        self.stable.heading("MIDDLE NAME", text="MIDDLE NAME")
        self.stable.heading("COURSE", text="COURSE")
        self.stable.heading("YEAR LEVEL", text="YEAR LEVEL")
        self.stable.insert("", tk.END, text="1", values=("2021-1574","PARAGOSO", "EDA GRACE","JUTBA","BSCS","2ND YEAR"))
        self.stable.insert("", tk.END, text="2", values=("2021-0622","SAYSON", "NANCY","MAHINAY","BSCS","2ND YEAR"))
        self.stable.pack(fill=BOTH,expand=True)
    # BUTTONS
        self.eeditbtn = customtkinter.CTkButton(self.tabview.tab("STUDENTS LIST"),text="EDIT STUDENT",font=("Helvetica",14),text_color="black",fg_color="lightgoldenrod2",border_width=2,hover= True,hover_color= "lightgoldenrod1",corner_radius=10,border_color= "lightgoldenrod2",width=100,height=35)
        self.eeditbtn.place(x=585,y=405)
        self.edeletebtn = customtkinter.CTkButton(self.tabview.tab("STUDENTS LIST"),text="delete student",font=("Helvetica",14),text_color="white",fg_color="red2",border_width=2,hover= True,hover_color= "red",corner_radius=10,border_color= "red2",width=100,height=35)
        self.edeletebtn.place(x=730,y=405)

    #**************************************************************** ADD COURSE TABVIEW ****************************************************************#
    def coursecom(self):
        self.courseframe = tk.Frame(self.mainframe,width=1150,height=810,background="gray1")
        self.courseframe.place(x=65,y=100)
        self.tabview = customtkinter.CTkTabview(master=self.courseframe,width=900,height=500)
        self.tabview.place(x=0,y=20)
        self.tabview.configure(text_color="black",fg_color="light yellow",segmented_button_fg_color="lightgoldenrod3",segmented_button_selected_color="light yellow",segmented_button_unselected_color="lightgoldenrod3",segmented_button_unselected_hover_color="light yellow",segmented_button_selected_hover_color="light yellow")
        self.tabview.add("ADD COURSE")  
        self.tabview.add("COURSES LIST") 
        self.tabview.set("COURSES LIST") 
    # LABELS
        self.clabel1 =customtkinter.CTkLabel(self.tabview.tab("ADD COURSE") ,text="COURSE INFORMATON:",text_color="black",font=("Helvetica",16,"bold"))
        self.clabel1.place(x=45,y=45)
        self.clabel2 =customtkinter.CTkLabel(self.tabview.tab("ADD COURSE") ,text="COURSE CODE:",text_color="black",font=("Helvetica",15))
        self.clabel2.place(x=45,y=120)
        self.clabel3 =customtkinter.CTkLabel(self.tabview.tab("ADD COURSE") ,text="COURSE NAME:",text_color="black",font=("Helvetica",15))
        self.clabel3.place(x=45,y=190)
    # ENTRIES
        self.ccodeent = customtkinter.CTkEntry(self.tabview.tab("ADD COURSE"),placeholder_text="e.g. BSCS",placeholder_text_color="lightgoldenrod4",border_color="lightgoldenrod2",fg_color="lightgoldenrod2",width=230,height=35)
        self.ccodeent.place(x=180,y=120)
        self.cnameent = customtkinter.CTkEntry(self.tabview.tab("ADD COURSE"),placeholder_text="e.g. BACHELOR OF SCIENCE IN COMPUTER SCIENCE",placeholder_text_color="lightgoldenrod4",border_color="lightgoldenrod2",fg_color="lightgoldenrod2",width=660,height=35)
        self.cnameent.place(x=180,y=190)
    # SAVE BUTTON
        self.ssavebtn = customtkinter.CTkButton(self.tabview.tab("ADD COURSE"),text="ADD COURSE",font=("Helvetica",14),text_color="black",fg_color="lightgoldenrod2",border_width=2,hover=True,hover_color= "lightgoldenrod1",corner_radius=10,border_color= "lightgoldenrod2",width=100,height=35)
        self.ssavebtn.place(x=400,y=260)

    #**************************************************************** COURSES LIST TABVIEW ****************************************************************#
        self.elabel7 =customtkinter.CTkLabel(self.tabview.tab("COURSES LIST"),text="COURSES LIST:",text_color="black",font=("Helvetica",16,"bold"))
        self.elabel7.place(x=45,y=45)
    # SEARCH
        self.elabel8 =customtkinter.CTkLabel(self.tabview.tab("COURSES LIST"),text="SEARCH:",text_color="black",font=("Helvetica",13))
        self.elabel8.place(x=610,y=45)
        self.csearchentry = customtkinter.CTkEntry(self.tabview.tab("COURSES LIST"),placeholder_text="e.g. BSCS",placeholder_text_color="lightgoldenrod4",border_color="lightgoldenrod2",fg_color="lightgoldenrod2",width=160,height=35)
        self.csearchentry.place(x=680,y=45)
    # TABLE
        self.tablestyle()
        self.table_frame = tk.Frame(self.tabview.tab("COURSES LIST"),bg="white")
        self.table_frame.place(x=55,y=120,width=1000,height=290)
        self.y_scroll = customtkinter.CTkScrollbar(self.table_frame,orientation=VERTICAL,button_color="lightgoldenrod4",button_hover_color="lightgoldenrod3")
        self.y_scroll.pack(side=RIGHT,fill=Y)
        self.ctable = ttk.Treeview(self.table_frame,yscrollcommand=self.y_scroll.set)
        self.y_scroll.configure(command=self.ctable.yview)
        self.ctable["columns"] = ("COURSE CODE","COURSE NAME")
        self.ctable.column("#0", width=0, stretch=NO)  
        self.ctable.column("COURSE CODE", width=50,anchor=CENTER)
        self.ctable.column("COURSE NAME", width=400,anchor=CENTER)
        self.ctable.heading("COURSE CODE", text="COURSE CODE")
        self.ctable.heading("COURSE NAME", text="COURSE NAME")
        self.ctable.insert("", tk.END, text="1", values=("BSCS","BACHELOR OF SCIENCE IN COMPUTER SCIENCE"))
        self.ctable.insert("", tk.END, text="2", values=("BSCA","BACHELOR OF SCIENCE IN COMPUTER APPLICATIONS"))
        self.ctable.insert("", tk.END, text="3", values=("BSIS","BACHELOR OF SCIENCE IN INFORMATION SYSTEM"))
        self.ctable.insert("", tk.END, text="4", values=("BSIT","BACHELOR OF SCIENCE IN INFORMATION TECHNOLOGY"))
        self.ctable.pack(fill=BOTH,expand=True)
    # BUTTONS
        self.eeditbtn = customtkinter.CTkButton(self.tabview.tab("COURSES LIST"),text="EDIT COURSE",font=("Helvetica",14),text_color="black",fg_color="lightgoldenrod2",border_width=2,hover= True,hover_color= "lightgoldenrod1",corner_radius=10,border_color= "lightgoldenrod2",width=100,height=35)
        self.eeditbtn.place(x=595,y=345)
        self.edeletebtn = customtkinter.CTkButton(self.tabview.tab("COURSES LIST"),text="delete course",font=("Helvetica",14),text_color="white",fg_color="red2",border_width=2,hover= True,hover_color= "red",corner_radius=10,border_color= "red2",width=100,height=35)
        self.edeletebtn.place(x=730,y=345)

if __name__ == "__main__":
    app = AttendanceSystemApp()
    app.mainloop()
