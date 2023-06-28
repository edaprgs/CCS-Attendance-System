# GROUP 12 - CLARIN, PARAGOSO, REPE
from tkinter import *
import customtkinter
from PIL import Image
import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as tkMessageBox
import sqlite3

win = customtkinter.CTk()
customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("blue")
win.title("Student Attendance System")
win.geometry("1200x700+0+0")
win.resizable(False, False)

#**************************************************************** DATABASE CONNECTION ****************************************************************#
# ESTABLISH DATABASE CONNECTION
conn = sqlite3.connect('attendancesystem.db')
cursor = conn.cursor()

# CREATE STUDENT TABLE
create_student = '''CREATE TABLE IF NOT EXISTS student (
	"student_ID"	TEXT NOT NULL,
	"lastName"	TEXT NOT NULL,
	"firstName"	TEXT NOT NULL,
	"midName"	TEXT NOT NULL,
	"year_level"	TEXT NOT NULL,
	"course_code"	TEXT NOT NULL,
	PRIMARY KEY("student_ID")
)'''
conn.execute(create_student)

# CREATE EVENT TABLE
create_event = '''CREATE TABLE IF NOT EXISTS event (
	"event_ID"	TEXT NOT NULL,
	"eventName"	TEXT NOT NULL,
	"start_date"	TEXT NOT NULL,
	"end_date"	TEXT NOT NULL,
	"school_year"	TEXT NOT NULL,
	"semester"	TEXT NOT NULL,
	PRIMARY KEY("event_ID")
)'''
conn.execute(create_event)

# CREATE COURSE TABLE
create_course = '''CREATE TABLE IF NOT EXISTS course (
	"course_code"	TEXT NOT NULL,
	"courseName"	TEXT NOT NULL,
	PRIMARY KEY("course_code")
)'''

conn.execute(create_course)
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
conn.execute(create_attends) 
conn.commit()

#**************************************************************** ATTENDANCE ****************************************************************#
def validate_student_id(student_id):
    # Check if the student ID is in the correct format (0000-0000)
    if len(student_id) != 9 or student_id[4] != '-':
        return False
    return True

def check_student_exists(student_id):
    conn = sqlite3.connect('attendancesystem.db')
    cursor = conn.cursor()
    # Check if the student ID exists in the student table
    query = "SELECT student_ID FROM student WHERE student_ID = ?"
    cursor.execute(query, (student_id,))
    result = cursor.fetchone()
    if result:
        return True
    conn.commit()
    conn.close()
    return False

def add_attendance(student_id, event_id, sign_type):
    conn = sqlite3.connect('attendancesystem.db')
    cursor = conn.cursor()
    # Check if the attendance record already exists
    exists_query = "SELECT * FROM attends WHERE student_ID = ? AND event_ID = ?"
    cursor.execute(exists_query, (student_id, event_id))
    existing_record = cursor.fetchone()
        
    if existing_record:
        tkMessageBox.showinfo("Attendance Recorded", "Attendance for this student at this event is already recorded.")
    else:
        # Add attendance record to the attends table based on the SIGN IN or SIGN OUT action
        if sign_type == 'IN':
            query = "INSERT INTO attends (student_ID, event_ID, signin_datetime) VALUES (?, ?, datetime('now'))"
        elif sign_type == 'OUT':
            query = "UPDATE attends SET signout_datetime = datetime('now') WHERE student_ID = ? AND event_ID = ?"
    cursor.execute(query, (student_id, event_id))
    conn.commit()
    update_student_table()
    conn.close()

def sign_in():
    student_id = sIDentry.get()
    event_id = eIDentry.get().upper()   
    if student_id=='' or event_id=='': tkMessageBox.showwarning("Warning","Please fill the empty field!")
    else: # Validate the student ID format and existence
        if not validate_student_id(student_id):
            tkMessageBox.showerror("Error", "Invalid student ID format. Please use the format 0000-0000.")
            return
        if not check_student_exists(student_id):
            tkMessageBox.showerror("Error", "Student ID does not exist.")
            return
    
        # Add attendance record (sign-in) to the attends table
        add_attendance(student_id, event_id, 'IN')
        tkMessageBox.showinfo("Message","Sign-in successful.")
        return

def sign_out():
    student_id = sIDentry.get()
    event_id = eIDentry.get().upper()
    if student_id=='' or event_id=='': tkMessageBox.showwarning("Warning","Please fill the empty field!")
    else:
        # Validate the student ID format and existence
        if not validate_student_id(student_id):
            tkMessageBox.showerror("Error", "Invalid student ID format. Please use the format 0000-0000.")
            return
        if not check_student_exists(student_id):
            tkMessageBox.showerror("Error", "Student ID does not exist.")
            return
        
        # Add attendance record (sign-out) to the attends table
        add_attendance(student_id, event_id, 'OUT')
        tkMessageBox.showinfo("Message","Sign-out successful.")
        return

