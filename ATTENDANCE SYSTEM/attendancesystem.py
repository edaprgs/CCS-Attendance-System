# COLLEGE OF COMPUTER STUDIES ATTENDANCE SYSTEM
# GROUP 12 - CLARIN, PARAGOSO, REPE
from tkinter import *
import customtkinter
from PIL import ImageTk,Image
from customtkinter import CTkImage
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
create_event = '''CREATE TABLE IF NOT EXISTS events (
	"event_ID"	TEXT NOT NULL,
	"eventName"	TEXT NOT NULL,
	"start_date"	TEXT NOT NULL,
	"end_date"	TEXT NOT NULL,
	"school_year"	TEXT NOT NULL,
	"semester"	TEXT NOT NULL,
	PRIMARY KEY("event_ID")
)'''
conn.execute(create_event)

# CREATE EVENT LOCATIONS TABLE
create_eventlocation = '''CREATE TABLE IF NOT EXISTS event_locations (
	"event_ID"	TEXT NOT NULL,
	"eventLocation"	TEXT NOT NULL,
	PRIMARY KEY("event_ID"),
    FOREIGN KEY("event_ID") REFERENCES "event"("event_ID")
)'''
conn.execute(create_eventlocation)

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

def validate_event_id(event_id):
    conn = sqlite3.connect('attendancesystem.db')
    cursor = conn.cursor()
# Check if the event ID exists in the events table
    query = "SELECT event_ID FROM events WHERE event_ID = ?"
    cursor.execute(query, (event_id,))
    result = cursor.fetchone()
    conn.close()
    if not result:
        return False 
    return True

def check_student_exists(student_id):
    conn = sqlite3.connect('attendancesystem.db')
    cursor = conn.cursor()
# Check if the student ID exists in the student table
    query = "SELECT student_ID FROM student WHERE student_ID = ?"
    cursor.execute(query, (student_id,))
    result = cursor.fetchone()
    conn.close()
    if result:
        return True
    return False

def add_attendance(student_id, event_id, sign_type):
    conn = sqlite3.connect('attendancesystem.db')
    cursor = conn.cursor()
# Check if the attendance record already exists
    exists_query = "SELECT * FROM attends WHERE student_ID = ? AND event_ID = ?"
    cursor.execute(exists_query, (student_id, event_id))
    existing_record = cursor.fetchone()
    
    if existing_record:
        if sign_type == 'IN':
            tkMessageBox.showinfo("Sign-in Attendance Recorded", "Sign-in Attendance for this student at this event is already recorded.")
        elif sign_type == 'OUT':
            existing_signout = existing_record[3]  
            if existing_signout != '-':
                tkMessageBox.showinfo("Sign-out Attendance Recorded", "Sign-out Attendance for this student at this event is already recorded.")
            else:
                query = "UPDATE attends SET signout_datetime = datetime('now') WHERE student_ID = ? AND event_ID = ?"
                cursor.execute(query, (student_id, event_id))
                conn.commit()
                update_student_table(event_id)
                tkMessageBox.showinfo("Signed Out", "The student has been signed out successfully.")
    else:
        if sign_type == 'IN':
            query = "INSERT INTO attends (student_ID, event_ID, signin_datetime, signout_datetime) VALUES (?, ?, datetime('now'), '-')"
            cursor.execute(query, (student_id, event_id))
            conn.commit()
            update_student_table(event_id)
            tkMessageBox.showinfo("Signed In", "The student has been signed in successfully.")
        else:
            tkMessageBox.showinfo("Message", "Attendance record not found.")
    clear_inputs()
    conn.close()

def sign_in():
    student_id = sIDentry.get()
    event_id = eIDentry.get().upper()   
    if student_id=='' or event_id=='': tkMessageBox.showwarning("Warning","Please fill the empty field!")
    else: 
        if not validate_student_id(student_id):
            tkMessageBox.showerror("Error", "Invalid student ID format. Please use the format 0000-0000.")
            return
        if not check_student_exists(student_id):
            tkMessageBox.showerror("Error", "Student ID does not exist.")
            return
        if not validate_event_id(event_id):
            tkMessageBox.showerror("Error", "Invalid event ID.")
            return
        add_attendance(student_id, event_id, 'IN')
        return
    
