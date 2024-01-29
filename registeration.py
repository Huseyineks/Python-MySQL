import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "huseyinilkerh1905",
    database = "registerationdatabase"
)

mycursor = db.cursor()


mycursor.execute("CREATE DATABASE registerationdatabase")