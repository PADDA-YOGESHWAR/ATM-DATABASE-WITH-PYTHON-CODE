import mysql.connector
from mysql.connector import Error
connection = mysql.connector.connect(host = 'localhost',database = 'atm' , user = '5D1' , password = 'Lucky143!',auth_plugin='mysql_native_password')

print("welcome to atm machine")
n = int(input("PRESS 1 FOR LOGIN & 0 FOR REGISTER :"))
password = ""
myname=""
deposite=""
id = ""

if n == 0:
    name = input("ENTER YOUR NAME : ")
    account_number = int(input("ENTER ACCOUNT NUMBER : "))
    deposite_amount = int(input("ENTER STARTING AMOUNT YOU WANT TO DEPOSITE : "))
    account_password = int(input("SET YOUR 4 DIGIT PIN : "))

    myname = name
    password = account_password
    deposite = deposite_amount
    id = account_number

    val = (myname,password,deposite,id)

    sql = "INSERT INTO atm_data(my_name,pass_word,de_po,i_d) VALUES (%s,%s,%s,%s)"
    mycursor = connection.cursor()

    mycursor.execute(sql,val)
    connection.commit()
    print("YOUR DETAILS ARE UPDATED IN THE DATABASE SUCCEFULLY..!")


elif n ==1 :
    info = int(input("ENTER YOUR ACCOUNT NUMBER : "))
    passw = int(input("ENTER PASSWORD : "))
    mycursor = connection.cursor()
    mycursor.execute("""SELECT * FROM atm_data where i_d = '%s'"""%(info))
    row = mycursor.fetchone()
    if mycursor.rowcount ==1:
        
        mycursor.execute("""SELECT * FROM atm_data where pass_word = '%s'"""%(passw))
        row = mycursor.fetchone()
        if mycursor.rowcount == 1:
            print("LOGINED SUCCEFULLY...!")
            d = int(input("ENTER 0 FOR DEPOSIT,\n 1 FOR WTHDRAWAL &\n 2 FOR EXIT : "))
            if d == 0:
                a = int(input("ENTER THE AMOUNT YOU WANT TO DEPOSITE : "))
                mycursor.execute("""SELECT de_po FROM atm_data  where pass_word= '%s'"""%(passw))
                col = mycursor.fetchone()
                x = list(col)
                for i in x :
                    z = (int(i))
                    c = z+a
                mycursor.execute("UPDATE atm_data SET de_po= %s where pass_word = '%s'"%(c,passw))
                print("YOUR AMOUNT IS SUCCEFULLY DEPOSITED..!")
            elif d == 1 :
                a = int(input("ENTER THE AMOUNT YOU WANT TO WITHDRAW : "))
                mycursor.execute("""SELECT de_po FROM atm_data  where pass_word = '%s'"""%(passw))
                col = mycursor.fetchone()
                x = list(col)
                for i in x :
                    z = (int(i))
                    c = z-a
                mycursor.execute("UPDATE atm_data SET de_po = '%s' where pass_word = '%s'"%(c,passw))
                print("PLEASE COLLECT YOUR CASH..!")
            elif d == 2 :
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