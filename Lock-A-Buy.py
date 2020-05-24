from tkinter import messagebox
from tkinter import *
from datetime import date
import sqlite3
import smtplib


class MyProject:
    def __init__(self, master):
        self.tf = Frame(master, background='lightblue', bd=14, relief=RIDGE)
        self.tf.pack(side=TOP, fill=BOTH, expand='true')
        # ADD images here into some variables
        self.label2 = Label(self.tf, text='LOCK-A-BUY\n May the store be with you',
                            font=('papyrus', 20, 'bold'),
                            bg='lightblue')
        self.label2.place(x=250, y=50)
        self.logo1 = PhotoImage(file='locklogo.png')
        self.label0 = Label(self.tf, image=self.logo1)
        self.label0.place(x=300, y=150)
        self.button = Button(self.tf, text="  Login", font=('papyrus', 16, 'bold'), command=self.mLogin)
        self.button2 = Button(self.tf, text=" Register", font=('papyrus', 16, 'bold'), command=self.mRegister)
        self.button3 = Button(self.tf, text=" Admin", font=('papyrus', 16, 'bold'), command=self.mAdmin)
        self.button.place(x=280, y=450)
        self.button2.place(x=510, y=450)
        self.button3.place(x=400, y=450)
        # images with register login buttons
        # add a little description about the shit

    def mRegister(self):
        root1 = Toplevel()
        root1.title("Register")
        root1.wm_geometry("800x700")

        page = MRegister(root1)
        # add  image variables up here next to root1

    def mLogin(self):
        root1 = Toplevel()
        root1.title("Login")
        root1.wm_geometry("700x500")
        login = MLogin(root1)
        # add  image variables up here next to root1

    def mAdmin(self):
        root1 = Toplevel()
        root1.title("Admin")
        root1.wm_geometry("1400x700")

        page = MAdmin(root1)


class MAdmin:
    def __init__(self, master):
        self.m = master
        self.frame1 = Frame(master, background='lightgreen', bd=14, relief=RIDGE)
        self.frame1.pack(side=TOP, fill=BOTH, expand='true')

        self.logo1 = PhotoImage(file='sidelogo.png')
        self.label0 = Label(self.frame1, image=self.logo1)
        self.label0.place(x=10, y=10)

        self.label2 = Label(self.frame1, text='Administration', font=('papyrus', 18, 'bold'),
                            bg='lightgreen')
        self.label2.place(x=200, y=40)

        self.label_2 = Label(self.frame1, text="Password", font=('papyrus', 14), bg='lightgreen')
        self.label_2.place(x=25, y=150)
        self.entry_2 = Entry(self.frame1, width=40, show='*')
        self.entry_2.place(x=150, y=150)
        self.b1 = Button(self.frame1, text=" Submit", font=('papyrus', 12, 'bold'), command=self.submit)
        self.b1.place(x=420, y=140)

        self.b3 = Button(self.frame1, text=" Back", font=('papyrus', 12, 'bold'), command=self.back)
        self.b3.place(x=530, y=140)

    def back(self):
        self.m.destroy()

    def submit(self):
        if str(self.entry_2.get()) == "banned":
            self.t1 = Text(self.frame1, width=100, height=70, bg='lightblue', font='serif', bd=7)
            self.t1.place(x=30, y=180)

            conn = sqlite3.connect("user_details.db")
            cursor = conn.execute("select * from billdata")
            texts = cursor.fetchall()
            l = len(texts)
            l1 = ['UID', 'Name', 'Mobile no', 'Address', '\tEmail', '\tSupermarket', '\tOrder details']
            for y in range(0, 7):
                self.t1.insert(END, l1[y] + "  \t")
                print(l1[y], end="\t")

            self.t1.insert(END, "\n")

            for text in texts:
                self.t1.insert(END, str(text))
                print(text)
                self.t1.insert(END, "\n")

            self.t1.config(state="disabled")


        else:
            print('invalid password')


class MRegister:
    def __init__(self, master):
        # add image variables next to master up here
        self.m = master
        self.frame1 = Frame(master, background='lightgreen', bd=14, relief=RIDGE)
        self.frame1.pack(side=TOP, fill=BOTH, expand='true')
        self.label2 = Label(self.frame1, text='Registration\n Fill your details', font=('papyrus', 18, 'bold'),
                            bg='lightgreen')
        self.label2.place(x=200, y=40)

        self.logo1 = PhotoImage(file='sidelogo.png')
        self.label0 = Label(self.frame1, image=self.logo1)
        self.label0.place(x=10, y=10)

        self.label_1 = Label(self.frame1, text="Name", font=('papyrus', 14), bg='lightgreen')
        self.label_1.place(x=25, y=130)
        self.entry_1 = Entry(self.frame1, width=40)
        self.entry_1.place(x=250, y=130)

        self.label_2 = Label(self.frame1, text="Password", font=('papyrus', 14), bg='lightgreen')
        self.label_2.place(x=25, y=180)
        self.entry_2 = Entry(self.frame1, width=40, show='*')
        self.entry_2.place(x=250, y=180)

        self.label_3 = Label(self.frame1, text="Contact No.", font=('papyrus', 14), bg='lightgreen')
        self.label_3.place(x=25, y=230)
        self.entry_3 = Entry(self.frame1, width=40)
        self.entry_3.place(x=250, y=230)

        self.label_4 = Label(self.frame1, text="Email ID", font=('papyrus', 14), bg='lightgreen')
        self.label_4.place(x=25, y=280)
        self.entry_4 = Entry(self.frame1, width=40)
        self.entry_4.place(x=250, y=280)

        self.label_5 = Label(self.frame1, text="Date of birth", font=('papyrus', 14), bg='lightgreen')
        self.label_5.place(x=25, y=330)

        self.label_6 = Label(self.frame1, text="Address", font=('papyrus', 14), bg='lightgreen')
        self.label_6.place(x=25, y=380)
        self.entry_6 = Entry(self.frame1, width=40)
        self.entry_6.place(x=250, y=380)

        self.date = StringVar()
        self.s1 = Spinbox(self.frame1, from_=1, to=31, textvariable=self.date, width=10)
        self.s1.place(x=250, y=330)

        self.month = StringVar()
        self.s2 = Spinbox(self.frame1, from_=1, to=12, textvariable=self.month, width=10)
        self.s2.place(x=340, y=330)

        self.year = StringVar()
        self.s3 = Spinbox(self.frame1, from_=1980, to=2010, textvariable=self.year, width=10)
        self.s3.place(x=440, y=330)

        self.label_7 = Label(self.frame1, text="Pin Code", font=('papyrus', 14), bg='lightgreen')
        self.label_7.place(x=25, y=430)
        self.entry_7 = Entry(self.frame1, width=40)
        self.entry_7.place(x=250, y=430)

        self.b1 = Button(self.frame1, text=" Submit", font=('Algerian', 12, 'bold'), command=self.submit)
        self.b1.place(x=100, y=500)

        self.b2 = Button(self.frame1, text=" Reset", font=('Algerian', 12, 'bold'), command=self.reset)
        self.b2.place(x=250, y=500)

        self.b3 = Button(self.frame1, text=" Back", font=('Algerian', 12, 'bold'), command=self.back)
        self.b3.place(x=400, y=500)

    def submit(self):
        if self.entry_1.get() == "" or self.entry_2.get() == "" or self.entry_3.get() == "" or self.entry_4.get() == "" or self.entry_7.get() == "":
            messagebox.showerror(parent=self.m, title="Error", message="Fill all fields")

        elif len(self.entry_3.get()) != 10:
            messagebox.showerror(parent=self.m, title="Error", message="Enter valid contact number")

        elif (str(self.entry_4.get()).endswith(".com") == False and str(self.entry_4.get()).endswith(
                ".in") == False and str(self.entry_4.get()).endswith(".co.in") == False) \
                or str(self.entry_4.get()).rfind("@") == -1:
            messagebox.showerror(parent=self.m, title="Error", message="Enter valid email id")

        elif len(self.entry_7.get()) != 6:
            messagebox.showerror(parent=self.m, title="Error", message="Enter valid pin code")

        else:
            ans = messagebox.askyesno(parent=self.m, message="Do you want to submit?", title="Confirmation")
            if ans > 0:
                conn = sqlite3.connect("user_details.db")
                cursor = conn.execute("select * from userdata")
                value = cursor.fetchall()
                leng = len(value)
                user_id = value[leng - 1][0] + 1

                name = self.entry_1.get()
                usercon_no = int(self.entry_3.get())
                user_pin_code = int(self.entry_7.get())
                user_add = self.entry_6.get()
                date = self.date.get()
                month = self.month.get()
                year = self.year.get()
                user_dob = str(year) + "-" + str(month) + "-" + str(date)
                user_email = self.entry_4.get()
                user_password = self.entry_2.get()

                try:
                    cursor = conn.execute(
                        "select * from userdata where name='" + name + "' and user_email='" + user_email + "' and user_dob='" + user_dob + "'")
                    if len(cursor.fetchall()) != 0:
                        raise ExistingException()
                    conn.execute("insert into userdata values(?,?,?,?,?,?,?,?)",
                                 (user_id, name, usercon_no, user_pin_code, user_add, user_dob, user_email,
                                  user_password))
                    conn.commit()
                    messagebox.showinfo(parent=self.m, message="Successfully added\nUser ID is " + str(user_id),
                                        title="Congratulation!!")
                    message = "Hi! " + str(name) + " You have successfully registered to Lock-A-Buy. " + str(
                        user_id) + " is your user ID."
                    sender = '18aasthagarg@gmail.com'
                    receiver = str(user_email)
                    try:
                        smtpObj = smtplib.SMTP('smtp.gmail.com', 25, 'localhost')
                        smtpObj.starttls()
                        smtpObj.login("18aasthagarg", "Bingpot99")
                        smtpObj.sendmail(sender, receiver, message)
                        print("successfully sent email")
                    except Exception as e:
                        print(e)

                except Exception as e:
                    print(e)
                    messagebox.showerror(parent=self.m, message="User already exists. Goto login page", title="Error")

                # now some sqlite shit to enter the above details into the database and show error if the registration details already exist
                # also display the user_id

    def reset(self):
        self.entry_1.delete(0, END)
        self.entry_2.delete(0, END)
        self.entry_3.delete(0, END)
        self.entry_4.delete(0, END)
        self.entry_6.delete(0, END)
        self.entry_7.delete(0, END)
        self.date.set("1")
        self.month.set("1")
        self.year.set("1980")

    def back(self):
        self.m.destroy()


class InvalidUserException(Exception):
    def __init__(self):
        print("Invalid user")


