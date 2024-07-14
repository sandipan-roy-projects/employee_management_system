import mysql.connector as local
add_data=local.connect(host="localhost",user="root",password="235689",database="project")
save_data=add_data.cursor()
save_data.execute("create table employee(Emp_Id varchar(100) not null,password varchar(20) not null,department varchar(50) not null,name varchar(100) not null,designation varchar(20) not null,Email varchar(100) not null,address varchar(200) not null,marital_status varchar(20) not null,DOB varchar(20) not null,DOJ varchar(20) not null,ID_type varchar(50) not null,ID_proof varchar(50) not null,gender varchar(10) not null,Phone_No varchar(10) not null,country varchar(50) not null,salary varchar(100) not null,constraint pk_employee PRIMARY KEY(Emp_Id))")
save_data.execute("alter table employee add UNIQUE(ID_proof)")
save_data.execute("alter table employee add UNIQUE(Phone_No)")
add_data.commit()