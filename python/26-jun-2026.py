import mysql.connector
def connect_to_db():
    connect = mysql.connector.connect(
         host="localhost",
         user="kailash chaudhary",
         password="password",
         database="loginsystem"
    )
    return connect
