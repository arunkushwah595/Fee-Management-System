import mysql.connector  # Import Library

mydb = mysql.connector.connect(host='localhost',user='root',password='1234',database='School') # Database

mycursor=mydb.cursor() # Create a Cursor


def stuInsert(): # Function To Insert Student Details in Student Table
    L=[]
    roll=int(input("Enter the roll number : "))
    L.append(roll)
    name=input("Enter the Name: ")
    L.append(name)
    age=int(input("Enter Age of Student : "))
    L.append(age)
    classs=input("Enter the Class : ")
    L.append(classs)
    city=input("Enter the City ofthe Student : ")
    L.append(city)
    stud=(L)
    sql="insert into student (roll,name,age,class,city) values (%s,%s,%s,%s,%s)"
    mycursor.execute(sql,stud)
    mydb.commit()
    
    
def stuView():  # Function to view the Student's details of specific Student
    print("Select the search criteria : ")
    print("1. Roll")
    print("2. Name")
    print("3. Age")
    print("4. City")
    print("5. All")
    ch=int(input("Enter the choice : "))
    if ch==1:
        s=int(input("Enter roll no : "))
        rl=(s,)
        sql="select * from student where roll=%s"
        mycursor.execute(sql,rl)
    elif ch==2:
        s=input("Enter Name : ")
        rl=(s,)
        sql="select * from student where name=%s"
        mycursor.execute(sql,rl)
    elif ch==3:
        s=int(input("Enter age : "))
        rl=(s,)
        sql="select * from student where age=%s"
        mycursor.execute(sql,rl)
    elif ch==4:
        s=input("Enter City : ")
        rl=(s,)
        sql="select * from student where City=%s"
        mycursor.execute(sql,rl)
    elif ch==5:
        sql="select * from student"
        mycursor.execute(sql)   
    res=mycursor.fetchall()
    print("The Students details are as follows : ")
    print("(ROll, Name, Age, Class, City)")
    for x in res:
        print(x)
        
        
        
def feeDeposit():  # Function to enter Fee Details in Fee Table
    L=[]
    roll=int(input("Enter the roll number : "))
    L.append(roll)
    feedeposit=int(input("Enter the Fee to be deposited : "))
    L.append(feedeposit)
    month=input("Enter month of fee : ")
    L.append(month)
    fee=(L)
    sql="insert into fee(roll,feeDeposit,Month) values (%s,%s,%s)"
    mycursor.execute(sql,fee)
    mydb.commit()
    print ("fee deposit successfully")
    
    
    
def feeView():  # Function to View Fee Details of a Particular Student
    print("Please enter the details to view the fee details :")
    roll=int(input("Enter the roll number of the student whose fee is to be viewed : "))
    sql="Select Student.Roll, Student.Name, Student.Class, sum(fee.feeDeposit), fee.month from Student INNER JOIN fee ON Student.roll=fee.roll and fee.roll = %s"
    rl=(roll,)
    mycursor.execute(sql,rl)
    res=mycursor.fetchall()
    print()
    print("(ROll,   Name,     Age,    Fee,  Month)")
    for x in res:
        print(x)
    
    
    
def removeStu():  # Delete Student's Details from both Tables(i.e. Student & Fee)
    roll=int(input("Enter the roll number of the student to be deleted : "))
    rl=(roll,)
    sql="Delete from fee where roll=%s"
    mycursor.execute(sql,rl)
    sql1="Delete from Student where roll=%s"
    mycursor.execute(sql1,rl)
    mydb.commit()
    print ("The Student detail of roll no",rl,"Successfully Deleted.")
    
    
    
def MenuSet(): # The Menu Function
    print("Enter 1 : To Add Student")
    print("Enter 2 : To View Student ")
    print("Enter 3 : To Deposit Fee ")
    print("Enter 4 : To Remove Student")
    print("Enter 5 : To View Fee of Any Student")
    
    try: #Using Exceptions For Validation
        userInput = int(input("Please Select An Above Option: "))
    except ValueError:
        exit("\nHy! That's Not A Number") #Error Message
    else:
        print("\n") 
        if(userInput == 1):
            stuInsert()   # Calling Function to Add Student
        elif (userInput==2):
            stuView()     # Calling Function to View Student's Details
        elif (userInput==3):
            feeDeposit()  # Calling Function to Deposit Fees
        elif (userInput==4):
            removeStu()   # Calling Function to Remove Student's Details
        elif (userInput==5):
            feeView()     # Calling Function to View Fee Details
        else:
            print("Enter correct choice. . .  ")  
            
                 
o="y"
while (o=="y" or o=="Y"):
    MenuSet() # Calling Menu fFunction
    o=input("\nWant To Run Again Y/n")
