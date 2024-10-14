from tkinter import *
import customtkinter
from PIL import ImageTk,Image
from tkinter import ttk
from tkinter import messagebox

from dbms.customer_backend import select_allcustomer
from dbms.customer_management import search_customer
from dbms.driver_management import select_alldriver, driver_select_all, driver_select_all22


class SearchDrivers():
    def __init__(self, main):
        self.main=main
        customtkinter.set_appearance_mode('dark')
        customtkinter.set_default_color_theme('blue')
        self.main.iconbitmap("C:/Users/SAEE/OneDrive/Desktop/Ritama_College/Ritama_DBMS_miniproj/Taxi-Booking-System1-master/Taxi-Booking-System1-master/Images/logo.ico")
        self.main.title("Taxi Booking System | Search Drivers")
        self.main.resizable(0, 0)
        frame_width = 1000
        frame_height = 500
        screen_width = self.main.winfo_screenwidth()
        screen_height = self.main.winfo_screenheight()
        x_cordinate = int((screen_width / 2) - (frame_width / 2))
        y_cordinate = int((screen_height / 2) - (frame_height / 2))
        self.main.geometry("{}x{}+{}+{}".format(frame_width, frame_height, x_cordinate + 200, y_cordinate))

        font1 = customtkinter.CTkFont(family='Times New Roman', size=30, weight='bold')
        font720 = customtkinter.CTkFont(family='Times New Roman', size=20, weight='bold')

        topFrame = customtkinter.CTkFrame(self.main, height=80)
        topFrame.pack(side=TOP, fill=BOTH)

        # ++++++++++++++++++++++++++++ID Label+++++++++++++++++++++++++++++++++++++
        idlbl = customtkinter.CTkLabel(master=topFrame, text="Search: ", font=font720)
        idlbl.place(x=20, y=20)

        # ++++++++++++++++++++++++++++++ID TextField++++++++++++++++++++++++++++++++++++++++++++++++++
        idtxt = customtkinter.CTkEntry(master=topFrame,font=font720,  placeholder_text="Driver Name", width=200)
        idtxt.place(x=100, y=20)


        style1 = ttk.Style()
        style1.theme_use("default")
        style1.configure("Treeview",
                         background="#2b2b2b",
                         foreground="white",
                         rowheight=25,
                         fieldbackground="#2b2b2b",
                         bordercolor="#343638",
                         borderwidth=0,
                         font=('Times New Roman', 16))
        style1.map('Treeview', background=[('selected', '#22559b')])

        style1.configure("Treeview.Heading",
                         background="#565b5e",
                         foreground="white",
                         relief="flat",
                         font=('Times New Roman', 17))
        style1.map("Treeview.Heading",
                   background=[('active', '#3484F0')], )

        customerTreeview=ttk.Treeview(self.main)
        customerTreeview.pack(side=BOTTOM, fill=BOTH, expand=TRUE)

        customerTreeview['columns']=('did','name','mobile','email','license','driverstatus')
        customerTreeview.column('#0', width=0, stretch=0)
        customerTreeview.column('did', width=100, anchor=CENTER)
        customerTreeview.column('name', width=150, anchor=CENTER)
        customerTreeview.column('mobile', width=100, anchor=CENTER)
        customerTreeview.column('email', width=100, anchor=CENTER)
        customerTreeview.column('license', width=100, anchor=CENTER)
        customerTreeview.column('driverstatus', width=200, anchor=CENTER)


        customerTreeview.heading('#0', text='', anchor=CENTER)
        customerTreeview.heading('did',text='Driver ID', anchor=CENTER)
        customerTreeview.heading('name', text='Name', anchor=CENTER)
        customerTreeview.heading('mobile', text='Mobile', anchor=CENTER)
        customerTreeview.heading('email', text='Email', anchor=CENTER)
        customerTreeview.heading('license', text='License No', anchor=CENTER)
        customerTreeview.heading('driverstatus', text='Driver Status', anchor=CENTER)


        def search_customer1():
            result = select_alldriver()
            for x in result:

                customerTreeview.insert(parent='', index='end', values=(x[0], x[1], x[2], x[3], x[4], x[6]))

        search_customer1()


        def search():
            val = idtxt.get()
            customerResult = driver_select_all22(val)
            customerTreeview.delete(*customerTreeview.get_children())

            for xx in customerResult:
                customerTreeview.insert(parent='', index='end',
                                        values=(xx[0], xx[1], xx[2], xx[3], xx[4], xx[6]))



        search_image = customtkinter.CTkImage(light_image=Image.open(
            "C:/Users/SAEE/OneDrive/Desktop/Ritama_College/Ritama_DBMS_miniproj/Taxi-Booking-System1-master/Taxi-Booking-System1-master/Images/search-alt-2-regular-24.png"))
        deletebtn = customtkinter.CTkButton(master=topFrame, command=search, image=search_image, text="Search",font=font720, width=180)
        deletebtn.place(x=320, y=20)





if __name__=='__main__':
    main=customtkinter.CTk()
    SearchDrivers(main)
    main.mainloop()
