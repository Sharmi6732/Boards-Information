from tkinter import *
from tkinter import messagebox
import sqlite3

root=Tk()
root.title("Login")
root.geometry('340x200')

UserName=StringVar()
Password=StringVar()
label_A = Label(root, text="UserName",width=20,font=("bold", 10))
label_A.place(x=0,y=30)

entry_A = Entry(root,textvar=UserName)
entry_A.place(x=120,y=30)

label_B = Label(root, text="Password",width=20,font=("bold", 10))
label_B.place(x=0,y=80)

entry_B = Entry(root,textvar=Password)
entry_B.place(x=120,y=80)


def login():

    window = Toplevel()
    window.geometry('1000x700')


    window.title("All India Senior School Certificate Examination Registration Form")

    Student_Name=StringVar()
    Student_ID=StringVar()
    Date_of_Birth=StringVar()
    c=StringVar()
    d=StringVar()
    var=IntVar()
    School_Name=StringVar()
    City=StringVar()
    Father_Name=StringVar()
    Mother_Name=StringVar()
    Residential_Address=StringVar()
    Mobile_Number=StringVar()
    State=StringVar()
    Physical_Disability=StringVar()
    e=StringVar()
    Stream=StringVar()

    var1=IntVar
    var2= IntVar()
    var3= IntVar()
    var4= IntVar()


    def database():
        name1=Student_Name.get()
        StudentID=Student_ID.get()
        DateofBirth1=Date_of_Birth.get()
        Gender1=var.get()
        Board1=d.get()
        Caste1=var1.get()
        SchoolName=School_Name.get()
        City1=City.get()
        Father_Name1=Father_Name.get()
        Mother_Name1=Mother_Name.get()
        Residential_Address1=Residential_Address.get()
        Mobile_Number1=Mobile_Number.get()
        State1=State.get()
        Physical_Disability1=Physical_Disability.get()
        Stream1=e.get()
        conn=sqlite3.connect("Form1.db")
        with conn:
            cursor=conn.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS Student(Student_Name TEXT,Student_ID TEXT,Date_of_Birth TEXT,Gender TEXT,Board TEXT,Caste TEXT,School_Name TEXT,City TEXT,Father_Name TEXT,Mother_Name TEXT,Residential_Address TEXT,Mobile_Number TEXT,State TEXT,Physical_Disability TEXT,Stream TEXT)')
        cursor.execute('INSERT INTO Student (Student_Name,Student_ID,Date_of_Birth,Gender,Board,Caste,School_Name,City,Father_Name,Mother_Name,Residential_Address,Mobile_Number,State,Physical_Disability,Stream) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',(name1,StudentID,DateofBirth1,Gender1,Board1,Caste1,SchoolName,City1,Father_Name1,Mother_Name1,Residential_Address1,Mobile_Number1,State1,Physical_Disability1,Stream1))
        conn.commit()
        messagebox.showinfo("","The data have been successfully imported")
    

    label_0 = Label(window, text="All India Senior School Certificate Examination(AISSCE)\nRegistration Form",width=50,font=("bold", 15))
    label_0.place(x=240,y=53)


    label_1 = Label(window, text="Student_Name",width=20,font=("bold", 10))
    label_1.place(x=30,y=130)

    entry_1 = Entry(window,textvar=Student_Name)
    entry_1.place(x=300,y=130)

    label_2 = Label(window, text="Student_ID",width=17,font=("bold", 10))
    label_2.place(x=30,y=180)

    entry_2 = Entry(window,textvar=Student_ID)
    entry_2.place(x=300,y=180)

    label_3 = Label(window, text="Date_of_Birth",width=17,font=("bold", 10))
    label_3.place(x=35,y=230)

    entry_3 = Entry(window,textvar=Date_of_Birth)
    entry_3.place(x=300,y=230)


    label_4 = Label(window, text="Gender",width=14,font=("bold", 10))
    label_4.place(x=30,y=280)
    var = IntVar()
    Radiobutton(window, text="Male",padx = 5, variable=var, value=1).place(x=220,y=280)
    Radiobutton(window, text="Female",padx = 20, variable=var, value=2).place(x=280,y=280)
    Radiobutton(window, text="Others",padx = 35, variable=var, value=3).place(x=360,y=280)


    label_6 = Label(window, text="Caste",width=13,font=("bold", 10))
    label_6.place(x=30,y=330)
    var1 = IntVar()
    Checkbutton(window, text="SC", variable=var1).place(x=240,y=330)
    var2 = IntVar()
    Checkbutton(window, text="ST", variable=var2).place(x=290,y=330)
    var3 = IntVar()
    Checkbutton(window, text="OBC", variable=var3).place(x=340,y=330)
    var4 = IntVar()
    Checkbutton(window, text="General", variable=var4).place(x=410,y=330)

    label_7 = Label(window, text="School_Name",width=18,font=("bold", 10))
    label_7.place(x=30,y=380)

    entry_7 = Entry(window,textvar=School_Name)
    entry_7.place(x=300,y=380)


    label_8 = Label(window, text="Board",width=13,font=("bold", 10))
    label_8.place(x=30,y=430)


    list2 = ['CBSE','ICSE','SSC','IB'];
    d=StringVar()
    droplist=OptionMenu(window,d, *list2)
    droplist.config(width=15)
    d.set('Select Your Board') 
    droplist.place(x=290,y=425)

    label_9 = Label(window, text="City",width=12,font=("bold", 10))
    label_9.place(x=30,y=480)

    entry_9 = Entry(window,textvar=City)
    entry_9.place(x=300,y=480)


    label_10 = Label(window, text="Father_Name",width=20,font=("bold", 10))
    label_10.place(x=500,y=130)

    entry_10 = Entry(window,textvar=Father_Name)
    entry_10.place(x=700,y=130)

    label_11 = Label(window, text="Mother_Name",width=20,font=("bold", 10))
    label_11.place(x=500,y=180)

    entry_11 = Entry(window,textvar=Mother_Name)
    entry_11.place(x=700,y=180)

    label_12 = Label(window, text="Residential_Address",width=20,font=("bold", 10))
    label_12.place(x=500,y=230)

    entry_12 = Entry(window,textvar=Residential_Address)
    entry_12.place(x=700,y=230)

    label_13 = Label(window, text="Mobile_Number",width=20,font=("bold", 10))
    label_13.place(x=500,y=280)

    entry_13 = Entry(window,textvar=Mobile_Number)
    entry_13.place(x=700,y=280)

    label_14 = Label(window, text="State",width=20,font=("bold", 10))
    label_14.place(x=500,y=330)

    entry_14 = Entry(window,textvar=State)
    entry_14.place(x=700,y=330)

    label_15 = Label(window, text="Physical_Disability",width=20,font=("bold", 10))
    label_15.place(x=500,y=380)

    entry_15 = Entry(window,textvar=Physical_Disability)
    entry_15.place(x=700,y=380)



    label_16 = Label(window, text="Stream",width=20,font=("bold", 10))
    label_16.place(x=500,y=432)

    list4 = ['Computer Science','Bio-Science','Commerce','Arts'];
    e=StringVar()
    droplist=OptionMenu(window,e, *list4)
    droplist.config(width=20)
    e.set('Select_Your_Stream') 
    droplist.place(x=700,y=430)

    Button(window, text='Submit',width=30,bg='brown',fg='white',command=database).place(x=420,y=530)


def on_button():
    if entry_A.get() == "admin" and entry_B.get()=="secret":
        login()
        messagebox.showinfo("","Logged In Successfully! ")
    elif entry_A.get() != "admin" or entry_B.get()!="secret":
        messagebox.showerror("Alert!","Unsuccessful Login")
        
button01 = Button(root, text="Submit",width=30,bg='brown',fg='white', command=on_button).place(x=70,y=150)

root.mainloop()
