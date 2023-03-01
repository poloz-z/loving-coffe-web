# minimal data base
from firebase import firebase

import json

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
           
         
            

                