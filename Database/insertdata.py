
"""
    This module is for inserting data into student table of batch11am database
"""
import pymysql as sql
CONN = sql.connect(host="localhost", port=3306, user="root", password="", database="batch11am")
CURSOR = CONN.cursor()
while input("\n Press any key to continue : "):
    FNAME = input("\n FirstName : ")
    LNAME = input("\n LastName : ")
    SUBJECT = input("\n Subject : ")
    AGE = int(input("\n Age : "))
    CMD = f"insert into student(fname, lname, subject, age) values('{FNAME}', '{LNAME}', '{SUBJECT}', {AGE})"
    CURSOR.execute(CMD)
    CONN.commit()  # for storing data permanently
    print("\n Data Inserted Successfuly")
print("\n Thanks for using our service....")
CONN.close()
