import tkinter as tk
from tkinter import font as tkfont
import os
from tkinter import *
# from tkinter import messagebox
# top = Tk()

# for linking all the windows
class Main(tk.Tk):
    bgr="images.png"
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title_font = tkfont.Font(family='Calibri', size=20, weight="bold")
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.bgr=tk.PhotoImage(file="images.png")
        self.frames = {}
        for F in (basepage,MainWindow,PMSforAdministrator,PMSforOperator,PMSforTicketor,PMSforCashier,LoginforAdministrator,RegisterforAdmintrator,AdministratorWindow,Customer):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame("MainWindow")
    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()
class basepage(tk.Frame):
    def __init__(self,parent,controller):
        super().__init__(parent)

        label_bkgr=tk.Label(self,image=controller.bgr)
        label_bkgr.place(relx=0.5,rely=0.5,anchor=CENTER)
# main window of the library management
class MainWindow(basepage):
    def __init__(self, parent, controller):
        super().__init__(parent,controller) ### This Code to be copied in every Class. and bg code removed
        self.controller = controller
        self.controller.iconphoto(False, tk.PhotoImage(file='PMS.png'))
        self.controller.title("Parking Management System")  # Title for Window
        self.controller.state('zoomed')  # Making full screen
        HeadingLabel1 = tk.Label(self, text="Parking Management System", font=('Calibri', 60,'bold'), foreground='#FFFFFF' , background='#808080')
        HeadingLabel1.pack()
        f = tkfont.Font(HeadingLabel1, HeadingLabel1.cget("font"))
        f.configure(underline=True)
        HeadingLabel1.configure(font=f)

        HeadingLabel2 = tk.Label(self, text="Welcome to the Parking System!", font=('Calibri', 15,'bold')).pack(pady=20)
        user1_Button = tk.Button(self, text='Administrator',
                                command=lambda: controller.show_frame("PMSforAdministrator"),
                                relief='raised', borderwidth=3, width=40, height=3).pack(pady=10)
        # command=lambda:LibraryManagementSystem.login()
        user2_Button = tk.Button(self, text='Operator',
                                 command=lambda: controller.show_frame("PMSforOperator"),
                                 relief='raised', borderwidth=3, width=40, height=3).pack(
            pady=10)  # Creating a register button
        user3_Button = tk.Button(self, text='Ticketor',
                                 command=lambda: controller.show_frame("PMSforTicketor"),
                                 relief='raised', borderwidth=3, width=40, height=3).pack(
            pady=10)
        user3_Button = tk.Button(self, text='Cashier',
                                 command=lambda: controller.show_frame("PMSforCashier"),
                                 relief='raised', borderwidth=3, width=40, height=3).pack(
            pady=10)
        Exit_Button = tk.Button(self, text="Exit", command=controller.destroy, relief="raised", borderwidth=3, width=40,
                                height=3).pack(pady=10)
        # Empty_Space = tk.Label(self, text='', font=('Helvetica', 13), fg='white', bg='#65428C')
        # Empty_Space.pack(fill='both', expand=True) #coloring half if the screen
# window for student login and registeration fo student
class PMSforAdministrator(basepage):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#358597')
        self.controller = controller
        self.controller.iconphoto(False, tk.PhotoImage(file='PMS.png'))
        self.controller.title("Parking Management System")
        self.controller.state('zoomed')
        HeadingLabel1 = tk.Label(self, text="Parking Management System", font=('Calibri', 60,), foreground='#F4A896',
                                 background='#358597')
        HeadingLabel1.pack()
        f = tkfont.Font(HeadingLabel1, HeadingLabel1.cget("font"))
        f.configure(underline=True)
        HeadingLabel1.configure(font=f)
        HeadingLabel2 = tk.Label(self, text='Administrator', font=('Calibri', 30, 'bold'), fg='#F4A896', bg='#358597')
        HeadingLabel2.pack()
        Space_Label = tk.Label(self, height=4, bg='#358597')  # Adding some space
        Space_Label.pack()
        f = tkfont.Font(HeadingLabel1, HeadingLabel1.cget("font"))
        f.configure(underline=True)
        HeadingLabel1.configure(font=f)
        Space_Label = tk.Label(self, height=8, bg='#358597')
        Space_Label.pack()
        login_Button = tk.Button(self, text='Login', command=lambda: controller.show_frame("LoginforAdministrator"),
                                 relief='raised', borderwidth=3, width=40, height=3)
        login_Button.pack(pady=10)

        Register_Button = tk.Button(self, text='Register', command=lambda: controller.show_frame("RegisterforAdmintrator"), relief='raised',borderwidth=3, width=40, height=3).pack(pady=10)

        Back_Button = tk.Button(self, text="Back", command=lambda: controller.show_frame("MainWindow"), relief="raised", borderwidth=3, width=40,
                                height=3).pack(pady=10)
