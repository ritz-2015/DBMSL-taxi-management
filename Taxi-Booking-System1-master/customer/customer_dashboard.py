import tkinter
from tkinter import *
import customtkinter
from datetime import date, time, datetime
from tkinter import ttk
from tkinter.ttk import Notebook, Style
from datetime import time, date
import datetime
import math
import tkinter as tk
import time
from time import strftime
import geocoder
import tkintermapview
from matplotlib import pyplot as plt
from sqlalchemy import create_engine
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pymysql
from PIL import ImageTk, Image
import pandas
from tkintermapview import TkinterMapView
from tkcalendar import DateEntry, Calendar
from tktimepicker import AnalogPicker, AnalogThemes, constants
from billing import customer_billing_history
from customer import login, customerprofile, Change_Password, customer_booking_history, viewprofilegui
from dbms.booking_backend import insert_booking, customerbooking_selectall, customerbooking_selectstatsubooked, \
    update_customer_booking1, delete_booking, customer_checkbooking
from dbms.customer_backend import validaecustomerbooking
from dbms.customer_management import delete_record
from dbms.myactivity_backend import delete_myactivity, selectall_myactivity
from dbms.passwordchange_backend import passwordChange
from driver import driverhistory
from libs import Global
from libs.booking_libs import BookingLibs
from tkinter import messagebox

from libs.customer_libs import Customer_Libs


