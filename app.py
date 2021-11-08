from datetime import date
from flask import Flask, request, jsonify
from flask_cors import CORS
from CRUD_USUARIOS import CRUD_USUARIOS
from CRUD_PUBLICACIONES import CRUD_PUBLICACIONES
import time

objusuarios=CRUD_USUARIOS()
objpublicaciones =CRUD_PUBLICACIONES()

#CREACIÓN DEL ADMINISTRADOR 
objusuarios.crearusuario("Cesar Reyes","Masculino","admin","admin@ipc1.com","admin@ipc1","Administrador")
objusuarios.crearusuario("Willy Cano","Masculino","wirocama","willyamigo@gmail.com","201700594","Administrador")

#CREACIÓN DE PUBLICACIONES
objpublicaciones.agregarpublicacion("Imagen","https://th.bing.com/th/id/OIP.y42HDI45TCnYROM-NfnckAHaE8?pid=ImgDet&w=900&h=600&rs=1","04/11/21", "Fotografía",1,"wirocama")
objpublicaciones.agregarpublicacion("Imagen","https://images2.alphacoders.com/609/609571.jpg","04/11/21", "Música",1,"wirocama")

#CREACIÓN DE CATEGORIAS
objpublicaciones.agregarcategoria("Fotografía")
objpublicaciones.agregarcategoria("Música")

#<iframe width="560" height="315" src="https://www.youtube.com/embed/2ElZTk8SzgQ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"></iframe>

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def index():

	return "<H1>BACKEND PROYECTO 2 </H1>"

@app.route('/login', methods=['POST'])
def login():

    if request.method == 'POST':
        usuario = request.json["usuario"]
        contrasenia = request.json["contrasenia"]
        
        verificador = objusuarios.validarusuario(usuario,contrasenia)
        
        return {
            "data": verificador
        }

@app.route('/crear_usuario', methods=['POST'])
def crear_usuario():

    if request.method == 'POST':
        nombre = request.json["nombre"]
        genero = request.json["genero"]
        nusuario = request.json["nusuario"]
        correo = request.json["correo"]
        contrasenia = request.json["contrasenia"]
        conf_contrasenia = request.json["conf_contrasenia"]
        tipousuario = request.json["tipousuario"]
        
        if contrasenia == conf_contrasenia:

            crear = objusuarios.crearusuario(nombre,genero,nusuario,correo,contrasenia,tipousuario)

            return{
                "data": crear
            }


        return{
            "data":{
                "mensaje": "La contraseña de verificación no coincide",
                "estado": 3
            }
        }

@app.route('/ver_usuario', methods=['POST'])
def ver_usuario():
    if request.method == 'POST':
        id = request.json["id"]

        ver = objusuarios.verusuario(int(id))
        if ver is not False:
            return {
                "data": ver
            }
        return {
            "mensaje":"Informacion no Disponible"
        }

@app.route('/modificar_usuario', methods=['POST'])
def modificar_usuario():
    if request.method == 'POST':

        id = request.json["id"]
        nombre = request.json["nombre"]
        genero = request.json["genero"]
        nusuario = request.json["nusuario"]
        correo = request.json["correo"]
        contrasenia = request.json["contrasenia"]
        conf_contrasenia = request.json["conf_contrasenia"]

        if contrasenia == conf_contrasenia:

            validar = objusuarios.disponibleusuario(int(id),nusuario)

            if validar is not False:
                modificar = objusuarios.modificarusuario(int(id), nombre, genero, nusuario, correo, contrasenia)
                return{
                    "data": modificar
                }
            return {
                "data": {
                    "mensaje": "El Nombre de Usuario no esta disponible",
                    "estado": 2
                }
            }              
        return{
            "data":{
                "mensaje": "La contraseña de verificación no coincide",
                "estado": 3
            }
        } 

@app.route('/eliminar_usuario', methods=['POST'])
def eliminar_usuario():
    if request.method == 'POST':

        id = request.json["id"]

        eliminar = objusuarios.eliminarusuario(id)

        if eliminar is not False:

            return {

                "Estado": "Se eliminó usuario"
            }


@app.route('/crear_publicacion', methods=['POST'])
def crear_publicacion():
    if request.method == 'POST':
 
       tipo = request.json["type"]
       url = request.json["url"]
       date = request.json["date"]
       category = request.json["category"]
       idU = request.json["idU"]
       usuario = request.json["usuario"]
       estado = request.json["estado"]

       if estado == 1:
           crearp = objpublicaciones.agregarpublicacion(tipo,url,time.strftime("%d/%m/%y"),category,idU,usuario)
           
       elif estado == 2:
           crearp = objpublicaciones.agregarpublicacion(tipo,url,date,category,idU,usuario)
           

       objpublicaciones.agregarcategoria(category)

       return crearp

@app.route('/publicaciones', methods=['GET'])
def publicaciones():
    
    return objpublicaciones.verpublicaciones()

@app.route('/categorias', methods=['GET'])
def categorias():

    return {
        "data":objpublicaciones.mostrarcategorias()
    }    
          
@app.route('/modificar_publicacion', methods=['POST'])
def modificar_publicacion():
    if request.method == 'POST':
        id = request.json["id"] 
        type = request.json["type"]
        url = request.json["url"]
        category = request.json["category"]

        modificarp = objpublicaciones.agregarpublicacion(type,url,date,category)

        if modificarp is not False:

           return modificarp


@app.route('/eliminar_publicacion', methods=['POST'])
def eliminar_publicacion():
    if request.method == 'POST':

        id = request.json["id"]

        eliminarp = objpublicaciones.eliminarpublicacion(id)
        if eliminarp is not False:
            return {

                "Estado": "Se eliminó publicación"
            }

@app.route('/conteo_likes', methods=['POST'])
def conteo_likes():
    if request.method == 'POST':

        id = request.json["id"]

        like = objpublicaciones.likes(id)

        if like is not False:
            return {

                "Estado": "Se agregó un like"
            }

if __name__ == "__main__":
	app.run(threaded=True, port=5000,debug=True)
