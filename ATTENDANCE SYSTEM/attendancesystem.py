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
import datetime

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
        conn = sqlite3.connect('attendancesystem.db')
        cursor = conn.cursor()
    # CREATE COURSE TABLE
        create_course = '''CREATE TABLE IF NOT EXISTS course (
            course_code	TEXT NOT NULL,
            courseName	TEXT NOT NULL,
            PRIMARY KEY(course_code))'''
        cursor.execute(create_course)

    # CREATE STUDENT TABLE
        create_student = '''CREATE TABLE IF NOT EXISTS student (
            student_ID	TEXT NOT NULL,
            lastName	TEXT NOT NULL,
            firstName	TEXT NOT NULL,
            midName	TEXT NOT NULL,
            year_level	TEXT NOT NULL,
            course_code	TEXT NOT NULL,
            PRIMARY KEY("student_ID"),
            FOREIGN KEY("course_code") REFERENCES course(course_code))'''
        cursor.execute(create_student)

    # CREATE EVENT TABLE
        create_event = '''CREATE TABLE IF NOT EXISTS events (
            event_ID	TEXT NOT NULL,
            eventName	TEXT NOT NULL,
            startdate	TEXT NOT NULL,
            enddate	TEXT NOT NULL,
            school_year	TEXT NOT NULL,
            semester	TEXT NOT NULL,
            PRIMARY KEY(event_ID))'''
        cursor.execute(create_event)

    # CREATE EVENT LOCATIONS TABLE
        create_eventlocation = '''CREATE TABLE IF NOT EXISTS event_locations (
            event_ID	TEXT NOT NULL,
            eventLocation	TEXT NOT NULL,
            FOREIGN KEY(event_ID) REFERENCES events(event_ID),
            PRIMARY KEY(event_ID))'''
        cursor.execute(create_eventlocation)

    # CREATE ATTENDANCE TABLE 
        create_attendance = '''CREATE TABLE IF NOT EXISTS attendance (
            student_ID	TEXT NOT NULL,
            event_ID	TEXT NOT NULL,
            signin_datetime	TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
            signout_datetime	TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
            PRIMARY KEY(student_ID,event_ID),
            FOREIGN KEY(student_ID) REFERENCES student(student_ID),
            FOREIGN KEY(event_ID) REFERENCES events(event_ID))'''
        cursor.execute(create_attendance)
        conn.commit()

#**************************************************************** MAIN WINDOW ****************************************************************#
    # BACKGROUND 
        self.mainframe = tk.Frame(self,width=1000,height=1000,background="gray1")
        self.mainframe.pack(fill="both")
        self.bg_img = customtkinter.CTkImage(light_image=Image.open("C:\\Users\\User\\Desktop\\ATTENDANCE SYSTEM\\Wolf16.jpg"),size=(500,800))
        self.label1 = customtkinter.CTkLabel(master=self.mainframe,text= "",image=self.bg_img,anchor='e')
        self.label1.pack(fill="x")
        self.eventbtn = customtkinter.CTkButton(self.mainframe,text="EVENTS",text_color="white",font=("Tahoma",16),width=100,height=40,fg_color="gray10",hover_color="gray15",command=self.eventcom)
        self.eventbtn.place(x=50,y=30)
        self.studentbtn = customtkinter.CTkButton(self.mainframe,text="STUDENTS",text_color="white",font=("Tahoma",16),width=100,height=40,fg_color="gray10",hover_color="gray15",command=self.studentcom)
        self.studentbtn.place(x=170,y=30)
        self.coursebtn = customtkinter.CTkButton(self.mainframe,text="COURSE",text_color="white",font=("Tahoma",16),width=100,height=40,fg_color="gray10",hover_color="gray15",command=self.coursecom)
        self.coursebtn.place(x=290,y=30)
        self.label2 =customtkinter.CTkLabel(self.mainframe,text="MSU-ILIGAN INSTITUTE OF TECHNOLOGY",text_color="papaya whip",font=("Helvetica",40,"bold"))
        self.label2.place(x=55,y=150)
        self.label3 =customtkinter.CTkLabel(self.mainframe,text="College of Computer Studies",text_color="white",font=("Helvetica",35,"bold"))
        self.label3.place(x=55,y=200)
        self.label4 =customtkinter.CTkLabel(self.mainframe,text="ATTENDANCE SYSTEM",text_color="lightgoldenrod3",font=("Rowdies",65,"bold"))
        self.label4.place(x=55,y=300)
        self.attendancebtn =customtkinter.CTkButton(self.mainframe,text="Mark Attendance",text_color="black",font=("Arial",20,"bold"),fg_color="lightgoldenrod3",hover=True,hover_color= "lightgoldenrod2",corner_radius=25,width=205,height=50,command=self.eventcom)
        self.attendancebtn.place(x=55,y=415)

    # TABLE STYLE CONFIGURATION
    def tablestyle(self):
        style = ttk.Style()
        style.configure("Treeview", background="light yellow2", fg="lightgoldenrod4", rowheight=35,
                        fieldbackground="lightgoldenrod4")
        style.configure("Treeview.Heading", font=('Calibri', 15, 'bold'), height=50)
        style.configure("Treeview", highlightthickness=0, bd=0, font=('Calibri', 14))
        style.layout("Treeview", [('Treeview.treearea', {'sticky': 'nswe'})])
        style.map("Treeview", background=[("selected", "lightgoldenrod4")])






# *********** EVENT *********** EVENT *********** EVENT *********** EVENT *********** EVENT *********** EVENT *********** #
    def eventcom(self):
        self.eventframe = tk.Frame(self.mainframe,width=1150,height=810,background="gray1")
        self.eventframe.place(x=65,y=100)
        self.tabview = customtkinter.CTkTabview(master=self.eventframe,width=900,height=555)
        self.tabview.place(x=0,y=20)
        self.tabview.configure(text_color="black",fg_color="light yellow",segmented_button_fg_color="lightgoldenrod3",segmented_button_selected_color="light yellow",segmented_button_unselected_color="lightgoldenrod3",segmented_button_unselected_hover_color="light yellow",segmented_button_selected_hover_color="light yellow")
        self.tabview.add("EVENTS")  
        self.tabview.add("ADD EVENT") 
        self.tabview.set("EVENTS") 
    # LABELS
        self.elabel1 =customtkinter.CTkLabel(self.tabview.tab("ADD EVENT"),text="EVENT INFORMATION:",text_color="black",font=("Helvetica",16,"bold"))
        self.elabel1.place(x=45,y=45)
        self.elabel3 =customtkinter.CTkLabel(self.tabview.tab("ADD EVENT"),text="EVENT:",text_color="black",font=("Helvetica",15))
        self.elabel3.place(x=45,y=120)
        self.elabel3 =customtkinter.CTkLabel(self.tabview.tab("ADD EVENT"),text="START DATE:",text_color="black",font=("Helvetica",15))
        self.elabel3.place(x=45,y=205)
        self.elabel4 =customtkinter.CTkLabel(self.tabview.tab("ADD EVENT"),text="SCHOOL YEAR:",text_color="black",font=("Helvetica",15))
        self.elabel4.place(x=535,y=120)
        self.elabel5 =customtkinter.CTkLabel(self.tabview.tab("ADD EVENT"),text="END DATE:",text_color="black",font=("Helvetica",15))
        self.elabel5.place(x=45,y=295)
        self.elabel6 =customtkinter.CTkLabel(self.tabview.tab("ADD EVENT"),text="SEMESTER:",text_color="black",font=("Helvetica",15))
        self.elabel6.place(x=535,y=205)
        self.elabel7 =customtkinter.CTkLabel(self.tabview.tab("ADD EVENT"),text="LOCATION:",text_color="black",font=("Helvetica",15))
        self.elabel7.place(x=535,y=295)
    # ENTRIES
        self.eNameentry = customtkinter.CTkEntry(self.tabview.tab("ADD EVENT"),placeholder_text="e.g. EVENT NAME",placeholder_text_color="lightgoldenrod4",border_color="lightgoldenrod2",fg_color="lightgoldenrod2",width=295,height=35)
        self.eNameentry.place(x=180,y=120)
        self.monthOM1_var = tkinter.StringVar(value="Month")
        self.monthOM1 = customtkinter.CTkOptionMenu(self.tabview.tab("ADD EVENT"),variable=self.monthOM1_var,values=["01","02","03","04","05","06","07","08","09","10","11","12"],text_color="black",dynamic_resizing=TRUE,width=90,fg_color="lightgoldenrod2",button_color="lightgoldenrod4",button_hover_color="lightgoldenrod4",dropdown_fg_color="lightgoldenrod2",dropdown_hover_color="lightgoldenrod3")
        self.monthOM1.place(x=180,y=205)
        self.dayOM1_var = tkinter.StringVar(value="Day")
        self.dayOM1 = customtkinter.CTkOptionMenu(self.tabview.tab("ADD EVENT"),variable=self.dayOM1_var,values=["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30"],text_color="black",dynamic_resizing=FALSE,width=75,fg_color="lightgoldenrod2",button_color="lightgoldenrod4",button_hover_color="lightgoldenrod4",dropdown_fg_color="lightgoldenrod2",dropdown_hover_color="lightgoldenrod3")
        self.dayOM1.place(x=295,y=205)
        self.yearOM1_var = tkinter.StringVar(value="Year")
        self.yearOM1 = customtkinter.CTkOptionMenu(self.tabview.tab("ADD EVENT"),variable=self.yearOM1_var,values=["2023","2024","2025","2026","2027","2028","2029","2030"],text_color="black",dynamic_resizing=TRUE,width=85,fg_color="lightgoldenrod2",button_color="lightgoldenrod4",button_hover_color="lightgoldenrod4",dropdown_fg_color="lightgoldenrod2",dropdown_hover_color="lightgoldenrod3")
        self.yearOM1.place(x=390,y=205)
        self.monthOM2_var = tkinter.StringVar(value="Month")
        self.monthOM2 = customtkinter.CTkOptionMenu(self.tabview.tab("ADD EVENT"),variable=self.monthOM2_var,values=["01","02","03","04","05","06","07","08","09","10","11","12"],text_color="black",dynamic_resizing=TRUE,width=90,fg_color="lightgoldenrod2",button_color="lightgoldenrod4",button_hover_color="lightgoldenrod4",dropdown_fg_color="lightgoldenrod2",dropdown_hover_color="lightgoldenrod3")
        self.monthOM2.place(x=180,y=295)
        self.dayOM2_var = tkinter.StringVar(value="Day")
        self.dayOM2 = customtkinter.CTkOptionMenu(self.tabview.tab("ADD EVENT"),variable=self.dayOM2_var,values=["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30"],text_color="black",dynamic_resizing=FALSE,width=75,fg_color="lightgoldenrod2",button_color="lightgoldenrod4",button_hover_color="lightgoldenrod4",dropdown_fg_color="lightgoldenrod2",dropdown_hover_color="lightgoldenrod3")
        self.dayOM2.place(x=295,y=295)
        self.yearOM2_var = tkinter.StringVar(value="Year")
        self.yearOM2 = customtkinter.CTkOptionMenu(self.tabview.tab("ADD EVENT"),variable=self.yearOM2_var,values=["2023","2024","2025","2026","2027","2028","2029","2030"],text_color="black",dynamic_resizing=TRUE,width=85,fg_color="lightgoldenrod2",button_color="lightgoldenrod4",button_hover_color="lightgoldenrod4",dropdown_fg_color="lightgoldenrod2",dropdown_hover_color="lightgoldenrod3")
        self.yearOM2.place(x=390,y=295)
        self.schoolyearOM_var = tkinter.StringVar(value="Select")
        self.schoolyearOM = customtkinter.CTkOptionMenu(self.tabview.tab("ADD EVENT"),variable=self.schoolyearOM_var,values=["2022-2023","2023-2024","2024-2025","2025-2026","2026-2027","2027-2028","2028-2029","2029-2030","2030-2031"],text_color="black",dynamic_resizing=FALSE,width=160,fg_color="lightgoldenrod2",button_color="lightgoldenrod4",button_hover_color="lightgoldenrod4",dropdown_fg_color="lightgoldenrod2",dropdown_hover_color="lightgoldenrod3")
        self.schoolyearOM.place(x=680,y=120)
        self.semesterOM_var = tkinter.StringVar(value="Select")
        self.semesterOM = customtkinter.CTkOptionMenu(self.tabview.tab("ADD EVENT"),variable=self.semesterOM_var,values=["1ST SEMESTER","2ND SEMESTER"],text_color="black",dynamic_resizing=TRUE,width=160,fg_color="lightgoldenrod2",button_color="lightgoldenrod4",button_hover_color="lightgoldenrod4",dropdown_fg_color="lightgoldenrod2",dropdown_hover_color="lightgoldenrod3")
        self.semesterOM.place(x=680,y=205)
        self.location = customtkinter.CTkEntry(self.tabview.tab("ADD EVENT"),placeholder_text="e.g. LOCATION",placeholder_text_color="lightgoldenrod4",border_color="lightgoldenrod2",fg_color="lightgoldenrod2",width=160,height=35)
        self.location.place(x=680,y=295)
    # SAVE BUTTON
        self.esavebtn = customtkinter.CTkButton(self.tabview.tab("ADD EVENT"),text="ADD EVENT",font=("Helvetica",14),text_color="black",fg_color="lightgoldenrod2",border_width=2,hover=True,hover_color= "lightgoldenrod1",corner_radius=10,border_color= "lightgoldenrod2",width=100,height=35,command=self.add_event)
        self.esavebtn.place(x=390,y=385)