class Customer_Dashboard(customtkinter.CTk):

    def __init__(self, root):
        self.root=root
        customtkinter.set_appearance_mode('dark')
        customtkinter.set_default_color_theme('blue')
        self.root.title("Customer Dashboard | Taxi Booking System")
        self.root.state('zoomed')
        self.root.bind('<Escape>', lambda e: root.destroy())
        #self.root.iconbitmap("C:/Users/SAEE/OneDrive/Desktop/Ritama_College/Ritama_DBMS_miniproj/Taxi-Booking-System1-master/Taxi-Booking-System1-master/Images/logo.ico")

        #++++++++++++++++++++++++++++++Menu+++++++++++++++++++++++++++++++=
        parent_menu=Menu(self.root)

        #-------------------------Exit function-----------------------
        def exit():
            self.root.destroy()

        #------------------------Logout function--------------------------
        def logout():
            self.root.destroy()
            root=customtkinter.CTk()
            login2=login.Login(root)
            root.mainloop()

        file=Menu(parent_menu, tearoff=0)
        file.add_command(label="Open")
        file.add_command(label="Logout", command=logout)
        file.add_command(label="Exit", command=exit)

        parent_menu.add_cascade(label="File", menu=file)
        self.root.config(menu=parent_menu)

        #++++++++++++++++++++++++++++++++Font Collection+++++++++++++++++++++++++++++++++++++++++++
        titlefont = customtkinter.CTkFont(family='Times New Roman', size=30, weight='bold')
        font720 = customtkinter.CTkFont(family='Times New Roman', size=20, weight='normal')
        labelfont=customtkinter.CTkFont(family='Times New Roman', size=20, weight='normal')
        sidemenufont = customtkinter.CTkFont(family='Times New Roman', size=20, weight='normal')

        #+++++++++++++++++++++++++++++Getting customer id using global++++++++++++++++++++++++++++
        customerid=customtkinter.CTkEntry(master=self.root)
        customerid.insert(0, Global.currentUser[0])

        # ++++++++++++++++++++++++++++++++Top Frame+++++++++++++++++++++++++++++++++++
        Top_Frame = customtkinter.CTkFrame(master=self.root, height=100)
        Top_Frame.pack(side=TOP, fill=BOTH, padx=10, pady=10)

        #-----------------------------Title Label-----------------------------------------
        title_lbl = customtkinter.CTkLabel(master=Top_Frame, text="TAXI BOOKING SYSTEM", font=titlefont)
        title_lbl.pack(side=LEFT, pady=20, padx=10)


        #-------------------------------------Welcome Label----------------------------------
        log_name_lbl=customtkinter.CTkLabel(master=Top_Frame, text="Welcome: {}".format(Global.currentUser[1]),font=titlefont)
        log_name_lbl.pack(side=RIGHT, pady=20, padx=10)



        # +++++++++++++++++++++++++++++++Left Frame+++++++++++++++++++++++++++++++++++++++
        left_frame = customtkinter.CTkFrame(master=self.root, width=300)
        left_frame.pack(side=LEFT, fill=BOTH, padx=(10,0), pady=10)

        Cover_Image = Image.open('C:/Users/SAEE/OneDrive/Desktop/Ritama_College/Ritama_DBMS_miniproj/Taxi-Booking-System1-master/Taxi-Booking-System1-master/Images/user-solid-120.png')
        photo1 = ImageTk.PhotoImage(Cover_Image)
        Cover_Image_label = tk.Label(left_frame, image=photo1, bg="#2a2d2e")
        Cover_Image_label.image = photo1
        Cover_Image_label.place(x=100, y=40)

        def my_time():
            time_string = strftime('%I:%M:%S %p')  # time format
            l1.configure(text=time_string)
            l1.after(1000, my_time)  # time delay of 1000 milliseconds

        l1 = customtkinter.CTkLabel(master=left_frame, font=font720)
        l1.place(x=90, y=150)
        my_time()

        #------------------------------Dashboard button-----------------------------------------
        assigndriver_btn_image = customtkinter.CTkImage(light_image=Image.open('C:/Users/SAEE/OneDrive/Desktop/Ritama_College/Ritama_DBMS_miniproj/Taxi-Booking-System1-master/Taxi-Booking-System1-master/Images/edit-alt-regular-24.png'))
        assigndriver_btn = customtkinter.CTkButton(master=left_frame, text="Dashboard             ", hover_color='black',
                                                   font=sidemenufont, width=200,
                                                   image=assigndriver_btn_image, fg_color='#2b2b2b')
        assigndriver_btn.place(x=50, y=200)

        #---------------------------Open profile function----------------------------
        def open_viewprofile():
            main = customtkinter.CTkToplevel()
            viewprofilegui.ViewCustomerProfile(main)
            main.mainloop()

        #-----------------------------My Profile Button------------------------------------------
        profile_img = customtkinter.CTkImage(light_image=Image.open('C:/Users/SAEE/OneDrive/Desktop/Ritama_College/Ritama_DBMS_miniproj/Taxi-Booking-System1-master/Taxi-Booking-System1-master/Images/user-account-solid-24.png'))
        profile_btn = customtkinter.CTkButton(master=left_frame, text="My Profile            ", hover_color='black',font=sidemenufont, width=200,command=open_viewprofile, image=profile_img, fg_color='#2b2b2b')
        profile_btn.place(x=50, y=250)

        # -----------------------------Booking History Function------------------------------------------
        def customerBookingHistory():
            main=customtkinter.CTkToplevel()
            customer_booking_history.CustomerBookingHistory(main)
            main.mainloop()

        # -----------------------------Booking History Button------------------------------------------
        managecustomers_btn_image = customtkinter.CTkImage(light_image=Image.open('C:/Users/SAEE/OneDrive/Desktop/Ritama_College/Ritama_DBMS_miniproj/Taxi-Booking-System1-master/Taxi-Booking-System1-master/Images/user-regular-24.png'))
        managecustomers_btn = customtkinter.CTkButton(master=left_frame, text="Booking History     ",command=customerBookingHistory, hover_color='black',font=sidemenufont, width=200,image=managecustomers_btn_image, fg_color='#2b2b2b')
        managecustomers_btn.place(x=50, y=300)

        # -----------------------------Driver History Function------------------------------------------
        def driverhistory720():
            root=customtkinter.CTkToplevel()
            driverhistory.DriverHistory(root)
            root.mainloop()

        # -----------------------------Driver History Button------------------------------------------
        managedrivers_btn_image = customtkinter.CTkImage(light_image=Image.open('C:/Users/SAEE/OneDrive/Desktop/Ritama_College/Ritama_DBMS_miniproj/Taxi-Booking-System1-master/Taxi-Booking-System1-master/Images/car-regular-24.png'))
        managedrivers_btn = customtkinter.CTkButton(master=left_frame, text="Drivers History     ",command=driverhistory720, hover_color='black',font=sidemenufont, width=200,image=managedrivers_btn_image, fg_color='#2b2b2b')
        managedrivers_btn.place(x=50, y=350)

        # -----------------------------Billing History Function------------------------------------------
        def customer_billing_history_gui():
            main=customtkinter.CTkToplevel()
            customer_billing_history.CustomerBillingHistory(main)
            main.mainloop()

        # -----------------------------Billing Button------------------------------------------
        billing_btn_image = customtkinter.CTkImage(light_image=Image.open('C:/Users/SAEE/OneDrive/Desktop/Ritama_College/Ritama_DBMS_miniproj/Taxi-Booking-System1-master/Taxi-Booking-System1-master/Images/id-card-regular-24.png'))
        billing_btn = customtkinter.CTkButton(master=left_frame, text="Billing                   ",command=customer_billing_history_gui, hover_color='black',font=sidemenufont, width=200,image=billing_btn_image, fg_color='#2b2b2b')
        billing_btn.place(x=50, y=400)

        # -----------------------------Change password toplevel gui------------------------------------------
        def change_password_gui():
            password=customtkinter.CTkToplevel()
            password.title("Taxi Booking System | Change Customer Password")
            password.iconbitmap("EC:/Users/SAEE/OneDrive/Desktop/Ritama_College/Ritama_DBMS_miniproj/Taxi-Booking-System1-master/Taxi-Booking-System1-master/Images/logo.ico")
            frame_width = 530
            frame_height = 400
            password.resizable(0, 0)
            screen_width = password.winfo_screenwidth()
            screen_height = password.winfo_screenheight()
            x_cordinate = int((screen_width / 2) - (frame_width / 2))
            y_cordinate = int((screen_height / 2) - (frame_height / 2))
            password.geometry('{}x{}+{}+{}'.format(frame_width, frame_height, x_cordinate + 70, y_cordinate - 70))


            frame = customtkinter.CTkFrame(password)
            frame.pack(fill=BOTH, expand=TRUE)

            font720 = customtkinter.CTkFont(family='Times New Roman', size=20, weight='normal')

            img = ImageTk.PhotoImage(Image.open("C:/Users/SAEE/OneDrive/Desktop/Ritama_College/Ritama_DBMS_miniproj/Taxi-Booking-System1-master/Taxi-Booking-System1-master/Images/user-solid-72.png"))
            image_label = Label(password, image=img, bg="#2b2b2b")
            image_label.image = img
            image_label.place(x=150, y=40)

            title_lbl = customtkinter.CTkLabel(master=password,text="Changing password for\n{}".format(Global.currentUser[1]),font=font720, bg_color="#2b2b2b")
            title_lbl.place(x=200, y=40)

            currentpw_lbl = customtkinter.CTkLabel(master=password, text="New Password: ", font=font720,
                                                   bg_color="#2b2b2b")
            currentpw_lbl.place(x=60, y=150)

            currentpw_txt = customtkinter.CTkEntry(master=password, font=font720, show='*', width=200)
            currentpw_txt.place(x=240, y=150)

            confirmpw_lbl = customtkinter.CTkLabel(master=password, text="Confirm Password: ", font=font720,
                                                   bg_color="#2b2b2b")
            confirmpw_lbl.place(x=60, y=220)

            conformpw_txt = customtkinter.CTkEntry(master=password, show='*', font=font720, width=200)
            conformpw_txt.place(x=240, y=220)

            def show_password():
                if i.get() == 1:
                    conformpw_txt.configure(show='')
                    currentpw_txt.configure(show='')
                else:
                    conformpw_txt.configure(show='*')
                    currentpw_txt.configure(show='*')

            i = customtkinter.IntVar()

            password_show = customtkinter.CTkCheckBox(password, text="Show password", variable=i,command=show_password, bg_color="#2b2b2b")
            password_show.place(x=240, y=260)

            idtxt = Entry(password)
            idtxt.insert(0, "{}".format(Global.currentUser[0]))

            def change_password():
                customerid = idtxt.get()
                password1 = currentpw_txt.get()
                newpassword = conformpw_txt.get()

                if password1 == newpassword:
                    password720 = Customer_Libs(cid=customerid, password=newpassword)
                    result = passwordChange(password720)
                    if result == True:
                        messagebox.showinfo("Taxi Booking System", "The password is changed successfully!")
                        self.root.destroy()
                        root=customtkinter.CTk()
                        login.Login(root)
                        root.mainloop()
                    else:
                        messagebox.showerror("Taxi Booking System", "Error occurred!")

                else:
                    messagebox.showerror("Taxi Booking System", "The password does not match. Please try again!")

            confirm_btn = customtkinter.CTkButton(master=password, command=change_password, text="Change Password!",font=font720)
            confirm_btn.place(x=230, y=310)

        # -----------------------------Change Password Button------------------------------------------
        viewcustomer_btn_image = customtkinter.CTkImage(light_image=Image.open('C:/Users/SAEE/OneDrive/Desktop/Ritama_College/Ritama_DBMS_miniproj/Taxi-Booking-System1-master/Taxi-Booking-System1-master/Images/key-solid-24.png'))
        viewcustomer_btn = customtkinter.CTkButton(master=left_frame, text="Change Password     ",command=change_password_gui, hover_color='black',font=sidemenufont, width=200,image=viewcustomer_btn_image, fg_color='#2b2b2b')
        viewcustomer_btn.place(x=50, y=450)

        # -----------------------------Delete account function------------------------------------------
        def delete_account():
            delete_account_dialog = customtkinter.CTkInputDialog(text="Do you want to delete you account? if you want to delete then type YES or NO to cancel", title="Delete an account")
            dialogResult=delete_account_dialog.get_input()
            if dialogResult=='YES':
                customeridd = customerid.get()
                deleteActivityResult = delete_myactivity(customeridd)
                deleteResult = delete_record(customeridd)
                if deleteResult and deleteActivityResult == True:
                    messagebox.showinfo("Taxi Booking System", "The account is deleted successfully")
                    self.root.destroy()
                    root=customtkinter.CTk()
                    login.Login(root)
                    root.mainloop()
            else:
                messagebox.showinfo("Taxi Booking System", "The account delete is cancelled")

        # -----------------------------Delete Account Button------------------------------------------
        delete_btn_image = customtkinter.CTkImage(light_image=Image.open('C:/Users/SAEE/OneDrive/Desktop/Ritama_College/Ritama_DBMS_miniproj/Taxi-Booking-System1-master/Taxi-Booking-System1-master/Images/user-x-regular-24.png'))
        detete_account_btn = customtkinter.CTkButton(master=left_frame,command=delete_account, text="Delete Account         ", hover_color='black',font=sidemenufont, width=200,image=delete_btn_image, fg_color='#2b2b2b')
        detete_account_btn.place(x=50, y=500)

        # -----------------------------Logout Function------------------------------------------
        def logout():
            self.root.destroy()
            root=customtkinter.CTk()
            login.Login(root)
            root.mainloop()

        # -----------------------------Logout Button------------------------------------------
        logout_btn_image = customtkinter.CTkImage(light_image=Image.open('C:/Users/SAEE/OneDrive/Desktop/Ritama_College/Ritama_DBMS_miniproj/Taxi-Booking-System1-master/Taxi-Booking-System1-master/Images/log-out-circle-regular-24.png'))
        logout_btn = customtkinter.CTkButton(master=left_frame, text="Logout                   ", fg_color='#2b2b2b',hover_color='black',font=sidemenufont, width=200,command=logout,  image=logout_btn_image)
        logout_btn.place(x=50, y=550)

        def combobox_callback(choice):
            customtkinter.set_appearance_mode(choice)
            if choice == 'light':
                Cover_Image_label['bg'] = "#dbdbdb"

            if choice == 'dark':
                Cover_Image_label['bg'] = "#2b2b2b"


        combobox = customtkinter.CTkComboBox(master=left_frame, values=["dark", 'light'],command=combobox_callback, font=sidemenufont, width=200)
        combobox.place(x=55, y=600)
        combobox.set("Appearance Mode")





        #+++++++++++++++++++++++++++++++Bottom Frame++++++++++++++++++++++++++++++++++++++++

        parent_tab=customtkinter.CTkTabview(self.root)
        parent_tab.pack(side=TOP, fill=BOTH, padx=10, pady=(0,20), expand=TRUE)

        #++++++++++++++++++++++Home Tab Frame+++++++++++++++++++++++++++++++++++++++++++
        parent_tab.add("Home")




        #+++++++++++++++++++++++++Welcome Label+++++++++++++++++++
        currentTime = datetime.datetime.now()
        currentTime.hour
        if currentTime.hour < 12:
            text="Good Morning"
        elif 12 <= currentTime.hour < 18:
            text="Good Afternoon"
        elif currentTime.hour>=20 and currentTime.hour<=23:
            text = "Good Night"
        else:
            text="Good Evening"
        welcome_lbl=customtkinter.CTkLabel(master=parent_tab.tab('Home'), text="{} {}!".format(text,Global.currentUser[1]), font=titlefont)
        welcome_lbl.place(x=10,y=20)

        pickup_address_lbl=customtkinter.CTkLabel(parent_tab.tab('Home'), text="Pick up address: ",font=labelfont)
        pickup_address_lbl.place(x=50, y=140)

        pickup_address_txt=customtkinter.CTkEntry(master=parent_tab.tab('Home'), font=font720, width=250)
        pickup_address_txt.place(x=230, y=140)

        date_lbl = customtkinter.CTkLabel(parent_tab.tab('Home'), text="Pick up date: ",font=labelfont)
        date_lbl.place(x=50, y=210)

        dt=date.today()
        style = ttk.Style()
        style.configure('my.DateEntry',
                        fieldbackground='#2a2d2e',
                        background='red',
                        foreground='black',
                        arrowcolor='white')

        date_lbl_txt = DateEntry(parent_tab.tab('Home'), font=('Times New Roman', 20,'normal'), width=22, date_pattern='yyyy-MM-dd',
                                 selectmode='day', style='my.DateEntry', background="green", bordercolor="red",
                               selectbackground="green", mindate=dt, disableddaybackground ="grey")
        date_lbl_txt.place(x=285, y=260)

        pickup_lbl=customtkinter.CTkLabel(parent_tab.tab('Home'), text="Pickup time:", font=labelfont)
        pickup_lbl.place(x=50, y=270)

        def updateTime(time):
            pick_up_time_lbl.delete(0, len(pick_up_time_lbl.get()))
            pick_up_time_lbl.insert(0, str("{}:{} {}".format(*time)))


        def time720():
            top = customtkinter.CTkToplevel(parent_tab.tab('Home'))
            top.title("Taxi Booking System")
            top.iconbitmap("C:/Users/SAEE/OneDrive/Desktop/Ritama_College/Ritama_DBMS_miniproj/Taxi-Booking-System1-master/Taxi-Booking-System1-master/Images/logo.ico")
            top.resizable(0,0)
            frame_width = 400
            frame_height = 500
            screen_width = top.winfo_screenwidth()
            screen_height = top.winfo_screenheight()
            x_cordinate = int((screen_width / 2) - (frame_width / 2))
            y_cordinate = int((screen_height / 2) - (frame_height / 2))
            top.geometry("{}x{}+{}+{}".format(frame_width, frame_height, x_cordinate, y_cordinate))
            time_picker = AnalogPicker(top, type=constants.HOURS12)
            time_picker.pack(expand=True, fill="both")
            theme = AnalogThemes(time_picker)
            theme.setDracula()
            ok_btn = customtkinter.CTkButton(master=top, text="Ok",command=lambda: updateTime(time_picker.time()))
            ok_btn.pack()


        time = ()

        pick_up_time_lbl = customtkinter.CTkEntry(master=parent_tab.tab('Home'),font=font720,  width=250)
        pick_up_time_lbl.bind("<Button-1>", lambda e: "break")
        pick_up_time_lbl.bind("<Key>", lambda e: "break")
        pick_up_time_lbl.place(x=230, y=270)

        time_img=customtkinter.CTkImage(light_image=Image.open("C:/Users/SAEE/OneDrive/Desktop/Ritama_College/Ritama_DBMS_miniproj/Taxi-Booking-System1-master/Taxi-Booking-System1-master/Images/time-five-regular-24.png"))
        pic_up_time_btn = customtkinter.CTkButton(master=parent_tab.tab('Home'),image=time_img,text="", fg_color="black", command=time720, font=font720, width=50)
        pic_up_time_btn.place(x=490, y=270)

        dropoff_lbl = customtkinter.CTkLabel(parent_tab.tab('Home'), text="Drop off address:", font=labelfont )
        dropoff_lbl.place(x=50, y=330)

        dropoff_txt1 = customtkinter.CTkEntry(master=parent_tab.tab('Home'), font=font720, width=250)
        dropoff_txt1.place(x=230, y=330)



        def request_booking():
            pickup=pickup_address_txt.get()
            date720=date_lbl_txt.get()
            picuptime=pick_up_time_lbl.get()
            dropoff=dropoff_txt1.get()
            cid11=customerid.get()

            booking=BookingLibs(cid=cid11, date=date720)
            checkResult=customer_checkbooking(booking)



            if pickup_address_txt.get()=='' or pick_up_time_lbl.get()=='' or dropoff_txt1.get()=='' or date_lbl_txt.get()=='':
                messagebox.showwarning("Taxi Booking System","Please enter all the field")

            elif checkResult!=None:
                messagebox.showwarning("Taxi Booking System","You have already requested on this date")

            else:
                booking = BookingLibs(pickupaddress=pickup, date=date720, time=picuptime,
                                      dropoffaddress=dropoff, bookingstatus='Pending', cid=cid11,did=None)

                ##################################
                print("Pickup Address:", booking.getPickupaddress())
                print("Date:", booking.getDate())
                print("Time:", booking.getTime())
                print("Dropoff Address:", booking.getDropoffaddress())
                print("Booking Status:", booking.getBookingstatus())
                print("Customer ID:", booking.getCid())
                print("Driver ID:", booking.getDid())

                insertResult = insert_booking(booking)
                messagebox.showinfo("Taxi Booking System", "The booking is requested successfully!")
                updatebookingtable.delete(*updatebookingtable.get_children())
                bookingtable()


        booking_btn=customtkinter.CTkButton(master=parent_tab.tab('Home'),command=request_booking, text="Request Booking", font=labelfont)
        booking_btn.place(x=230, y=400)

        #mapFrame=Frame(parent_tab.tab('Home'), bg="white")
        #mapFrame.place(x=700, y=80)

        #myloc = geocoder.ip('me')
        #map_widget = tkintermapview.TkinterMapView(mapFrame, width=770, height=600)
        #map_widget.set_address(myloc, marker=True)
        #map_widget.pack(side=RIGHT, fill=BOTH, pady=(10),padx=(10))


        #++++++++++++++++++++++Update Booking+++++++++++++++++++++++++
        parent_tab.add("Update Booking")

        updatebbokingframe=customtkinter.CTkFrame(master=parent_tab.tab('Update Booking'), width=470)
        updatebbokingframe.pack(side=LEFT, fill=BOTH, pady=(50,100))

        self.pickuptxt1=StringVar()

        pickup_address_lbl = customtkinter.CTkLabel(parent_tab.tab('Update Booking'),bg_color="#333333" ,text="Pick up address: ", font=labelfont)
        pickup_address_lbl.place(x=20, y=150)

        pickupaddresstxt = customtkinter.CTkEntry(master=parent_tab.tab('Update Booking'), font=font720, width=250)
        pickupaddresstxt.place(x=170, y=150)

        date_lbl = customtkinter.CTkLabel(parent_tab.tab('Update Booking'),bg_color="#333333", text="Pick up date: ", font=labelfont)
        date_lbl.place(x=20, y=200)

        dt = date.today()
        style = ttk.Style()
        style.configure('my.DateEntry',
                        fieldbackground='#2a2d2e',
                        background='red',
                        foreground='black',
                        arrowcolor='white')

        updatedatetxt = DateEntry(parent_tab.tab('Update Booking'), font=('Times New Roman', 20, 'normal'), width=22,
                                 date_pattern='yyyy-MM-dd',
                                 selectmode='day', style='my.DateEntry', background="green", bordercolor="red",
                                 selectbackground="green", mindate=dt, disableddaybackground="grey")
        updatedatetxt.place(x=210, y=240)

        pickup_lbl = customtkinter.CTkLabel(parent_tab.tab('Update Booking'),bg_color="#333333", text="Pickup time:", font=labelfont)
        pickup_lbl.place(x=20, y=250)

        def updateTime2(time):
            updatepickuptxt.delete(0, len(updatepickuptxt.get()))
            updatepickuptxt.insert(0, str("{}:{} {}".format(*time)))

        def time720():
            top = customtkinter.CTkToplevel(parent_tab.tab('Update Booking'))
            top.title("Taxi Booking System")
            top.iconbitmap("C:/Users/SAEE/OneDrive/Desktop/Ritama_College/Ritama_DBMS_miniproj/Taxi-Booking-System1-master/Taxi-Booking-System1-master/Images/logo.ico")
            top.resizable(0, 0)
            frame_width = 400
            frame_height = 500
            screen_width = top.winfo_screenwidth()
            screen_height = top.winfo_screenheight()
            x_cordinate = int((screen_width / 2) - (frame_width / 2))
            y_cordinate = int((screen_height / 2) - (frame_height / 2))
            top.geometry("{}x{}+{}+{}".format(frame_width, frame_height, x_cordinate, y_cordinate))
            time_picker = AnalogPicker(top, type=constants.HOURS12)
            time_picker.pack(expand=True, fill="both")
            theme = AnalogThemes(time_picker)
            theme.setDracula()
            ok_btn = customtkinter.CTkButton(master=top, text="Ok", command=lambda: updateTime2(time_picker.time()))
            ok_btn.pack()

        time = ()

        updatepickuptxt = customtkinter.CTkEntry(master=parent_tab.tab('Update Booking'),textvariable=self.pickuptxt1, font=font720, width=250)
        updatepickuptxt.bind("<Button-1>", lambda e: "break")
        updatepickuptxt.bind("<Key>", lambda e: "break")
        updatepickuptxt.place(x=170, y=250)

        time_img = customtkinter.CTkImage(light_image=Image.open("C:/Users/SAEE/OneDrive/Desktop/Ritama_College/Ritama_DBMS_miniproj/Taxi-Booking-System1-master/Taxi-Booking-System1-master/Images/time-five-regular-24.png"))
        pic_up_time_btn = customtkinter.CTkButton(master=parent_tab.tab('Update Booking'), image=time_img, text="",fg_color="black", command=time720, font=font720, width=40)
        pic_up_time_btn.place(x=423, y=252)

        dropoff_lbl = customtkinter.CTkLabel(parent_tab.tab('Update Booking'),bg_color="#333333", text="Drop off address:", font=labelfont)
        dropoff_lbl.place(x=20, y=300)



        updatedropofftxt = customtkinter.CTkEntry(master=parent_tab.tab('Update Booking'), font=font720, width=250)
        updatedropofftxt.place(x=170, y=300)

        updatebookingid = Entry(self.root)



        def update_customer_booking():
            today=date.today()
            today720=str(today)

            validateresult=validaecustomerbooking(customerid.get())
            val3=validateresult[0]
            val4=val3[0]

            if updatebookingid.get()=='' or pickupaddresstxt.get()=='' or updatedatetxt.get()=='' or updatepickuptxt.get()=='' or updatedropofftxt.get()=='':
                messagebox.showwarning("Taxi Booking System","Please fill all the fields")

            elif validateresult!=None:
                date3=updatedatetxt.get()
                if date3<today720:
                    messagebox.showwarning("Taxi Booking System","You have outdated date. Please select new pickup date!")

                else:
                    updateBooking = BookingLibs(bookingid=updatebookingid.get(), pickupaddress=pickupaddresstxt.get(),
                                                date=updatedatetxt.get(), time=updatepickuptxt.get(),
                                                dropoffaddress=updatedropofftxt.get())

                    updatebookingResult = update_customer_booking1(updateBooking)
                    if updatebookingResult == True:

                        messagebox.showinfo("Taxi Booking System", "The booking request is updated successfully")
                        updatebookingtable.delete(*updatebookingtable.get_children())
                        bookingtable()


                    else:
                        messagebox.showerror("Taxi Booking System", "Error Occurred")








        update_booking_btn = customtkinter.CTkButton(master=parent_tab.tab('Update Booking'),text="Update",command=update_customer_booking, font=labelfont)
        update_booking_btn.place(x=170, y=350)

        def cancel_booking():
            updateID=updatebookingid.get()
            Deleteresult=delete_booking(updateID)
            if Deleteresult==True:
                messagebox.showinfo("Taxi Booking System","The booking is cancel successfully!")
                updatebookingtable.delete(*updatebookingtable.get_children())
                bookingtable()

            else:
                messagebox.showerror("Taxi Booking System","Error Occurred")

        cancel_booking_btn = customtkinter.CTkButton(master=parent_tab.tab('Update Booking'),command=cancel_booking, text="Cancel",font=labelfont)
        cancel_booking_btn.place(x=320, y=350)



        updatebookingtable=ttk.Treeview(parent_tab.tab('Update Booking'))
        updatebookingtable.pack(side=RIGHT, fill=BOTH, pady=(70,0))

        # -----------------------------Update Booking Table-----------------------------------------
        updatebookingtable['columns']=('id', 'pickupaddress','date','time','dropoffaddress','driverid','status')
        updatebookingtable.column('#0', width=0, stretch=0)
        updatebookingtable.column('id', width=100, anchor=CENTER)
        updatebookingtable.column('pickupaddress', width=200, anchor=CENTER)
        updatebookingtable.column('date', width=120, anchor=CENTER)
        updatebookingtable.column('time', width=100, anchor=CENTER)
        updatebookingtable.column('dropoffaddress', width=200, anchor=CENTER)
        updatebookingtable.column('status', width=100, anchor=CENTER)
        updatebookingtable.column('driverid', width=100, anchor=CENTER)

        updatebookingtable.heading('#0', text='', anchor=CENTER)
        updatebookingtable.heading('id', text="ID", anchor=CENTER)
        updatebookingtable.heading('pickupaddress', text="Pickup address", anchor=CENTER)
        updatebookingtable.heading('date', text="Date", anchor=CENTER)
        updatebookingtable.heading('time', text="Time", anchor=CENTER)
        updatebookingtable.heading('dropoffaddress', text="Drop off address", anchor=CENTER)
        updatebookingtable.heading('driverid', text="Driver ID", anchor=CENTER)
        updatebookingtable.heading('status', text="Status", anchor=CENTER)

        def displaySelectedItem(a):

            pickupaddresstxt.delete(0, END)
            updatedatetxt.delete(0, END)
            updatepickuptxt.delete(0, END)
            updatedropofftxt.delete(0, END)
            updatebookingid.delete(0, END)


            selectedItem = updatebookingtable.selection()[0]
            updatebookingid.insert(0, updatebookingtable.item(selectedItem)['values'][0])
            pickupaddresstxt.insert(0, updatebookingtable.item(selectedItem)['values'][1])
            updatedatetxt.insert(0, updatebookingtable.item(selectedItem)['values'][2])
            updatepickuptxt.insert(0, updatebookingtable.item(selectedItem)['values'][3])
            updatedropofftxt.insert(0, updatebookingtable.item(selectedItem)['values'][4])



        updatebookingtable.bind("<<TreeviewSelect>>", displaySelectedItem)

        # -----------------------------Display data in table function------------------------------------------
        def bookingtable():
            cusidd = Entry(self.root)
            cusidd.insert(0, Global.currentUser[0])
            iddd = cusidd.get()
            Bookresult = customerbooking_selectstatsubooked(iddd)
            i = 0
            for ro in Bookresult:
                updatebookingtable.insert(parent='', index='end',
                                    values=(ro[0], ro[1], ro[2], ro[3], ro[4], ro[7], ro[5]))
                i = i + 1




        #++++++++++++++++++++++++++++++++++Riding History Tab+++++++++++++++++++++++++++++++
        parent_tab.add("Riding History")

        bookinghistoryTable=ttk.Treeview(parent_tab.tab('Riding History'))

        bookinghistoryTable['columns']=('bookingid','pickupaddress','dropoffaddress','date','time')
        bookinghistoryTable.column('#0', width=0, stretch=0)
        bookinghistoryTable.column('bookingid', width=100, anchor=CENTER)
        bookinghistoryTable.column('pickupaddress', width=100, anchor=CENTER)
        bookinghistoryTable.column('dropoffaddress', width=100, anchor=CENTER)
        bookinghistoryTable.column('date', width=100, anchor=CENTER)
        bookinghistoryTable.column('time', width=100, anchor=CENTER)

        bookinghistoryTable.heading('#0', text='', anchor=CENTER)
        bookinghistoryTable.heading('bookingid', text='Booking ID', anchor=CENTER)
        bookinghistoryTable.heading('pickupaddress', text='Pickup Address', anchor=CENTER)
        bookinghistoryTable.heading('dropoffaddress', text='Dropoff Address', anchor=CENTER)
        bookinghistoryTable.heading('date', text='Date', anchor=CENTER)
        bookinghistoryTable.heading('time', text='Time', anchor=CENTER)
        bookinghistoryTable.pack(side=TOP, fill=BOTH, expand=TRUE)

        def bookinghistory():


            Bookresult=customerbooking_selectall(customerid.get())

            for x in Bookresult:
                bookinghistoryTable.insert(parent='', index='end', values=(x[0],x[1],x[4],x[2],x[3]))

        bookinghistory()




        parent_tab.add("Report")
        parent_tab.tab('Report').configure(fg_color="white")

        #++++++++++++++++++++++++++Activity Tab Frame++++++++++++++++++++++
        parent_tab.add("Activity")

        tab4_frame = customtkinter.CTkFrame(master=parent_tab.tab('Activity'))
        tab4_frame.pack(fill=BOTH, expand=True)

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

        treeView = ttk.Treeview(tab4_frame, )
        treeView['columns'] = ('myid', "system", "model", "machine", "processor", "date", "date2")
        treeView.column('#0', width=0, stretch=0)
        treeView.column('myid', width=50, anchor=CENTER)
        treeView.column('system', width=100, anchor=CENTER)
        treeView.column('model', width=150, anchor=CENTER)
        treeView.column('machine', width=100, anchor=CENTER)
        treeView.column('processor', width=300, anchor=CENTER)
        treeView.column('date', width=100, anchor=CENTER)
        treeView.column('date2', width=100, anchor=CENTER)

        treeView.heading('#0', text='', anchor=CENTER)
        treeView.heading('myid', text='ID', anchor=CENTER)
        treeView.heading('system', text='System', anchor=CENTER)
        treeView.heading('model', text='System Username', anchor=CENTER)
        treeView.heading('machine', text='Machine', anchor=CENTER)
        treeView.heading('processor', text='Processor', anchor=CENTER)
        treeView.heading('date', text='Date', anchor=CENTER)
        treeView.heading('date2', text='Time', anchor=CENTER)

        treeView.pack(side=TOP, fill=BOTH, expand=TRUE)
        cusidd = Entry(self.root)
        cusidd.insert(0, Global.currentUser[0])
        iddd = cusidd.get()

        def activitytable():
            cusidd = Entry(self.root)
            cusidd.insert(0, Global.currentUser[0])
            iddd = cusidd.get()
            Bookresult = selectall_myactivity(iddd)
            i = 0
            for ro in Bookresult:
                treeView.insert(parent='', index='end',
                                    values=(ro[0], ro[1], ro[2], ro[3], ro[4], ro[5], ro[6]))
                i = i + 1

        activitytable()

        username = 'root'        # Your MySQL username
        password = '@sql'  # Your MySQL password
        database = 'taxi_booking_system'  # Your MySQL database name

        sql_engine = create_engine('mysql+pymysql://root:@localhost/taxi_booking_system')
        db_connection = sql_engine.connect()

        # -----------------------------No of time account accessed report------------------------------------------
        my_colors = [(.9, .4, .6), (.1, .3, .8)]
        query = "SELECT *,count(myid) as ID FROM myactivity WHERE cid=" + iddd + " group by date limit 5 "
        df = pandas.read_sql(query, db_connection, index_col='date')
        fig = df.plot.bar(title="No of times account accessed", y='ID',rot=360, figsize=(6, 6), color=my_colors, legend=True,grid=False).get_figure()
        plot = FigureCanvasTkAgg(fig, parent_tab.tab('Report'))
        plot.get_tk_widget().place(x=100, y=5)

        # -----------------------------Booking analysis------------------------------------------
        query720 = "SELECT *, count(bookingid) as ID  FROM booking WHERE cid=" + iddd + " group by date"
        df = pandas.read_sql(query720, db_connection, index_col='date')
        fig2 = df.plot.line(title="Booking Records", y='ID', figsize=(5.5, 6)).get_figure();
        plot2 = FigureCanvasTkAgg(fig2, parent_tab.tab('Report'))
        plot2.get_tk_widget().place(x=800, y=5)




        bookingtable()


if __name__=='__main__':
    root=customtkinter.CTk()
    Customer_Dashboard(root)
    root.mainloop()





