import mysql.connector
print("Connecting")
class Database:
    def __init__(self):
        self.connection =mysql.connector.connect(
            host="localhost",
            user=""
        )