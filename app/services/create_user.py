from connection import Connection
from auth import decrypt_password

class User:
    def __init__(self, username:str|None=None,password:str|None = None,
                email:str|None=None,phone_no:int|None=None):
        self._username = username
        self._email_id = email
        self.__password = password
        self._phone_no = phone_no
        self.conn = Connection()
    
    def create_user(self):
        cursor = self.conn.open_connection()
        SQL = cursor.execute("INSERT INTO user_details(username,email_id,password,phone_no) VALUES (?, ?, ?, ?)",(self._username,self._email_id,self.__password,self._phone_no))
        self.conn.close_connection()

    def authenicate_user(self):
        cursor = self.conn.open_connection()
        creds_check  = cursor.execute('''select password from user_details where username="{0}"'''.format(self._username)).fetchone()
        user_password = decrypt_password(creds_check[0])
        self.conn.close_connection()
        return user_password == self.__password
            
    def delete_user(self):
        cursor = self.conn.open_connection()
        delete_user = cursor.execute("delete from user_details where username = {0}".format(self._username)).fetchone()
        if delete_user:
            return "Success"
        cursor.close()
        return None
