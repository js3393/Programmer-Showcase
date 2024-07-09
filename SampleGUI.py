#Theater Management System Login
from tkinter import *
import tkinter as tk
import createAcc
import loginWindow
import priceWindow
import loginStatus

from tkinter import messagebox

class TmsGui:
    def __init__(self):
        self.main_win = tk.Tk()
        self.main_win.title("Theater Management Systems")
        self.main_win.minsize(width = 420, height = 200)
        self.main_win.config(bg= "black")
       
        #Loop that sets the row of the main window
        for r in range(3):
            self.main_win.rowconfigure(r, minsize =100)

        #Loop that sets the columns of the main window
        for c in range(3):
            self.main_win.columnconfigure(c, minsize= 140)
       
        #IMG for main window
        photo = PhotoImage(file="TML3.png")

        self.labelGIF = tk.Label(image= photo)

        self.labelGIF.image = photo

        self.labelGIF.grid(row= 0, column = 0, columnspan = 3, rowspan= 2)
       
       

        self.heading_label = tk.Label(text='-Theater Management Systems-',\
                            font=("Times", 16), fg = "white", bg="red")
        self.heading_label.grid(row=0,column=0, columnspan=3)

        self.login_button = tk.Button(text='Login', width= 15, bg="red",\
                            font=("Times", 10), fg= "white", command= self.login_win)
        self.login_button.grid(row=2,column=0)

        self.createAcc_button = tk.Button(text= 'Create Account', width= 15,\
                                font=("Times", 10), bg= "red", fg = "white",\
                                command= self.create_acc)
        self.createAcc_button.grid(row=2, column=1)

        self.close_button = tk.Button(text= '  Close  ', width= 15, bg="red",\
                            font=("Times", 10), fg= "white", \
                            command= self.main_win.destroy)
        self.close_button.grid(row= 2 ,column=2)
                                     

        tk.mainloop()
    def create_acc(self):
        cAcc = createAcc.CreateAcct()
       
       
    def login_win(self):
        lw= loginWindow.LoginWin()
        lw.log_win.wait_window()
       
        if loginStatus.logStatus == "YES":
   
            self.main_win.destroy()
            price= priceWindow.TmsPricing()
       
theaterMs = TmsGui()
