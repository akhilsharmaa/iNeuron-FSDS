import mysql.connector as connection

mydb = connection.connect(host = "localhost", user= "root", passwd= "akhilsharmaa");
courser = mydb.cursor();

# courser.execute("create table akhilesh.ineoron(emp_id int(10) , emp_name varchar(80) , emp_mailid varchar(20) , emp_salary int(6)) ");

# courser.execute('''insert into akhilesh.ineoron values ( 1 ,  "Akhil" , "akhilesh@gmail" , 60020)''')
# mydb.commit()

courser.execute("select * from akhilesh.ineoron");

# print(courser.fetchall())
l = [];

for i in courser.fetchall() : 
    l.append(i);

for i in l : 
    print(i[1])


# courser.commit()

# print(courser.fetchall())