# main window for Employees
class PMSforOperator(basepage):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#358597')
        self.controller = controller
        self.controller.iconphoto(False, tk.PhotoImage(file='PMS.png'))
        self.controller.title("Parking Management System")
        self.controller.state('zoomed')
        HeadingLabel1 = tk.Label(self, text="Parking Management System", font=('Calibri', 60,), foreground='#F4A896',
                                 background='#358597')
        HeadingLabel1.pack()
        f = tkfont.Font(HeadingLabel1, HeadingLabel1.cget("font"))
        f.configure(underline=True)
        HeadingLabel1.configure(font=f)
        HeadingLabel2 = tk.Label(self, text='Operator', font=('Calibri', 30, 'bold'), fg='#F4A896', bg='#358597')
        HeadingLabel2.pack()
        Space_Label = tk.Label(self, height=4, bg='#358597')
        Space_Label.pack()  # Adding some space
        f = tkfont.Font(HeadingLabel1, HeadingLabel1.cget("font"))
        f.configure(underline=True)
        HeadingLabel1.configure(font=f)
        Space_Label = tk.Label(self, height=8, bg='#358597')
        Space_Label.pack()
        Login_Button = tk.Button(self, text='Login', command=lambda: controller.show_frame("LoginforAll"),
                                 relief='raised', borderwidth=3, width=40, height=3)
        Login_Button.pack(pady=10)
        Back_Button = tk.Button(self, text="Back", command=lambda: controller.show_frame("MainWindow"), relief="raised",
                                borderwidth=3, width=40,
                                height=3).pack(pady=10)

class PMSforTicketor(basepage):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#358597')
        self.controller = controller
        self.controller.iconphoto(False, tk.PhotoImage(file='PMS.png'))
        self.controller.title("Parking Management System")
        self.controller.state('zoomed')
        HeadingLabel1 = tk.Label(self, text="Parking Management System", font=('Calibri', 60,), foreground='#F4A896',
                                 background='#358597')
        HeadingLabel1.pack()
        f = tkfont.Font(HeadingLabel1, HeadingLabel1.cget("font"))
        f.configure(underline=True)
        HeadingLabel1.configure(font=f)
        HeadingLabel2 = tk.Label(self, text='Ticketor', font=('Calibri', 30, 'bold'), fg='#F4A896', bg='#358597')
        HeadingLabel2.pack()
        Space_Label = tk.Label(self, height=4, bg='#358597')
        Space_Label.pack()  # Adding some space
        f = tkfont.Font(HeadingLabel1, HeadingLabel1.cget("font"))
        f.configure(underline=True)
        HeadingLabel1.configure(font=f)
        Space_Label = tk.Label(self, height=8, bg='#358597')
        Space_Label.pack()
        Login_Button = tk.Button(self, text='Login', command=lambda: controller.show_frame("LoginforAll"),
                                 relief='raised', borderwidth=3, width=40, height=3)
        Login_Button.pack(pady=10)

        Back_Button = tk.Button(self, text="Back", command=lambda: controller.show_frame("MainWindow"), relief="raised", borderwidth=3, width=40,height=3).pack(pady=10)

