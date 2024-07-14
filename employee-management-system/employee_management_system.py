from tkinter import *
from tkinter import ttk
import mysql.connector as local
from tkinter.messagebox import showinfo
from tkinter import messagebox
from tkcalendar import *;
from PIL import ImageTk, Image
import random
import re

class Employee:

    def __init__(self,root):
        self.add_data=local.connect(host="localhost",user="root",password="235689",database="project")
        self.save_data=self.add_data.cursor()
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Employee Management System")
        self.is_on=True
        self.on = PhotoImage(file = "on.png")
        self.off = PhotoImage(file = "off.png")
        lbl_title=Label(self.root,text="ZOGNITO PVT. LTD.",font=('times new roman',37,'bold'),fg='darkblue',bg='white')
        lbl_title.place(x=0,y=0,width=1530,height=50)

        #image frame

        img_frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        img_frame.place(x=0,y=50,width=1530,height=180)
        
        self.image1=Image.open("Leave-Management-System-Desktop-Banner.jpg")
        self.r_image=self.image1.resize((300,170))
        test = ImageTk.PhotoImage(self.r_image)
        label1 =Label(img_frame,image=test)
        label1.image = test
        label1.place(x=950, y=2)

        self.image2=Image.open("employee-engagement (1) (1).png")
        self.r_image1=self.image2.resize((400,170))
        test1 = ImageTk.PhotoImage(self.r_image1)
        label2 =Label(img_frame,image=test1)
        label2.image = test1
        label2.place(x=550, y=2)
        
        self.image3=Image.open("Employee Engagement 0811-1200x675.png")
        self.r_image2=self.image3.resize((300,170))
        test2 = ImageTk.PhotoImage(self.r_image2)
        label3 =Label(img_frame,image=test2)
        label3.image = test2
        label3.place(x=245, y=2)


        #Main Frame

        Main_Frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        Main_Frame.place(x=0,y=230,height=560,width=1530)

        #Upper Frame
               
        Up_Frame=LabelFrame(Main_Frame,bd=2,relief=RIDGE,bg='white',fg='red',text="Employee Details",font=('times new roman',11,'bold'))
        Up_Frame.place(x=5,y=5,height=260,width=1520)

        #Labels and Entries

        self.var_empId=StringVar()
        self.var_dep=StringVar()
        self.var_desig=StringVar()
        self.var_add=StringVar()
        self.var_dob=StringVar()
        self.var_idtype=StringVar()
        self.var_id=StringVar()
        self.var_name=StringVar()
        self.var_email=StringVar()
        self.var_married=StringVar()
        self.var_doj=StringVar()
        self.var_gender=StringVar()
        self.var_phone=StringVar()
        self.var_country=StringVar()
        self.var_salary=StringVar()
        self.var_search=StringVar()
        self.var_value=StringVar()

        lb_empId=Label(Up_Frame,text="Emp_Id",font=('times new roman',11,'bold'),bg='white')
        lb_empId.grid(row=0,column=0,padx=10,pady=10,sticky=W)
        self.en_empId=ttk.Entry(Up_Frame,textvariable=self.var_empId,state=DISABLED,width=22,font=('times new roman',11,'bold'))
        self.en_empId.grid(row=0,column=1,padx=30,pady=10)
        lb_togglebutton=Label(Up_Frame,text="Edit details",font=('times new roman',11,'bold'),bg='white')
        lb_togglebutton.grid(row=0,column=4,padx=30,pady=5)
        
        self.togg_button = Button(Up_Frame, image = self.on, bd = 0,command=self.switch)
        self.togg_button.grid(row=0,column=5)
        lb_dep=Label(Up_Frame,text='Department',font=('times new roman',11,'bold'),bg='white')
        lb_dep.grid(row=1,column=0,padx=10,pady=5,sticky=W)
        self.combo_dep=ttk.Combobox(Up_Frame,textvariable=self.var_dep,font=('times new roman',11,'bold'),width=20,state='readonly')
        self.combo_dep['value']=('Select Department','HR','Software Engineer','CEO','Manager')
        self.combo_dep.current(0)
        self.combo_dep.grid(row=1,column=1,padx=30,pady=5,sticky=W)
        lb_desig=Label(Up_Frame,text='Designation',font=('times new roman',11,'bold'),bg='white')
        lb_desig.grid(row=2,column=0,padx=10,pady=5,sticky=W)
        self.en_desig=ttk.Entry(Up_Frame,textvariable=self.var_desig,width=22,font=('times new roman',11,'bold'))
        self.en_desig.grid(row=2,column=1,padx=30,pady=5)
        lb_add=Label(Up_Frame,text='Address',font=('times new roman',11,'bold'),bg='white')
        lb_add.grid(row=3,column=0,padx=10,pady=5,sticky=W)
        self.en_add=ttk.Entry(Up_Frame,textvariable=self.var_add,width=22,font=('times new roman',11,'bold'))
        self.en_add.grid(row=3,column=1,padx=30,pady=5)
        lb_dob=Label(Up_Frame,text='DOB',font=('times new roman',11,'bold'),bg='white')
        lb_dob.grid(row=4,column=0,padx=10,pady=5,sticky=W)
        self.en_dob=DateEntry(Up_Frame,textvariable=self.var_dob,width=20,font=('times new roman',11,'bold'),date_pattern="dd-mm-yyyy")
        self.en_dob.grid(row=4,column=1,padx=30,pady=5)
        self.combo_id=ttk.Combobox(Up_Frame,textvariable=self.var_idtype,font=('times new roman',11,'bold'),width=17,state='readonly')
        self.combo_id['value']=('Select ID Proof','Aadhar Card','Passport','Voter ID Card','Pan Card')
        self.combo_id.current(0)
        self.combo_id.grid(row=5,column=0,padx=10,pady=5,sticky=W)
        self.en_id=ttk.Entry(Up_Frame,textvariable=self.var_id,width=22,font=('times new roman',11,'bold'))
        self.en_id.grid(row=5,column=1,padx=30,pady=5)
        lb_name=Label(Up_Frame,text='Name',font=('times new roman',11,'bold'),bg='white')
        lb_name.grid(row=1,column=2,padx=30,pady=5,sticky=W)
        self.en_name=ttk.Entry(Up_Frame,textvariable=self.var_name,width=22,font=('times new roman',11,'bold'))
        self.en_name.grid(row=1,column=3,padx=30,pady=5)
        lb_email=Label(Up_Frame,text='Email',font=('times new roman',11,'bold'),bg='white')
        lb_email.grid(row=2,column=2,padx=30,pady=5,sticky=W)
        self.en_email=ttk.Entry(Up_Frame,textvariable=self.var_email,width=22,font=('times new roman',11,'bold'))
        self.en_email.grid(row=2,column=3,padx=30,pady=5)
        lb_married=Label(Up_Frame,text='Married Status',font=('times new roman',11,'bold'),bg='white')
        lb_married.grid(row=3,column=2,padx=30,pady=5)
        self.combo_married=ttk.Combobox(Up_Frame,textvariable=self.var_married,font=('times new roman',11,'bold'),width=20,state='readonly')
        self.combo_married['value']=('Select','Married','Unmarried')
        self.combo_married.current(0)
        self.combo_married.grid(row=3,column=3,padx=30,pady=5,sticky=W)
        lb_doj=Label(Up_Frame,text='Date of Joining',font=('times new roman',11,'bold'),bg='white')
        lb_doj.grid(row=4,column=2,padx=30,pady=5,sticky=W)
        self.en_doj=DateEntry(Up_Frame,textvariable=self.var_doj,width=20,font=('times new roman',11,'bold'),date_pattern="dd-mm-yyyy")
        self.en_doj.grid(row=4,column=3,padx=30,pady=5)
        lb_gender=Label(Up_Frame,text='Gender',font=('times new roman',11,'bold'),bg='white')
        lb_gender.grid(row=5,column=2,padx=30,pady=5,sticky=W)
        self.combo_gender=ttk.Combobox(Up_Frame,textvariable=self.var_gender,font=('times new roman',11,'bold'),width=20,state='readonly')
        self.combo_gender['value']=('Select','Male','Female','Others')
        self.combo_gender.current(0)
        self.combo_gender.grid(row=5,column=3,padx=30,pady=5,sticky=W)
        lb_phone=Label(Up_Frame,text='Phone No',font=('times new roman',11,'bold'),bg='white')
        lb_phone.grid(row=1,column=4,padx=30,pady=5,sticky=W)
        self.en_phone=ttk.Entry(Up_Frame,textvariable=self.var_phone,width=22,font=('times new roman',11,'bold'))
        self.en_phone.grid(row=1,column=5,padx=30,pady=5)
        lb_country=Label(Up_Frame,text='Country',font=('times new roman',11,'bold'),bg='white')
        lb_country.grid(row=2,column=4,padx=30,pady=5,sticky=W)
        self.en_country=ttk.Entry(Up_Frame,textvariable=self.var_country,width=22,font=('times new roman',11,'bold'))
        self.en_country.grid(row=2,column=5,padx=30,pady=5)
        lb_salary=Label(Up_Frame,text='Salary',font=('times new roman',11,'bold'),bg='white')
        lb_salary.grid(row=3,column=4,padx=30,pady=5,sticky=W)
        self.en_salary=ttk.Entry(Up_Frame,textvariable=self.var_salary,width=22,font=('times new roman',11,'bold'))
        self.en_salary.grid(row=3,column=5,padx=30,pady=5)

        #Button Frame

        button_frame=Frame(Up_Frame,bd=2,relief=RIDGE,bg='White')
        button_frame.place(x=1260,y=38,width=190,height=195)
        
        button_add=Button(button_frame,text="Save",font=('times new roman',14,'bold'),width=16,bg='blue',fg='white')
        button_add["command"]=self.add
        button_add.grid(row=0,column=0,padx=1,pady=5)
        button_update=Button(button_frame,text="Update",font=('times new roman',14,'bold'),width=16,bg='blue',fg='white')
        button_update["command"]=self.update
        button_update.grid(row=1,column=0,padx=1,pady=5)
        button_delete=Button(button_frame,text="Delete",font=('times new roman',14,'bold'),width=16,bg='blue',fg='white')
        button_delete["command"]=self.delete
        button_delete.grid(row=2,column=0,padx=1,pady=5)
        button_reset=Button(button_frame,text="Reset",font=('times new roman',14,'bold'),width=16,bg='blue',fg='white')
        button_reset["command"]=self.reset
        button_reset.grid(row=3,column=0,padx=1,pady=5)

        #Down Frame
               
        Down_Frame=LabelFrame(Main_Frame,bd=2,relief=RIDGE,bg='white',fg='red',text="Show Employee Details",font=('times new roman',11,'bold'))
        Down_Frame.place(x=5,y=265,height=290,width=1520)

        search_frame=LabelFrame(Down_Frame,bd=2,relief=RIDGE,bg='white',text="Search Employee Information",font=('times new roman',11,'bold'))
        search_frame.place(x=5,y=0,height=60,width=1510)

        search_lbl=Label(search_frame,text="Search by",font=('times new roman',11,'bold'),bg='red',fg='white')
        search_lbl.place(x=5,y=5,width=100,height=23)
        combo_search=ttk.Combobox(search_frame,textvariable=self.var_search,font=('times new roman',11,'bold'),width=17,state='readonly')
        combo_search['value']=('Select','Emp_Id','Phone No')
        combo_search.current(0)
        combo_search.place(x=150,y=5)
        entry_search=ttk.Entry(search_frame,textvariable= self.var_value,width=22,font=('times new roman',11,'bold'))
        entry_search.place(x=330,y=5,width=250,height=23)
        button_search=Button(search_frame,text="Search",font=('times new roman',11,'bold'),width=16,bg='blue',fg='white')
        button_search["command"]=self.search
        button_search.place(x=870,y=3)
        button_show=Button(search_frame,text="Show All",font=('times new roman',11,'bold'),width=16,bg='blue',fg='white')
        button_show["command"]=self.showAll
        button_show.place(x=1040,y=3)
    
        show_frame=LabelFrame(Down_Frame,bd=2,relief=RIDGE,bg='white',text="Show Employee Information",font=('times new roman',11,'bold'))
        show_frame.place(x=5,y=60,height=210,width=1510)
        scroll_x=ttk.Scrollbar(show_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(show_frame,orient=VERTICAL)
        self.table=ttk.Treeview(show_frame,column=("Emp_Id","Password","Dept.","Name","Desig","Email","Address","married","DOB","DOJ","ID Type","ID Proof","Gender","Phone","Country","salary","CL","ML"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.table.xview)
        scroll_y.config(command=self.table.yview)
        self.table.heading('Emp_Id',text='Emp_Id')
        self.table.heading('Password',text='Password')
        self.table.heading('Dept.',text='Department')
        self.table.heading('Name',text='Name')
        self.table.heading('Desig',text='Desigation')
        self.table.heading('Email',text='Email ID')
        self.table.heading('Address',text='Address')
        self.table.heading('married',text='Marriage status')
        self.table.heading('DOB',text='DOB')
        self.table.heading('DOJ',text='DOJ')
        self.table.heading('ID Type',text='ID Type')
        self.table.heading('ID Proof',text='ID Proof')
        self.table.heading('Gender',text='Gender')
        self.table.heading('Phone',text='Phone No.')
        self.table.heading('Country',text='Country')
        self.table.heading('salary',text='Salary')

        self.table['show']='headings'
        self.table.column("Emp_Id",width=200)
        self.table.column("Password",width=200)
        self.table.column("Dept.",width=200)
        self.table.column("Name",width=200)
        self.table.column("Desig",width=200)
        self.table.column("Email",width=200)
        self.table.column("Address",width=200)
        self.table.column("married",width=200)
        self.table.column("DOB",width=200)
        self.table.column("DOJ",width=200)
        self.table.column("ID Type",width=200)
        self.table.column("ID Proof",width=200)
        self.table.column("Gender",width=200)
        self.table.column("Phone",width=200)
        self.table.column("Country",width=200)
        self.table.column("salary",width=200)
        self.table.pack(fill=BOTH,expand=1) 
        self.table.bind("<ButtonRelease>",self.get_cursor)

    def enable(self):
        self.combo_dep.config(state="enabled")
        self.en_desig.config(state="enabled")
        self.en_add.config(state="enabled")
        self.en_dob.config(state="enabled")
        self.combo_id.config(state="enabled")
        self.en_id.config(state="enabled")
        self.en_name.config(state="enabled")
        self.en_email.config(state="enabled")
        self.combo_married.config(state="enabled")
        self.en_doj.config(state="enabled")
        self.combo_gender.config(state="enabled")
        self.en_phone.config(state="enabled")
        self.en_country.config(state="enabled")
        self.en_salary.config(state="enabled")

    def disable(self):
        self.combo_dep.config(state="disabled")
        self.en_desig.config(state="disabled")
        self.en_add.config(state="disabled")
        self.en_dob.config(state="disabled")
        self.combo_id.config(state="disabled")
        self.en_id.config(state="disabled")
        self.en_name.config(state="disabled")
        self.en_email.config(state="disabled")
        self.combo_married.config(state="disabled")
        self.en_doj.config(state="disabled")
        self.combo_gender.config(state="disabled")
        self.en_phone.config(state="disabled")
        self.en_country.config(state="disabled")
        self.en_salary.config(state="disabled")

    def switch(self):
        if self.is_on:
            self.togg_button.config(image = self.off)
            self.disable()
            self.is_on = False
        else:
            self.togg_button.config(image = self.on)
            self.enable()
            self.is_on = True

    #sava data function

    def add(self):
        try:
            l=[]
            n=self.var_name.get()
            no=str(random.random())
            self.user_id=n[:2]+n[-2:]+no[2:6]
            l.append(self.user_id)
            passwd=int((random.random())*(int(self.var_phone.get())))
            l.append(passwd)
            dept=self.var_dep.get()
            l.append(dept)
            name=self.var_name.get()
            l.append(name)
            desig=self.var_desig.get()
            l.append(desig)
            email=self.var_email.get()
            l.append(email)
            address=self.var_add.get()
            l.append(address)
            married=self.var_married.get()
            l.append(married)
            dob=self.var_dob.get()
            l.append(dob)
            doj=self.var_doj.get()
            l.append(doj)
            id_type=self.var_idtype.get()
            l.append(id_type)
            id=self.var_id.get()
            l.append(id)
            gender=self.var_gender.get()
            l.append(gender)
            phone=self.var_phone.get()
            l.append(phone)
            country=self.var_country.get()
            l.append(country)
            salary=self.var_salary.get()
            l.append(salary)
            t=tuple(l)
            pattern_email=r"[\w.-]+@[\w.-]+"
            match=re.search(pattern_email,email)
            if((id_type=="Select ID Proof")or(dept=="Select Department")or(name=="")or(desig=="")or(address=="")or(id=="")or(married=="Select")or(gender=="Select")or(country=="")or(salary=="")):
                messagebox.showerror('Error',"All fields required")
            elif(id_type=="Aadhar Card"):
                pattern_id=r"\d{12}"
                match_adhar=re.search(pattern_id,id)
                if(match_adhar):
                    if(len(self.var_phone.get())==10):
                        if (match):
                            query="insert into employee(Emp_Id,password,department,name,designation,Email,address,marital_status,DOB,DOJ,ID_type,ID_proof,gender,Phone_No,country,salary) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                            self.save_data.execute(query,t)
                            showinfo(title="Login Credentials",message="Employee ID: "+self.user_id+"  Employee's password is "+str(passwd))
                            self.add_data.commit()
                            self.togg_button.config(image = self.off)
                            self.is_on=False
                            self.disable()
                            self.var_empId.set(self.user_id)
                        else:
                            messagebox.showerror('Error',"Please give email ID properly")
                    else:
                        messagebox.showerror('Error',"Invalid Phone No")
                else:
                    messagebox.showerror('Error',"Invalid ID Proof No")
            else:
                pattern_id1=r"[A-Z]+[0-9]+"
                match_others=re.search(pattern_id1,id)
                if(match_others):
                    if(len(self.var_phone.get())==10):
                        if (match):
                            query="insert into employee(Emp_Id,password,department,name,designation,Email,address,marital_status,DOB,DOJ,ID_type,ID_proof,gender,Phone_No,country,salary) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                            self.save_data.execute(query,t)
                            showinfo(title="Login Credentials",message="Employee ID: "+self.user_id+"  Employee's password is "+str(passwd))
                            self.add_data.commit()
                            self.togg_button.config(image = self.off)
                            self.is_on=False
                            self.disable()      
                            self.var_empId.set(self.user_id)
                        else:
                            messagebox.showerror('Error',"Please give email ID properly")
                    else:
                        messagebox.showerror('Error',"Invalid Phone No")
                else:
                    messagebox.showerror('Error',"Invalid ID Proof No")
        except Exception as es:
            messagebox.showerror("Error",f'Due to:{str(es)}',parent=self.root)
            
    #update function

    def update(self):
        if self.var_empId.get()=="":
            messagebox.showerror('Error',"All Fields are required")
        else:
            try:
                up=messagebox.askyesno('Update','Are you sure to update this employee details?')
                if(up>0):
                    self.save_data.execute('update employee set department=%s,name=%s,designation=%s,Email=%s,address=%s,ID_proof=%s,marital_status=%s,DOB=%s,DOJ=%s,ID_type=%s,gender=%s,Phone_No=%s,country=%s,salary=%s where Emp_Id=%s',(self.var_dep.get(),self.var_name.get(),self.var_desig.get(),self.var_email.get(),self.var_add.get(),self.var_id.get(),self.var_married.get(),self.var_dob.get(),self.var_doj.get(),self.var_idtype.get(),self.var_gender.get(),self.var_phone.get(),self.var_country.get(),self.var_salary.get(),self.var_empId.get()))
                    self.add_data.commit()
                    showinfo(title="Confirmation",message="Employee's data has been successfully updated")
                else:
                    if not up:
                        return
            except Exception as es:
                messagebox.showerror("Error",f'Due to:{str(es)}',parent=self.root)

    #Delete function

    def delete(self):
        if self.var_empId.get()=="":
            messagebox.showerror('Error',"All Fields are required")
        else:
            try:
                delt=messagebox.askyesno('Delete','Are you sure to delete this employee details?')
                if(delt>0):
                    self.save_data.execute('delete from employee where Emp_Id=%s',(self.var_empId.get(),))
                    self.add_data.commit()
                    showinfo(title="Confirmation",message="Employee's data has been successfully Deleted")
                    self.reset()
                    self.showAll()
                else:
                    if not delt:
                        return
            except Exception as es:
                messagebox.showerror("Error",f'Due to:{str(es)}',parent=self.root)

    #reset function

    def reset(self):
        self.var_empId.set("")
        self.var_dep.set("Select Department")
        self.var_name.set("")
        self.var_desig.set("")
        self.var_email.set("")
        self.var_add.set("")
        self.var_married.set("Select")
        self.var_dob.set("")
        self.var_doj.set("")
        self.var_idtype.set("Select ID Proof")
        self.var_id.set("")
        self.var_gender.set("Select")
        self.var_phone.set("")
        self.var_country.set("")
        self.var_salary.set("")

    #search function

    def search(self):
        try:
            search=self.var_search.get()
            value=self.var_value.get()
            if(search=="Emp_Id"):
                self.save_data.execute('select * from employee where Emp_Id=%s',(value,))
            elif(search=="Phone No"):
                self.save_data.execute('select * from employee where Phone_No=%s',(value,))
            data=self.save_data.fetchall()
            if((len(data)==0)and(value!="")):
                messagebox.showerror("Error","Credentials not matched")
            elif((len(data)==0)and(value=="")):
                messagebox.showerror("Error","Please enter details")
            else:
                self.table.delete(*self.table.get_children())
                for i in data:
                    self.table.insert("",END,values=i)
                self.add_data.commit()
        except Exception as es:
            messagebox.showerror("Error",f'Due to:{str(es)}',parent=self.root)

    #showall function

    def showAll(self):
        self.save_data.execute("select * from employee")
        details=self.save_data.fetchall()
        self.table.delete(*self.table.get_children())
        for i in details:
            self.table.insert("",END,values=i)
        self.add_data.commit()

    def get_cursor(self,event=""):
        cursor_row=self.table.focus()
        content=self.table.item(cursor_row)
        data=content['values']
        self.var_empId.set(data[0])
        self.var_dep.set(data[2])
        self.var_name.set(data[3])
        self.var_desig.set(data[4])
        self.var_email.set(data[5])
        self.var_add.set(data[6])
        self.var_married.set(data[7])
        self.var_dob.set(data[8])
        self.var_doj.set(data[9])
        self.var_idtype.set(data[10])
        self.var_id.set(data[11])
        self.var_gender.set(data[12])
        self.var_phone.set(data[13])
        self.var_country.set(data[14])
        self.var_salary.set(data[15])
        self.disable()
        self.togg_button.config(image = self.off)
        self.is_on=False

if __name__ == "__main__":
    root=Tk()
    obj=Employee(root)
    root.mainloop()