#**************************************************************** EVENTS LIST TABVIEW ****************************************************************#
        self.elabel7 =customtkinter.CTkLabel(self.tabview.tab("EVENTS"),text="EVENTS:",text_color="black",font=("Helvetica",16,"bold"))
        self.elabel7.place(x=50,y=45)
    # SEARCH
        self.elabel8 =customtkinter.CTkLabel(self.tabview.tab("EVENTS"),text="SEARCH:",text_color="black",font=("Helvetica",13))
        self.elabel8.place(x=610,y=45)
        self.esearch_var = StringVar()
        self.esearchentry = customtkinter.CTkEntry(self.tabview.tab("EVENTS"),textvariable=self.esearch_var,placeholder_text="e.g. ####-####",placeholder_text_color="lightgoldenrod4",border_color="lightgoldenrod2",fg_color="lightgoldenrod2",width=160,height=35)
        self.esearchentry.place(x=680,y=45)
        self.esearchentry.bind("<KeyRelease>", self.search_event)

# ******** LIST OF EVENTS
        self.tablestyle()
        self.table_frame = tk.Frame(self.tabview.tab("EVENTS"),bg="white")
        self.table_frame.place(x=55,y=125,width=1000,height=360)
        self.y_scroll = customtkinter.CTkScrollbar(self.table_frame,orientation=VERTICAL,button_color="lightgoldenrod4",button_hover_color="lightgoldenrod3",fg_color="light yellow")
        self.y_scroll.pack(side=RIGHT,fill=Y)
        self.etable = ttk.Treeview(self.table_frame,yscrollcommand=self.y_scroll.set)
        self.y_scroll.configure(command=self.etable.yview)
        self.etable["columns"] = ("event_ID","eventName","startDate","endDate","school_year","semester","eventLocation")
        self.etable.column("#0", width=0, stretch=NO)  
        self.etable.column("event_ID", width=10,anchor=CENTER)
        self.etable.column("eventName", width=200,anchor=CENTER)
        self.etable.column("startDate", width=80,anchor=CENTER)
        self.etable.column("endDate", width=80,anchor=CENTER)
        self.etable.column("school_year", width=100,anchor=CENTER)
        self.etable.column("semester", width=100,anchor=CENTER)
        self.etable.column("eventLocation", width=150,anchor=CENTER)
        self.etable.heading("event_ID", text="#")
        self.etable.heading("eventName", text="EVENT")
        self.etable.heading("startDate", text="START DATE")
        self.etable.heading("endDate", text="END DATE")
        self.etable.heading("school_year", text="SCHOOL YEAR")
        self.etable.heading("semester", text="SEMESTER")
        self.etable.heading("eventLocation", text="LOCATION")
        self.etable.pack(fill=BOTH,expand=True)
    # FETCH DATA FROM DATABASE AND DISPLAY ON THE TABLE
        conn = sqlite3.connect('attendancesystem.db')
        cursor = conn.cursor()
        display_data_query = cursor.execute("SELECT events.event_ID, events.eventName, events.startDate, events.endDate, events.school_year, events.semester, event_locations.eventLocation FROM events JOIN event_locations ON events.event_ID = event_locations.event_ID ORDER BY events.event_ID ASC")
        fetch = display_data_query.fetchall()
        for data in fetch:
            self.etable.insert('', 'end', values=(data[0], data[1], data[2], data[3], data[4], data[5],data[6]))
        conn.commit()
        conn.close()
    # BUTTONS
        self.eviewbtn = customtkinter.CTkButton(self.tabview.tab("EVENTS"),text="VIEW ATTENDANCE",font=("Helvetica",14),text_color="white",fg_color="lightgoldenrod4",border_width=2,hover= True,hover_color= "khaki4",corner_radius=10,border_color= "lightgoldenrod4",width=100,height=35,command=self.view_attendance)
        self.eviewbtn.place(x=45,y=405)
        self.eeditbtn = customtkinter.CTkButton(self.tabview.tab("EVENTS"),text="EDIT EVENT",font=("Helvetica",14),text_color="black",fg_color="lightgoldenrod2",border_width=2,hover= True,hover_color= "lightgoldenrod1",corner_radius=10,border_color= "lightgoldenrod2",width=100,height=35,command=self.edit_event)
        self.eeditbtn.place(x=625,y=405)
        self.edeletebtn = customtkinter.CTkButton(self.tabview.tab("EVENTS"),text="delete event",font=("Helvetica",14),text_color="white",fg_color="red2",border_width=2,hover= True,hover_color= "red",corner_radius=10,border_color= "red2",width=100,height=35,command=self.delete_event)
        self.edeletebtn.place(x=745,y=405)
        self.eupdatebtn = customtkinter.CTkButton(self.tabview.tab("EVENTS"),text="REFRESH",font=("Helvetica",14),text_color="black",fg_color="lightgoldenrod2",border_width=2,hover= True,hover_color= "lightgoldenrod1",corner_radius=10,border_color= "lightgoldenrod2",width=100,height=35,command=self.update_event_table)
        self.eupdatebtn.place(x=510,y=405)

    # UPDATE EVENT TABLE
    def update_event_table(self):
        conn = sqlite3.connect('attendancesystem.db')
        cursor = conn.cursor() 
        self.etable.delete(*self.etable.get_children())
        display_data_query = cursor.execute("SELECT events.event_ID, events.eventName, events.startDate, events.endDate, events.school_year, events.semester, event_locations.eventLocation FROM events JOIN event_locations ON events.event_ID = event_locations.event_ID ORDER BY events.event_ID ASC")
        fetch = display_data_query.fetchall()
        for data in fetch:
            self.etable.insert('', 'end', values=(data[0],data[1],data[2],data[3],data[4],data[5],data[6]))
        conn.commit()
        conn.close()

# ******** SEARCH EVENT
    def search_event(self,ev):
        conn = sqlite3.connect('attendancesystem.db')
        cursor = conn.cursor() 
        event_name = self.esearchentry.get()
        if event_name != "":      
            self.etable.delete(*self.etable.get_children())
            search_event_query = "SELECT events.*, event_locations.eventLocation FROM events JOIN event_locations ON events.event_ID = event_locations.event_ID WHERE events.eventName LIKE ?"
            cursor.execute(search_event_query, ('%' + event_name + '%',))
            events = cursor.fetchall()
            for event in events:
                self.etable.insert("", "end", values=event)
            conn.close()

    def clear_event_inputs(self):
        self.eNameentry.delete(0, END)
        self.monthOM1_var.set('Month')
        self.dayOM1_var.set('Day')
        self.yearOM1_var.set('Year')
        self.monthOM2_var.set('Month')
        self.dayOM2_var.set('Day')
        self.yearOM2_var.set('Year')
        self.schoolyearOM_var.set('Select')
        self.semesterOM_var.set('Select')
        self.location.delete(0, END)

