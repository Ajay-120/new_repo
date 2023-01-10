import mysql.connector as m
mydatabase=m.connect(host="localhost",user="root",password="root",database="Bank")


def openacc():
    n=input("enter the name: ")
    op=int(input("enter the opening balance: "))
    co=int(input("enter the contact number: "))
    data1=(n,op,co)
    data2=(n,op)
    query1=("insert into accounts(name,balance,contact_no) values(%s,%s,%s)")
    query2=("insert into amounts(name,balance) values(%s,%s)")
    x=mydatabase.cursor()
    x.execute(query1,data1)
    x.execute(query2,data2)

    mydatabase.commit()
    query = "select acc_no from accounts where contact_no=%s"
    s=(co,)
    x.execute(query,s)
    result = x.fetchone()  # here we get tuples equivalent to the number of records
    for record in result:
        print("your account no ",record)

    print("data entered successfully ")
    print(" ")
    start()
def deposit():
   a=int(input("enter the amount you want to deposit: "))
   ac=int(input("enter the account number :"))
   data=(ac,)
   q="select balance from amounts where acc_no=%s"
   x=mydatabase.cursor()
   x.execute(q,data)
   result=x.fetchone()

   t=result[0]+a
   sql=("update amounts set balance=%s where acc_no=%s")
   d=(t,ac)
   x.execute(sql,d)
   mydatabase.commit()
   print(" ")
   start()


def withdraw():
   a=int(input("enter the amount you want to withdraw: "))
   ac=int(input("enter the account number :"))
   data=(ac,)
   q="select balance from amounts where acc_no=%s"
   x=mydatabase.cursor()
   x.execute(q,data)
   result=x.fetchone()

   t=result[0]-a
   if t<0:
       print("exceeded withdrawal amount!!!!!!! "
             " your current balance is ",result[0])
       start()
   sql=("update amounts set balance=%s where acc_no=%s")
   d=(t,ac)
   x.execute(sql,d)
   mydatabase.commit()
   print(" ")
   start()

def showbalance():
    co=int(input("enter the account no: "))
    x=mydatabase.cursor()
    query = "select balance from amounts where acc_no=%s"
    s = (co,)
    x.execute(query, s)
    result = x.fetchone()  # here we get tuples equivalent to the number of records
    for record in result:
        print("your  current balance  is ", record)
    print(" ")
    start()

def start():
    print("   1.open new account\n "
          "  2.deposit money\n"
          "   3.withdraw money\n"
          "   4.show balance\n"
          "   5.exit")

    choose=int(input("enter the choice: "))
    if (choose==1):
         openacc()
    elif (choose==2):
         deposit()
    elif (choose==3):
         withdraw()
    elif (choose==4):
         showbalance()
    elif (choose==5):
         exit()
    else:
        print("invald choice")
start()