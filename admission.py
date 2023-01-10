import mysql.connector as m
mydatabase=m.connect(host="localhost",user="root",password="root",database="admission")


def addstudent():
    n=input("enter the first name: ")
    l=input("enter the  last name: ")
    dept=input("enter the department: ")
    co=int(input("enter the contact number: "))
    data1=(n,l,dept,co)

    query1=("insert into student(firstname,lastname,dept,contact_no) values(%s,%s,%s,%s)")

    x=mydatabase.cursor()
    x.execute(query1,data1)
    #x.execute(query2,data2)

    mydatabase.commit()


    print("data entered successfully ")
    print(" ")
    start()
def deletestudent():
   a=int(input("enter the student id: "))
   #ac=int(input("enter the account number :"))
   data=(a,)
   q="delete from student where id_no=%s"
   x=mydatabase.cursor()
   x.execute(q,data)
   #result=x.fetchone()


   #mydatabase.commit()
   print("data is modified ")
   start()


def updatestudent():
   a=input("enter the department: ")
   ac=int(input("enter the id_no:"))
   data=(a,ac)
   x = mydatabase.cursor()

   sql=("update student set dept=%s where id_no=%s")

   x.execute(sql,data)
   mydatabase.commit()
   print("modification is done")
   start()

def showstudent():

    x=mydatabase.cursor()
    query = "select * from student"

    x.execute(query)
    result = x.fetchall()  # here we get tuples equivalent to the number of records
    for record in result:
        print(record)
    print(" ")
    start()

def start():
    print("   1.Add Student\n "
          "  2.delete student\n"
          "   3.update student\n"
          "   4.show student\n"
          "   5.exit")

    choose=int(input("enter the choice: "))
    if (choose==1):
         addstudent()
    elif (choose==2):
         deletestudent()
    elif (choose==3):
         updatestudent()
    elif (choose==4):
         showstudent()
    elif (choose==5):
         exit()
    else:
        print("invald choice")
start()