class PMSforCashier(basepage):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#358597')
        self.controller = controller
        self.controller.iconphoto(False, tk.PhotoImage(file='PMS.png'))
        self.controller.title("Library Management System")
        self.controller.state('zoomed')
        HeadingLabel1 = tk.Label(self, text="Library Management System", font=('Calibri', 60,), foreground='#F4A896',
                                 background='#358597')
        HeadingLabel1.pack()
        f = tkfont.Font(HeadingLabel1, HeadingLabel1.cget("font"))
        f.configure(underline=True)
        HeadingLabel1.configure(font=f)
        HeadingLabel2 = tk.Label(self, text='Cashier', font=('Calibri', 30, 'bold'), fg='#F4A896', bg='#358597')
        HeadingLabel2.pack()
        Space_Label = tk.Label(self, height=4, bg='#358597')
        Space_Label.pack()  # Adding some space
        f = tkfont.Font(HeadingLabel1, HeadingLabel1.cget("font"))
        f.configure(underline=True)
        HeadingLabel1.configure(font=f)
        Space_Label = tk.Label(self, height=8, bg='#358597')
        Space_Label.pack()
        Login_Button = tk.Button(self, text='Login', command=lambda: controller.show_frame("LoginforAll"),
                                 relief='raised', borderwidth=3, width=40, height=3)
        Login_Button.pack(pady=10)

        Back_Button = tk.Button(self, text="Back", command=lambda: controller.show_frame("MainWindow"), relief="raised", borderwidth=3, width=40,height=3).pack(pady=10)

class LoginforAdministrator(basepage):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#358597')
        self.AdmID = ''
        self.password = ''
        self.controller = controller
        self.controller.iconphoto(False, tk.PhotoImage(file='PMS.png'))
        self.controller.title("Parking Management System ")
        self.controller.state('zoomed')
        HeadingLabel1 = tk.Label(self, text="Parking Management System", font=('Calibri', 60,), foreground='#F4A896',
                                 background='#358597')
        HeadingLabel1.pack()
        f = tkfont.Font(HeadingLabel1, HeadingLabel1.cget("font"))
        f.configure(underline=True)
        HeadingLabel1.configure(font=f)
        HeadingLabel2 = tk.Label(self, text='Administrator', font=('Calibri', 30, 'bold'), fg='#F4A896', bg='#358597')
        HeadingLabel2.pack()
        HeadingLabel3 = tk.Label(self, text='Log In', font=('Calibri', 30,'bold'), fg='#F4A896', bg='#358597')
        HeadingLabel3.pack()
        Space_Label = tk.Label(self, height=6, bg='#358597')
        Space_Label.pack()  # Adding some space
        ID_verify = tk.StringVar()
        password_verify = tk.StringVar()
        tk.Label(self, text="Administrator ID", font=('Calibri', 15), fg='#F4A896', bg='#358597', ).pack()
        # Username input
        self.AdministratorID = tk.Entry(self, textvariable=ID_verify, font=('Calibri', 15), width=22).pack(ipady=7)
        tk.Label(self, text="Password", font=('Calibri', 15), fg='#F4A896', bg='#358597').pack(pady=10)
        # Password input
        self.password = tk.Entry(self, textvariable=password_verify, font=('Calibri', 15), width=22, show = '*').pack(ipady=7)
        space_label = tk.Label(self,height=2 , bg = '#358597').pack()
        def login_verify():
            ID = ID_verify.get()   #Getting variable data
            password = password_verify.get()   #Getting variable data
            here = os.path.dirname(os.path.realpath(__file__))
            subdir = 'Users'
            filepath = os.path.join(here , subdir)
            list_of_file = os.listdir('Users')
            if ID in list_of_file:   #Password checker
                file = open(filepath + '\\' + ID , 'r')
                verify = file.read().splitlines()
                if password in verify:
                    controller.show_frame('Customer')
                else:
                    tk.Label(self, text = 'Incorrect Password!', fg="red", bg="#358597", font=("Calibri", 18)).pack()
            else:
                tk.Label(self,text = 'Invalid User!', fg="red", bg="#358597", font=("Calibri", 18)).pack()
        Enter_Button = tk.Button(self, text='Enter',command =lambda: controller.show_frame("AdministratorWindow"), relief='raised', borderwidth=3, width=40, height=3).pack(pady=10) #Creating an Enter button
        Back_Button = tk.Button(self, text='Back', command=lambda: controller.show_frame("PMSforAdministrator"),relief='raised', borderwidth=3, width=40, height=3).pack(pady=10)

