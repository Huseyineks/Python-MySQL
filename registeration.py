import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "huseyinilkerh1905",
    database = "registerationdatabase"
)

mycursor = db.cursor()

sent = "INSERT INTO Person(first_name,last_name,country,password) VALUES(%s,%s,%s,%s)"

key = input("To exit press q to continue press w: ")
while key != 'q':
 
 first_name = input("Input a first name: ")
 last_name = input("Input a last name: ")
 country = input("Input a country: ")
 password = input("Input a password: ")
 
 mycursor.execute(sent,(first_name,last_name,country,password))
 db.commit()

 key = input("To exit press q to continue press w: ")