class ExistingException(Exception):
    def __init__(self):
        print("User already exists")


class MLogin:
    def __init__(self, master):
        # image variables must be passed up here next to master
        self.m = master
        # image variables store in some variables
        self.frame1 = Frame(master, background='lightgreen', bd=14, relief=RIDGE)
        self.frame1.pack(side=TOP, fill=BOTH, expand='true')
        self.label2 = Label(self.frame1, text='Login Page ', font=('papyrus', 18, 'bold'),
                            bg='lightgreen')
        self.label2.place(x=300, y=40)
        self.logo1 = PhotoImage(file='sidelogo.png')
        self.label0 = Label(self.frame1, image=self.logo1)
        self.label0.place(x=10, y=10)
        self.label_1 = Label(self.frame1, text="User Id: ", font=('papyrus', 14), bg='lightgreen')
        self.label_1.place(x=125, y=150)
        self.entry_1 = Entry(self.frame1, width=40)
        self.entry_1.place(x=260, y=150)
        self.label_2 = Label(self.frame1, text="Password:", font=('papyrus', 14), bg='lightgreen')
        self.label_2.place(x=125, y=210)
        self.entry_2 = Entry(self.frame1, width=40, show="*")
        self.entry_2.place(x=260, y=210)
        self.b1 = Button(self.frame1, text=" Login ", font=('Courier', 12, 'bold'), command=self.success)
        self.b1.place(x=250, y=300)
        self.b2 = Button(self.frame1, text=" Reset ", font=('Courier', 12, 'bold'), command=self.reset)
        self.b2.place(x=350, y=300)
        self.b3 = Button(self.frame1, text=" Back ", font=('Courier', 12, 'bold'), command=self.exit)
        self.b3.place(x=450, y=300)

    def success(self):
        try:
            if (self.entry_1.get() == "" or self.entry_2.get() == ""):
                messagebox.showerror(parent=self.m, message="Please fill all the details", title="Error")
            elif (type(int(self.entry_1.get())) != int):
                pass
            else:
                try:
                    conn = sqlite3.connect("user_details.db")
                    cursor = conn.execute(
                        "select * from userdata where user_id='" + self.entry_1.get() + "' and user_password='" + self.entry_2.get() + "'")
                    if len(cursor.fetchall()) == 0:
                        raise InvalidUserException

                    # now check the login useid and password - again some sql shit
                    root2 = Toplevel()
                    id = self.entry_1.get()
                    root2.title("All Supermarkets")
                    root2.wm_geometry("900x700")
                    login2 = MSupermarkets(root2, id)
                    # image variables of logo and all shall be passed up here next to root2

                except InvalidUserException as e:
                    print(e)
                    messagebox.showerror(parent=self.m, message="Invalid credentials", title="Error")


        except ValueError as e:
            messagebox.showerror(parent=self.m, message="User ID must be a number", title="Error")

        except Exception as e:
            messagebox.showerror(parent=self.m, message="Invalid credentials", title="Error")

    def reset(self):
        self.entry_1.delete(0, END)
        self.entry_2.delete(0, END)

    def exit(self):
        self.m.destroy()


class MSupermarkets:
    def __init__(self, master, id):
        # image variables up here next to master
        self.id = id

        self.frame1 = Frame(master, height=500, width=600, bd=14)
        self.frame1.config(background='pink')
        self.frame1.pack(fill=BOTH, expand='true')
        self.logo1 = PhotoImage(file='sidelogo.png')
        self.label0 = Label(self.frame1, image=self.logo1)
        self.label0.place(x=10, y=30)

        self.label0 = Label(self.frame1, text='Select a supermarket', font=('papyrus', 20, 'bold'), bg='pink')
        self.label0.grid(row=1, column=30)
        self.sm = IntVar()

        self.logo2 = PhotoImage(file='spencer.png')
        self.label3 = Label(self.frame1, image=self.logo2)
        self.label3.place(x=570, y=50)

        self.sm1 = Radiobutton(self.frame1, text='Spencers', font='Times', variable=self.sm, value=1, height=3,
                               width=20, highlightcolor='yellow').grid(row=13, column=40)

        self.logo3 = PhotoImage(file='easyday.png')
        self.label4 = Label(self.frame1, image=self.logo3)
        self.label4.place(x=570, y=100)

        self.sm2 = Radiobutton(self.frame1, text='Easyday', font='Times', variable=self.sm, value=2, height=3,
                               width=20).grid(row=20, column=40)

        self.logo4 = PhotoImage(file='bigbazaar.png')
        self.label5 = Label(self.frame1, image=self.logo4)
        self.label5.place(x=570, y=170)

        self.sm3 = Radiobutton(self.frame1, text='Big Bazar', font='Times', variable=self.sm, value=3, height=3,
                               width=20).grid(row=27,
                                              column=40)

        self.logo5 = PhotoImage(file='familymart.png')
        self.label6 = Label(self.frame1, image=self.logo5)
        self.label6.place(x=570, y=230)

        self.sm4 = Radiobutton(self.frame1, text='Family Mart', font='Times', variable=self.sm, value=4, height=3,
                               width=20).grid(
            row=34, column=40)

        self.logo6 = PhotoImage(file='pappustore.png')
        self.label7 = Label(self.frame1, image=self.logo6)
        self.label7.place(x=570, y=310)

        self.sm5 = Radiobutton(self.frame1, text='Pappu Store', font='Times', variable=self.sm, value=5, height=3,
                               width=20).grid(
            row=41, column=40)

        self.b1 = Button(self.frame1, text="OK", font=('Algerian', 12), command=self.check_sm)
        self.b1.grid(row=42, column=40)

        self.b2 = Button(self.frame1, text="LOG OUT", font=('Algerian', 15), command=self.logout)
        self.b2.place(x=600, y=0)

    def logout(self):
        root1 = Toplevel()
        root1.title("MyProject")
        root1.wm_geometry("800x700")
        page1 = MyProject(root1)

    def check_sm(self):
        self.sup = self.sm.get()
        # now we have to check from database if the supermarket selected is in that pin code region or not
        if self.sup >= 1 and self.sup <= 5:
            root3 = Toplevel()
            root3.title("All Categories")
            root3.wm_geometry("800x900")
            login3 = MCategories(root3, self.sup, self.id)


class MCategories:
    def __init__(self, master, sup, id):
        self.sup = sup
        self.id = id
        self.frame1 = Frame(master, height=500, width=600, bd=14)
        self.frame1.config(background='lightgreen')
        self.frame1.pack(fill=BOTH, expand='true')

        self.logo0 = PhotoImage(file='sidelogo.png')
        self.label00 = Label(self.frame1, image=self.logo0)
        self.label00.place(x=1, y=1)

        self.label0 = Label(self.frame1, text='Select one category', font=('papyrus', 20, 'bold'), bg='orange')
        self.label0.place(x=200, y=30)

        self.logo1 = PhotoImage(file='Grocer.png')
        self.label1 = Label(self.frame1, image=self.logo1)
        self.label1.place(x=60, y=120)

        self.button0 = Button(self.frame1, text=" Groceries", font=('Algerian', 16, 'bold'), command=self.mGrocery)
        self.button0.place(x=150, y=100)

        self.logo2 = PhotoImage(file='veg.png')
        self.label2 = Label(self.frame1, image=self.logo2)
        self.label2.place(x=420, y=120)

        self.button1 = Button(self.frame1, text=" Vegetables & Fruits ", font=('Algerian', 16, 'bold'),
                              command=self.mVeg)
        self.button1.place(x=440, y=100)

        self.logo3 = PhotoImage(file='dair.png')
        self.label3 = Label(self.frame1, image=self.logo3)
        self.label3.place(x=60, y=430)

        self.button2 = Button(self.frame1, text=" Dairy Products", font=('Algerian', 16, 'bold'), command=self.mDairy)
        self.button2.place(x=140, y=420)

        self.logo4 = PhotoImage(file='liq.png')
        self.label4 = Label(self.frame1, image=self.logo4)
        self.label4.place(x=420, y=430)

        self.button3 = Button(self.frame1, text=" Liquor and Beverages", font=('Algerian', 16, 'bold'),
                              command=self.mLiquor)
        self.button3.place(x=440, y=420)

        self.b4 = Button(self.frame1, text="LOG OUT", font=('Algerian', 15), command=self.logout)
        self.b4.place(x=600, y=0)

    def logout(self):
        root1 = Toplevel()
        root1.title("MyProject")
        root1.wm_geometry("800x700")
        page1 = MyProject(root1)

    def mGrocery(self):
        root1 = Toplevel()
        root1.title("Groceries")
        root1.wm_geometry("1400x700")
        cat1 = MGrocery(root1, self.sup, self.id)

    def mVeg(self):
        root1 = Toplevel()
        root1.title("Vegetables and Fruits")
        root1.wm_geometry("1400x700")
        cat2 = MVeg(root1, self.sup, self.id)

    def mDairy(self):
        root1 = Toplevel()
        root1.title("Dairy Products")
        root1.wm_geometry("1400x700")
        cat2 = MDairy(root1, self.sup, self.id)

    def mLiquor(self):
        root1 = Toplevel()
        root1.title("Beverages and Liquor")
        root1.wm_geometry("1400x700")
        cat2 = MLiquor(root1, self.sup, self.id)


