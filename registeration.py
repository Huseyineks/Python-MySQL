import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "huseyinilkerh1905",
    database = "registerationdatabase"
)

mycursor = db.cursor()

mycursor.execute("INSERT INTO Person(first_name,last_name,country,password) VALUES(%s,%s,%s,%s)",("Huseyin","Demirdelen","Spain","password123"))

db.commit()