### **SQL Commands to create both the tables**





####  ***For Student table:***



###### &nbsp;mysql> CREATE TABLE student (roll int(5) Primary key, 

###### &nbsp;			      name varchar(20) NOT NULL, 

###### &nbsp;			      age int(2) NOTNULL,

###### &nbsp;			      class varchar(3) NOT NULL,

###### &nbsp;		 	      City varchar(10));





####  ***For Fee table:***



###### &nbsp;mysql> CREATE TABLE fee (roll int(5) references Student(roll),

###### &nbsp;			FeeDeposit int(6) NOT NULL, 

###### &nbsp;			month varchar(10) NOT NULL);

