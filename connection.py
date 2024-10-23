import pymysql
import pymysql.cursors

def connect_to_db():
            return  pymysql.connect(
                host = "127.0.0.1",
                user = "root",
                password = "Aa36997362",
                port = 3306,
                db = "inventory_db",    # Name of your databse
                cursorclass=pymysql.cursors.DictCursor  # To get results as dictionaries
            )