# ******** ADD EVENT
    def add_event(self):
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
        location = self.location.get().upper()

        # PRINT VALUES FOR DEBUGGING
        print("Event Name:", eventName)
        print("Start Date:", start_date)
        print("End Date:", end_date)
        print("School Year:", school_year)
        print("Semester:", semester)
        print("Location:",location)

        if eventName == '' or start_date == '' or end_date == '' or school_year == '' or semester == '' or location == '':
            tkMessageBox.showwarning("Warning", "Please fill in all the fields!")
        else:
            conn = sqlite3.connect('attendancesystem.db')
            cursor = conn.cursor()
            # CHECK IF THERE EXIST AN EVENT WITH THE SAME NAME AND LOCATION
            event_exists_query = "SELECT events.event_ID FROM events JOIN event_locations ON events.event_ID = event_locations.event_ID WHERE events.eventName = ? AND event_locations.eventLocation = ?"
            cursor.execute(event_exists_query, (eventName, location))
            existing_event = cursor.fetchone()

            if existing_event:
                tkMessageBox.showerror("Error", "An event with the same name and location already exists.")
                return
                
            # INSERT THE DATA TO THE EVENTS TABLE
            else:
                data_insert_query = '''INSERT INTO events (eventName, startdate, enddate, school_year, semester) VALUES (?, ?, ?, ?, ?)'''
                cursor.execute(data_insert_query, (eventName, start_date, end_date, school_year, semester))
                conn.commit()
                # RETRIEVE THE ID OF THE NEWLY ADDED EVENT
                event_id = cursor.lastrowid
                # INSERT THE LOCATION INTO THE EVENT LOCATIONS TABLE
                location_insert_query = '''INSERT INTO event_locations (event_ID, eventLocation) VALUES (?, ?)'''
                cursor.execute(location_insert_query, (event_id, location))
                conn.commit()
                tkMessageBox.showinfo("Message", "Event information added successfully")

        self.clear_event_inputs()
        self.update_event_table()
        conn.close()

# ******** DELETE EVENT
    def delete_event(self):
        if not self.etable.selection():
            tkMessageBox.showerror("Error", "No item selected. Please select an event from the table.")
            return

        decision = tkMessageBox.askquestion("Warning", "Are you sure you want to delete the selected event?")
        if decision != 'yes':
            return
        else:
            selected_item = self.etable.focus()
            item_values = self.etable.item(selected_item)['values']
            event_id = item_values[0]
            try:
                conn = sqlite3.connect('attendancesystem.db')
                cursor = conn.cursor()

                # CHECK IF THE EVENT HAS ATTENDANCE RECORDS
                query = "SELECT COUNT(*) FROM attendance WHERE event_ID = ?"
                cursor.execute(query, (event_id,))
                attendance_count = cursor.fetchone()[0]
                if attendance_count > 0:
                    tkMessageBox.showerror("Error", "The event has attendance records. Event cannot be deleted.")
                    conn.close()
                    return

                # CHECK IF THE START DATE MATCHES THE CURRENT DATE
                current_date = datetime.datetime.now().date()
                start_date = datetime.datetime.strptime(item_values[2], "%m/%d/%Y").date()
                if start_date <= current_date:
                    tkMessageBox.showerror("Error", "Cannot delete the event. The event has already started.")
                    conn.close()
                    return

                # DELETE THE EVENT IF IT DOES NOT CONFORM WITH THE CONDITIONS
                delete_event_query = "DELETE FROM events WHERE event_ID = ?"
                delete_location_query = "DELETE FROM event_locations WHERE event_ID = ?"
                cursor.execute(delete_event_query, (event_id,))
                cursor.execute(delete_location_query, (event_id,))
                conn.commit()

                # REMOVE THE EVENT FROM THE TABLE
                self.etable.delete(selected_item)
                tkMessageBox.showinfo("Message", "The event has been deleted successfully!")
            except sqlite3.Error as e:
                tkMessageBox.showerror("Error", "An error has occurred: {}".format(str(e)))
            finally:
                conn.close()
            self.update_event_table()

# ******** EDIT EVENT
    def update_event_info(self):
        decision = tkMessageBox.askyesno("Warning", "Are you sure you want to make changes in the event information?")
        if not decision:
            tkMessageBox.showinfo("Message", "The changes have not been saved")
            return

        conn = sqlite3.connect('attendancesystem.db')
        cursor = conn.cursor()

        selected_event = self.etable.focus()
        id_details = str(self.etable.item(selected_event)['values'][0])
        event_ID = str(id_details)

        start_date = "{}/{}/{}".format(self.monthOM1_var.get(), self.dayOM1_var.get(), self.yearOM1_var.get())
        end_date = "{}/{}/{}".format(self.monthOM2_var.get(), self.dayOM2_var.get(), self.yearOM2_var.get())

        if not self.eentry1.get().strip():
            tkMessageBox.showwarning("Warning", "Event name cannot be empty")
            return
        
        new_event_name = self.eentry1.get().upper()
        new_event_location = self.elocation.get().upper()
        new_school_year = self.schoolyearOM_var.get()
        new_semester = self.semesterOM_var.get()

        # CHECK IF THERE IS AN EVENT WITH THE SAME NAME AND LOCATION
        check_query = '''SELECT events.event_ID FROM events JOIN event_locations ON events.event_ID = event_locations.event_ID WHERE eventName = ? AND eventLocation = ? AND events.event_ID != ?'''
        cursor.execute(check_query, (new_event_name, new_event_location, event_ID))
        existing_event = cursor.fetchone()

        if existing_event:
            tkMessageBox.showerror("Error", "An event with the same name and location already exists.")
            return

        update_event_query = '''UPDATE events SET eventName = ?, startdate = ?, enddate = ?, school_year = ?, semester = ? WHERE event_ID = ?'''
        cursor.execute(update_event_query, (new_event_name, start_date, end_date, new_school_year, new_semester, event_ID))

        location_query = '''UPDATE event_locations SET eventLocation = ? WHERE event_ID = ?'''
        cursor.execute(location_query, (new_event_location, event_ID))
        conn.commit()

        tkMessageBox.showinfo("Message", "The edited information has been updated successfully!")
        self.eventcom()
        self.editframe.destroy()
        self.update_event_table()

    def edit_event(self):
        if not self.etable.selection():
            tkMessageBox.showerror("Error", "No item selected. Please select an event from the table.")
            return
        conn = sqlite3.connect('attendancesystem.db')
        cursor = conn.cursor()

        selected_event = self.etable.focus()
        id_details = str(self.etable.item(selected_event)['values'][0])
        cursor.execute("SELECT events.*, event_locations.eventLocation FROM events JOIN event_locations ON events.event_ID = event_locations.event_ID WHERE events.event_ID = '" + str(id_details)+"'")
        data1 = cursor.fetchall()

        global eentry1; global monthOM2_var; global dayOM2_var; global yearOM2_var; global schoolyearOM_var; global semesterOM_var; global elocation

        def go_back():
            self.eventcom()
            self.editframe.destroy()

        self.editframe = tk.Frame(self.mainframe, width=1150, height=810, background="gray1")
        self.editframe.place(x=65, y=100)
        self.tabview = customtkinter.CTkTabview(master=self.editframe, width=900, height=555)
        self.tabview.place(x=0, y=20)
        self.tabview.configure(text_color="black", fg_color="light yellow", segmented_button_fg_color="lightgoldenrod3", segmented_button_selected_color="light yellow", segmented_button_unselected_color="lightgoldenrod3", segmented_button_unselected_hover_color="light yellow", segmented_button_selected_hover_color="light yellow")
        self.tabview.add("EDIT EVENT")  
        self.esavebtn = customtkinter.CTkButton(self.editframe, text="SAVE CHANGES", text_color="black", font=("Arial", 16), fg_color="lightgoldenrod2", bg_color="light yellow", hover=True, hover_color="lightgoldenrod1", corner_radius=10, width=100, height=35, command=self.update_event_info)
        self.esavebtn.place(x=360, y=465)
        self.backbtn = customtkinter.CTkButton(self.editframe, text="BACK", text_color="white", font=("Arial", 18, "bold"), fg_color="gray15", bg_color="light yellow", hover=True, hover_color="gray18", corner_radius=10, width=100, height=40, command=go_back)
        self.backbtn.place(x=730, y=70)
    # LABELS
        self.elabel1 = customtkinter.CTkLabel(self.editframe,text="EVENT:",text_color="black",font=("Helvetica",15),bg_color="light yellow")
        self.elabel1.place(x=45,y=170)
        self.elabel2 = customtkinter.CTkLabel(self.editframe,text="START DATE:",text_color="black",font=("Helvetica",15),bg_color="light yellow")
        self.elabel2.place(x=45,y=255)
        self.elabel3 = customtkinter.CTkLabel(self.editframe,text="END DATE:",text_color="black",font=("Helvetica",15),bg_color="light yellow")
        self.elabel3.place(x=480,y=255)
        self.elabel4 = customtkinter.CTkLabel(self.editframe,text="SCHOOL YEAR:",text_color="black",font=("Helvetica",15),bg_color="light yellow")
        self.elabel4.place(x=45,y=345)
        self.elabel4 = customtkinter.CTkLabel(self.editframe,text="SEMESTER:",text_color="black",font=("Helvetica",15),bg_color="light yellow")
        self.elabel4.place(x=480,y=345)
        self.elabel5 = customtkinter.CTkLabel(self.editframe,text="LOCATION:",text_color="black",font=("Helvetica",15),bg_color="light yellow")
        self.elabel5.place(x=480,y=170)
    # ENTRIES
        self.eentry1 = customtkinter.CTkEntry(self.editframe,placeholder_text="e.g. EVENT NAME",bg_color="light yellow",placeholder_text_color="lightgoldenrod4",border_color="lightgoldenrod2",fg_color="lightgoldenrod2",width=270,height=35)
        self.eentry1.place(x=175,y=170)
        self.monthOM1_var = tkinter.StringVar(value="Month")
        self.monthOM1 = customtkinter.CTkOptionMenu(self.editframe,bg_color="light yellow",variable=self.monthOM1_var,values=["01","02","03","04","05","06","07","08","09","10","11","12"],text_color="black",dynamic_resizing=TRUE,width=100,fg_color="lightgoldenrod2",button_color="lightgoldenrod4",button_hover_color="lightgoldenrod4",dropdown_fg_color="lightgoldenrod2",dropdown_hover_color="lightgoldenrod3")
        self.monthOM1.place(x=175,y=255)
        self.dayOM1_var = tkinter.StringVar(value="Day")
        self.dayOM1 = customtkinter.CTkOptionMenu(self.editframe,bg_color="light yellow",variable=self.dayOM1_var,values=["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30"],text_color="black",dynamic_resizing=FALSE,width=75,fg_color="lightgoldenrod2",button_color="lightgoldenrod4",button_hover_color="lightgoldenrod4",dropdown_fg_color="lightgoldenrod2",dropdown_hover_color="lightgoldenrod3")
        self.dayOM1.place(x=280,y=255)
        self.yearOM1_var = tkinter.StringVar(value="Year")
        self.yearOM1 = customtkinter.CTkOptionMenu(self.editframe,bg_color="light yellow",variable=self.yearOM1_var,values=["2023","2024","2025","2026","2027","2028","2029","2030"],text_color="black",dynamic_resizing=TRUE,width=85,fg_color="lightgoldenrod2",button_color="lightgoldenrod4",button_hover_color="lightgoldenrod4",dropdown_fg_color="lightgoldenrod2",dropdown_hover_color="lightgoldenrod3")
        self.yearOM1.place(x=360,y=255)
        self.monthOM2_var = tkinter.StringVar(value="Month")
        self.monthOM2 = customtkinter.CTkOptionMenu(self.editframe,bg_color="light yellow",variable=self.monthOM2_var,values=["01","02","03","04","05","06","07","08","09","10","11","12"],text_color="black",dynamic_resizing=TRUE,width=90,fg_color="lightgoldenrod2",button_color="lightgoldenrod4",button_hover_color="lightgoldenrod4",dropdown_fg_color="lightgoldenrod2",dropdown_hover_color="lightgoldenrod3")
        self.monthOM2.place(x=590,y=255)
        self.dayOM2_var = tkinter.StringVar(value="Day")
        self.dayOM2 = customtkinter.CTkOptionMenu(self.editframe,bg_color="light yellow",variable=self.dayOM2_var,values=["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30"],text_color="black",dynamic_resizing=FALSE,width=75,fg_color="lightgoldenrod2",button_color="lightgoldenrod4",button_hover_color="lightgoldenrod4",dropdown_fg_color="lightgoldenrod2",dropdown_hover_color="lightgoldenrod3")
        self.dayOM2.place(x=685,y=255)
        self.yearOM2_var = tkinter.StringVar(value="Year")
        self.yearOM2 = customtkinter.CTkOptionMenu(self.editframe,bg_color="light yellow",variable=self.yearOM2_var,values=["2023","2024","2025","2026","2027","2028","2029","2030"],text_color="black",dynamic_resizing=TRUE,width=85,fg_color="lightgoldenrod2",button_color="lightgoldenrod4",button_hover_color="lightgoldenrod4",dropdown_fg_color="lightgoldenrod2",dropdown_hover_color="lightgoldenrod3")
        self.yearOM2.place(x=765,y=255)
        self.schoolyearOM_var = tkinter.StringVar(value="Select")
        self.schoolyearOM = customtkinter.CTkOptionMenu(self.editframe,bg_color="light yellow",variable=self.schoolyearOM_var,values=["2022-2023","2023-2024","2024-2025","2025-2026","2026-2027","2027-2028","2028-2029","2029-2030","2030-2031"],text_color="black",dynamic_resizing=FALSE,width=270,fg_color="lightgoldenrod2",button_color="lightgoldenrod4",button_hover_color="lightgoldenrod4",dropdown_fg_color="lightgoldenrod2",dropdown_hover_color="lightgoldenrod3")
        self.schoolyearOM.place(x=175,y=345)
        self.semesterOM_var = tkinter.StringVar(value="Select")
        self.semesterOM = customtkinter.CTkOptionMenu(self.editframe,variable=self.semesterOM_var,values=["1ST SEMESTER","2ND SEMESTER"],bg_color="light yellow",text_color="black",dynamic_resizing=TRUE,width=260,fg_color="lightgoldenrod2",button_color="lightgoldenrod4",button_hover_color="lightgoldenrod4",dropdown_fg_color="lightgoldenrod2",dropdown_hover_color="lightgoldenrod3")
        self.semesterOM.place(x=590,y=345)
        self.elocation = customtkinter.CTkEntry(self.editframe,placeholder_text="e.g. LOCATION",bg_color="light yellow",placeholder_text_color="lightgoldenrod4",border_color="lightgoldenrod2",fg_color="lightgoldenrod2",width=260,height=35)
        self.elocation.place(x=590,y=170)

        for selected_data in data1:
            self.eentry1.insert(0, selected_data[1])
            start_date = selected_data[2]
            month1, day1, year1 = start_date.split("/")
            self.monthOM1_var.set(month1)
            self.dayOM1_var.set(day1)
            self.yearOM1_var.set(year1)
            end_date = selected_data[3]
            month2, day2, year2 = end_date.split("/")
            self.monthOM2_var.set(month2)
            self.dayOM2_var.set(day2)
            self.yearOM2_var.set(year2)
            self.schoolyearOM_var.set(selected_data[4])
            self.semesterOM_var.set(selected_data[5])
            self.elocation.insert(0, selected_data[6])