class RegisterforAdmintrator(basepage):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#358597')
        self.AdmName = ''
        self.AdmID = ''
        self.AdmMobileNo = ''
        self.AdmGender = ''
        self.AdmDOB = ''
        self.AdmAddress = ''
        self.controller = controller
        self.controller.iconphoto(False, tk.PhotoImage(file='PMs.png'))
        self.controller.title("Parking Management System ")
        self.controller.state('zoomed')
        HeadingLabel1 = tk.Label(self, text="Administrator Registration", font=('Calibri', 40, 'bold'), foreground='#F4A896',
                                 background='#358597')
        Space_Label = tk.Label(self, height=5, bg='#358597')
        Space_Label.pack()  # Adding some space
        HeadingLabel2 = tk.Label(self, text="Enter Details Below To Register!", font=('Calibri', 15, 'bold'),
                                 bg='#358597', fg='#F4A896')
        HeadingLabel2.pack()
        AdmName_verify = tk.StringVar()
        AdmID_verify = tk.StringVar()
        AdmMobileNo_verify = tk.StringVar()
        AdmGender_verify = tk.StringVar()
        AdmDOB_verify = tk.StringVar()
        AdmAddress_verify = tk.StringVar()
        password_verify = tk.StringVar()
        here = os.path.dirname(os.path.realpath(__file__))
        subdir = "Users"
        filepath = os.path.join(here, subdir)
        files = os.listdir()
        if subdir in files:
            pass
        else:
            os.mkdir(os.path.join(here, subdir))
        def register_Administrator():
            name = AdmName_verify.get()
            ID = AdmID_verify.get()
            MobileNo = AdmMobileNo_verify.get()
            Gender = AdmGender_verify.get()
            DOB = AdmDOB_verify.get()
            Address = AdmAddress_verify.get()
            password = password_verify.get()
            if ID == '1' or ID == '2' or ID == '3':  # Student Roll No.
                try:
                    f = open(filepath + '\\' + ID, 'a+')
                    f.write(name + "\n")
                    f.write(ID + "\n")
                    f.write(MobileNo + "\n")
                    f.write(Gender + "\n")
                    f.write(DOB + "\n")
                    f.write(Address + "\n")
                    f.write(password)
                    f.close()
                    tk.Label(self, text='Student has been successfully Registered!', fg='#00ff00', bg='#358597',
                             font=('Calibri', 18)).pack()
                except IOError:
                    print('Invalid Path!')
            else:
                tk.Label(self, text="Register yourself again!", fg="red", bg="#358597", font=("Calibri", 18)).pack()
        tk.Label(self, text="Name", font=('Calibri', 15), fg='#F4A896', bg='#358597', ).pack()
        # Name
        self.name = tk.Entry(self, textvariable=AdmName_verify, font=('Calibri', 15), width=22).pack()
        tk.Label(self, text="Admistrator ID", font=('Calibri', 15), fg='#F4A896', bg='#358597', ).pack()
        # Customer ID
        self.ID = tk.Entry(self, textvariable=AdmID_verify, font=('Calibri', 15), width=22).pack()
        # PAssword
        tk.Label(self, text="Password", font=('Calibri', 15), fg='#F4A896', bg='#358597', ).pack()
        # Customer ID
        self.ID = tk.Entry(self, textvariable=password_verify, font=('Calibri', 15), width=22).pack()
        tk.Label(self, text="Mobile No", font=('Calibri', 15), fg='#F4A896', bg='#358597').pack()
        # Customer Mobile No
        self.MobileNo = tk.Entry(self, textvariable=AdmMobileNo_verify, font=('Calibri', 15), width=22).pack()
        tk.Label(self, text="Gender", font=('Calibri', 15), fg='#F4A896', bg='#358597', ).pack()
        # Customer Gender
        self.gender = tk.Entry(self, textvariable=AdmGender_verify, font=('Calibri', 15), width=22).pack()
        tk.Label(self, text="DOB", font=('Calibri', 15), fg='#F4A896', bg='#358597', ).pack()
        # Customer DOB
        self.DOB = tk.Entry(self, textvariable=AdmDOB_verify, font=('Calibri', 15), width=22).pack()
        tk.Label(self, text="Address", font=('Calibri', 15), fg='#F4A896', bg='#358597', ).pack()
        # Customer Address
        self.gender = tk.Entry(self, textvariable=AdmAddress_verify, font=('Calibri', 15), width=22).pack()
        Space = tk.Label(self, height=2, bg='#358597').pack()  # Adding some space
        Register_Button = tk.Button(self, text='Register', command=RegisterforAdmintrator, relief='raised', borderwidth=3,
                                    width=40, height=3).pack(pady=10)
        Back_Button = tk.Button(self, text='Back',
                                command=lambda: controller.show_frame("PMSforAdministrator"),
                                relief='raised', borderwidth=3, width=40, height=3).pack(pady=10)

