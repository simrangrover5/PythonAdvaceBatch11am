
"""
    This module is for fetching data from student table
"""
import pymysql as sql
CONN = sql.connect(host="localhost", port=3306, user="root", password="", database="batch11am")
CURSOR = CONN.cursor()
CMD = "select * from student"
CURSOR.execute(CMD)
DATA = CURSOR.fetchall()
for row in DATA:
    print(f"\n FirstName : ", row[0])
    print(f"\n LastName : ", row[1])
    print(f"\n Subject : ", row[2])
    print(f"\n Age : ", row[3])
    print("_"*80)
