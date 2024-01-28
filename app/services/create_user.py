from app.connection import Connection

class User:
    def __init__(self, username:str,password:str,
                email:str|None=None,phone_no:int|None=None):
        self._username = username
        self._email_id = email
        self.__password = password
        self._phone_no = phone_no
        self.conn = Connection()
    
    def create_user(self):
        cursor = self.conn.open_connection()
        SQL = ("INSERT INTO user_details(username,email_id,password,phone_no) VALUES (?, ?, ?, ?)"\
                ,(self._username,self._email_id,self.__password,self._phone_no))
        cursor.execute(SQL)
        cursor.commit()
        cursor.close()

    def login_user(self):
        cursor = self.conn.open_connection()
        creds_check  = cursor.execute("select username from user_details where username={0}\
                       and password={1}".format(self._username,self.__password)).fetchone()
        if creds_check:
            pass
        cursor.close()

    def delete_user(self):
        cursor = self.conn.open_connection()
        delete_user = cursor.execute("delete from user_details where username = {0}".format(self._username)).fetchone()
        if delete_user:
            return "Success"
        cursor.close()
        return None