class AdministratorWindow(basepage):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#358597')
        self.username = ''
        self.password = ''
        self.controller = controller
        self.controller.iconphoto(False, tk.PhotoImage(file='PMS.png'))
        self.controller.title("Parking Management System ")
        self.controller.state('zoomed')
        HeadingLabel1 = tk.Label(self, text="Parking Management System", font=('Calibri', 60,), foreground='#F4A896',
                                 background='#358597')
        HeadingLabel1.pack()
        f = tkfont.Font(HeadingLabel1, HeadingLabel1.cget("font"))
        f.configure(underline=True)
        HeadingLabel1.configure(font=f)
        HeadingLabel2 = tk.Label(self, text='Administrator', font=('Calibri', 30, 'bold'), fg='#F4A896', bg='#358597')
        HeadingLabel2.pack()
        Space_Label = tk.Label(self, height=4, bg='#358597')
        Space_Label.pack()  # Adding some space
        username_verify = tk.StringVar()
        password_verify = tk.StringVar()
        Register_Button = tk.Button(self, text='Register Customer detail', command=lambda: controller.show_frame("Customer"),
                                    relief='raised', borderwidth=3, width=40, height=3)
        Register_Button.pack(pady=10)

        update_Button = tk.Button(self, text='Update Customer detail',command=lambda: controller.show_frame("Customer"),
                                    relief='raised', borderwidth=3, width=40, height=3)
        update_Button.pack(pady=10)

        view_Button = tk.Button(self, text='View Customer detail',
                                  command=lambda: controller.show_frame("Customer"),
                                  relief='raised', borderwidth=3, width=40, height=3)
        view_Button.pack(pady=10)

        delete_Button = tk.Button(self, text='Delete Customer detail',
                                command=lambda: controller.show_frame("Customer"),
                                relief='raised', borderwidth=3, width=40, height=3)
        delete_Button.pack(pady=10)

        search_Button = tk.Button(self, text='Search Customer detail',
                                command=lambda: controller.show_frame("Customer"),
                                relief='raised', borderwidth=3, width=40, height=3)
        search_Button.pack(pady=10)

        logout_Button = tk.Button(self, text='Log out',
                                command=lambda: controller.show_frame("MainWindow"),
                                relief='raised', borderwidth=3, width=40, height=3)
        logout_Button.pack(pady=10)
        def login_verify():
            username = username_verify.get()  # Getting variable data
            password = password_verify.get()  # Getting variable data
            here = os.path.dirname(os.path.realpath(__file__))
            subdir = 'Users'
            filepath = os.path.join(here, subdir)
            list_of_file = os.listdir('Users')
            if username in list_of_file:  # Password checker
                file = open(filepath + '\\' + username, 'r')
                verify = file.read().splitlines()
                if password in verify:
                    controller.show_frame('Mainwin2forLib')
                else:
                    tk.Label(self, text='Incorrect Password!', fg="red", bg="#358597", font=("Calibri", 18)).pack()
            else:
                tk.Label(self, text='Invalid User!', fg="red", bg="#358597", font=("Calibri", 18)).pack()
