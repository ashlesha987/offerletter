#!/usr/bin/python
import MySQLdb
import csv

db = MySQLdb.connect(host="localhost",  
                     user="root",	
                     passwd="AmarMmc1234",   
                     db="woclo") 

# Create a Cursor object to execute queries.
cur = db.cursor()
cursor = db.cursor(MySQLdb.cursors.DictCursor)


#creating a list of dictionaries. each dictionary will be a tuple from 2 joint myql tables--in this case, User_Dummy and Internship_Dummy 


 
cur = db.cursor()
cursor.execute("select first_name, last_name, gender, start_date, end_date, course, collegename, branch from personal_user inner join internship_certificate on personal_user.id=internship_certificate.personal_id")
rows_ListOfDict=cursor.fetchall()
print rows_ListOfDict



#to save this list of dictionaries as a CSV file

csv_columns = ['first_name', 'last_name', 'gender', 'start_date', 'end_date', 'course', 'collegename', 'branch']

csv_file = "MySQLData.csv"

try:
 with open(csv_file, 'w') as csvfile:
  writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
  writer.writeheader()
  for data in rows_ListOfDict:
   writer.writerow(data)

except IOError:
 print ("I/O error")


#with open('MySQLData.csv') as csvfile:
 #reader = csv.DictReader(csvfile)
 #for row in reader:
  #print(row['first_name'], row['last_name'], row['gender'], row['start_date'], row['end_date'], row['course'], row['collegename'], row['branch'])