class MGrocery:
    def __init__(self, master, sup, id):
        self.m = master
        self.sup = sup
        self.id = id
        self.tf = Frame(master, height=100, width=900, bd=14, relief=RIDGE)
        self.tf.pack(fill=BOTH, expand='true', side=TOP)
        self.tf.config(background='orange')

        self.lf = Frame(master, height=600, width=300, bd=14, relief=RIDGE)
        self.lf.pack(fill=BOTH, expand='true', side=LEFT)
        self.lf.config(background='orange')

        self.lf1 = Frame(master, height=600, width=300, bd=14, relief=RIDGE)
        self.lf1.pack(fill=BOTH, expand='true', side=LEFT)
        self.lf1.config(background='orange')

        self.lf2 = Frame(master, height=600, width=300, bd=14, relief=RIDGE)
        self.lf2.pack(fill=BOTH, expand='true', side=RIGHT)
        self.lf2.config(background='orange')

        self.b4 = Button(self.tf, text="LOG OUT", font=('Algerian', 15), command=self.logout)
        self.b4.place(x=1200, y=5)

        self.label1 = Label(self.tf, text='Lock-A-Buy Groceries\n\tAll products are available in limited quantity',
                            font=('papyrus', 18, 'bold'),
                            bg='orange', anchor=E)
        self.label1.grid(row=1, column=2, columnspan=8)
        self.logo1 = PhotoImage(file='esidelogo.png')
        self.label0 = Label(self.tf, image=self.logo1)
        self.label0.place(x=0, y=0)

        # Labels of Products
        self.m1 = Label(self.lf, text="Products", font=('papyrus', 16, 'bold'), bg='orange', justify="center")
        self.m1.place(x=25, y=0)

        self.v1 = IntVar()
        self.c1 = Checkbutton(self.lf, text="Basmati Rice", font=('Courier', 14, 'bold'), bg='orange',
                              variable=self.v1)
        self.c1.place(x=10, y=50)

        self.v2 = IntVar()
        self.c2 = Checkbutton(self.lf, text="Soyabean Oil", font=('Courier', 14, 'bold'), bg='orange',
                              variable=self.v2)
        self.c2.place(x=10, y=110)

        self.v3 = IntVar()
        self.c3 = Checkbutton(self.lf, text="Salt", font=('Courier', 14, 'bold'), bg='orange',
                              variable=self.v3)
        self.c3.place(x=10, y=170)

        self.v4 = IntVar()
        self.c4 = Checkbutton(self.lf, text="Sugar", font=('Courier', 14, 'bold'), bg='orange',
                              variable=self.v4)
        self.c4.place(x=10, y=230)

        self.v5 = IntVar()
        self.c5 = Checkbutton(self.lf, text="Desi Ghee", font=('Courier', 14, 'bold'), bg='orange',
                              variable=self.v5)
        self.c5.place(x=10, y=290)

        # quantity of Products
        self.m2 = Label(self.lf, text="Qty(kg)", font=('papyrus', 16, 'bold'), bg='orange', justify="center")
        self.m2.place(x=170, y=0)

        self.sv1 = IntVar()
        choice1 = {5, 10}
        self.pop1 = OptionMenu(self.lf, self.sv1, *choice1)
        self.pop1.place(x=170, y=50)

        self.sv2 = IntVar()
        choice2 = {1, 2}
        self.pop2 = OptionMenu(self.lf, self.sv2, *choice2)
        self.pop2.place(x=170, y=110)

        self.sv3 = IntVar()
        choice3 = {1, 2}
        self.pop3 = OptionMenu(self.lf, self.sv3, *choice3)
        self.pop3.place(x=170, y=170)

        self.sv4 = IntVar()
        choice4 = {1, 5}
        self.pop4 = OptionMenu(self.lf, self.sv4, *choice4)
        self.pop4.place(x=170, y=230)

        self.sv5 = IntVar()
        choice5 = {1, 2}
        self.pop5 = OptionMenu(self.lf, self.sv5, *choice5)
        self.pop5.place(x=170, y=290)

        # price
        self.m3 = Label(self.lf, text="Price/kg", font=('papyrus', 16, 'bold'), bg='orange', justify="center")
        self.m3.place(x=300, y=0)

        self.ml1 = Label(self.lf, text="65", font=('Courier', 14, 'bold'), bg='orange')
        self.ml1.place(x=300, y=50)

        self.ml2 = Label(self.lf, text="110", font=('Courier', 14, 'bold'), bg='orange')
        self.ml2.place(x=300, y=110)

        self.ml3 = Label(self.lf, text="19", font=('Courier', 14, 'bold'), bg='orange')
        self.ml3.place(x=300, y=170)

        self.ml4 = Label(self.lf, text="45", font=('Courier', 14, 'bold'), bg='orange')
        self.ml4.place(x=300, y=230)

        self.ml5 = Label(self.lf, text="400", font=('Courier', 14, 'bold'), bg='orange')
        self.ml5.place(x=300, y=290)

        # Labels of flour
        self.d1 = Label(self.lf1, text="Flour", font=('papyrus', 16, 'bold'), bg='orange', justify="center")
        self.d1.place(x=50, y=0)

        self.vd1 = IntVar()
        self.cd1 = Checkbutton(self.lf1, text="Chaaki Atta", font=('Courier', 14, 'bold'), bg='orange',
                               variable=self.vd1)
        self.cd1.place(x=20, y=50)

        self.vd2 = IntVar()
        self.cd2 = Checkbutton(self.lf1, text="Besan", font=('Courier', 14, 'bold'), bg='orange',
                               variable=self.vd2)
        self.cd2.place(x=20, y=110)

        self.vd3 = IntVar()
        self.cd3 = Checkbutton(self.lf1, text="Sooji", font=('Courier', 14, 'bold'), bg='orange',
                               variable=self.vd3)
        self.cd3.place(x=20, y=170)

        self.vd4 = IntVar()
        self.cd4 = Checkbutton(self.lf1, text="Maida", font=('Courier', 14, 'bold'), bg='orange',
                               variable=self.vd4)
        self.cd4.place(x=20, y=230)

        # quantity of flours
        self.d2 = Label(self.lf1, text="Qty", font=('papyrus', 16, 'bold'), bg='orange', justify="center")
        self.d2.place(x=170, y=0)

        self.svd1 = IntVar()
        choiced1 = {5, 10}
        self.popd1 = OptionMenu(self.lf1, self.svd1, *choiced1)
        self.popd1.place(x=170, y=50)

        self.svd2 = IntVar()
        choiced2 = {1, 2}
        self.popd2 = OptionMenu(self.lf1, self.svd2, *choiced2)
        self.popd2.place(x=170, y=110)

        self.svd3 = IntVar()
        choiced3 = {1, 2}
        self.popd3 = OptionMenu(self.lf1, self.svd3, *choiced3)
        self.popd3.place(x=170, y=170)

        self.svd4 = IntVar()
        choiced4 = {1, 2}
        self.popd4 = OptionMenu(self.lf1, self.svd4, *choiced4)
        self.popd4.place(x=170, y=230)

        # price of flour
        self.d3 = Label(self.lf1, text="Price", font=('papyrus', 16, 'bold'), bg='orange', justify="center")
        self.d3.place(x=300, y=0)

        self.dl1 = Label(self.lf1, text="30", font=('Courier', 14, 'bold'), bg='orange')
        self.dl1.place(x=300, y=50)

        self.dl2 = Label(self.lf1, text="100", font=('Courier', 14, 'bold'), bg='orange')
        self.dl2.place(x=300, y=110)

        self.dl3 = Label(self.lf1, text="80", font=('Courier', 14, 'bold'), bg='orange')
        self.dl3.place(x=300, y=170)

        self.dl4 = Label(self.lf1, text="80", font=('Courier', 14, 'bold'), bg='orange')
        self.dl4.place(x=300, y=230)

        # label of pulses
        self.d_1 = Label(self.lf2, text="Pulses", font=('papyrus', 16, 'bold'), bg='orange', justify="center")
        self.d_1.place(x=40, y=0)

        self.vd_1 = IntVar()
        self.cd_1 = Checkbutton(self.lf2, text="Arhar Dal", font=('Courier', 14, 'bold'), bg='orange',
                                variable=self.vd_1)
        self.cd_1.place(x=10, y=50)

        self.vd_2 = IntVar()
        self.cd_2 = Checkbutton(self.lf2, text="Moong Dal", font=('Courier', 14, 'bold'), bg='orange',
                                variable=self.vd_2)
        self.cd_2.place(x=10, y=110)

        self.vd_3 = IntVar()
        self.cd_3 = Checkbutton(self.lf2, text="Masoor Dal", font=('Courier', 14, 'bold'), bg='orange',
                                variable=self.vd_3)
        self.cd_3.place(x=10, y=170)

        # quantity
        self.d_2 = Label(self.lf2, text="Quantity", font=('papyrus', 16, 'bold'), bg='orange', justify="center")
        self.d_2.place(x=160, y=0)

        self.svd_1 = IntVar()
        choiced_1 = {1, 2}
        self.popd_1 = OptionMenu(self.lf2, self.svd_1, *choiced_1)
        self.popd_1.place(x=170, y=50)

        self.svd_2 = IntVar()
        choiced_2 = {1, 2}
        self.popd_2 = OptionMenu(self.lf2, self.svd_2, *choiced_2)
        self.popd_2.place(x=170, y=110)

        self.svd_3 = IntVar()
        choiced_3 = {1, 2}
        self.popd_3 = OptionMenu(self.lf2, self.svd_3, *choiced_1)
        self.popd_3.place(x=170, y=170)

        # price
        self.d_3 = Label(self.lf2, text="Price", font=('papyrus', 16, 'bold'), bg='orange', justify="center")
        self.d_3.place(x=290, y=0)

        self.d_l1 = Label(self.lf2, text="120", font=('Courier', 14, 'bold'), bg='orange')
        self.d_l1.place(x=300, y=50)

        self.d_l2 = Label(self.lf2, text="100", font=('Courier', 14, 'bold'), bg='orange')
        self.d_l2.place(x=300, y=110)

        self.d_l3 = Label(self.lf2, text="100", font=('Courier', 14, 'bold'), bg='orange')
        self.d_l3.place(x=300, y=170)

        self.button = Button(self.lf2, text=" Generate Bill", font=('Algerian', 12, 'bold'), command=self.mBill)
        self.button2 = Button(self.lf2, text=" Back", font=('Algerian', 12, 'bold'), command=self.back)
        self.button3 = Button(self.lf2, text="Reset", font=('Algerian', 12, 'bold'), command=self.reset)
        self.button3.place(x=220, y=400)
        self.button.place(x=20, y=400)
        self.button2.place(x=320, y=400)

    def logout(self):
        root1 = Toplevel()
        root1.title("MyProject")
        root1.wm_geometry("800x700")
        page1 = MyProject(root1)

    def reset(self):
        self.v1.set(0)
        self.v2.set(0)
        self.v3.set(0)
        self.v4.set(0)
        self.v5.set(0)
        self.sv1.set(0)
        self.sv2.set(0)
        self.sv3.set(0)
        self.sv4.set(0)
        self.sv5.set(0)
        self.vd1.set(0)
        self.vd2.set(0)
        self.vd3.set(0)
        self.vd4.set(0)
        self.svd1.set(0)
        self.svd2.set(0)
        self.svd3.set(0)
        self.svd4.set(0)
        self.vd_1.set(0)
        self.vd_2.set(0)
        self.vd_3.set(0)
        self.svd_1.set(0)
        self.svd_2.set(0)
        self.svd_3.set(0)
        self.t1.config(state='normal')
        self.t1.delete('1.0', END)
        self.t1.config(state='disabled')

    def back(self):
        self.m.destroy()

    def mBill(self):
        root4 = Toplevel()
        root4.title("BILL")
        root4.wm_geometry("600x600")
        gst = price = 0.0
        rec = dict()
        c = 1
        subp = 0.0
        plist = [65, 110, 19, 45, 400, 30, 100, 80, 80, 120, 100, 100]
        if (self.v1.get() == 1):
            item = str(self.c1.cget("text"))
            qty = int(self.sv1.get())
            price = qty * plist[0]
            rec[c] = [item, qty, price]
            subp += price
            c += 1

        if (self.v2.get() == 1):
            item = str(self.c2.cget("text"))
            qty = int(self.sv2.get())
            price = qty * plist[1]
            rec[c] = [item, qty, price]
            subp += price
            c += 1

        if (self.v3.get() == 1):
            item = str(self.c3.cget("text"))
            qty = int(self.sv3.get())
            price = qty * plist[2]
            rec[c] = [item, qty, price]
            subp += price
            c += 1

        if (self.v4.get() == 1):
            item = str(self.c4.cget("text"))
            qty = int(self.sv4.get())
            price = qty * plist[3]
            rec[c] = [item, qty, price]
            subp += price
            c += 1

        if (self.v5.get() == 1):
            item = str(self.c5.cget("text"))
            qty = int(self.sv5.get())
            price = qty * plist[4]
            rec[c] = [item, qty, price]
            subp += price
            c += 1

        if (self.vd1.get() == 1):
            item = str(self.cd1.cget("text"))
            qty = int(self.svd1.get())
            price = qty * plist[5]
            rec[c] = [item, qty, price]
            subp += price
            c += 1
        if (self.vd2.get() == 1):
            item = str(self.cd2.cget("text"))
            qty = int(self.svd2.get())
            price = qty * plist[6]
            rec[c] = [item, qty, price]
            subp += price
            c += 1

        if (self.vd3.get() == 1):
            item = str(self.cd3.cget("text"))
            qty = int(self.svd3.get())
            price = qty * plist[7]
            rec[c] = [item, qty, price]
            subp += price
            c += 1

        if (self.vd4.get() == 1):
            item = str(self.cd4.cget("text"))
            qty = int(self.svd4.get())
            price = qty * plist[8]
            rec[c] = [item, qty, price]
            subp += price
            c += 1

        if (self.vd_1.get() == 1):
            item = str(self.cd_1.cget("text"))
            qty = int(self.svd_1.get())
            price = qty * plist[9]
            rec[c] = [item, qty, price]
            subp += price
            c += 1

        if (self.vd_2.get() == 1):
            item = str(self.cd_2.cget("text"))
            qty = int(self.svd_2.get())
            price = qty * plist[10]
            rec[c] = [item, qty, price]
            subp += price
            c += 1

        if (self.vd_3.get() == 1):
            item = str(self.cd_3.cget("text"))
            qty = int(self.svd_3.get())
            price = qty * plist[11]
            rec[c] = [item, qty, price]
            subp += price
            c += 1

        gst += 0.18 * subp
        rec[c] = gst
        totalprice = gst + subp
        gb = CalculateBill(root4, self.sup, totalprice, rec, self.id)

        self.b2 = Button(self.frame1, text="LOG OUT", font=('Algerian', 15), command=self.logout)
        self.b2.place(x=600, y=0)

    def logout(self):
        root1 = Toplevel()
        root1.title("MyProject")
        root1.wm_geometry("800x700")
        page1 = MyProject(root1)