# *********** ATTENDANCE *********** ATTENDANCE *********** ATTENDANCE *********** ATTENDANCE *********** ATTENDANCE *********** ATTENDANCE *********** #
    def view_attendance(self):
        conn = sqlite3.connect('attendancesystem.db')
        cursor = conn.cursor()
    
        if not self.etable.selection():
            tkMessageBox.showerror("Error", "No item selected. Please select an event from the table.")
            return
        # RETRIEVE THE SELECTED EVENT ID AND EVENT NAME FROM THE TABLE
        selected_item = self.etable.selection()[0]
        event_id = self.etable.item(selected_item, "values")[0]
        self.etable.focus()

        def go_back():
            self.eventcom()
            self.attendanceframe.destroy()

        def validate_attendance_time(event_id):
            conn = sqlite3.connect('attendancesystem.db')
            cursor = conn.cursor()
            validate_datetime_query = "SELECT startdate, enddate FROM events WHERE event_ID = ?"
            cursor.execute(validate_datetime_query, (event_id,))
            start_date_str, end_date_str = cursor.fetchone()

            print("Event ID:", event_id)
            print("Start date:", start_date_str)
            print("End date:", end_date_str)

            current_datetime = datetime.datetime.now()
            print("Current datetime:", current_datetime)

            start_date = datetime.datetime.strptime(start_date_str, '%m/%d/%Y')
            end_date = datetime.datetime.strptime(end_date_str, '%m/%d/%Y')

            print("Parsed start date:", start_date)
            print("Parsed end date:", end_date)

            return start_date <= current_datetime <= end_date or current_datetime.date() == end_date.date()

        def sign_in():
            student_id = self.aIDentry.get()
            if student_id == '':
                tkMessageBox.showwarning("Warning", "Please fill the empty field!")
            # RETRIEVE THE LOCATION BASED ON THE EVENT ID
            location_query = "SELECT eventLocation FROM event_locations WHERE event_ID = ?"
            cursor.execute(location_query, (event_id,))
            location = cursor.fetchone()[0]

            if location is None:
                tkMessageBox.showerror("Error", "Location not found for the selected event.")
                return    
            else:
                if not validate_student_id(student_id):
                    tkMessageBox.showerror("Error", "Invalid student ID format. Please use the format 0000-0000.")
                    clear_inputs()
                    return
                if not check_student_exists(student_id):
                    tkMessageBox.showerror("Error", "Student ID does not exist.")
                    clear_inputs()
                    return
                if not validate_attendance_time(event_id):
                    tkMessageBox.showerror("Error", "Attendance sign-in is currently not allowed. Please verify the sign-in duration or the appropriate day for signing in")
                    clear_inputs()
                    return
                add_attendance(student_id, 'IN', location)

        def sign_out():
            student_id = self.aIDentry.get()
            if student_id == '':
                tkMessageBox.showwarning("Warning", "Please fill the empty field!")
            # RETRIEVE THE LOCATION BASED ON THE EVENT ID
            location_query = "SELECT eventLocation FROM event_locations WHERE event_ID = ?"
            cursor.execute(location_query, (event_id,))
            location = cursor.fetchone()[0]

            if location is None:
                tkMessageBox.showerror("Error", "Location not found for the selected event.")
                return
            else:
                if not validate_student_id(student_id):
                    tkMessageBox.showerror("Error", "Invalid student ID format. Please use the format 0000-0000.")
                    clear_inputs()
                    return
                if not check_student_exists(student_id):
                    tkMessageBox.showerror("Error", "Student ID does not exist.")
                    clear_inputs()
                    return
                if not validate_attendance_time(event_id):
                    tkMessageBox.showerror("Error", "Attendance sign-out is currently not allowed. Please verify the sign-out duration or the appropriate day for signing out")
                    clear_inputs()
                    return
                add_attendance(student_id, 'OUT', location)
        
        self.attendanceframe = tk.Frame(self.mainframe, width=1150, height=810, background="gray1")
        self.attendanceframe.place(x=65, y=100)
        self.tabview = customtkinter.CTkTabview(master=self.attendanceframe, width=900, height=555)
        self.tabview.place(x=0, y=20)
        self.tabview.configure(text_color="black", fg_color="light yellow", segmented_button_fg_color="lightgoldenrod3", segmented_button_selected_color="light yellow", segmented_button_unselected_color="lightgoldenrod3", segmented_button_unselected_hover_color="light yellow", segmented_button_selected_hover_color="light yellow")
        self.tabview.add("EVENT ATTENDANCE")  
        self.backbtn = customtkinter.CTkButton(self.attendanceframe, text="BACK", text_color="black", font=("Arial", 18, "bold"), fg_color="lightgoldenrod2", bg_color="light yellow", hover=True, hover_color="lightgoldenrod1", corner_radius=10, width=100, height=40, command=go_back)
        self.backbtn.place(x=50, y=70)
        self.aIDentry = customtkinter.CTkEntry(self.attendanceframe,font=("Arial",45,"bold"),placeholder_text="####-####",bg_color="light yellow",placeholder_text_color="lightgoldenrod4",border_color="lightgoldenrod2",fg_color="lightgoldenrod2",width=450,height=80,justify="center")
        self.aIDentry.place(x=225,y=120)
        signinbtn =customtkinter.CTkButton(self.attendanceframe,text="SIGN IN",bg_color="light yellow",text_color="white",font=("Arial",20,"bold"),fg_color="lightgoldenrod4",hover=True,hover_color= "khaki4",corner_radius=10,width=205,height=50,command=sign_in)
        signinbtn.place(x=225,y=220)
        signoutbtn =customtkinter.CTkButton(self.attendanceframe,text="SIGN OUT",bg_color="light yellow",text_color="white",font=("Arial",20,"bold"),fg_color="gray12",hover=True,hover_color= "gray18",corner_radius=10,width=205,height=50,command=sign_out)
        signoutbtn.place(x=470,y=220)
        # DISPLAY ATTENDANCE LIST
        self.tablestyle()
        self.tableframe = tk.Frame(self.tabview.tab("EVENT ATTENDANCE"), background="light yellow")
        self.tableframe.place(x=55,y=290,width=1000,height=290)
        self.y_scroll = customtkinter.CTkScrollbar(self.tableframe, orientation=VERTICAL, button_color="lightgoldenrod4", button_hover_color="lightgoldenrod3", fg_color="light yellow")
        self.y_scroll.pack(side=RIGHT, fill=Y)
        self.atable = ttk.Treeview(self.tableframe, columns=("eventName","student_ID", "slastName", "signin_datetime", "signout_datetime","elocation"), show="headings", yscrollcommand=self.y_scroll.set)
        self.atable.pack(fill=BOTH, expand=True)
        self.y_scroll.configure(command=self.atable.yview)
        # HEADINGS
        self.atable.heading("eventName", text="EVENT")
        self.atable.heading("student_ID", text="STUDENT ID")
        self.atable.heading("slastName", text="NAME")
        self.atable.heading("signin_datetime", text="SIGN IN DATE/TIME")
        self.atable.heading("signout_datetime", text="SIGN OUT DATE/TIME")
        self.atable.heading("elocation", text="LOCATION")
        # COLUMNS
        self.atable.column("eventName", width=80, anchor=CENTER)
        self.atable.column("student_ID", width=50, anchor=CENTER)
        self.atable.column("slastName", width=80, anchor=CENTER)
        self.atable.column("signin_datetime", width=150, anchor=CENTER)
        self.atable.column("signout_datetime", width=150, anchor=CENTER)
        self.atable.column("elocation", width=100, anchor=CENTER)
        # RETRIEVE AND DISPLAY ATTENDANCE RECORDS FOR THE SELECTED EVENT 
        self.atable.delete(*self.atable.get_children())
        display_data_query = cursor.execute("SELECT events.eventName, student.student_ID, student.lastName, attendance.signin_datetime, attendance.signout_datetime, eventLocation FROM attendance JOIN student ON attendance.student_ID = student.student_ID JOIN events ON attendance.event_ID = events.event_ID JOIN event_locations ON events.event_ID = event_locations.event_ID WHERE attendance.event_ID = ? ORDER BY student.lastName ASC", (event_id,))
        fetch = display_data_query.fetchall()
        for data in fetch:
            self.atable.insert('', 'end', values=(data[0], data[1], data[2], data[3], data[4], data[5]))
        conn.commit()

        def update_attendance_table(event_id):
            conn = sqlite3.connect('attendancesystem.db')
            cursor = conn.cursor()
            self.atable.delete(*self.atable.get_children())
            display_data_query = cursor.execute("SELECT events.eventName, student.student_ID, student.lastName, attendance.signin_datetime, attendance.signout_datetime, eventLocation FROM attendance JOIN student ON attendance.student_ID = student.student_ID JOIN events ON attendance.event_ID = events.event_ID JOIN event_locations ON events.event_ID = event_locations.event_ID WHERE attendance.event_ID = ? ORDER BY student.lastName ASC", (event_id,))
            fetch = display_data_query.fetchall()
            for data in fetch:
                self.atable.insert('', 'end', values=(data[0], data[1], data[2], data[3], data[4],data[5]))
            conn.commit()
            conn.close()

        # CHECK STUDENT ID FORMAT
        def validate_student_id(student_id):
            if len(student_id) != 9 or student_id[4] != '-':
                return False
            return True
        
        # CHECK IF STUDENT ID EXISTS IN THE STUDENT TABLE
        def check_student_exists(student_id):
            conn = sqlite3.connect('attendancesystem.db')
            cursor = conn.cursor()
            query = "SELECT student_ID FROM student WHERE student_ID = ?"
            cursor.execute(query, (student_id,))
            result = cursor.fetchone()
            conn.close()
            if result:
                return True
            return False
        
        # RECORD ATTENDANCE
        def add_attendance(student_id, sign_type, location):
            conn = sqlite3.connect('attendancesystem.db')
            cursor = conn.cursor()

            # RETRIEVE THE EVENT ID BASED ON THE SELECTED EVENT ON THE TABLE
            selected_event_name = self.etable.item(self.etable.focus())['values'][1]
            selected_event_location = self.etable.item(self.etable.focus())['values'][6]
            event_query = "SELECT events.event_ID FROM events JOIN event_locations ON events.event_ID = event_locations.event_ID WHERE events.eventName = ? AND event_locations.eventLocation = ?"
            cursor.execute(event_query, (selected_event_name, selected_event_location))
            event_id = cursor.fetchone()[0]

            exists_query = "SELECT attendance.* FROM attendance JOIN events ON attendance.event_ID = events.event_ID JOIN event_locations ON events.event_ID = event_locations.event_ID WHERE attendance.student_ID = ? AND attendance.event_ID = ? AND event_locations.eventLocation = ?"
            cursor.execute(exists_query, (student_id, event_id, location))
            existing_record = cursor.fetchone()

            # PRINT VALUES FOR DEBUGGING
            print("Event ID:", event_id)
            print("Event Name:", selected_event_name)
            print("Event Location:",selected_event_location)

            if existing_record:
                if sign_type == 'IN':
                    tkMessageBox.showerror("Sign-in Attendance Recorded", "Sign-in Attendance for this student at this day and location is already recorded.")
                elif sign_type == 'OUT':
                    existing_signout = existing_record[3]
                    if existing_signout != '-':
                        tkMessageBox.showerror("Sign-out Attendance Recorded", "Sign-out Attendance for this student at this day and location is already recorded.")
                    else:
                        query = "UPDATE attendance SET signout_datetime = datetime('now') WHERE student_ID = ? AND event_ID = ?"
                        cursor.execute(query, (student_id, event_id))
                        conn.commit()
                        update_attendance_table(event_id)
                        tkMessageBox.showinfo("Signed Out", "The student has been signed out successfully.")
                conn.close()
                clear_inputs()
                return

            if sign_type == 'IN':
                query = "INSERT INTO attendance (student_ID, event_ID, signin_datetime, signout_datetime) VALUES (?, ?, datetime('now'), '-')"
                cursor.execute(query, (student_id, event_id))
                conn.commit()
                update_attendance_table(event_id)
                tkMessageBox.showinfo("Signed In", "The student has been signed in successfully.")
            else:
                tkMessageBox.showerror("Message", "Attendance record not found.")

            conn.close()
            clear_inputs()

        def clear_inputs():
                self.aIDentry.delete(0, END)








