from app.connection import Connection

class Post:
    def __init__(self,username,postcontent={}):
        self._username = username
        self._postcontent = postcontent
        self.conn = Connection()

    def create_post(self):
        cursor = self.conn.open_connection()
        SQL = ("INSERT INTO user_post(username,post_content)VALUES(?,?)"\
               (self._username,self._postcontent))
        cursor.execute(SQL)
        cursor.commit()
        cursor.close()
    
    def list_post(self):
        cursor = self.conn.open_connection()
        post_list = cursor.execute("select post_content from user_post ORDER BY create_date DESC").fetchall()
        cursor.close()
        return post_list if post_list else {}

    def delete_post(self):
        cursor = self.conn.open_connection()
        delete_user = cursor.execute("delete from user_post where username = {0}".format(self._username)).fetchone()
        cursor.close()
        return "Success" if delete_user else None

    def update_post(self,updated_content):
        cursor = self.conn.open_connection()
        update_post = cursor.execute("update user_post set post_content={0} where username={1}"\
                                     .format(updated_content,self._username)).fetchone()
        return True if update_post else False