class MDairy:
    def __init__(self, master, sup, id):
        self.m = master
        self.sup = sup
        self.id = id
        self.tf = Frame(master, height=100, width=900, bd=14, relief=RIDGE)
        self.tf.pack(fill=BOTH, expand='true', side=TOP)
        self.tf.config(background='orange')

        self.lf = Frame(master, height=600, width=300, bd=14, relief=RIDGE)
        self.lf.pack(fill=BOTH, expand='true', side=LEFT)
        self.lf.config(background='orange')

        self.lf1 = Frame(master, height=600, width=300, bd=14, relief=RIDGE)
        self.lf1.pack(fill=BOTH, expand='true', side=LEFT)
        self.lf1.config(background='orange')

        self.lf2 = Frame(master, height=600, width=300, bd=14, relief=RIDGE)
        self.lf2.pack(fill=BOTH, expand='true', side=RIGHT)
        self.lf2.config(background='orange')

        self.label1 = Label(self.tf,
                            text='Lock-A-Buy Dairy Products \n\tAll products are available in limited quantity',
                            font=('papyrus', 18, 'bold'),
                            bg='orange', anchor=E)
        self.label1.grid(row=1, column=3, columnspan=5)
        self.logo1 = PhotoImage(file='esidelogo.png')
        self.label0 = Label(self.tf, image=self.logo1)
        self.label0.place(x=1, y=1)

        self.b4 = Button(self.tf, text="LOG OUT", font=('Algerian', 15), command=self.logout)
        self.b4.place(x=1200, y=5)

        # labels of dairy
        self.m1 = Label(self.lf, text="Products", font=('papyrus', 16, 'bold'), bg='orange', justify="center")
        self.m1.place(x=25, y=0)

        self.v1 = IntVar()
        self.c1 = Checkbutton(self.lf, text="Butter", font=('Courier', 14, 'bold'), bg='orange',
                              variable=self.v1)
        self.c1.place(x=10, y=50)

        self.v2 = IntVar()
        self.c2 = Checkbutton(self.lf, text="Yogurt", font=('Courier', 14, 'bold'), bg='orange',
                              variable=self.v2)
        self.c2.place(x=10, y=100)

        self.v3 = IntVar()
        self.c3 = Checkbutton(self.lf, text="Panner", font=('Courier', 14, 'bold'), bg='orange',
                              variable=self.v3)
        self.c3.place(x=10, y=150)

        self.v4 = IntVar()
        self.c4 = Checkbutton(self.lf, text="Cheese", font=('Courier', 14, 'bold'), bg='orange',
                              variable=self.v4)
        self.c4.place(x=10, y=200)

        self.v5 = IntVar()
        self.c5 = Checkbutton(self.lf, text="Mawa", font=('Courier', 14, 'bold'), bg='orange',
                              variable=self.v5)
        self.c5.place(x=10, y=250)

        # quantity of dairy
        self.m2 = Label(self.lf, text="Qty(kg)", font=('papyrus', 16, 'bold'), bg='orange', justify="center")
        self.m2.place(x=170, y=0)

        self.sv1 = IntVar()
        choice1 = {0.05, 0.1, 0.2, 0.5, 1}
        self.pop1 = OptionMenu(self.lf, self.sv1, *choice1)
        self.pop1.place(x=170, y=50)

        self.sv2 = IntVar()
        choice2 = {0.1, 0.4, 1, 2, 3}
        self.pop2 = OptionMenu(self.lf, self.sv2, *choice2)
        self.pop2.place(x=170, y=100)

        self.sv3 = IntVar()
        choice3 = {0.1, 0.25, 0.5, 1, 2}
        self.pop3 = OptionMenu(self.lf, self.sv3, *choice3)
        self.pop3.place(x=170, y=150)

        self.sv4 = IntVar()
        choice4 = {0.1, 0.2, 0.5, 1, 2}
        self.pop4 = OptionMenu(self.lf, self.sv4, *choice4)
        self.pop4.place(x=170, y=200)

        self.sv5 = IntVar()
        choice5 = {0.1, 0.25, 0.5, 1, 2}
        self.pop5 = OptionMenu(self.lf, self.sv5, *choice5)
        self.pop5.place(x=170, y=250)

        # price of dairy

        self.m3 = Label(self.lf, text="Price/kg", font=('papyrus', 16, 'bold'), bg='orange', justify="center")
        self.m3.place(x=300, y=0)

        self.ml1 = Label(self.lf, text="445", font=('Courier', 14, 'bold'), bg='orange')
        self.ml1.place(x=300, y=50)

        self.ml2 = Label(self.lf, text="60", font=('Courier', 14, 'bold'), bg='orange')
        self.ml2.place(x=300, y=100)

        self.ml3 = Label(self.lf, text="250", font=('Courier', 14, 'bold'), bg='orange')
        self.ml3.place(x=300, y=150)

        self.ml4 = Label(self.lf, text="400", font=('Courier', 14, 'bold'), bg='orange')
        self.ml4.place(x=300, y=200)

        self.ml5 = Label(self.lf, text="250", font=('Courier', 14, 'bold'), bg='orange')
        self.ml5.place(x=300, y=250)

        # labels of lf1

        self.d1 = Label(self.lf1, text="Products", font=('papyrus', 16, 'bold'), bg='orange', justify="center")
        self.d1.place(x=20, y=0)

        self.vd1 = IntVar()
        self.cd1 = Checkbutton(self.lf1, text="Milk", font=('Courier', 14, 'bold'), bg='orange',
                               variable=self.vd1)
        self.cd1.place(x=20, y=50)

        self.vd2 = IntVar()
        self.cd2 = Checkbutton(self.lf1, text="Milk Cream", font=('Courier', 14, 'bold'), bg='orange',
                               variable=self.vd2)
        self.cd2.place(x=20, y=100)

        self.vd3 = IntVar()
        self.cd3 = Checkbutton(self.lf1, text="Lassi", font=('Courier', 14, 'bold'), bg='orange',
                               variable=self.vd3)
        self.cd3.place(x=20, y=150)

        self.vd4 = IntVar()
        self.cd4 = Checkbutton(self.lf1, text="Toned Milk", font=('Courier', 14, 'bold'), bg='orange',
                               variable=self.vd4)
        self.cd4.place(x=20, y=200)

        # quantity of lf1
        self.d2 = Label(self.lf1, text="Qty(l)", font=('papyrus', 16, 'bold'), bg='orange', justify="center")
        self.d2.place(x=170, y=0)

        self.svd1 = IntVar()
        choiced1 = {0.2, 0.5, 1, 2}
        self.popd1 = OptionMenu(self.lf1, self.svd1, *choiced1)
        self.popd1.place(x=170, y=50)

        self.svd2 = IntVar()
        choiced2 = {0.25, 0.5, 1}
        self.popd2 = OptionMenu(self.lf1, self.svd2, *choiced2)
        self.popd2.place(x=170, y=100)

        self.svd3 = IntVar()
        choiced3 = {0.2, 0.25, 1}
        self.popd3 = OptionMenu(self.lf1, self.svd3, *choiced3)
        self.popd3.place(x=170, y=150)

        self.svd4 = IntVar()
        choiced4 = {0.2, 0.5, 1, 2}
        self.popd4 = OptionMenu(self.lf1, self.svd4, *choiced4)
        self.popd4.place(x=170, y=200)

        # price of products lf1
        self.d3 = Label(self.lf1, text="Price", font=('papyrus', 16, 'bold'), bg='orange', justify="center")
        self.d3.place(x=300, y=0)

        self.dl1 = Label(self.lf1, text="56", font=('Courier', 14, 'bold'), bg='orange')
        self.dl1.place(x=300, y=50)

        self.dl2 = Label(self.lf1, text="120", font=('Courier', 14, 'bold'), bg='orange')
        self.dl2.place(x=300, y=100)

        self.dl3 = Label(self.lf1, text="65", font=('Courier', 14, 'bold'), bg='orange')
        self.dl3.place(x=300, y=150)

        self.dl4 = Label(self.lf1, text="45", font=('Courier', 14, 'bold'), bg='orange')
        self.dl4.place(x=300, y=200)

        # label of icecream
        self.d_1 = Label(self.lf2, text="Ice-cream", font=('papyrus', 16, 'bold'), bg='orange', justify="center")
        self.d_1.place(x=10, y=0)

        self.vd_1 = IntVar()
        self.cd_1 = Checkbutton(self.lf2, text="Vanilla", font=('Courier', 14, 'bold'), bg='orange',
                                variable=self.vd_1)
        self.cd_1.place(x=10, y=50)

        self.vd_2 = IntVar()
        self.cd_2 = Checkbutton(self.lf2, text="Butterscotch", font=('Courier', 14, 'bold'), bg='orange',
                                variable=self.vd_2)
        self.cd_2.place(x=10, y=100)

        self.vd_3 = IntVar()
        self.cd_3 = Checkbutton(self.lf2, text="Chocolate", font=('Courier', 14, 'bold'), bg='orange',
                                variable=self.vd_3)
        self.cd_3.place(x=10, y=150)

        # quantity of ice-cream
        self.d_2 = Label(self.lf2, text="Qty", font=('papyrus', 16, 'bold'), bg='orange', justify="center")
        self.d_2.place(x=160, y=0)

        self.svd_1 = IntVar()
        choiced_1 = {1, 2, 3, 4, 5}
        self.popd_1 = OptionMenu(self.lf2, self.svd_1, *choiced_1)
        self.popd_1.place(x=170, y=50)

        self.svd_2 = IntVar()
        choiced_2 = {1, 2, 3, 4, 5}
        self.popd_2 = OptionMenu(self.lf2, self.svd_2, *choiced_2)
        self.popd_2.place(x=170, y=100)

        self.svd_3 = IntVar()
        choiced_3 = {1, 2, 3, 4, 5}
        self.popd_3 = OptionMenu(self.lf2, self.svd_3, *choiced_1)
        self.popd_3.place(x=170, y=150)

        # price of ice-cream
        self.d_3 = Label(self.lf2, text="Price(\scoop)", font=('papyrus', 16, 'bold'), bg='orange', justify="center")
        self.d_3.place(x=270, y=0)

        self.d_l1 = Label(self.lf2, text="20", font=('Courier', 14, 'bold'), bg='orange')
        self.d_l1.place(x=300, y=50)

        self.d_l2 = Label(self.lf2, text="30", font=('Courier', 14, 'bold'), bg='orange')
        self.d_l2.place(x=300, y=100)

        self.d_l3 = Label(self.lf2, text="40", font=('Courier', 14, 'bold'), bg='orange')
        self.d_l3.place(x=300, y=150)

        self.button = Button(self.lf2, text=" Generate Bill", font=('Algerian', 12, 'bold'), command=self.mBill)
        self.button2 = Button(self.lf2, text=" Back", font=('Algerian', 12, 'bold'), command=self.back)
        self.button3 = Button(self.lf2, text="Reset", font=('Algerian', 12, 'bold'), command=self.reset)
        self.button3.place(x=220, y=400)
        self.button.place(x=20, y=400)
        self.button2.place(x=320, y=400)

    def logout(self):
        root1 = Toplevel()
        root1.title("MyProject")
        root1.wm_geometry("800x700")
        page1 = MyProject(root1)

    def reset(self):
        self.v1.set(0)
        self.v2.set(0)
        self.v3.set(0)
        self.v4.set(0)
        self.v5.set(0)
        self.sv1.set(0)
        self.sv2.set(0)
        self.sv3.set(0)
        self.sv4.set(0)
        self.sv5.set(0)
        self.vd1.set(0)
        self.vd2.set(0)
        self.vd3.set(0)
        self.vd4.set(0)
        self.svd1.set(0)
        self.svd2.set(0)
        self.svd3.set(0)
        self.svd4.set(0)
        self.vd_1.set(0)
        self.vd_2.set(0)
        self.vd_3.set(0)
        self.svd_1.set(0)
        self.svd_2.set(0)
        self.svd_3.set(0)
        self.t1.config(state='normal')
        self.t1.delete('1.0', END)
        self.t1.config(state='disabled')

    def mBill(self):
        root4 = Toplevel()
        root4.title("BILL")
        root4.wm_geometry("600x600")
        gst = price = 0.0
        plist = [445, 60, 250, 400, 250, 56, 120, 65, 45, 20, 30, 40]
        rec = dict()
        c = 1
        subp = 0.0
        if (self.v1.get() == 1):
            item = str(self.c1.cget("text"))
            qty = int(self.sv1.get())
            price = qty * plist[0]
            rec[c] = [item, qty, price]
            subp += price
            c += 1

        if (self.v2.get() == 1):
            item = str(self.c2.cget("text"))
            qty = int(self.sv2.get())
            price = qty * plist[1]
            rec[c] = [item, qty, price]
            subp += price
            c += 1

        if (self.v3.get() == 1):
            item = str(self.c3.cget("text"))
            qty = int(self.sv3.get())
            price = qty * plist[2]
            rec[c] = [item, qty, price]
            subp += price
            c += 1

        if (self.v4.get() == 1):
            item = str(self.c4.cget("text"))
            qty = int(self.sv4.get())
            price = qty * plist[3]
            rec[c] = [item, qty, price]
            subp += price
            c += 1

        if (self.v5.get() == 1):
            item = str(self.c5.cget("text"))
            qty = int(self.sv5.get())
            price = qty * plist[4]
            rec[c] = [item, qty, price]
            subp += price
            c += 1

        if (self.vd1.get() == 1):
            item = str(self.cd1.cget("text"))
            qty = int(self.svd1.get())
            price = qty * plist[5]
            rec[c] = [item, qty, price]
            subp += price
            c += 1
        if (self.vd2.get() == 1):
            item = str(self.cd2.cget("text"))
            qty = int(self.svd2.get())
            price = qty * plist[6]
            rec[c] = [item, qty, price]
            subp += price
            c += 1

        if (self.vd3.get() == 1):
            item = str(self.cd3.cget("text"))
            qty = int(self.svd3.get())
            price = qty * plist[7]
            rec[c] = [item, qty, price]
            subp += price
            c += 1

        if (self.vd4.get() == 1):
            item = str(self.cd4.cget("text"))
            qty = int(self.svd4.get())
            price = qty * plist[8]
            rec[c] = [item, qty, price]
            subp += price
            c += 1

        if (self.vd_1.get() == 1):
            item = str(self.cd_1.cget("text"))
            qty = int(self.svd_1.get())
            price = qty * plist[9]
            rec[c] = [item, qty, price]
            subp += price
            c += 1

        if (self.vd_2.get() == 1):
            item = str(self.cd_2.cget("text"))
            qty = int(self.svd_2.get())
            price = qty * plist[10]
            rec[c] = [item, qty, price]
            subp += price
            c += 1

        if (self.vd_3.get() == 1):
            item = str(self.cd_3.cget("text"))
            qty = int(self.svd_3.get())
            price = qty * plist[11]
            rec[c] = [item, qty, price]
            subp += price
            c += 1

        gst += 0.18 * subp
        rec[c] = gst
        totalprice = gst + subp
        db = CalculateBill(root4, self.sup, totalprice, rec, self.id)

    def back(self):
        self.m.destroy()

        self.b2 = Button(self.frame1, text="LOG OUT", font=('Algerian', 15), command=self.logout)
        self.b2.place(x=600, y=0)

    def logout(self):
        root1 = Toplevel()
        root1.title("MyProject")
        root1.wm_geometry("800x700")
        page1 = MyProject(root1)


