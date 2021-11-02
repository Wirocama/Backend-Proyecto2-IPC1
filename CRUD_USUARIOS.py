from usuarios import usuarios
import json

class CRUD_USUARIOS:

    def __init__(self):
        self.listadousuarios = []
        self.contador = 0

    def crearusuario(self,nombre, genero, nusuario,correo,contrasenia,tipousuario):
        for usuario in self.listadousuarios:
            if usuario.getusuario()==nusuario:
                print ("El usuario ya existe") 
                return False
        self.listadousuarios.append(usuarios(self.contador,nombre,genero,nusuario,correo,contrasenia,tipousuario))
        self.contador=self.contador+1
        print ("el usuario fue registrado con exito")
        return True

    def validarusuario(self,nusuario, contrasenia):
        for usuario in self.listadousuarios:
            if usuario.getusuario() ==nusuario and usuario.getcontrasenia()==contrasenia:
                return usuario
        return False

  
    def modificarusuario(self,id,nombre, genero, nusuario,correo,contrasenia):
        for usuario in self.listadousuarios:
            if usuario.getid() == id:
                usuario.setnusuario(nusuario)
                usuario.setnombre(nombre)
                usuario.setgenero(genero)
                usuario.setcorreo(correo)
                usuario.setcontrasenia(contrasenia)
                return usuario.infousuario()
        return False

    def verusuario(self,id):
        for usuario in self.listadousuarios:
            if usuario.getid() ==id:
                return usuario.infousuario()
        return False
    
    def eliminarusuario(self,id):
        self.listadousuarios.pop(id)
        return True

    def verlistado(self):
        return json.dumps(usuario.infousuario() for usuario in self.listadousuarios)


    




        

           