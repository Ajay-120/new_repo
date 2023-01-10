import mysql.connector as m
mydatabase=m.connect(host="localhost",user="root",password="root",database="mybank")


def openacc():
    n=input("enter the name: ")
    op=int(input("enter the opening balance: "))
    co=int(input("enter the contact number: "))
    data1=(n,op,co)
    data2=(n,op)
    query1=("insert into account(name,balance,contact_no) values(%s,%s,%s)")
    query2=("insert into amount(name,balance) values(%s,%s)")
    x=mydatabase.cursor()
    x.execute(query1,data1)
    x.execute(query2,data2)

    mydatabase.commit()
    query = "select acc_no from account where contact_no=%s"
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
   n=input("bankholder name: ")
   data=(ac,)
   q="select balance from account where acc_no=%s"
   x = mydatabase.cursor()
   x.execute(q, data)
   result = x.fetchone()
   """s="select name from account where acc_no=%s"
   x.execute(s,data)
   re=x.fetchone()"""

   t=result[0]+a

   sql=("update account set balance=%s where acc_no=%s")
   d=(t,ac)
   x.execute(sql,d)
   sq=("insert into tranc_acc(name,balance,acc_no) values(%s,%s,%s)")
   m=(n,t,ac)
   x.execute(sq,m)
   mydatabase.commit()
   print(" ")
   start()


def withdraw():
   a=int(input("enter the amount you want to withdraw: "))
   ac=int(input("enter the account number :"))
   n=input("bankholder name: ")
   data=(ac,)
   q="select balance from account where acc_no=%s"
   x=mydatabase.cursor()
   x.execute(q,data)
   result=x.fetchone()

   t=result[0]-a
   if t<0:
       print("exceeded withdrawal amount!!!!!!! "
             " your current balance is ",result[0])
       start()
   sql=("update account set balance=%s where acc_no=%s")
   d=(t,ac)
   x.execute(sql,d)
   sq = ("insert into tranc_acc(name,balance,acc_no) values(%s,%s,%s)")
   m = (n, t, ac)
   x.execute(sq, m)
   mydatabase.commit()
   print(" ")
   start()

def showbalance():
    co=int(input("enter the account no: "))
    x=mydatabase.cursor()
    query = "select * from tranc_acc where acc_no=%s"
    s = (co,)
    x.execute(query, s)
    result = x.fetchall()  # here we get tuples equivalent to the number of records
    for record in result:
        print(record)
    print(" ")
    start()

def start():
    print("   1.open new account\n "
          "  2.desposit money\n"
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