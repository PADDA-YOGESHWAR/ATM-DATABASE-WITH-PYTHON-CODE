import mysql.connector
from mysql.connector import Error
 
connection = mysql.connector.connect(host = 'localhost',database = 'gayathri' , user = '514' , password = 'Gayathri@123',auth_plugin='mysql_native_password',consume_results=True)
print("welcome to hospital...!")
n = int(input("Enter 0 if you are a doctor and 1 if you are a patient : "))
doctor_name = ""
doctor_age = ""
specialization = ""
doctor_gender = ""
doctor_password = ""
patient_age = ""
patient_name = ""
patient_gender = ""
if n == 0 :
    print("Hii.. Doctor...!")
    a= int(input("Press 0 if you are a new doctor and press 1 if you are already existed doctor and update your information : "))
    if a== 0:
        print("WELCOME TO MVGR HEALTH CARE...")
        name = input("Please Enter your name : ")
        age = int(input("Please Enter your age : "))
        spl = input("Enter your specialization : ")
        gen = input("Enter your gender(Male/Female/Others) : ")
        pwd = input("Please set any password : ")
        doctor_name = name
        doctor_age = age
        specialization = spl
        doctor_gender = gen
        doctor_password = pwd
        val = (doctor_name,doctor_age,specialization,doctor_gender,doctor_password)
        sql = "INSERT INTO doctors(dname,dage,specialization,dgender,dpassword) VALUES (%s,%s,%s,%s,%s)"
        mycursor = connection.cursor()
        mycursor.execute(sql,val)
        mycursor.execute("""select d_id from doctors where dname = '%s'"""%(doctor_name))
        doctor_id = mycursor.fetchone()
        print("Your Doctor ID is : ",int(doctor_id[0]))
        print("Your details are sucessfully Entered...")
        connection.commit()
    elif a == 1:
        print("Hii Doctor.. Nice to see you again..")
        doctor_id = int(input("Enter your ID : "))
        pwd = input("Enter your password : ")
        mycursor = connection.cursor()
        mycursor.execute("""SELECT * FROM doctors where d_id = '%s'"""%(doctor_id))
        row = mycursor.fetchone()
        if mycursor.rowcount ==1:
            mycursor.execute("""SELECT * FROM doctors where dpassword = '%s'"""%(pwd))
            row = mycursor.fetchone()
            if mycursor.rowcount == 1:
                print("LOGINED SUCCEFULLY...!")
                b = int(input("Press 0 to update your age\n 1 to update your specialization and \n2 update timing : "))
                if b == 0:
                    new_age = int(input("Enter your present age : "))
                    mycursor.execute("UPDATE doctors set dage = %s where d_id = '%s'"%(new_age,doctor_id))
                    mycursor = connection.cursor()
                    connection.commit()
                elif b ==1:
                    new_spl = input("Enter your new specialization (this will be replaced with old specialization): ")
                    mycursor.execute("""UPDATE doctors set specialization = '%s' where d_id = %s"""%(new_spl,doctor_id))
                    mycursor = connection.cursor()
                    connection.commit()
                elif b == 2:
                    print("please rember you are supposed to available daily at same timing.. variable timings are not encouraged by MVGR CARE")
                    print("Please enter railway time (24hrs format)")
                    come = input("Intime :")
                    go = input("Outtime : ")
                    emptylst = []
                    print("Press 1 if u are available and 0 if you are not available")
                    print("Here day 1 means monday, day 2 means tuesday and sequence continues till sunday again")
                    mycursor.execute("SELECT specialization FROM doctors where d_id = %s"%(doctor_id))
                    special = mycursor.fetchone()[0]
                    i = 0
                    while i<7:
                        print("Available in day : ",i+1)
                        temp = int(input())
                        if temp == 0:
                            emptylst.append('Not_available')
                        elif temp == 1:
                            emptylst.append('Available')
                        else:
                            i = i-1
                            print("Please enter either 0 or 1")
                        temp = 0
                        i= i+1
                    mycursor.execute("")
                    val1 = (doctor_id,special,come,go,emptylst[0],emptylst[1],emptylst[2],emptylst[3],emptylst[4],emptylst[5],emptylst[6])
                    mycursor.execute("""SELECT * FROM timings where d_id = '%s'"""%(doctor_id))
                    row = mycursor.fetchone()
                    if mycursor.rowcount == 1:
                        mycursor.execute("UPDATE timings set start_time=%s,end_time= %s,monday='%s',tuesday='%s',wednesday='%s',thursday='%s',friday='%s',saturday='%s',sunday='%s' where d_id = %s"%(come,go,emptylst[0],emptylst[1],emptylst[2],emptylst[3],emptylst[4],emptylst[5],emptylst[6],doctor_id))
                    else:
                        sql1 = "INSERT INTO timings(d_id,specialization,start_time,end_time,monday,tuesday,wednesday,thursday,friday,saturday,sunday) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                        mycursor = connection.cursor()
                        mycursor.execute(sql1,val1)
                    connection.commit()
            else:
                print("Incorrect password... please try again")
                exit(0)
        else:
            print("No such ID number is present...please try again with correct ID")
            exit(0)
    else:
        print("process incomplete...! please try again and enter correct details..")
        exit(0)
    connection.commit()
elif n == 1:
    print("we will surely help you...! please enter your futher details to get appointment..")
    page = int(input("Please Enter your age : "))
    pname = input("Enter your name : ")
    pgender = input("Enter your gender(Male/Female/Others) :")
    patient_age = page
    patient_name = pname
    patient_gender = pgender
    val = (patient_age,patient_name,patient_gender)
    sql = "INSERT INTO patients(age,pname,gender) VALUES (%s,%s,%s)"
    mycursor = connection.cursor()
    mycursor.execute(sql,val)
    connection.commit()
    mycursor.execute("""select p_id from patients where pname = '%s'"""%(patient_name))
    patient_id = mycursor.fetchone()
    print("Your patient ID is : ",int(patient_id[0]))
    print("choose your diagnosist : ")
    print("Available diagnosists are : ")
    print("\n")
    print("Doctor ID\t","specialist\t","timing available","monday\t","tuesday\t","wednesday\t","thursday\t","friday\t","\tsaturday\t","sunday")
    print("\n")
    mycursor.execute("""select * from timings""")
    data = mycursor.fetchall()
    for i in range(0,len(data)):
        print(data[i][0],"\t\t",data[i][1],"\t",data[i][2],"to",data[i][3],"\t",data[i][4],"\t",data[i][5],"\t",data[i][6],"\t",data[i][7],"\t",data[i][8],"\t",data[i][9],"\t",data[i][10],"\n")
    print("please check the availablity and book your appointment... no refund will be given if you booked for not available time")
    doc_id = int(input(("Please select the doctor ID by your requirements ")))
    day = input("which day you want the appointment : ")
    values = (doc_id,patient_id[0],day)
    query = "INSERT INTO get_appointment(d_id,p_id,appointment_day) values (%s,%s,%s)"
    mycursor = connection.cursor()
    mycursor.execute(query,values)
    connection.commit()
    mycursor.execute("""select appointment_no from get_appointment where p_id = '%s'"""%(patient_id))
    appointment_id = mycursor.fetchone()
    print("Your patient ID is : ",int(appointment_id[0]))
    print("Sucessfully you have booked your appointment")
    print("Come with your patient ID, pay amount and get diagnotised")
else:
    print("process incomplete...! please try again and enter correct details..")
    exit(0)
         
