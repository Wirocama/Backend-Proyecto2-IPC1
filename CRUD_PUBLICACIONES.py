from publicaciones import publicaciones
import json

class CRUD_PUBLICACIONES:

    def __init__(self):

        self.listaPublicaciones = [] 
        self.listaCategorias = []
        self.contador = 0

    def agregarpublicacion(self,tipo,url,date,category,idU,usuario):

        self.listaPublicaciones.append(publicaciones(self.contador,tipo,url,date,category,0,idU,usuario))
        self.contador =+ 1 

        print("Se hizo una nueva publicación")

        return {
            "type": tipo,
            "url": url,
            "date": date,
            "category": category,
            "estado": 1,
            "usuario": usuario
        }

    def modificarpublicacion(self,id,tipo,url,category):

        for publicacion in self.listaPublicaciones:
            if publicacion.getid() == id:
                publicacion.settipo(tipo) 
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

    def agregarcategoria(self, categoria):

        for listado in self.listaCategorias:
            if listado == categoria:
                return False
        print("Se agrego la categoría: " + categoria)        
        self.listaCategorias.append(categoria)
        return True

    def mostrarcategorias(self):

        self.listaCategorias.sort()
        return self.listaCategorias



		    