# *********** STUDENT *********** STUDENT *********** STUDENT *********** STUDENT *********** STUDENT *********** STUDENT *********** #
    def studentcom(self):
        self.studentframe = tk.Frame(self.mainframe,width=1150,height=810,background="gray1")
        self.studentframe.place(x=65,y=100)
        self.tabview = customtkinter.CTkTabview(master=self.studentframe,width=900,height=560)
        self.tabview.place(x=0,y=20)
        self.tabview.configure(text_color="black",fg_color="light yellow",segmented_button_fg_color="lightgoldenrod3",segmented_button_selected_color="light yellow",segmented_button_unselected_color="lightgoldenrod3",segmented_button_unselected_hover_color="light yellow",segmented_button_selected_hover_color="light yellow")
        self.tabview.add("STUDENTS")  
        self.tabview.add("ADD STUDENT") 
        self.tabview.set("STUDENTS") 
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
    # ENTRIES
        self.slNameent = customtkinter.CTkEntry(self.tabview.tab("ADD STUDENT"),placeholder_text="e.g. PARAGOSO",placeholder_text_color="lightgoldenrod4",border_color="lightgoldenrod2",fg_color="lightgoldenrod2",width=230,height=35)
        self.slNameent.place(x=180,y=120)
        self.sfNameent = customtkinter.CTkEntry(self.tabview.tab("ADD STUDENT"),placeholder_text="e.g. EDA GRACE",placeholder_text_color="lightgoldenrod4",border_color="lightgoldenrod2",fg_color="lightgoldenrod2",width=230,height=35)
        self.sfNameent.place(x=180,y=205)
        self.smNameent = customtkinter.CTkEntry(self.tabview.tab("ADD STUDENT"),placeholder_text="e.g. JUTBA",placeholder_text_color="lightgoldenrod4",border_color="lightgoldenrod2",fg_color="lightgoldenrod2",width=230,height=35)
        self.smNameent.place(x=180,y=295)
        self.sIDent = customtkinter.CTkEntry(self.tabview.tab("ADD STUDENT"),placeholder_text="e.g. 2021-1574",placeholder_text_color="lightgoldenrod4",border_color="lightgoldenrod2",fg_color="lightgoldenrod2",width=230,height=35)
        self.sIDent.place(x=610,y=120)
        conn = sqlite3.connect('attendancesystem.db')
        cursor = conn.cursor() 
        cursor.execute("SELECT DISTINCT course_code FROM course")
        course_list = [r[0] for r in cursor.fetchall()]
        conn.commit()
        conn.close()
        self.scourse_var = tkinter.StringVar(value='Select')
        self.scourseOM = customtkinter.CTkOptionMenu(self.tabview.tab("ADD STUDENT"),values=course_list,variable=self.scourse_var,text_color="black",dynamic_resizing=TRUE,width=230,fg_color="lightgoldenrod2",button_color="lightgoldenrod4",button_hover_color="lightgoldenrod4",dropdown_fg_color="lightgoldenrod2",dropdown_hover_color="lightgoldenrod3")
        self.scourseOM.place(x=610,y=205)
        self.syearlevel_var = customtkinter.StringVar(value="Select")
        self.syearlevelOM = customtkinter.CTkOptionMenu(self.tabview.tab("ADD STUDENT"),variable=self.syearlevel_var,values=["1ST YEAR","2ND YEAR","3RD YEAR","4TH YEAR"],text_color="black",dynamic_resizing=TRUE,width=230,fg_color="lightgoldenrod2",button_color="lightgoldenrod4",button_hover_color="lightgoldenrod4",dropdown_fg_color="lightgoldenrod2",dropdown_hover_color="lightgoldenrod3")
        self.syearlevelOM.place(x=610,y=295)
    # SAVE BUTTON TO ADD STUDENT
        self.ssavebtn = customtkinter.CTkButton(self.tabview.tab("ADD STUDENT"),text="ADD STUDENT",font=("Helvetica",14),text_color="black",fg_color="lightgoldenrod2",border_width=2,hover=True,hover_color= "lightgoldenrod1",corner_radius=10,border_color= "lightgoldenrod2",width=100,height=35,command=self.add_student)
        self.ssavebtn.place(x=400,y=390)