class MVeg:
    def __init__(self, master, sup, id):
        self.m = master
        self.sup = sup
        self.id = id
        self.tf = Frame(master, height=100, width=900, bd=14, relief=RIDGE)
        self.tf.pack(fill=BOTH, expand='true', side=TOP)
        self.tf.config(background='orange')

        self.lf = Frame(master, height=600, width=300, bd=14, relief=RIDGE)
        self.lf.pack(fill=BOTH, expand='true', side=LEFT)
        self.lf.config(background='orange')

        self.lf1 = Frame(master, height=600, width=300, bd=14, relief=RIDGE)
        self.lf1.pack(fill=BOTH, expand='true', side=LEFT)
        self.lf1.config(background='orange')

        self.lf2 = Frame(master, height=600, width=300, bd=14, relief=RIDGE)
        self.lf2.pack(fill=BOTH, expand='true', side=RIGHT)
        self.lf2.config(background='orange')

        self.label1 = Label(self.tf,
                            text='\tLock-A-Buy Vegetables and Fruits\n\tAll products are available in limited quantity',
                            font=('papyrus', 18, 'bold'),
                            bg='orange', anchor=E)
        self.label1.grid(row=1, column=1, columnspan=5)
        self.logo1 = PhotoImage(file='esidelogo.png')
        self.label0 = Label(self.tf, image=self.logo1)
        self.label0.place(x=0, y=0)

        self.b4 = Button(self.tf, text="LOG OUT", font=('Algerian', 15), command=self.logout)
        self.b4.place(x=1200, y=5)

        # Labels of Products
        self.m1 = Label(self.lf, text="Vegetables", font=('papyrus', 16, 'bold'), bg='orange', justify="center")
        self.m1.place(x=25, y=0)

        self.v1 = IntVar()
        self.c1 = Checkbutton(self.lf, text="Potato", font=('Courier', 14, 'bold'), bg='orange',
                              variable=self.v1)
        self.c1.place(x=10, y=50)

        self.v2 = IntVar()
        self.c2 = Checkbutton(self.lf, text="Onion", font=('Courier', 14, 'bold'), bg='orange',
                              variable=self.v2)
        self.c2.place(x=10, y=100)

        self.v3 = IntVar()
        self.c3 = Checkbutton(self.lf, text="Tomato", font=('Courier', 14, 'bold'), bg='orange',
                              variable=self.v3)
        self.c3.place(x=10, y=150)

        self.v4 = IntVar()
        self.c4 = Checkbutton(self.lf, text="Ladyfinger", font=('Courier', 11, 'bold'), bg='orange',
                              variable=self.v4)
        self.c4.place(x=10, y=200)

        self.v5 = IntVar()
        self.c5 = Checkbutton(self.lf, text="Jack Fruit", font=('Courier', 14, 'bold'), bg='orange',
                              variable=self.v5)
        self.c5.place(x=10, y=250)

        # quantity of vegetables
        self.m2 = Label(self.lf, text="Qty(kg)", font=('papyrus', 16, 'bold'), bg='orange', justify="center")
        self.m2.place(x=170, y=0)

        self.sv1 = IntVar()
        choice1 = {1, 2, 3, 4, 5}
        self.pop1 = OptionMenu(self.lf, self.sv1, *choice1)
        self.pop1.place(x=170, y=50)

        self.sv2 = IntVar()
        choice2 = {1, 2, 3, 4, 5}
        self.pop2 = OptionMenu(self.lf, self.sv2, *choice2)
        self.pop2.place(x=170, y=100)

        self.sv3 = IntVar()
        choice3 = {1, 2, 3, 4, 5}
        self.pop3 = OptionMenu(self.lf, self.sv3, *choice3)
        self.pop3.place(x=170, y=150)

        self.sv4 = IntVar()
        choice4 = {1, 2, 3, 4}
        self.pop4 = OptionMenu(self.lf, self.sv4, *choice4)
        self.pop4.place(x=170, y=200)

        self.sv5 = IntVar()
        choice5 = {1, 2, 3, 4, 5}
        self.pop5 = OptionMenu(self.lf, self.sv5, *choice5)
        self.pop5.place(x=170, y=250)

        # price
        self.m3 = Label(self.lf, text="Price/kg", font=('papyrus', 16, 'bold'), bg='orange', justify="center")
        self.m3.place(x=300, y=0)

        self.ml1 = Label(self.lf, text="20", font=('Courier', 14, 'bold'), bg='orange')
        self.ml1.place(x=300, y=50)

        self.ml2 = Label(self.lf, text="15", font=('Courier', 14, 'bold'), bg='orange')
        self.ml2.place(x=300, y=100)

        self.ml3 = Label(self.lf, text="20", font=('Courier', 14, 'bold'), bg='orange')
        self.ml3.place(x=300, y=150)

        self.ml3 = Label(self.lf, text="30", font=('Courier', 14, 'bold'), bg='orange')
        self.ml3.place(x=300, y=200)

        self.ml3 = Label(self.lf, text="40", font=('Courier', 14, 'bold'), bg='orange')
        self.ml3.place(x=300, y=250)

        # labels of fruits

        self.d1 = Label(self.lf1, text="Fruits", font=('papyrus', 16, 'bold'), bg='orange', justify="center")
        self.d1.place(x=50, y=0)

        self.vd1 = IntVar()
        self.cd1 = Checkbutton(self.lf1, text="Mango", font=('Courier', 14, 'bold'), bg='orange',
                               variable=self.vd1)
        self.cd1.place(x=20, y=50)

        self.vd2 = IntVar()
        self.cd2 = Checkbutton(self.lf1, text="Pomegranate", font=('Courier', 14, 'bold'), bg='orange',
                               variable=self.vd2)
        self.cd2.place(x=20, y=100)

        self.vd3 = IntVar()
        self.cd3 = Checkbutton(self.lf1, text="Papaya", font=('Courier', 14, 'bold'), bg='orange',
                               variable=self.vd3)
        self.cd3.place(x=20, y=150)

        self.vd4 = IntVar()
        self.cd4 = Checkbutton(self.lf1, text="Watemelon", font=('Courier', 14, 'bold'), bg='orange',
                               variable=self.vd4)
        self.cd4.place(x=20, y=200)

        # quantity of fruits
        self.d2 = Label(self.lf1, text="Qty(kg)", font=('papyrus', 16, 'bold'), bg='orange', justify="center")
        self.d2.place(x=170, y=0)

        self.svd1 = IntVar()
        choiced1 = {1, 2, 3, 4, 5}
        self.popd1 = OptionMenu(self.lf1, self.svd1, *choiced1)
        self.popd1.place(x=170, y=50)

        self.svd2 = IntVar()
        choiced2 = {1, 2, 3}
        self.popd2 = OptionMenu(self.lf1, self.svd2, *choiced2)
        self.popd2.place(x=170, y=100)

        self.svd3 = IntVar()
        choiced3 = {1, 2, 3, 4, 5}
        self.popd3 = OptionMenu(self.lf1, self.svd3, *choiced3)
        self.popd3.place(x=170, y=150)

        self.svd4 = IntVar()
        choiced4 = {1, 2, 3, 4, 5}
        self.popd4 = OptionMenu(self.lf1, self.svd4, *choiced4)
        self.popd4.place(x=170, y=200)

        # price of fruits
        self.d3 = Label(self.lf1, text="Price(/kg)", font=('papyrus', 16, 'bold'), bg='orange', justify="center")
        self.d3.place(x=290, y=0)

        self.dl1 = Label(self.lf1, text="70", font=('Courier', 14, 'bold'), bg='orange')
        self.dl1.place(x=300, y=50)

        self.dl2 = Label(self.lf1, text="90", font=('Courier', 14, 'bold'), bg='orange')
        self.dl2.place(x=300, y=100)

        self.dl3 = Label(self.lf1, text="30", font=('Courier', 14, 'bold'), bg='orange')
        self.dl3.place(x=300, y=150)

        self.dl4 = Label(self.lf1, text="15", font=('Courier', 14, 'bold'), bg='orange')
        self.dl4.place(x=300, y=200)

        # labels of additional
        self.d_1 = Label(self.lf2, text="Add-ons", font=('papyrus', 16, 'bold'), bg='orange', justify="center")
        self.d_1.place(x=40, y=0)

        self.vd_1 = IntVar()
        self.cd_1 = Checkbutton(self.lf2, text="Lemon", font=('Courier', 14, 'bold'), bg='orange',
                                variable=self.vd_1)
        self.cd_1.place(x=10, y=50)

        self.vd_2 = IntVar()
        self.cd_2 = Checkbutton(self.lf2, text="Coriander", font=('Courier', 14, 'bold'), bg='orange',
                                variable=self.vd_2)
        self.cd_2.place(x=10, y=100)

        self.vd_3 = IntVar()
        self.cd_3 = Checkbutton(self.lf2, text="Spearmint", font=('Courier', 14, 'bold'), bg='orange',
                                variable=self.vd_3)
        self.cd_3.place(x=10, y=150)

        # quantity
        self.d_2 = Label(self.lf2, text="Qty(pcs)", font=('papyrus', 16, 'bold'), bg='orange', justify="center")
        self.d_2.place(x=160, y=0)

        self.svd_1 = IntVar()
        choiced_1 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
        self.popd_1 = OptionMenu(self.lf2, self.svd_1, *choiced_1)
        self.popd_1.place(x=170, y=50)

        self.svd_2 = IntVar()
        choiced_2 = {1, 2, 3, 4, 5}
        self.popd_2 = OptionMenu(self.lf2, self.svd_2, *choiced_2)
        self.popd_2.place(x=170, y=100)

        self.svd_3 = IntVar()
        choiced_3 = {1, 2, 3, 4, 5}
        self.popd_3 = OptionMenu(self.lf2, self.svd_3, *choiced_1)
        self.popd_3.place(x=170, y=150)

        # price
        self.d_3 = Label(self.lf2, text="Price(/pc)", font=('papyrus', 16, 'bold'), bg='orange', justify="center")
        self.d_3.place(x=290, y=0)

        self.d_l1 = Label(self.lf2, text="2", font=('Courier', 14, 'bold'), bg='orange')
        self.d_l1.place(x=300, y=50)

        self.d_l2 = Label(self.lf2, text="5", font=('Courier', 14, 'bold'), bg='orange')
        self.d_l2.place(x=300, y=100)

        self.d_l3 = Label(self.lf2, text="5", font=('Courier', 14, 'bold'), bg='orange')
        self.d_l3.place(x=300, y=150)

        self.button = Button(self.lf2, text=" Generate Bill", font=('Algerian', 12, 'bold'), command=self.mBill)
        self.button2 = Button(self.lf2, text=" Back", font=('Algerian', 12, 'bold'), command=self.back)
        self.button3 = Button(self.lf2, text="Reset", font=('Algerian', 12, 'bold'), command=self.reset)
        self.button.place(x=20, y=400)
        self.button2.place(x=320, y=400)
        self.button3.place(x=220, y=400)

    def logout(self):
        root1 = Toplevel()
        root1.title("MyProject")
        root1.wm_geometry("800x700")
        page1 = MyProject(root1)

    def reset(self):
        self.v1.set(0)
        self.v2.set(0)
        self.v3.set(0)
        self.v4.set(0)
        self.v5.set(0)
        self.sv1.set(0)
        self.sv2.set(0)
        self.sv3.set(0)
        self.sv4.set(0)
        self.sv5.set(0)
        self.vd1.set(0)
        self.vd2.set(0)
        self.vd3.set(0)
        self.vd4.set(0)
        self.svd1.set(0)
        self.svd2.set(0)
        self.svd3.set(0)
        self.svd4.set(0)
        self.vd_1.set(0)
        self.vd_2.set(0)
        self.vd_3.set(0)
        self.svd_1.set(0)
        self.svd_2.set(0)
        self.svd_3.set(0)
        self.t1.config(state='normal')
        self.t1.delete('1.0', END)
        self.t1.config(state='disabled')

    def back(self):
        self.m.destroy()

    def mBill(self):
        root4 = Toplevel()
        root4.title("BILL")
        root4.wm_geometry("600x600")
        gst = price = 0.0
        plist = [20, 15, 20, 30, 40, 70, 90, 30, 15, 2, 5, 5]
        rec = dict()
        c = 1
        subp = 0.0
        if (self.v1.get() == 1):
            item = str(self.c1.cget("text"))
            qty = int(self.sv1.get())
            price = qty * plist[0]
            rec[c] = [item, qty, price]
            subp += price
            c += 1

        if (self.v2.get() == 1):
            item = str(self.c2.cget("text"))
            qty = int(self.sv2.get())
            price = qty * plist[1]
            rec[c] = [item, qty, price]
            subp += price
            c += 1

        if (self.v3.get() == 1):
            item = str(self.c3.cget("text"))
            qty = int(self.sv3.get())
            price = qty * plist[2]
            rec[c] = [item, qty, price]
            subp += price
            c += 1

        if (self.v4.get() == 1):
            item = str(self.c4.cget("text"))
            qty = int(self.sv4.get())
            price = qty * plist[3]
            rec[c] = [item, qty, price]
            subp += price
            c += 1

        if (self.v5.get() == 1):
            item = str(self.c5.cget("text"))
            qty = int(self.sv5.get())
            price = qty * plist[4]
            rec[c] = [item, qty, price]
            subp += price
            c += 1

        if (self.vd1.get() == 1):
            item = str(self.cd1.cget("text"))
            qty = int(self.svd1.get())
            price = qty * plist[5]
            rec[c] = [item, qty, price]
            subp += price
            c += 1
        if (self.vd2.get() == 1):
            item = str(self.cd2.cget("text"))
            qty = int(self.svd2.get())
            price = qty * plist[6]
            rec[c] = [item, qty, price]
            subp += price
            c += 1

        if (self.vd3.get() == 1):
            item = str(self.cd3.cget("text"))
            qty = int(self.svd3.get())
            price = qty * plist[7]
            rec[c] = [item, qty, price]
            subp += price
            c += 1

        if (self.vd4.get() == 1):
            item = str(self.cd4.cget("text"))
            qty = int(self.svd4.get())
            price = qty * plist[8]
            rec[c] = [item, qty, price]
            subp += price
            c += 1

        if (self.vd_1.get() == 1):
            item = str(self.cd_1.cget("text"))
            qty = int(self.svd_1.get())
            price = qty * plist[9]
            rec[c] = [item, qty, price]
            subp += price
            c += 1

        if (self.vd_2.get() == 1):
            item = str(self.cd_2.cget("text"))
            qty = int(self.svd_2.get())
            price = qty * plist[10]
            rec[c] = [item, qty, price]
            subp += price
            c += 1

        if (self.vd_3.get() == 1):
            item = str(self.cd_3.cget("text"))
            qty = int(self.svd_3.get())
            price = qty * plist[11]
            rec[c] = [item, qty, price]
            subp += price
            c += 1

        gst += 0.18 * subp
        rec[c] = gst
        totalprice = gst + subp
        vb = CalculateBill(root4, self.sup, totalprice, rec, self.id)

        self.b2 = Button(self.frame1, text="LOG OUT", font=('Algerian', 15), command=self.logout)
        self.b2.place(x=600, y=0)

    def logout(self):
        root1 = Toplevel()
        root1.title("MyProject")
        root1.wm_geometry("800x700")
        page1 = MyProject(root1)