#**************************************************************** UI ****************************************************************#
def table_style():
        style=ttk.Style()
        style.theme_use("vista")
        style.configure("Treeview",background="light cyan",fg="black",rowheight=35,fieldbackground="white")
        style.configure("Treeview.Heading", font=('Calibri', 13,'bold')) 
        style.configure("Treeview", highlightthickness=0, bd=0, font=('Calibri', 12)) 
        style.layout("Treeview", [('Treeview.treearea', {'sticky': 'nswe'})]) 
        style.map("Treeview",background=[("selected","turquoise4")])

# BACKGROUND 
mainframe = tk.Frame(win,width=1000,height=1000,bg="light cyan")
mainframe.pack(fill="both")
bg_img = customtkinter.CTkImage(light_image=Image.open("C:\\Users\\User\\Desktop\\ATTENDANCE SYSTEM\\Wolf30.jpg"),size=(465,765))
label1 = customtkinter.CTkLabel(master=mainframe,text= "",image=bg_img,anchor='w')
label1.pack(fill="x")
frame1 = tk.Frame(mainframe,width=910,height=865,background="light cyan")
frame1.place(x=585,y=5)

# ATTENDANCE
label1 =customtkinter.CTkLabel(frame1,text="ATTENDANCE",text_color="dark slate gray",font=("Rowdies",60,"bold"))
label1.place(x=150,y=40)
label2 =customtkinter.CTkLabel(frame1,text="COLLEGE OF COMPUTER STUDIES",text_color="dark slate gray",font=("Arial",16))
label2.place(x=235,y=120)
label3 =customtkinter.CTkLabel(frame1,text="Enter Your Student Identification Number",text_color="dark slate gray",font=("Arial",15))
label3.place(x=233,y=200)
sIDentry = customtkinter.CTkEntry(frame1,placeholder_text="student id",font=("Roboto",35,"bold"),text_color="gray20",placeholder_text_color="gray70",border_color="lightcyan2",fg_color="white",width=450,height=60,justify="center")
sIDentry.place(x=140,y=240)
eIDentry = customtkinter.CTkEntry(frame1,placeholder_text="event id",font=("Roboto",20,"bold"),text_color="gray20",placeholder_text_color="gray70",border_color="lightcyan2",fg_color="white",width=300,height=40,justify="center")
eIDentry.place(x=220,y=310)
signinbtn =customtkinter.CTkButton(frame1,text="SIGN IN",text_color="white",font=("Arial",20,"bold"),fg_color="turquoise4",hover=True,hover_color= "cyan4",corner_radius=10,width=205,height=50,command=sign_in)
signinbtn.place(x=140,y=370)
signoutbtn =customtkinter.CTkButton(frame1,text="SIGN OUT",text_color="white",font=("Arial",20,"bold"),fg_color="gray12",hover=True,hover_color= "gray18",corner_radius=10,width=205,height=50,command=sign_out)
signoutbtn.place(x=385,y=370)

# DISPLAY ATTENDANCE LIST
table_style()
frame2 = tk.Frame(frame1,background="light cyan")
frame2.place(x=120, y=575, width=690, height=200)
y_scroll = customtkinter.CTkScrollbar(frame2, orientation=tk.VERTICAL,button_color="dark slate gray",button_hover_color="dark slate gray",fg_color="light cyan")
y_scroll.pack(side=RIGHT,fill=Y)
atable = ttk.Treeview(frame2, columns=("student_id", "event_id", "sign_in", "sign_out"), show="headings", yscrollcommand=y_scroll.set)
atable.pack(fill=BOTH,expand=True)
y_scroll.configure(command=atable.yview)

# HEADINGS
atable.heading("student_id", text="STUDENT ID")
atable.heading("event_id", text="EVENT ID")
atable.heading("sign_in", text="SIGN IN DATE TIME")
atable.heading("sign_out", text="SIGN OUT DATE TIME")

# COLUMNS
atable.column("student_id", width=100,anchor=CENTER)
atable.column("event_id", width=100,anchor=CENTER)
atable.column("sign_in", width=150,anchor=CENTER)
atable.column("sign_out", width=150,anchor=CENTER)

# DATA
display_data_query = cursor.execute("SELECT * FROM attends ORDER BY student_ID")
fetch = display_data_query.fetchall()
for data in fetch:
    atable.insert('', 'end', values=(data[0], data[1], data[2], data[3]))
conn.commit()

#**************************************************************** UPDATE STUDENT LIST ON THE TABLE ****************************************************************#
def update_student_table():
    conn = sqlite3.connect('attendancesystem.db')
    cursor = conn.cursor()
    atable.delete(*atable.get_children())
    display_data_query = cursor.execute("SELECT * FROM attends ORDER BY student_ID ASC")
    fetch = display_data_query.fetchall()
    for data in fetch:
        atable.insert('', 'end', values=(data[0],data[1],data[2],data[3]))
    conn.commit()
    conn.close()

conn.close()
win.mainloop()
