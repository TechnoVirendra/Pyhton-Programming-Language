# Import and Connect Work .
import platform
import os
import mysql.connector as mysql
mydb=mysql.connect(host="localhost",user="root",password="")
cursor=mydb.cursor()
sql="create database Billing_system;"
sql1="use billing_system;"
sql2="create table customer(C_Id int,C_Name varchar(15),Item_Code char(3),Item_Name varchar(25),Price varchar(10),Qnt int,Disc varchar(8),Amount varchar(15));"
cursor.execute(sql)
cursor.execute(sql1)
cursor.execute(sql2)

# Using Insert Command.

def strinsert():
    L=[]
    C_Id=input("Enter Customer Id: ")
    L.append(C_Id)
    C_Name=input("Enter Customer Name: ")
    L.append(C_Name)
    Item_Code=int(input("Enter Item Code : "))
    L.append(Item_Code)
    Item_Name=input("Enter Item Name : ")
    L.append(Item_Name)
    Price=input("Enter The Price Of Item : ")
    L.append(Price)
    Qnt=int(input("Enter Number Of Items Purchase : "))
    L.append(Qnt)
    Disc=int(input("Enter Discount Of Items : "))
    L.append(Disc)
    S=(L)
    sq="insert into customer(C_Name,C_Id,Item_Code,Item_Name,Price,Qnt,Disc,Amount)values(%s,%s,%s,%s,%s,%s,%s,Price*Qnt-Disc);"
    cursor.execute(sq,S)
    mydb.commit()

# View Data.

def StuView():
    print("Select The Search Criteria : ")
    print("1. Customer Id ")
    print("2. Customer Name ")
    print("3. All ")
    choice=int(input("Enter Your Choice : "))
    if choice==1:
        z=input("Enter Customer Id : ")
        r1=(z,)
        sq="select * from customer where C_Id=%s;"
        cursor.execute(sq,r1)
    elif choice==2:
        z=input("Enter Customer Name : ")
        r1=(z,)
        sq="select * from customer where C_Name=%s;"
        cursor.execute(sq,r1)
    elif choice==3:
        sq="select * from customer;"
        cursor.execute(sq)
    res= cursor.fetchall()
    print(" Bill Details As follows : ")
    print("C_Name,C_Id,Item_Code,Item_Name,Price,Qnt,Disc,Amount")
    for x in res:
        print(x)

# Remove Items

def removeStu():
    Item_Name=input("Enter Item Name which have not Purchase : ")
    r1=(Item_Name)
    sq="delete from customer where Item_Name='%s';"
    mydb.commit()

# Menu Set.

def Menuset():
    print("Enter 1 : To Add Details ")
    print("Enter 2 : To View Details ")
    print("Enter 3 : To Remove Items ")
    try:
        userInput=int(input("Please Select An Above Option : "))
    except ValueError:
        exit("\nHy! That's Not A Number")
    else:
        print("\n")
    if(userInput ==1):
        strinsert()
    elif(userInput ==2):
        StuView()
    elif(userInput ==3):
        removeStu()
    else:
        print("Enter Correct Choice . . . ")
        Menuset()

# Run Opton.

def runAgain():
    run=input("\n Want To Run Y/N : ")
    while(run.lower()=='y'):
        if(platform.system()=="Windows"):
            print(os.system('cls'))
        else:
            print(os.system('clear'))
        Menuset()
        run=input("\n Want To Run Again Y/N : ")
runAgain()
sq="drop database Billing_System;"
cursor.execute(sq)
