import mysql.connector
from mysql.connector import Error
 
connection = mysql.connector.connect(host = 'localhost',database = 'atm' , user = '5D1' , password = 'Lucky143!',auth_plugin='mysql_native_password')
 
print("WELCOME, HII I AM ATM MACHINE")
n = int(input("PRESS 0 TO CREATE AN ACCOUNT and 1 TO LOGIN YOUR EXISTING ACCOUNT : "))
password = ""
myname=""
id = ""
 
if n == 0:
    name = input("ENTER YOUR NAME : ")
    account_number = int(input("ENTER ACCOUNT NUMBER : "))
    account_password = int(input("SET YOUR 4 DIGIT PIN : "))
 
    myname = name
    password = account_password
    id = account_number
    val = (id,myname,password)
    val2 = (id,0.0)
    sql = "INSERT INTO accounts(account_number,account_holder,account_password) VALUES (%s,%s,%s)"
    sql2 = "INSERT INTO balance(account_number ,account_balance) VALUES (%s,%s)"
    mycursor = connection.cursor()
    mycursor.execute(sql,val)
    mycursor.execute(sql2,val2)
    connection.commit()
    print("CONGRATS...! YOU HAVE SUCESSFULLY CREATED YOUR ACCOUNT..")
    print("YOUR DETAILS ARE UPDATED IN THE DATABASE SUCCEFULLY..!")
 
if n ==1 :
    info = int(input("ENTER YOUR ACCOUNT NUMBER : "))
    passw = int(input("ENTER PASSWORD : "))
    mycursor = connection.cursor()
    mycursor.execute("""SELECT * FROM accounts where account_number = '%s'"""%(info))
    row = mycursor.fetchone()
    if mycursor.rowcount ==1:
        mycursor.execute("""SELECT * FROM accounts where account_password = '%s'"""%(passw))
        row = mycursor.fetchone()
        if mycursor.rowcount == 1:
            print("LOGINED SUCCEFULLY...!")
            d = int(input("ENTER 0 FOR DEPOSIT,\n 1 FOR WTHDRAWAL ,\n 2 BALANCE ENQURY \n 3 change password & 4 exit : "))
            if d == 0:
                a = int(input("ENTER THE AMOUNT YOU WANT TO DEPOSITE : "))
                mycursor.execute("""SELECT account_balance FROM balance  where account_number = '%s'"""%(info))
                col = mycursor.fetchone()
                c = int(col[0]) + a
                mycursor.execute("UPDATE balance SET account_balance = %s where account_number = '%s'"%(c,info))
                print("YOUR AMOUNT IS SUCCEFULLY DEPOSITED..!")
            elif d == 1 :
                a = int(input("ENTER THE AMOUNT YOU WANT TO WITHDRAW : "))
                mycursor.execute("""SELECT account_balance FROM balance  where account_number = '%s'"""%(info))
                col = mycursor.fetchone()
                c = int(col[0]) - a
                if c < 0:
                    print("Insufficient funds")
                else:
                    mycursor.execute("UPDATE balance SET account_balance = '%s' where account_number = '%s'"%(c,info))
                    print("PLEASE COLLECT YOUR CASH..!")
            elif d == 2:
                mycursor.execute("""select account_balance from balance where account_number = '%s'"""%(info))
                bal = mycursor.fetchone()
                print("Your account balance is : ",int(bal[0]))
            elif d == 3:
                a = int(input("ENTER THE NEW PIN YOU WANT TO REPLACE WITH THE OLD ONE : "))
                mycursor.execute("UPDATE accounts set account_password = %s where account_number = '%s'"%(a,info))
            elif d == 4:
                print("OPERATION COMPLETED..!")
                exit(0)
            else:
                print("WARNING...!YOU HAVE ENTERED THE WRONG OPTION PLEASE TRY AGAIN...!")
        else:
            print("INVALID PASSWORD")
    else:
        print("ACCOUNT DOESN'T EXIT IN THE DATABASE...\nPLEASE REGISTER IF YOU ARE A NEW USER OR ENTER CORRECT DETAILS AND TRY AGAIN")
    connection.commit()
else:
    print("PLEASE ENTER THE CORRECT OPTION...!")
    exit(0)