def sign_out():
    student_id = sIDentry.get()
    event_id = eIDentry.get().upper()
    if student_id=='' or event_id=='': tkMessageBox.showwarning("Warning","Please fill the empty field!")
    else:
        if not validate_student_id(student_id):
            tkMessageBox.showerror("Error", "Invalid student ID format. Please use the format 0000-0000.")
            return
        if not check_student_exists(student_id):
            tkMessageBox.showerror("Error", "Student ID does not exist.")
            return
        if not validate_event_id(event_id):
            tkMessageBox.showerror("Error", "Invalid event ID.")
            return       
        add_attendance(student_id, event_id, 'OUT')
        return

def clear_inputs():
        sIDentry.delete(0, END)
        eIDentry.delete(0, END)

#**************************************************************** UI ****************************************************************#
def table_style():
    style=ttk.Style()
    style.theme_use("vista")
    style.configure("Treeview",background="light cyan",fg="black",rowheight=35,fieldbackground="white")
    style.configure("Treeview.Heading", font=('Calibri', 15,'bold')) 
    style.configure("Treeview", highlightthickness=0, bd=0, font=('Calibri', 14)) 
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

# ATTENDANCE LABELS
label1 =customtkinter.CTkLabel(frame1,text="ATTENDANCE",text_color="dark slate gray",font=("Rowdies",60,"bold"))
label1.place(x=150,y=40)
label2 =customtkinter.CTkLabel(frame1,text="COLLEGE OF COMPUTER STUDIES",text_color="dark slate gray",font=("Arial",16))
label2.place(x=235,y=120)
label3 =customtkinter.CTkLabel(frame1,text="Enter Your Student Identification Number",text_color="dark slate gray",font=("Arial",15))
label3.place(x=233,y=200)
# ATTENDANCE ENTRIES
sIDentry = customtkinter.CTkEntry(frame1,placeholder_text="student id",font=("Arial",35,"bold"),text_color="gray20",placeholder_text_color="gray70",border_color="lightcyan2",fg_color="white",width=450,height=60,justify="center")
sIDentry.place(x=140,y=240)
eIDentry = customtkinter.CTkEntry(frame1,placeholder_text="event id",font=("Arial",20,"bold"),text_color="gray20",placeholder_text_color="gray70",border_color="lightcyan2",fg_color="white",width=300,height=40,justify="center")
eIDentry.place(x=220,y=310)
# ATTENDANCE BUTTONS
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
def update_student_table(event_id):
    conn = sqlite3.connect('attendancesystem.db')
    cursor = conn.cursor()
    atable.delete(*atable.get_children())
    display_data_query = cursor.execute("SELECT * FROM attends WHERE event_ID = ? ORDER BY student_ID ASC", (event_id,))
    fetch = display_data_query.fetchall()
    for data in fetch:
        atable.insert('', 'end', values=(data[0], data[1], data[2], data[3]))
    conn.commit()
    conn.close()

#**************************************************************** BSCS ATTENDANCE ****************************************************************#
def bscs_attendance():
# RETURN TO THE MAIN WINDOW
    def go_back():
        frame1.place(x=590, y=5)
        frame3.destroy()
    frame3 = tk.Frame(mainframe,width=910,height=865,background="light cyan")
    frame3.place(x=590,y=5)
    label2 =customtkinter.CTkLabel(frame3,text="BACHELOR OF SCIENCE IN COMPUTER SCIENCE ATTENDANCE",text_color="dark slate gray",font=("Arial",16))
    label2.place(x=155,y=15)
    backbtn =customtkinter.CTkButton(frame3,text="RETURN",text_color="white",font=("Arial",18,"bold"),fg_color="gray12",hover=True,hover_color= "gray18",corner_radius=10,width=100,height=40,command=go_back)
    backbtn.place(x=10,y=10)

    table_style()
    frame4 = tk.Frame(frame3,background="light cyan")
    frame4.place(x=10, y=150, width=875, height=600)
    y_scroll = customtkinter.CTkScrollbar(frame4, orientation=tk.VERTICAL,button_color="dark slate gray",button_hover_color="dark slate gray",fg_color="light cyan")
    y_scroll.pack(side=RIGHT,fill=Y)
    cstable = ttk.Treeview(frame4, columns=("student_ID","course_code","event_ID","signin_datetime","signout_datetime"), show="headings",yscrollcommand=y_scroll.set)
    cstable.pack(fill=BOTH,expand=True)

    # COLUMNS
    cstable.column("#0", width=0, stretch=NO)  
    cstable.column("student_ID", width=60,anchor=CENTER)
    cstable.column("course_code", width=60,anchor=CENTER)
    cstable.column("event_ID", width=60,anchor=CENTER)
    cstable.column("signin_datetime", width=120,anchor=CENTER)
    cstable.column("signout_datetime", width=130,anchor=CENTER)

    # HEADINGS
    cstable.heading("student_ID", text="STUDENT ID")
    cstable.heading("course_code", text="COURSE CODE")
    cstable.heading("event_ID", text="EVENT ID")
    cstable.heading("signin_datetime", text="SIGN IN DATE/TIME")
    cstable.heading("signout_datetime", text="SIGN OUT DATE/TIME")

    conn = sqlite3.connect('attendancesystem.db')
    cursor = conn.cursor()
    # Execute the query and fetch the attendance records
    display_data_query = cursor.execute('''SELECT student.student_ID, course.course_code, events.event_id, attends.signin_datetime, attends.signout_datetime FROM student 
    INNER JOIN attends ON student.student_ID = attends.student_ID INNER JOIN events ON attends.event_ID = events.event_ID INNER JOIN course ON student.course_code = course.course_code WHERE course.course_code = 'BSCS' ''')
    attendance_records = display_data_query.fetchall()
    # Populate the Treeview with the attendance records
    for record in attendance_records:
        cstable.insert('', 'end', values=(record[0], record[1], record[2], record[3], record[4]))
    conn.commit()

