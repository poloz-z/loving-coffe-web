# minimal data base
#import sqlite3
from firebase import firebase

#class DataBase():
#    def __init__(self):
#        self.database = sqlite3.connect("u_data.dat")
#        self.data_c = self.database.cursor()
#        self.data_c.execute("""
#          CREATE TABLE IF NOT EXISTS user_data
#          (usuario text, correo text, password text)
#        """)

firebase = firebase.FirebaseApplication('https://loving-coffe-default-rtdb.firebaseio.com/',None)

class DataBase():
       def add_user(estees,usuario,correo,password):         
            datos = {
                       "usuario": usuario,
                       "correo": correo,
                       "password": password
                    }   
            resultado = firebase.post('/base_datos/personas', datos)
            if resultado: 
                    return resultado

    def user_auth(noseque, usuario, clave):
           find = firebase.get('/base_datos/personas', None)
           json_dic = json.dumps(find)
           json_index = json.loads(json_dic)
           for x in find:
                  #print(json_index[x]['password'])
                  if(json_index[x]['usuario'] == usuario and json_index[x]['password'] == clave):
                         return True
                  else:
                         return False
                    
#    def add_user(self,usuario,correo,password):
#        self.data_c.execute("""
#          INSERT INTO user_data (usuario,correo,password) 
#          VALUES (?,?,?)
#        """,(usuario, correo, password))
#        self.database.commit()

#    def user_query(self,usuario):
#        self.data_c.execute("""
#            SELECT usuario FROM user_data WHERE usuario=?
#        """,(usuario,))
#        for x in self.data_c:
#            return x[0]

#    def pass_query(self,password):
#        self.data_c.execute("""
#            SELECT password FROM user_data WHERE password=?
#        """,(password,))
#        for x in self.data_c:
#            return x[0]

#    def close(self):
#        self.database.close()
#        self.data_c.close()