class MLiquor:
    def __init__(self, master, sup, id):
        self.m = master
        self.sup = sup
        self.id = id
        self.tf = Frame(master, height=100, width=900, bd=14, relief=RIDGE)
        self.tf.pack(fill=BOTH, expand='true', side=TOP)
        self.tf.config(background='orange')

        self.lf = Frame(master, height=600, width=300, bd=14, relief=RIDGE)
        self.lf.pack(fill=BOTH, expand='true', side=LEFT)
        self.lf.config(background='orange')

        self.lf1 = Frame(master, height=600, width=300, bd=14, relief=RIDGE)
        self.lf1.pack(fill=BOTH, expand='true', side=LEFT)
        self.lf1.config(background='orange')

        self.lf2 = Frame(master, height=600, width=300, bd=14, relief=RIDGE)
        self.lf2.pack(fill=BOTH, expand='true', side=RIGHT)
        self.lf2.config(background='orange')

        self.label1 = Label(self.tf,
                            text='\tLock-A-Buy Liquor and Beverages\n\tAll products are available in limited quantity',
                            font=('papyrus', 18, 'bold'),
                            bg='orange', anchor=E)
        self.label1.grid(row=1, column=1, columnspan=5)
        self.logo1 = PhotoImage(file='esidelogo.png')
        self.label0 = Label(self.tf, image=self.logo1)
        self.label0.place(x=0, y=0)

        self.b4 = Button(self.tf, text="LOG OUT", font=('Algerian', 15), command=self.logout)
        self.b4.place(x=1200, y=5)

        # Labels of Products
        self.m1 = Label(self.lf, text="Drinks", font=('papyrus', 16, 'bold'), bg='orange', justify="center")
        self.m1.place(x=25, y=0)

        self.v1 = IntVar()
        self.c1 = Checkbutton(self.lf, text="Blenders Pride", font=('Courier', 14, 'bold'), bg='orange',
                              variable=self.v1)
        self.c1.place(x=10, y=50)

        self.v2 = IntVar()
        self.c2 = Checkbutton(self.lf, text="Royal Stag", font=('Courier', 14, 'bold'), bg='orange',
                              variable=self.v2)
        self.c2.place(x=10, y=100)

        self.v3 = IntVar()
        self.c3 = Checkbutton(self.lf, text="Imperial Blue", font=('Courier', 14, 'bold'), bg='orange',
                              variable=self.v3)
        self.c3.place(x=10, y=150)

        self.v4 = IntVar()
        self.c4 = Checkbutton(self.lf, text="Old Monk", font=('Courier', 14, 'bold'), bg='orange',
                              variable=self.v4)
        self.c4.place(x=10, y=200)

        self.v5 = IntVar()
        self.c5 = Checkbutton(self.lf, text="100 Pipers", font=('Courier', 14, 'bold'), bg='orange',
                              variable=self.v5)
        self.c5.place(x=10, y=250)

        # quantity of Products
        self.m2 = Label(self.lf, text="Qty", font=('papyrus', 16, 'bold'), bg='orange', justify="center")
        self.m2.place(x=170, y=0)

        self.sv1 = IntVar()
        choice1 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
        self.pop1 = OptionMenu(self.lf, self.sv1, *choice1)
        self.pop1.place(x=170, y=50)

        self.sv2 = IntVar()
        choice2 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
        self.pop2 = OptionMenu(self.lf, self.sv2, *choice2)
        self.pop2.place(x=170, y=100)

        self.sv3 = IntVar()
        choice3 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
        self.pop3 = OptionMenu(self.lf, self.sv3, *choice3)
        self.pop3.place(x=170, y=150)

        self.sv4 = IntVar()
        choice4 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
        self.pop4 = OptionMenu(self.lf, self.sv4, *choice4)
        self.pop4.place(x=170, y=200)

        self.sv5 = IntVar()
        choice5 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
        self.pop5 = OptionMenu(self.lf, self.sv5, *choice5)
        self.pop5.place(x=170, y=250)

        # price
        self.m3 = Label(self.lf, text="Price", font=('papyrus', 16, 'bold'), bg='orange', justify="center")
        self.m3.place(x=300, y=0)

        self.ml1 = Label(self.lf, text="500", font=('Courier', 14, 'bold'), bg='orange')
        self.ml1.place(x=300, y=50)

        self.ml2 = Label(self.lf, text="350", font=('Courier', 14, 'bold'), bg='orange')
        self.ml2.place(x=300, y=100)

        self.ml3 = Label(self.lf, text="400", font=('Courier', 14, 'bold'), bg='orange')
        self.ml3.place(x=300, y=150)

        self.ml4 = Label(self.lf, text="250", font=('Courier', 14, 'bold'), bg='orange')
        self.ml4.place(x=300, y=200)

        self.ml5 = Label(self.lf, text="950", font=('Courier', 14, 'bold'), bg='orange')
        self.ml5.place(x=300, y=250)

        # Labels of drink
        self.d1 = Label(self.lf1, text="Drinks", font=('papyrus', 16, 'bold'), bg='orange', justify="center")
        self.d1.place(x=50, y=0)

        self.vd1 = IntVar()
        self.cd1 = Checkbutton(self.lf1, text="Pepsi", font=('Courier', 14, 'bold'), bg='orange',
                               variable=self.vd1)
        self.cd1.place(x=20, y=50)

        self.vd2 = IntVar()
        self.cd2 = Checkbutton(self.lf1, text="Thumbs Up", font=('Courier', 14, 'bold'), bg='orange',
                               variable=self.vd2)
        self.cd2.place(x=20, y=100)

        self.vd3 = IntVar()
        self.cd3 = Checkbutton(self.lf1, text="Sprite", font=('Courier', 14, 'bold'), bg='orange',
                               variable=self.vd3)
        self.cd3.place(x=20, y=150)

        self.vd4 = IntVar()
        self.cd4 = Checkbutton(self.lf1, text="Mirinda", font=('Courier', 14, 'bold'), bg='orange',
                               variable=self.vd4)
        self.cd4.place(x=20, y=200)

        # quantity
        self.d2 = Label(self.lf1, text="Qty", font=('papyrus', 16, 'bold'), bg='orange', justify="center")
        self.d2.place(x=170, y=0)

        self.svd1 = IntVar()
        choiced1 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
        self.popd1 = OptionMenu(self.lf1, self.svd1, *choiced1)
        self.popd1.place(x=170, y=50)

        self.svd2 = IntVar()
        choiced2 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
        self.popd2 = OptionMenu(self.lf1, self.svd2, *choiced2)
        self.popd2.place(x=170, y=100)

        self.svd3 = IntVar()
        choiced3 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
        self.popd3 = OptionMenu(self.lf1, self.svd3, *choiced3)
        self.popd3.place(x=170, y=150)

        self.svd4 = IntVar()
        choiced4 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
        self.popd4 = OptionMenu(self.lf1, self.svd4, *choiced4)
        self.popd4.place(x=170, y=200)

        # price of flour
        self.d3 = Label(self.lf1, text="Price", font=('papyrus', 16, 'bold'), bg='orange', justify="center")
        self.d3.place(x=300, y=0)

        self.dl1 = Label(self.lf1, text="35", font=('Courier', 14, 'bold'), bg='orange')
        self.dl1.place(x=300, y=50)

        self.dl2 = Label(self.lf1, text="25", font=('Courier', 14, 'bold'), bg='orange')
        self.dl2.place(x=300, y=100)

        self.dl3 = Label(self.lf1, text="25", font=('Courier', 14, 'bold'), bg='orange')
        self.dl3.place(x=300, y=150)

        self.dl4 = Label(self.lf1, text="35", font=('Courier', 14, 'bold'), bg='orange')
        self.dl4.place(x=300, y=200)

        # label of pulses
        self.d_1 = Label(self.lf2, text="Drinks", font=('papyrus', 16, 'bold'), bg='orange', justify="center")
        self.d_1.place(x=40, y=0)

        self.vd_1 = IntVar()
        self.cd_1 = Checkbutton(self.lf2, text="Fresh Lime Soda", font=('Courier', 14, 'bold'), bg='orange',
                                variable=self.vd_1)
        self.cd_1.place(x=10, y=50)

        self.vd_2 = IntVar()
        self.cd_2 = Checkbutton(self.lf2, text="Iced Tea", font=('Courier', 14, 'bold'), bg='orange',
                                variable=self.vd_2)
        self.cd_2.place(x=10, y=100)

        self.vd_3 = IntVar()
        self.cd_3 = Checkbutton(self.lf2, text="Cold Coffee", font=('Courier', 14, 'bold'), bg='orange',
                                variable=self.vd_3)
        self.cd_3.place(x=10, y=150)

        # quantity
        self.d_2 = Label(self.lf2, text="Quantity", font=('papyrus', 16, 'bold'), bg='orange', justify="center")
        self.d_2.place(x=160, y=0)

        self.svd_1 = IntVar()
        choiced_1 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
        self.popd_1 = OptionMenu(self.lf2, self.svd_1, *choiced_1)
        self.popd_1.place(x=170, y=50)

        self.svd_2 = IntVar()
        choiced_2 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
        self.popd_2 = OptionMenu(self.lf2, self.svd_2, *choiced_2)
        self.popd_2.place(x=170, y=100)

        self.svd_3 = IntVar()
        choiced_3 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
        self.popd_3 = OptionMenu(self.lf2, self.svd_3, *choiced_1)
        self.popd_3.place(x=170, y=150)

        # price
        self.d_3 = Label(self.lf2, text="Price", font=('papyrus', 16, 'bold'), bg='orange', justify="center")
        self.d_3.place(x=290, y=0)

        self.d_l1 = Label(self.lf2, text="50", font=('Courier', 14, 'bold'), bg='orange')
        self.d_l1.place(x=300, y=50)

        self.d_l2 = Label(self.lf2, text="60", font=('Courier', 14, 'bold'), bg='orange')
        self.d_l2.place(x=300, y=100)

        self.d_l3 = Label(self.lf2, text="70", font=('Courier', 14, 'bold'), bg='orange')
        self.d_l3.place(x=300, y=150)

        self.button = Button(self.lf2, text=" Generate Bill", font=('Algerian', 12, 'bold'), command=self.mBill)
        self.button2 = Button(self.lf2, text=" Back", font=('Algerian', 12, 'bold'), command=self.back)
        self.button3 = Button(self.lf2, text="Reset", font=('Algerian', 12, 'bold'), command=self.reset)
        self.button3.place(x=220, y=400)
        self.button.place(x=20, y=400)
        self.button2.place(x=320, y=400)

    def logout(self):
        root1 = Toplevel()
        root1.title("MyProject")
        root1.wm_geometry("800x700")
        page1 = MyProject(root1)

    def reset(self):
        self.v1.set(0)
        self.v2.set(0)
        self.v3.set(0)
        self.v4.set(0)
        self.v5.set(0)
        self.sv1.set(0)
        self.sv2.set(0)
        self.sv3.set(0)
        self.sv4.set(0)
        self.sv5.set(0)
        self.vd1.set(0)
        self.vd2.set(0)
        self.vd3.set(0)
        self.vd4.set(0)
        self.svd1.set(0)
        self.svd2.set(0)
        self.svd3.set(0)
        self.svd4.set(0)
        self.vd_1.set(0)
        self.vd_2.set(0)
        self.vd_3.set(0)
        self.svd_1.set(0)
        self.svd_2.set(0)
        self.svd_3.set(0)
        self.t1.config(state='normal')
        self.t1.delete('1.0', END)
        self.t1.config(state='disabled')

    def back(self):
        self.m.destroy()

    def mBill(self):
        root4 = Toplevel()
        root4.title("BILL")
        root4.wm_geometry("600x600")
        gst = price = 0.0
        rec = dict()
        c = 1
        subp = 0.0
        plist = [500, 350, 370, 250, 950, 35, 25, 25, 35, 50, 60, 70]
        if (self.v1.get() == 1):
            item = str(self.c1.cget("text"))
            qty = int(self.sv1.get())
            price = qty * plist[0]
            rec[c] = [item, qty, price]
            subp += price
            c += 1

        if (self.v2.get() == 1):
            item = str(self.c2.cget("text"))
            qty = int(self.sv2.get())
            price = qty * plist[1]
            rec[c] = [item, qty, price]
            subp += price
            c += 1

        if (self.v3.get() == 1):
            item = str(self.c3.cget("text"))
            qty = int(self.sv3.get())
            price = qty * plist[2]
            rec[c] = [item, qty, price]
            subp += price
            c += 1

        if (self.v4.get() == 1):
            item = str(self.c4.cget("text"))
            qty = int(self.sv4.get())
            price = qty * plist[3]
            rec[c] = [item, qty, price]
            subp += price
            c += 1

        if (self.v5.get() == 1):
            item = str(self.c5.cget("text"))
            qty = int(self.sv5.get())
            price = qty * plist[4]
            rec[c] = [item, qty, price]
            subp += price
            c += 1

        if (self.vd1.get() == 1):
            item = str(self.cd1.cget("text"))
            qty = int(self.svd1.get())
            price = qty * plist[5]
            rec[c] = [item, qty, price]
            subp += price
            c += 1
        if (self.vd2.get() == 1):
            item = str(self.cd2.cget("text"))
            qty = int(self.svd2.get())
            price = qty * plist[6]
            rec[c] = [item, qty, price]
            subp += price
            c += 1

        if (self.vd3.get() == 1):
            item = str(self.cd3.cget("text"))
            qty = int(self.svd3.get())
            price = qty * plist[7]
            rec[c] = [item, qty, price]
            subp += price
            c += 1

        if (self.vd4.get() == 1):
            item = str(self.cd4.cget("text"))
            qty = int(self.svd4.get())
            price = qty * plist[8]
            rec[c] = [item, qty, price]
            subp += price
            c += 1

        if (self.vd_1.get() == 1):
            item = str(self.cd_1.cget("text"))
            qty = int(self.svd_1.get())
            price = qty * plist[9]
            rec[c] = [item, qty, price]
            subp += price
            c += 1

        if (self.vd_2.get() == 1):
            item = str(self.cd_2.cget("text"))
            qty = int(self.svd_2.get())
            price = qty * plist[10]
            rec[c] = [item, qty, price]
            subp += price
            c += 1

        if (self.vd_3.get() == 1):
            item = str(self.cd_3.cget("text"))
            qty = int(self.svd_3.get())
            price = qty * plist[11]
            rec[c] = [item, qty, price]
            subp += price
            c += 1

        gst += 0.18 * subp
        rec[c] = gst
        totalprice = gst + subp
        lb = CalculateBill(root4, self.sup, totalprice, rec, self.id)

        self.b2 = Button(self.frame1, text="LOG OUT", font=('Algerian', 15), command=self.logout)
        self.b2.place(x=600, y=0)

    def logout(self):
        root1 = Toplevel()
        root1.title("MyProject")
        root1.wm_geometry("800x700")
        page1 = MyProject(root1)


