import mysql.connector
import os

class CMLAccountManager():
    def __init__(self, db_username, db_password) -> None:
        self.config = {
            'user': db_username,
            'password': db_password,
            'host': 'cml4.csie.ntu.edu.tw',  # 默認是 'localhost'
            'database': 'CMLabWebSite',
            'raise_on_warnings': True,
            'ssl_disabled': True
        }

        self.conn = mysql.connector.connect(**self.config)
        print("Connection successful")
        self.conn.close()

    def find_user(self, username):
        try:
            cursor = self.conn.cursor(buffered=True)
        except:
            if self.conn.is_connected():
                self.conn.close()
            print("Restart DB Connection")
            self.conn = mysql.connector.connect(**self.config)
            cursor = self.conn.cursor(buffered=True)

        query = "SELECT * FROM `People` WHERE `account`=%s"
        param = (username, )

        cursor.execute(query, param)
        result = cursor.fetchone()

        cursor.close()

        return result