#**************************************************************** STUDENTS LIST TABVIEW ****************************************************************#
        self.elabel7 =customtkinter.CTkLabel(self.tabview.tab("STUDENTS"),text="STUDENTS LIST:",text_color="black",font=("Helvetica",16,"bold"))
        self.elabel7.place(x=45,y=45)
    # SEARCH
        self.elabel8 =customtkinter.CTkLabel(self.tabview.tab("STUDENTS"),text="SEARCH:",text_color="black",font=("Helvetica",13))
        self.elabel8.place(x=610,y=45)
        self.ssearch_var = StringVar()
        self.ssearchentry = customtkinter.CTkEntry(self.tabview.tab("STUDENTS"),textvariable=self.ssearch_var,placeholder_text="e.g. 2021-1574",placeholder_text_color="lightgoldenrod4",border_color="lightgoldenrod2",fg_color="lightgoldenrod2",width=160,height=35)
        self.ssearchentry.place(x=680,y=45)
        self.ssearchentry.bind("<KeyRelease>", self.search_student)
# ******** LIST OF STUDENTS
        self.tablestyle()
        self.table_frame = tk.Frame(self.tabview.tab("STUDENTS"),bg="white")
        self.table_frame.place(x=55,y=125,width=1000,height=360)
        self.y_scroll = customtkinter.CTkScrollbar(self.table_frame,orientation=VERTICAL,button_color="lightgoldenrod4",button_hover_color="lightgoldenrod3",fg_color="light yellow")
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
        self.stable.pack(fill=BOTH,expand=True)
        # FETCH DATA FROM DATABASE AND DISPLAY ON THE TABLE
        conn = sqlite3.connect('attendancesystem.db')
        cursor = conn.cursor()
        display_data_query = cursor.execute("SELECT * FROM student ORDER BY lastName ASC")
        fetch = display_data_query.fetchall()
        for data in fetch:
            self.stable.insert('', 'end', values=(data[0], data[1], data[2], data[3], data[4], data[5]))
        conn.commit()
        conn.close()
    # BUTTONS
        self.seditbtn = customtkinter.CTkButton(self.tabview.tab("STUDENTS"),text="EDIT STUDENT",font=("Helvetica",14),text_color="black",fg_color="lightgoldenrod2",border_width=2,hover= True,hover_color= "lightgoldenrod1",corner_radius=10,border_color= "lightgoldenrod2",width=100,height=35,command=self.edit_student)
        self.seditbtn.place(x=590,y=405)
        self.supdatebtn = customtkinter.CTkButton(self.tabview.tab("STUDENTS"),text="REFRESH",font=("Helvetica",14),text_color="black",fg_color="lightgoldenrod2",border_width=2,hover= True,hover_color= "lightgoldenrod1",corner_radius=10,border_color= "lightgoldenrod2",width=100,height=35,command=self.update_student_table)
        self.supdatebtn.place(x=480,y=405)
        self.sdeletebtn = customtkinter.CTkButton(self.tabview.tab("STUDENTS"),text="delete student",font=("Helvetica",14),text_color="white",fg_color="red2",border_width=2,hover= True,hover_color= "red",corner_radius=10,border_color= "red2",width=100,height=35,command=self.delete_student)
        self.sdeletebtn.place(x=730,y=405)

    # UPDATE STUDENT TABLE
    def update_student_table(self):
        conn = sqlite3.connect('attendancesystem.db')
        cursor = conn.cursor() 
        self.stable.delete(*self.stable.get_children())
        display_data_query = cursor.execute("SELECT * FROM student ORDER BY lastName ASC")
        fetch = display_data_query.fetchall()
        for data in fetch:
            self.stable.insert('', 'end', values=(data[0],data[1],data[2],data[3],data[4],data[5]))
        conn.commit()
        conn.close()

# ******** SEARCH STUDENT
    def search_student(self,ev):
        conn = sqlite3.connect('attendancesystem.db')
        cursor = conn.cursor() 
        if self.ssearchentry.get() != "":      
            self.stable.delete(*self.stable.get_children())
            search_term = '%' + self.ssearchentry.get() + '%'
            display_search_query = cursor.execute("SELECT * FROM student WHERE student_ID LIKE ? OR lastName LIKE ? or firstName LIKE ? or midName LIKE ? or year_level LIKE ? or course_code LIKE ?",(search_term,search_term.upper(),search_term.upper(),search_term.upper(),search_term.upper(),search_term.upper()))
            fetch = display_search_query.fetchall()
            for data in fetch:
                self.stable.insert('', 'end', values=(data))
                conn.commit()
            conn.close()

# ******** ADD STUDENT
    def clear_student_inputs(self):
        self.sIDent.delete(0, END)
        self.slNameent.delete(0, END)
        self.sfNameent.delete(0, END)
        self.smNameent.delete(0, END)
        self.syearlevel_var.set('Select')
        self.scourse_var.set('Select')

    def add_student(self):
        conn = sqlite3.connect('attendancesystem.db')
        cursor = conn.cursor() 
        student_ID = self.sIDent.get()
        last_name = self.slNameent.get().upper()
        first_name = self.sfNameent.get().upper()
        mid_name = self.smNameent.get().upper()
        year_level = self.syearlevel_var.get()
        course_code = self.scourse_var.get()

        if student_ID=='' or last_name=='' or first_name=='' or mid_name=='' or year_level=='' or course_code=='': tkMessageBox.showwarning("Warning","Please fill the empty field!")
        else:
            if self.student_exists(cursor, student_ID):
                tkMessageBox.showerror("Error", "There is already a student with the same student ID in the system!")
            else:
                data_insert_query = '''INSERT INTO student (student_ID,lastName,firstName,midName,year_level,course_code) VALUES (?,?,?,?,?,?)'''
                data_insert_tuple = (student_ID,last_name,first_name,mid_name,year_level,course_code)
                cursor.execute(data_insert_query,data_insert_tuple)
                conn.commit()
                tkMessageBox.showinfo("Message","Student information added successfully")
        conn.commit()
        self.update_student_table()
        self.clear_student_inputs()

    # CHECK IF THE SAME STUDENT ID ALREADY EXISTS IN THE DATABASE
    def student_exists(self, cursor, student_ID):
        conn = sqlite3.connect('attendancesystem.db')
        cursor = conn.cursor()
        query = '''SELECT * FROM student WHERE student_ID = ?'''
        cursor.execute(query, (student_ID,))
        conn.commit()
        if cursor.fetchone():
            return True
        conn.close()
        return False

# ******** DELETE STUDENT
    def delete_student(self):
        if not self.stable.selection():
            tkMessageBox.showerror("Error", "No item selected. Please select a student from the table.")
            return
        
        decision = tkMessageBox.askquestion("Warning","Are you sure you want to delete the selected student?")
        if decision != 'yes':
            return
        else:
            try:
                selected_item = self.stable.selection()[0]
                delete_data = str(self.stable.item(selected_item)['values'][0])
                conn = sqlite3.connect('attendancesystem.db')
                cursor = conn.cursor() 
                cursor.execute("DELETE FROM student WHERE student_ID = '" + str(delete_data)+"'")
                conn.commit()
                tkMessageBox.showinfo("Message", "The student is deleted successfully!")
                conn.close()
            except:
                tkMessageBox.showerror("Error","An error has occured")
                return
        self.update_student_table()

