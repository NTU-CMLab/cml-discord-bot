import mysql.connector
import os

class CMLAccountManager():
    def __init__(self, db_username, db_password) -> None:
        config = {
            'user': db_username,
            'password': db_password,
            'host': 'cml4.csie.ntu.edu.tw',  # 默認是 'localhost'
            'database': 'CMLabWebSite',
            'raise_on_warnings': True,
            'ssl_disabled': True
        }

        self.conn = mysql.connector.connect(**config)
        print("Connection successful")

    def find_user(self, username):
        cursor = self.conn.cursor()
        query = "SELECT * FROM `People` WHERE `account`=%s"
        param = (username, )

        cursor.execute(query, param)
        result = cursor.fetchone()

        cursor.close()

        return result
