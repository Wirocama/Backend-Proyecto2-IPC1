from usuarios import usuarios
import json

class CRUD_USUARIOS:

    def __init__(self):
        self.listadousuarios = []
        self.contador = 0

    def crearusuario(self,nombre, genero, nusuario,correo,contrasenia,tipousuario):
        for usuario in self.listadousuarios:
            if usuario.getusuario()==nusuario:
                print("El Usuario Ya Existe")
                return {
                    "mensaje": "El Usuario Ya Existe",
                    "estado": 2
                }
        self.listadousuarios.append(usuarios(self.contador,nombre,genero,nusuario,correo,contrasenia,tipousuario))

        self.contador += 1

        print ("el usuario " + nusuario + " fue registrado con exito")
        return {
            "nombre": nombre,
            "genero": genero,
            "usuario": nusuario,
            "correo": correo,
            "tipousuario": tipousuario,
            "estado": 1
        }

    def validarusuario(self,nusuario, contrasenia):
        for usuario in self.listadousuarios:
            if usuario.getusuario() == nusuario:
                if usuario.getcontrasenia() == contrasenia:
                    return {
                        "id": usuario.getid(),
                        "nombre": usuario.getnombre(),
                        "usuario": usuario.getusuario(),
                        "correo": usuario.getcorreo(),
                        "tipousuario": usuario.gettipousuario(),
                        "estado": 1
                    }
                return {
                    "usuario": usuario.getusuario(),
                    "contraseña": "Error en la contraseña",
                    "estado": 2
                }        

        return {
                "usuario": "Usuario no encontrado",
                "estado": 3
            }    
    
    def disponibleusuario(self,id, nusuario):
        for usuario in self.listadousuarios:
            if usuario.getusuario() == nusuario:
                if usuario.getid() == id:
                    return True
                return False
        return True  

    def modificarusuario(self,id,nombre, genero, nusuario,correo,contrasenia):

        for usuario in self.listadousuarios:
            if usuario.getid() == id:
                usuario.setnusuario(nusuario)
                usuario.setnombre(nombre)
                usuario.setgenero(genero)
                usuario.setcorreo(correo)
                usuario.setcontrasenia(contrasenia)
                return {
                    "nombre":nombre,
                    "genero":genero,
                    "usuario":nusuario,
                    "correo":correo,
                    "estado": 1
                }
              
    def verusuario(self,id):
        for usuario in self.listadousuarios:
            if usuario.getid() == id:
                return usuario.infousuario()
        return False        
         
    def eliminarusuario(self,id):
        self.listadousuarios.pop(id)
        return True

    def verlistado(self):
        return json.dumps(usuario.infousuario() for usuario in self.listadousuarios)


    




        

           