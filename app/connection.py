import sqlite3

class Connection:
    def __init__(self):
        self.conn = sqlite3.connect("")
        self.cursor = self.conn.cursor()
    
    def open_connection(self):
        return self.cursor

    def close_connection(self):
        self.conn.commit()
        self.cursor.close()
