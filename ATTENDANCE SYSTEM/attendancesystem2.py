# GROUP 12 - CLARIN, PARAGOSO, REPE
from tkinter import *
import customtkinter
from PIL import Image
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

win = customtkinter.CTk()
customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("blue")
win.title("Student Attendance System")
win.geometry("1200x700+0+0")
win.resizable(False, False)

#**************************************************************** MAIN WINDOW ****************************************************************#
# BACKGROUND 
mainframe = tk.Frame(win,width=1000,height=1000,bg="light cyan")
mainframe.pack(fill="both")
bg_img = customtkinter.CTkImage(light_image=Image.open("C:\\Users\\User\\Desktop\\ATTENDANCE SYSTEM\\Wolf30.jpg"),size=(465,765))
label1 = customtkinter.CTkLabel(master=mainframe,text= "",image=bg_img,anchor='w')
label1.pack(fill="x")
frame1 = tk.Frame(mainframe,width=910,height=865,background="light cyan")
frame1.place(x=585,y=5)
# ATTENDANCE
label1 =customtkinter.CTkLabel(frame1,text="ATTENDANCE",text_color="turquoise4",font=("Verdana",60,"bold"))
label1.place(x=140,y=60)
label2 =customtkinter.CTkLabel(frame1,text="Enter Your Identification Number",text_color="gray40",font=("Arial",16))
label2.place(x=250,y=200)
label3 =customtkinter.CTkLabel(frame1,text="To Sign In or Sign Out",text_color="gray40",font=("Arial",15))
label3.place(x=290,y=230)
eIDentry = customtkinter.CTkEntry(frame1,placeholder_text="e.g. 2021-1574",font=("Arial",35,"bold"),text_color="gray30",placeholder_text_color="gray80",border_color="light cyan2",fg_color="light cyan2",width=450,height=60,justify="center")
eIDentry.place(x=140,y=300)
signinbtn =customtkinter.CTkButton(frame1,text="SIGN IN",text_color="black",font=("Arial",18),fg_color="cornsilk2",hover=True,hover_color= "cornsilk1",corner_radius=10,width=150,height=50)
signinbtn.place(x=190,y=390)
signoutbtn =customtkinter.CTkButton(frame1,text="SIGN OUT",text_color="white",font=("Arial",18),fg_color="lemonchiffon4",hover=True,hover_color= "navajowhite4",corner_radius=10,width=150,height=50)
signoutbtn.place(x=390,y=390)

win.mainloop()