class CalculateBill():
    def __init__(self, master, sup, n, rec1, id):
        # add image variables next to master up here
        self.m = master
        self.sup = sup
        self.id = id
        self.frame1 = Frame(master, background='orange', bd=14, relief=RIDGE)
        self.frame1.pack(side=TOP, fill=BOTH, expand='true')

        self.logo1 = PhotoImage(file='sidelogo.png')
        self.label00 = Label(self.frame1, image=self.logo1)
        self.label00.place(x=1, y=1)

        self.label0 = Label(self.frame1, text='INVOICE', font=('Courier', 40, 'bold'), bg='orange', anchor=CENTER)
        self.label0.place(x=150, y=20)

        self.t1 = Text(self.frame1, width=50, height=20, bg='lightblue', font='serif', bd=7)
        self.t1.place(x=60, y=125)

        self.t1.insert(END, " \t\t     Lock-A-Buy\n")
        self.t1.insert(END, "\t\tMay the store be with you \n")
        self.t1.insert(END, "\t\tGet before you blink\n\n")
        self.button = Button(self.frame1, text=" Submit", font=('Algerian', 12, 'bold'), command=self.submit)
        self.button2 = Button(self.frame1, text=" Back", font=('Algerian', 12, 'bold'), command=self.back)
        self.button.place(x=150, y=500)
        self.button2.place(x=350, y=500)
        self.num = self.sup
        self.tp = n
        today = date.today().strftime('%d-%m-%Y')
        dict = {1: "\tSPENCERS", 2: "\tEasyDay", 3: "\tBIG BAZAR", 4: "\tFAMILY MART", 5: "\tPAPPU STORE"}
        self.t1.insert(END, str(dict[self.num]))
        self.t1.insert(END, "\n\n        ")
        self.t1.insert(END, str(today))
        self.t1.insert(END, "\n\n")
        tgst = rec1.popitem()
        y, z = tgst
        self.t1.insert(END, "S.No.\t Item\t  \t Quantity\t\tPrice\n\n")
        for k, v in rec1.items():
            self.t1.insert(END, str(k))
            self.t1.insert(END, "\t")
            self.t1.insert(END, str(v[0]))
            self.t1.insert(END, "\t\t")
            self.t1.insert(END, str(v[1]))
            self.t1.insert(END, "\t\t")
            self.t1.insert(END, str(v[2]))
            self.t1.insert(END, "\n")

        self.t1.insert(END, "\n\n\tGST:   Rs.")
        self.t1.insert(END, str(round(z, 1)))
        self.t1.insert(END, "\n\n\tTotal amount:    Rs.")
        self.t1.insert(END, str(round(self.tp, 0)))

        # end the text box
        self.t1.config(state="disabled")

        btext = ""
        for k, v in rec1.items():
            stext = str(v[0]) + " X " + str(v[1]) + " - "
            btext += stext

        ta = str(round(self.tp, 0))

        sp = str(dict[self.num]).strip()

        # saving into database
        conn = sqlite3.connect('user_details.db')

        cursor = conn.execute(
            "select user_id, name, usercon_no, user_add, user_email from userdata where user_id=" + str(self.id))
        user = []

        for i in cursor.fetchone():
            user.append(i)

        conn.execute("insert into billdata values(?,?,?,?,?,?,?,?)",
                     (user[0], user[1], user[2], user[3], user[4], sp, btext, ta))
        conn.commit()

    def submit(self):
        # condition to check if total amount>0
        # if the amount >0 then following code
        ans = messagebox.askyesno(parent=self.m, message="Do you want to submit?", title="Confirmation")
        if ans > 0:
            # maybe save the amount in database
            messagebox.showinfo(parent=self.m, message="Order successfully placed ", title="Congratulation!!")
            self.back()

    def back(self):
        self.m.destroy()


root = Tk()
root.title("LOCK-A-BUY")
root.wm_geometry("900x625")
myProject = MyProject(root)
root.mainloop()