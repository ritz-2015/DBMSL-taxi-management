from tkinter import *
import customtkinter
from tkinter import ttk

from dbms.billing_backend import billing_history12, customer_billing_history
from dbms.booking_backend import customerbooking_selectall
from dbms.driver_history_backend import customer_driver_history
from libs import Global


class CustomerBookingHistory():
    def __init__(self, main):
        self.main=main
        customtkinter.set_appearance_mode('dark')
        customtkinter.set_default_color_theme('blue')
        self.main.title("{} Booking History".format(Global.currentUser[1]))
        self.main.resizable(0, 0)
        frame_width = 1050
        frame_height = 500
        screen_width = self.main.winfo_screenwidth()
        screen_height = self.main.winfo_screenheight()
        x_cordinate = int((screen_width / 2) - (frame_width / 2))
        y_cordinate = int((screen_height / 2) - (frame_height / 2))
        self.main.geometry('{}x{}+{}+{}'.format(frame_width, frame_height, x_cordinate+50, y_cordinate+50))
        self.main.bind("<Escape>", lambda e:self.main.destroy())
        self.main.iconbitmap("C:/Users/SAEE/OneDrive/Desktop/Ritama_College/Ritama_DBMS_miniproj/Taxi-Booking-System1-master/Taxi-Booking-System1-master/Images/logo.ico")

        font1 = customtkinter.CTkFont(family='Times New Roman', size=30, weight='bold')

        # +++++++++++++++++++++++++++++Getting customer id using global++++++++++++++++++++++++++++
        customerid = customtkinter.CTkEntry(master=self.main)
        customerid.insert(0, Global.currentUser[0])

        topFrame = customtkinter.CTkFrame(self.main, height=80)
        topFrame.pack(side=TOP, fill=BOTH)

        titlelabel = customtkinter.CTkLabel(topFrame, text='{} Booking History'.format(Global.currentUser[1]), font=font1)
        titlelabel.place(relx=0.5, rely=0.5, anchor=CENTER)

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

        treeView=ttk.Treeview(self.main)
        treeView.pack(side=BOTTOM, fill=BOTH, expand=True)
        treeView['columns'] = ('bookingid', 'pickupaddress', 'dropofaddress', 'date', 'time')
        treeView.column('#0', width=0, stretch=0)
        treeView.column('bookingid', width=100, anchor=CENTER)
        treeView.column('pickupaddress', width=100, anchor=CENTER)
        treeView.column('dropofaddress', width=100, anchor=CENTER)
        treeView.column('date', width=100, anchor=CENTER)
        treeView.column('time', width=100, anchor=CENTER)

        treeView.heading('#0', text='', anchor=CENTER)
        treeView.heading('bookingid', text='Booking ID', anchor=CENTER)
        treeView.heading('pickupaddress', text='Pickup Address', anchor=CENTER)
        treeView.heading('dropofaddress', text='Dropoff Address', anchor=CENTER)
        treeView.heading('date', text='Date', anchor=CENTER)
        treeView.heading('time', text='Time', anchor=CENTER)
        treeView.pack(side=TOP, fill=BOTH, expand=TRUE)

        def bookinghistory():
            Bookresult = customerbooking_selectall(customerid.get())

            for x in Bookresult:
                treeView.insert(parent='', index='end', values=(x[0], x[1], x[4], x[2], x[3]))

        bookinghistory()






if __name__=='__main__':
    main=customtkinter.CTk()
    CustomerBookingHistory(main)
    main.mainloop()