#**************************************************************** BSCA ATTENDANCE ****************************************************************#
def bsca_attendance():
# RETURN TO THE MAIN WINDOW
    def go_back():
        frame1.place(x=590, y=5)
        frame3.destroy()
    frame3 = tk.Frame(mainframe,width=910,height=865,background="light cyan")
    frame3.place(x=590,y=5)
    label2 =customtkinter.CTkLabel(frame3,text="BACHELOR OF SCIENCE IN COMPUTER APPLICATION ATTENDANCE",text_color="dark slate gray",font=("Arial",16))
    label2.place(x=155,y=15)
    backbtn =customtkinter.CTkButton(frame3,text="RETURN",text_color="white",font=("Arial",18,"bold"),fg_color="gray12",hover=True,hover_color= "gray18",corner_radius=10,width=100,height=40,command=go_back)
    backbtn.place(x=10,y=10)

    table_style()
    frame4 = tk.Frame(frame3,background="light cyan")
    frame4.place(x=10, y=150, width=875, height=600)
    y_scroll = customtkinter.CTkScrollbar(frame4, orientation=tk.VERTICAL,button_color="dark slate gray",button_hover_color="dark slate gray",fg_color="light cyan")
    y_scroll.pack(side=RIGHT,fill=Y)
    catable = ttk.Treeview(frame4, columns=("student_ID","course_code","event_ID","signin_datetime","signout_datetime"), show="headings",yscrollcommand=y_scroll.set)
    catable.pack(fill=BOTH,expand=True)

    # COLUMNS
    catable.column("#0", width=0, stretch=NO)  
    catable.column("student_ID", width=60,anchor=CENTER)
    catable.column("course_code", width=60,anchor=CENTER)
    catable.column("event_ID", width=60,anchor=CENTER)
    catable.column("signin_datetime", width=120,anchor=CENTER)
    catable.column("signout_datetime", width=130,anchor=CENTER)

    # HEADINGS
    catable.heading("student_ID", text="STUDENT ID")
    catable.heading("course_code", text="COURSE CODE")
    catable.heading("event_ID", text="EVENT ID")
    catable.heading("signin_datetime", text="SIGN IN DATE/TIME")
    catable.heading("signout_datetime", text="SIGN OUT DATE/TIME")

    conn = sqlite3.connect('attendancesystem.db')
    cursor = conn.cursor()
    # Execute the query and fetch the attendance records
    display_data_query = cursor.execute('''SELECT student.student_ID, course.course_code, events.event_id, attends.signin_datetime, attends.signout_datetime FROM student 
    INNER JOIN attends ON student.student_ID = attends.student_ID INNER JOIN events ON attends.event_ID = events.event_ID INNER JOIN course ON student.course_code = course.course_code WHERE course.course_code = 'BSCA' ''')
    attendance_records = display_data_query.fetchall()
    # Populate the Treeview with the attendance records
    for record in attendance_records:
        catable.insert('', 'end', values=(record[0], record[1], record[2], record[3], record[4]))
    conn.commit()