# ******** EDIT STUDENT
    def update_student_info(self):
        decision = tkMessageBox.askyesno("Warning", "Are you sure you want to make changes in the student information?")
        if not decision:
            tkMessageBox.showinfo("Message", "The changes have not been saved")
            return

        conn = sqlite3.connect('attendancesystem.db')
        cursor = conn.cursor()

        selected_student = self.stable.focus()
        id_details = str(self.stable.item(selected_student)['values'][0])
        student_ID = str(id_details)
        cursor.execute('''UPDATE student SET lastName = :lastName,firstName = :firstName,midName = :midName,
            year_level = :year_level,course_code = :course_code WHERE student_ID = :student_ID''',
                {'lastName': self.slNameent.get().upper(),'firstName': self.sfNameent.get().upper(),'midName': self.smNameent.get().upper(),
                    'year_level': self.syearlevel_var.get(),'course_code': self.scourse_var.get(),'student_ID': student_ID})
        conn.commit()
        conn.close()
        tkMessageBox.showinfo("Message", "The edited information has been updated successfully!")
        self.studentcom()
        self.editframe.destroy()
        self.update_student_table()

    def edit_student(self):
        if not self.stable.selection():
            tkMessageBox.showerror("Error", "No item selected. Please select a student from the table.")
            return
        conn = sqlite3.connect('attendancesystem.db')
        cursor = conn.cursor()

        selected_student = self.stable.focus()
        id_details = str(self.stable.item(selected_student)['values'][0])
        cursor.execute("SELECT * FROM student WHERE student_ID = '" + str(id_details)+"'")
        data = cursor.fetchall()

        global slNameent; global sfNameent; global smNameent; global scourse_var; global syearlevel_var

        def go_back():
            self.studentcom()
            self.editframe.destroy()

        self.editframe = tk.Frame(self.mainframe, width=1150, height=810, background="gray1")
        self.editframe.place(x=65, y=100)
        self.tabview = customtkinter.CTkTabview(master=self.editframe, width=900, height=555)
        self.tabview.place(x=0, y=20)
        self.tabview.configure(text_color="black", fg_color="light yellow", segmented_button_fg_color="lightgoldenrod3", segmented_button_selected_color="light yellow", segmented_button_unselected_color="lightgoldenrod3", segmented_button_unselected_hover_color="light yellow", segmented_button_selected_hover_color="light yellow")
        self.tabview.add("EDIT STUDENT")  
        self.ssavebtn = customtkinter.CTkButton(self.editframe, text="SAVE CHANGES", text_color="black", font=("Arial", 16), fg_color="lightgoldenrod2", bg_color="light yellow", hover=True, hover_color="lightgoldenrod1", corner_radius=10, width=100, height=35, command=self.update_student_info)
        self.ssavebtn.place(x=380, y=460)
        self.backbtn = customtkinter.CTkButton(self.editframe, text="BACK", text_color="black", font=("Arial", 18, "bold"), fg_color="lightgoldenrod2", bg_color="light yellow", hover=True, hover_color="lightgoldenrod1", corner_radius=10, width=100, height=40, command=go_back)
        self.backbtn.place(x=740, y=70)
    # LABELS
        self.slabel1 =customtkinter.CTkLabel(self.editframe,bg_color="light yellow",text="STUDENT INFORMATION:",text_color="black",font=("Helvetica",16,"bold"))
        self.slabel1.place(x=45,y=120)
        self.slabel2 =customtkinter.CTkLabel(self.editframe,bg_color="light yellow",text="LAST NAME:",text_color="black",font=("Helvetica",15))
        self.slabel2.place(x=45,y=195)
        self.slabel3 =customtkinter.CTkLabel(self.editframe,bg_color="light yellow",text="FIRST NAME:",text_color="black",font=("Helvetica",15))
        self.slabel3.place(x=45,y=280)
        self.slabel3 =customtkinter.CTkLabel(self.editframe,bg_color="light yellow",text="MIDDLE NAME:",text_color="black",font=("Helvetica",15))
        self.slabel3.place(x=45,y=370)
        self.slabel5 =customtkinter.CTkLabel(self.editframe,bg_color="light yellow",text="COURSE:",text_color="black",font=("Helvetica",15))
        self.slabel5.place(x=480,y=195)
        self.slabel6 =customtkinter.CTkLabel(self.editframe,bg_color="light yellow",text="YEAR LEVEL:",text_color="black",font=("Helvetica",15))
        self.slabel6.place(x=480,y=280)
    # ENTRIES
        self.slNameent = customtkinter.CTkEntry(self.editframe,bg_color="light yellow",placeholder_text="e.g. PARAGOSO",placeholder_text_color="lightgoldenrod4",border_color="lightgoldenrod2",fg_color="lightgoldenrod2",width=230,height=35)
        self.slNameent.place(x=180,y=195)
        self.sfNameent = customtkinter.CTkEntry(self.editframe,bg_color="light yellow",placeholder_text="e.g. EDA GRACE",placeholder_text_color="lightgoldenrod4",border_color="lightgoldenrod2",fg_color="lightgoldenrod2",width=230,height=35)
        self.sfNameent.place(x=180,y=280)
        self.smNameent = customtkinter.CTkEntry(self.editframe,bg_color="light yellow",placeholder_text="e.g. JUTBA",placeholder_text_color="lightgoldenrod4",border_color="lightgoldenrod2",fg_color="lightgoldenrod2",width=230,height=35)
        self.smNameent.place(x=180,y=370)
        conn = sqlite3.connect('attendancesystem.db')
        cursor = conn.cursor() 
        cursor.execute("SELECT DISTINCT course_code FROM course")
        course_list = [r[0] for r in cursor.fetchall()]
        conn.commit()
        conn.close()
        self.scourse_var = customtkinter.StringVar(value="Select")
        self.scourseOM = customtkinter.CTkOptionMenu(self.editframe,values=course_list,variable=self.scourse_var,bg_color="light yellow",text_color="black",dynamic_resizing=TRUE,width=230,fg_color="lightgoldenrod2",button_color="lightgoldenrod4",button_hover_color="lightgoldenrod4",dropdown_fg_color="lightgoldenrod2",dropdown_hover_color="lightgoldenrod3")
        self.scourseOM.place(x=610,y=195)
        self.syearlevel_var = customtkinter.StringVar(value="Select")
        self.syearlevelOM = customtkinter.CTkOptionMenu(self.editframe,bg_color="light yellow",variable=self.syearlevel_var,values=["1ST YEAR","2ND YEAR","3RD YEAR","4TH YEAR"],text_color="black",dynamic_resizing=TRUE,width=230,fg_color="lightgoldenrod2",button_color="lightgoldenrod4",button_hover_color="lightgoldenrod4",dropdown_fg_color="lightgoldenrod2",dropdown_hover_color="lightgoldenrod3")
        self.syearlevelOM.place(x=610,y=280)

        for selected_data in data:
            self.slNameent.insert(0,selected_data[1])
            self.sfNameent.insert(0,selected_data[2])
            self.smNameent.insert(0,selected_data[3])
            self.syearlevel_var.set(selected_data[4])
            self.scourse_var.set(selected_data[5])






# *********** COURSE *********** COURSE *********** COURSE *********** COURSE *********** COURSE *********** COURSE *********** #
    def coursecom(self):
        self.courseframe = tk.Frame(self.mainframe,width=1150,height=810,background="gray1")
        self.courseframe.place(x=65,y=100)
        self.tabview = customtkinter.CTkTabview(master=self.courseframe,width=900,height=500)
        self.tabview.place(x=0,y=20)
        self.tabview.configure(text_color="black",fg_color="light yellow",segmented_button_fg_color="lightgoldenrod3",segmented_button_selected_color="light yellow",segmented_button_unselected_color="lightgoldenrod3",segmented_button_unselected_hover_color="light yellow",segmented_button_selected_hover_color="light yellow")
        self.tabview.add("COURSES")  
        self.tabview.add("ADD COURSE") 
        self.tabview.set("COURSES")
    # LABELS
        self.clabel1 =customtkinter.CTkLabel(self.tabview.tab("ADD COURSE") ,text="COURSE INFORMATON:",text_color="black",font=("Helvetica",16,"bold"))
        self.clabel1.place(x=45,y=45)
        self.clabel2 =customtkinter.CTkLabel(self.tabview.tab("ADD COURSE") ,text="COURSE CODE:",text_color="black",font=("Helvetica",15))
        self.clabel2.place(x=45,y=120)
        self.clabel3 =customtkinter.CTkLabel(self.tabview.tab("ADD COURSE") ,text="COURSE:",text_color="black",font=("Helvetica",15))
        self.clabel3.place(x=45,y=190)
    # ENTRIES
        self.ccodeent = customtkinter.CTkEntry(self.tabview.tab("ADD COURSE"),placeholder_text="e.g. BSCS",placeholder_text_color="lightgoldenrod4",border_color="lightgoldenrod2",fg_color="lightgoldenrod2",width=230,height=35)
        self.ccodeent.place(x=180,y=120)
        self.cnameent = customtkinter.CTkEntry(self.tabview.tab("ADD COURSE"),placeholder_text="e.g. BACHELOR OF SCIENCE IN COMPUTER SCIENCE",placeholder_text_color="lightgoldenrod4",border_color="lightgoldenrod2",fg_color="lightgoldenrod2",width=660,height=35)
        self.cnameent.place(x=180,y=190)
    # SAVE BUTTON TO ADD COURSE
        self.csavebtn = customtkinter.CTkButton(self.tabview.tab("ADD COURSE"),text="ADD COURSE",font=("Helvetica",14),text_color="black",fg_color="lightgoldenrod2",border_width=2,hover=True,hover_color= "lightgoldenrod1",corner_radius=10,border_color= "lightgoldenrod2",width=100,height=35,command=self.add_course)
        self.csavebtn.place(x=385,y=260)

