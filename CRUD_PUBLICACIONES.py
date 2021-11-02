from publicaciones import publicaciones
import json

class CRUD_PUBLICACIONES:

    def __init__(self):

        self.listaPublicaciones = [] 
        self.contador = 0

    def agregarpublicacion(self,type,url,date,category):

        self.listaPublicaciones.append(publicaciones(self.contador,type,url,date,category,0))
        self.contador = self.contador + 1

        print("Se hizo una nueva publicación")
        return True

    def modificarpublicacion(self,id,type,url,category):

        for publicacion in self.listaPublicaciones:
            if publicacion.getid() == id:
                publicacion.settype(type) 
                publicacion.seturl(url) 
                publicacion.setcategory(category) 

                return publicacion.infopublicacion()

        return False

    def eliminarpublicacion(self, id):
        self.listaPublicaciones.pop(id)

        return True

    def likes(self, id):
        for publicacion in self.listaPublicaciones:
            if publicacion.getid() == id:
                publicacion.setlikes() 
                return True

    def verpublicaciones(self):

        return json.dumps([publicacion.infopublicacion() for publicacion in self.listaPublicaciones])                           




        
