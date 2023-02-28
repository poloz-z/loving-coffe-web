# minimal data base
import sqlite3

class DataBase():
    def __init__(self):
        self.database = sqlite3.connect("u_data.dat")
        self.data_c = self.database.cursor()
        self.data_c.execute("""
          CREATE TABLE IF NOT EXISTS user_data
          (usuario text, correo text, password text)
        """)

    def add_user(self,usuario,correo,password):
        #self.usuario = usuario
        #self.correo = correo
        #self.password = password
        self.data_c.execute("""
          INSERT INTO user_data (usuario,correo,password) 
          VALUES (?,?,?)
        """,(usuario, correo, password))
        self.database.commit()

    def user_query(self,usuario):
        self.data_c.execute("""
            SELECT usuario FROM user_data WHERE usuario=?
        """,(usuario,))
        for x in self.data_c:
            return x[0]

    def pass_query(self,password):
        self.data_c.execute("""
            SELECT password FROM user_data WHERE password=?
        """,(password,))
        for x in self.data_c:
            return x[0]

    def close(self):
        self.database.close()
        self.data_c.close()