#**************************************************************** BSIT ATTENDANCE ****************************************************************#
def bsit_attendance():
# RETURN TO THE MAIN WINDOW
    def go_back():
        frame1.place(x=590, y=5)
        frame3.destroy()
    frame3 = tk.Frame(mainframe,width=910,height=865,background="light cyan")
    frame3.place(x=590,y=5)
    label2 =customtkinter.CTkLabel(frame3,text="BACHELOR OF SCIENCE IN INFORMATION TECHNOLOGY ATTENDANCE",text_color="dark slate gray",font=("Arial",16))
    label2.place(x=155,y=15)
    backbtn =customtkinter.CTkButton(frame3,text="RETURN",text_color="white",font=("Arial",18,"bold"),fg_color="gray12",hover=True,hover_color= "gray18",corner_radius=10,width=100,height=40,command=go_back)
    backbtn.place(x=10,y=10)

    table_style()
    frame4 = tk.Frame(frame3,background="light cyan")
    frame4.place(x=10, y=150, width=875, height=600)
    y_scroll = customtkinter.CTkScrollbar(frame4, orientation=tk.VERTICAL,button_color="dark slate gray",button_hover_color="dark slate gray",fg_color="light cyan")
    y_scroll.pack(side=RIGHT,fill=Y)
    ittable = ttk.Treeview(frame4, columns=("student_ID","course_code","event_ID","signin_datetime","signout_datetime"), show="headings",yscrollcommand=y_scroll.set)
    ittable.pack(fill=BOTH,expand=True)

    # COLUMNS
    ittable.column("#0", width=0, stretch=NO)  
    ittable.column("student_ID", width=60,anchor=CENTER)
    ittable.column("course_code", width=60,anchor=CENTER)
    ittable.column("event_ID", width=60,anchor=CENTER)
    ittable.column("signin_datetime", width=120,anchor=CENTER)
    ittable.column("signout_datetime", width=130,anchor=CENTER)

    # HEADINGS
    ittable.heading("student_ID", text="STUDENT ID")
    ittable.heading("course_code", text="COURSE CODE")
    ittable.heading("event_ID", text="EVENT ID")
    ittable.heading("signin_datetime", text="SIGN IN DATE/TIME")
    ittable.heading("signout_datetime", text="SIGN OUT DATE/TIME")

    conn = sqlite3.connect('attendancesystem.db')
    cursor = conn.cursor()
    # Execute the query and fetch the attendance records
    display_data_query = cursor.execute('''SELECT student.student_ID, course.course_code, events.event_id, attends.signin_datetime, attends.signout_datetime FROM student 
    INNER JOIN attends ON student.student_ID = attends.student_ID INNER JOIN events ON attends.event_ID = events.event_ID INNER JOIN course ON student.course_code = course.course_code WHERE course.course_code = 'BSIT' ''')
    attendance_records = display_data_query.fetchall()
    # Populate the Treeview with the attendance records
    for record in attendance_records:
        ittable.insert('', 'end', values=(record[0], record[1], record[2], record[3], record[4]))
    conn.commit()