#**************************************************************** COURSES LIST TABVIEW ****************************************************************#
        self.elabel7 =customtkinter.CTkLabel(self.tabview.tab("COURSES"),text="COURSES LIST:",text_color="black",font=("Helvetica",16,"bold"))
        self.elabel7.place(x=45,y=45)
    # SEARCH
        self.elabel8 =customtkinter.CTkLabel(self.tabview.tab("COURSES"),text="SEARCH:",text_color="black",font=("Helvetica",13))
        self.elabel8.place(x=610,y=45)
        self.csearch_var = StringVar()
        self.csearchentry = customtkinter.CTkEntry(self.tabview.tab("COURSES"),textvariable=self.csearch_var,placeholder_text="e.g. BSCS",placeholder_text_color="lightgoldenrod4",border_color="lightgoldenrod2",fg_color="lightgoldenrod2",width=160,height=35)
        self.csearchentry.place(x=680,y=45)
        self.csearchentry.bind("<KeyRelease>", self.search_course)
    # ******** LIST OF COURSES
        self.tablestyle()
        self.table_frame = tk.Frame(self.tabview.tab("COURSES"),bg="white")
        self.table_frame.place(x=55,y=120,width=1000,height=290)
        self.y_scroll = customtkinter.CTkScrollbar(self.table_frame,orientation=VERTICAL,button_color="lightgoldenrod4",button_hover_color="lightgoldenrod3",fg_color="light yellow")
        self.y_scroll.pack(side=RIGHT,fill=Y)
        self.ctable = ttk.Treeview(self.table_frame,yscrollcommand=self.y_scroll.set)
        self.y_scroll.configure(command=self.ctable.yview)
        self.ctable["columns"] = ("COURSE CODE","COURSE NAME")
        self.ctable.column("#0", width=0, stretch=NO)  
        self.ctable.column("COURSE CODE", width=50,anchor=CENTER)
        self.ctable.column("COURSE NAME", width=400,anchor=CENTER)
        self.ctable.heading("COURSE CODE", text="COURSE CODE")
        self.ctable.heading("COURSE NAME", text="COURSE NAME")
        self.ctable.pack(fill=BOTH,expand=True)
    # FETCH DATA FROM DATABASE AND DISPLAY ON THE TABLE
        conn = sqlite3.connect('attendancesystem.db')
        cursor = conn.cursor()
        display_data_query = cursor.execute("SELECT * FROM course ORDER BY course_code ASC")
        fetch = display_data_query.fetchall()
        for data in fetch:
            self.ctable.insert('', 'end', values=(data[0], data[1]))
        conn.commit()
        conn.close()
    # BUTTONS
        self.ceditbtn = customtkinter.CTkButton(self.tabview.tab("COURSES"),text="EDIT COURSE",font=("Helvetica",14),text_color="black",fg_color="lightgoldenrod2",border_width=2,hover= True,hover_color= "lightgoldenrod1",corner_radius=10,border_color= "lightgoldenrod2",width=100,height=35,command=self.edit_course)
        self.ceditbtn.place(x=595,y=345)
        self.cupdatebtn = customtkinter.CTkButton(self.tabview.tab("COURSES"),text="REFRESH",font=("Helvetica",14),text_color="black",fg_color="lightgoldenrod2",border_width=2,hover= True,hover_color= "lightgoldenrod1",corner_radius=10,border_color= "lightgoldenrod2",width=100,height=35,command=self.update_course_table)
        self.cupdatebtn.place(x=480,y=345)
        self.cdeletebtn = customtkinter.CTkButton(self.tabview.tab("COURSES"),text="delete course",font=("Helvetica",14),text_color="white",fg_color="red2",border_width=2,hover= True,hover_color= "red",corner_radius=10,border_color= "red2",width=100,height=35,command=self.delete_course)
        self.cdeletebtn.place(x=730,y=345)

    # UPDATE COURSE TABLE
    def update_course_table(self):
        conn = sqlite3.connect('attendancesystem.db')
        cursor = conn.cursor() 
        self.ctable.delete(*self.ctable.get_children())
        display_data_query = cursor.execute("SELECT * FROM course ORDER BY course_code ASC")
        fetch = display_data_query.fetchall()
        for data in fetch:
            self.ctable.insert('', 'end', values=(data[0],data[1]))
        conn.commit()
        conn.close()

# ******** SEARCH COURSE
    def search_course(self,ev):
        conn = sqlite3.connect('attendancesystem.db')
        cursor = conn.cursor() 
        if self.csearchentry.get() != "":      
            self.ctable.delete(*self.ctable.get_children())
            search_term = '%' + self.csearchentry.get() + '%'
            display_search_query = cursor.execute("SELECT * FROM course WHERE course_code LIKE ? OR courseName LIKE ?",(search_term.upper(),search_term.upper()))
            fetch = display_search_query.fetchall()
            for data in fetch:
                self.ctable.insert('', 'end', values=(data))
                conn.commit()
            conn.close()

# ******** ADD COURSE
    def clear_course_inputs(self):
        self.ccodeent.delete(0, END)
        self.cnameent.delete(0, END)

    def add_course(self):
        conn = sqlite3.connect('attendancesystem.db')
        cursor = conn.cursor()
    # get the course info from the input fields
        course_code = self.ccodeent.get().upper()
        course = self.cnameent.get().upper()
    # input in database
        if course_code=='' or course=='': tkMessageBox.showwarning("Warning","Fill the empty field!")
        else:
            if self.course_exists(cursor, course_code,course):
                tkMessageBox.showerror("Error", "The course cannot be added. It already exists!")
            else:
                data_insert_query = '''INSERT INTO course (course_code,courseName) VALUES (?,?)'''
                data_insert_tuple = (course_code,course)
                tkMessageBox.showinfo("Message","Course added successfully")
                cursor.execute(data_insert_query,data_insert_tuple)
                conn.commit()
        conn.close()
        self.clear_course_inputs()
        self.update_course_table()
    
    # Check if a course with the same code and name already exists in the database
    def course_exists(self, cursor, course_code,course):
        conn = sqlite3.connect('attendancesystem.db')
        cursor = conn.cursor()
        query = '''SELECT * FROM course WHERE course_code = ? or courseName LIKE ?'''
        search_term = '%' + course + '%'
        cursor.execute(query, (course_code, search_term))
        conn.commit()
        if cursor.fetchone():
            return True
        conn.close()
        return False

# ******** DELETE COURSE
    def delete_course(self):
        if not self.ctable.selection():
            tkMessageBox.showerror("Error", "No item selected. Please select a course from the table.")
            return
        
        decision = tkMessageBox.askquestion("Warning", "Are you sure you want to delete the selected course?")
        if decision != 'yes':
            return
        else:
            selected_item = self.ctable.selection()[0]
            delete_data = str(self.ctable.item(selected_item)['values'][0])
            try:
                conn = sqlite3.connect('attendancesystem.db')
                cursor = conn.cursor()
                cursor.execute("SELECT COUNT(*) FROM student WHERE course_code = ?", (delete_data,))
                count = cursor.fetchone()[0]
                if count > 0:
                    tkMessageBox.showwarning("Warning", "There are students enrolled in this course. Course cannot be deleted.")
                    return
                cursor.execute("DELETE FROM course WHERE course_code = ?", (delete_data,))
                conn.commit()
                conn.close()
                tkMessageBox.showinfo("Message", "The course has been deleted successfully!")
            except:
                tkMessageBox.showerror("Error", "An error has occurred")
                return
        self.update_course_table()

# ******** EDIT COURSE
    def update_course_info(self):
        decision = tkMessageBox.askyesno("Warning", "Are you sure you want to make changes in the course information?")
        if not decision:
            tkMessageBox.showinfo("Message", "The changes have not been saved")
            return
        conn = sqlite3.connect('attendancesystem.db')
        cursor = conn.cursor()

        selected_code = self.ctable.focus()
        code_details = str(self.ctable.item(selected_code)['values'][0])
        course_data = str(code_details)
        new_course = self.cnameent.get().upper()
        if self.coursename_exists(cursor,new_course):
                tkMessageBox.showerror("Error", "The course cannot be added. It already exists!")
        else:
            cursor.execute('''UPDATE course SET courseName = :new_course WHERE course_code = :course_code''',{'new_course': new_course, 'course_code': course_data})
            conn.commit()
        conn.close()
        tkMessageBox.showinfo("Message", "The edited information has been updated successfully!")
        self.coursecom()
        self.editframe.destroy()
        self.update_course_table()
    
    def coursename_exists(self, cursor,courseName):
        conn = sqlite3.connect('attendancesystem.db')
        cursor = conn.cursor()
        query = '''SELECT * FROM course WHERE courseName = ?'''
        cursor.execute(query, (courseName,))
        conn.commit()
        if cursor.fetchone():
            return True
        conn.close()
        return False

    def edit_course(self):
        if not self.ctable.selection():
            tkMessageBox.showerror("Error", "No item selected. Please select a course from the table.")
            return
        conn = sqlite3.connect('attendancesystem.db')
        cursor = conn.cursor()

        selected_course = self.ctable.focus()
        code_details = str(self.ctable.item(selected_course)['values'][0])
        cursor.execute("SELECT * FROM course WHERE course_code = '" + str(code_details)+"'")
        data = cursor.fetchall()

        global ccodeent; global cnameent

        def go_back():
            self.coursecom()
            self.editframe.destroy()

        self.editframe = tk.Frame(self.mainframe, width=1150, height=600, background="gray1")
        self.editframe.place(x=65, y=100)
        self.tabview = customtkinter.CTkTabview(master=self.editframe, width=900, height=555)
        self.tabview.place(x=0, y=20)
        self.tabview.configure(text_color="black", fg_color="light yellow", segmented_button_fg_color="lightgoldenrod3", segmented_button_selected_color="light yellow", segmented_button_unselected_color="lightgoldenrod3", segmented_button_unselected_hover_color="light yellow", segmented_button_selected_hover_color="light yellow")
        self.tabview.add("EDIT COURSE")  
        self.csavebtn = customtkinter.CTkButton(self.editframe, text="SAVE CHANGES", text_color="black", font=("Arial", 16), fg_color="lightgoldenrod2", bg_color="light yellow", hover=True, hover_color="lightgoldenrod1", corner_radius=10, width=100, height=35, command=self.update_course_info)
        self.csavebtn.place(x=380, y=260)
        self.backbtn = customtkinter.CTkButton(self.editframe, text="BACK", text_color="black", font=("Arial", 18, "bold"), fg_color="lightgoldenrod2", bg_color="light yellow", hover=True, hover_color="lightgoldenrod1", corner_radius=10, width=100, height=40, command=go_back)
        self.backbtn.place(x=740, y=70)
    # LABELS
        self.clabel1 =customtkinter.CTkLabel(self.editframe,bg_color="light yellow",text="COURSE INFORMATON:",text_color="black",font=("Helvetica",16,"bold"))
        self.clabel1.place(x=45,y=120)
        self.clabel3 =customtkinter.CTkLabel(self.editframe,bg_color="light yellow",text="COURSE:",text_color="black",font=("Helvetica",15))
        self.clabel3.place(x=45,y=195)
    # ENTRIES
        self.cnameent = customtkinter.CTkEntry(self.editframe,bg_color="light yellow",placeholder_text="e.g. BACHELOR OF SCIENCE IN COMPUTER SCIENCE",placeholder_text_color="lightgoldenrod4",border_color="lightgoldenrod2",fg_color="lightgoldenrod2",width=680,height=35)
        self.cnameent.place(x=160,y=195)

        for selected_data in data:
            self.cnameent.insert(0,selected_data[1])

if __name__ == "__main__":
    app = AttendanceSystemApp()
    app.mainloop()