class Customer(basepage):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#358597')
        self.CustName = ''
        self.CustID = ''
        self.CustMobileNo = ''
        self.CustGender = ''
        self.CustDOB = ''
        self.CustAddress = ''
        self.controller = controller
        self.controller.iconphoto(False, tk.PhotoImage(file='PMS.png'))
        self.controller.title("Parking Management System ")
        self.controller.state('zoomed')
        HeadingLabel1 = tk.Label(self, text="Parking Management System", font=('Calibri', 60,), foreground='#F4A896',
                                 background='#358597')
        HeadingLabel1.pack()
        f = tkfont.Font(HeadingLabel1, HeadingLabel1.cget("font"))
        f.configure(underline=True)
        HeadingLabel1.configure(font=f)
        space = tk.Label(self, height=8, bg='#358597').pack()
        f = tkfont.Font(HeadingLabel1, HeadingLabel1.cget('font'))
        f.configure(underline=True)
        HeadingLabel1.configure(font=f)
        space1 = tk.Label(self, height=2, bg='#358597').pack()
        HeadingLabel = tk.Label(self, text="Customer Details", font=('Calibri', 15, 'bold'),
                                bg='#358597', fg='#F4A896')
        HeadingLabel.pack()
        CustName_verify = tk.StringVar()
        CustID_verify = tk.StringVar()
        CustMobileNo_verify = tk.StringVar()
        CustGender_verify = tk.StringVar()
        CustDOB_verify = tk.StringVar()
        CustAddress_verify = tk.StringVar()
        here = os.path.dirname(os.path.realpath(__file__))
        subdir = 'Books'
        subdir2 = 'New Books'
        filepath = os.path.join(here, subdir)
        filepath2 = os.path.join(here, subdir2)
        files = os.listdir()
        if subdir in files:
            pass
        else:
            os.mkdir(os.path.join(here, subdir))
        if subdir2 in files:
            pass
        else:
            os.mkdir(os.path.join(here, subdir2))
        def Add_customer():
            name = CustName_verify.get()
            ID = CustID_verify.get()
            MobileNo = CustMobileNo_verify.get()
            Gender = CustGender_verify.get()
            DOB = CustDOB_verify.get()
            Address = CustAddress_verify.get()
            list_of_file = os.listdir('Books')
            if isbn in list_of_file:
                file = open(filepath + '\\' + name, 'r')
                file.close()
                # verify = file.read().splitlines()
                # if name in verify:
                tk.Label(self, text='This Book is already Present!', fg='red', bg='#358597',
                         font=('Calibri', 18), ).pack()
            else:
                data = open(filepath2 + '\\' + name, 'w')
                data.write(f"name: {name}\nID: {ID}\nMobileNo: {MobileNo}\nGender: {Gender}\nDOB: {DOB}\nAddress:{Address}")
                data.close()
                data = open(filepath + '\\' + name, 'w')
                data.write(f"name: {name}\nID: {ID}\nMobileNo: {MobileNo}\nGender: {Gender}\nDOB: {DOB}\nAddress:{Address}")
                data.close()
                tk.Label(self, text='Book has been Added!', fg='#00ff00', bg='#358597',
                         font=('Times New Roman', 18)).pack()
        # list_all_file = os.listdir()
        # tk.Label(self,text=list_all_file ,font = ('times New Roman' , 8),fg='black',bg = 'white' , ).pack(pady=10)
        tk.Label(self, text="Name", font=('Calibri', 15), fg='#358597', bg='#358597', ).pack()
        #Name
        self.name = tk.Entry(self, textvariable=CustName_verify, font=('Calibri', 15), width=22).pack()
        tk.Label(self, text="Cutomer ID", font=('Calibri', 15), fg='#F4A896', bg='#358597', ).pack()
        #Customer ID
        self.ID= tk.Entry(self, textvariable=CustID_verify, font=('Calibri', 15), width=22).pack()
        tk.Label(self, text="Mobile No", font=('Calibri', 15), fg='#F4A896', bg='#358597').pack()
        #Customer Mobile No
        self.MobileNo = tk.Entry(self, textvariable=CustMobileNo_verify, font=('Calibri', 15), width=22).pack()
        tk.Label(self, text="Gender", font=('Calibri', 15), fg='#F4A896', bg='#358597', ).pack()
        #Customer Gender
        self.gender = tk.Entry(self, textvariable=CustGender_verify, font=('Calibri', 15), width=22).pack()
        tk.Label(self, text="DOB", font=('Calibri', 15), fg='#F4A896', bg='#358597', ).pack()
        # Customer DOB
        self.DOB = tk.Entry(self, textvariable=CustDOB_verify, font=('Calibri', 15), width=22).pack()
        tk.Label(self, text="Address", font=('Calibri', 15), fg='#F4A896', bg='#358597', ).pack()
        # Customer Address
        self.gender = tk.Entry(self, textvariable=CustAddress_verify, font=('Calibri', 15), width=22).pack()
        Enter_Button = tk.Button(self, text='Enter', command=Add_customer, relief='raised', borderwidth=3, width=40,
                                 height=3).pack(pady=10)
        back_Button = tk.Button(self, text='Back', command=lambda: controller.show_frame("LoginforAdministrator"),
                                relief='raised', borderwidth=3, width=40, height=3).pack(pady=10)

if __name__ == "__main__":
    app = Main()
    app.mainloop()