#**************************************************************** BSIS ATTENDANCE ****************************************************************#
def bsis_attendance():
# RETURN TO THE MAIN WINDOW
    def go_back():
        frame1.place(x=590, y=5)
        frame3.destroy()
    frame3 = tk.Frame(mainframe,width=910,height=865,background="light cyan")
    frame3.place(x=590,y=5)
    label2 =customtkinter.CTkLabel(frame3,text="BACHELOR OF SCIENCE IN INFORMATION SYSTEM ATTENDANCE",text_color="dark slate gray",font=("Arial",16))
    label2.place(x=155,y=15)
    backbtn =customtkinter.CTkButton(frame3,text="RETURN",text_color="white",font=("Arial",18,"bold"),fg_color="gray12",hover=True,hover_color= "gray18",corner_radius=10,width=100,height=40,command=go_back)
    backbtn.place(x=10,y=10)

    table_style()
    frame4 = tk.Frame(frame3,background="light cyan")
    frame4.place(x=10, y=150, width=875, height=600)
    y_scroll = customtkinter.CTkScrollbar(frame4, orientation=tk.VERTICAL,button_color="dark slate gray",button_hover_color="dark slate gray",fg_color="light cyan")
    y_scroll.pack(side=RIGHT,fill=Y)
    istable = ttk.Treeview(frame4, columns=("student_ID","course_code","event_ID","signin_datetime","signout_datetime"), show="headings",yscrollcommand=y_scroll.set)
    istable.pack(fill=BOTH,expand=True)

    # COLUMNS
    istable.column("#0", width=0, stretch=NO)  
    istable.column("student_ID", width=60,anchor=CENTER)
    istable.column("course_code", width=60,anchor=CENTER)
    istable.column("event_ID", width=60,anchor=CENTER)
    istable.column("signin_datetime", width=120,anchor=CENTER)
    istable.column("signout_datetime", width=130,anchor=CENTER)

    # HEADINGS
    istable.heading("student_ID", text="STUDENT ID")
    istable.heading("course_code", text="COURSE CODE")
    istable.heading("event_ID", text="EVENT ID")
    istable.heading("signin_datetime", text="SIGN IN DATE/TIME")
    istable.heading("signout_datetime", text="SIGN OUT DATE/TIME")

    conn = sqlite3.connect('attendancesystem.db')
    cursor = conn.cursor()
    # Execute the query and fetch the attendance records
    display_data_query = cursor.execute('''SELECT student.student_ID, course.course_code, events.event_id, attends.signin_datetime, attends.signout_datetime FROM student 
    INNER JOIN attends ON student.student_ID = attends.student_ID INNER JOIN events ON attends.event_ID = events.event_ID INNER JOIN course ON student.course_code = course.course_code WHERE course.course_code = 'BSIS' ''')
    attendance_records = display_data_query.fetchall()
    # Populate the Treeview with the attendance records
    for record in attendance_records:
        istable.insert('', 'end', values=(record[0], record[1], record[2], record[3], record[4]))
    conn.commit()

#**************************************************************** TOGGLE MENU ****************************************************************#
def toggle_win():
    tframe=Frame(frame1,width=350,height=865,bg='turquoise4')
    tframe.place(x=0,y=0)

    def bttn(x,y,text,bcolor,fcolor,cmd):
     
        def on_entera(e):
            myButton1['background'] = bcolor #ffcc66
            myButton1['foreground']= 'black'  #000d33

        def on_leavea(e):
            myButton1['background'] = fcolor
            myButton1['foreground']= 'white'

        button_width = 50
        button_height = 3

        def command_wrapper():
            cmd()
            tframe.place_forget()

        myButton1 = Button(tframe,text=text,width=button_width,height=button_height,fg='white',border=0,bg=fcolor,activeforeground='white',
                    activebackground='white',command=command_wrapper,font=('Arial', 13,"bold"))
                      
        myButton1.bind("<Enter>", on_entera)
        myButton1.bind("<Leave>", on_leavea)
        myButton1.place(x=180,y=y,anchor='center')
        return myButton1

    buttons = []
    buttons.append(bttn(0, 100, 'BSCS ATTENDANCE', 'turquoise3', 'turquoise4', bscs_attendance))
    buttons.append(bttn(0, 170, 'BSCA ATTENDANCE', 'turquoise3', 'turquoise4', bsca_attendance))
    buttons.append(bttn(0, 240, 'BSIS ATTENDANCE', 'turquoise3', 'turquoise4', bsis_attendance))
    buttons.append(bttn(0, 310, 'BSIT ATTENDANCE', 'turquoise3', 'turquoise4', bsit_attendance))
    #buttons.append(bttn(0, 380, 'A C E R', 'turquoise3', 'turquoise4', None))
    #buttons.append(bttn(0, 450, 'A C E R', 'turquoise3', 'turquoise4', None))

    def close_menu():
        tframe.place_forget()

    global img2
    image2 = Image.open("close.png")
    new_size = (50,50) 
    resized_image = image2.resize(new_size)
    img2 = ImageTk.PhotoImage(resized_image)

    Button(tframe,image=img2,border=0,command=close_menu,bg='turquoise4',activebackground='turquoise4').place(x=5,y=10)
    
image1 = Image.open("open.png")
new_size = (50,50) 
resized_image = image1.resize(new_size)
img1 = ImageTk.PhotoImage(resized_image)

Button(frame1,image=img1,command=toggle_win,border=0,bg='light cyan',activebackground='light cyan').place(x=5,y=10)

win.mainloop()
