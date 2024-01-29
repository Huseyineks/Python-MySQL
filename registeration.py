import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "huseyinilkerh1905",
    database = "registerationdatabase"
)

mycursor = db.cursor()

mycursor.execute("CREATE TABLE Person (person_id int PRIMARY KEY AUTO_INCREMENT,first_name VARCHAR(50) NOT NULL,last_name VARCHAR(50) NOT NULL,country VARCHAR(20),password VARCHAR(100) NOT NULL)")