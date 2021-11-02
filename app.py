from datetime import date
from flask import Flask, request, jsonify
from flask.helpers import url_for
from flask_cors import CORS
from CRUD_USUARIOS import CRUD_USUARIOS
from CRUD_PUBLICACIONES import CRUD_PUBLICACIONES


objusuarios=CRUD_USUARIOS()
objpublicaciones =CRUD_PUBLICACIONES()

#CREACION DEL ADMINISTRADOR 
objusuarios.crearusuario("Cesar Reyes","M","admin","admin@ipc1.com","admin@ipc1","Administrador")


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
        if verificador is not False:
            return{
                "id":verificador.id,
                "nombre":verificador.nombre,
                "genero":verificador.genero,
                "usuario":verificador.nusuario,
                "correo":verificador.correo,
                "contraseña":verificador.contrasenia,
                "tipo usuario":verificador.tipousuario
            }
        return{
            "Estado":"Usuario no encontrado"
        }

@app.route('/crear_usuario', methods=['POST'])
def crear_usuario():
    if request.method == 'POST':
        nombre = request.json["nombre"]
        genero = request.json["genero"]
        nusuario = request.json["nusuario"]
        correo = request.json["correo"]
        contrasenia = request.json["contrasenia"]
        tipousuario = request.json["tipousuario"]

        crear = objusuarios.crearusuario(nombre,genero,nusuario,correo,contrasenia,tipousuario)
        if crear is not False:
            return {
                "nombre":nombre,
                "genero":genero,
                "usuario":nusuario,
                "correo":correo,
                "contraseña":contrasenia,
                "tipo usuario":tipousuario    
            }
        return {
            "ERROR":"El usuario ya existe"
        }
@app.route('/ver_usuario', methods=['POST'])
def ver_usuario():
    if request.method == 'POST':
        id = request.json["id"]

        ver = objusuarios.verusuario(id)
        if ver is not False:
            return ver
        return {
            "ERROR":"Informacion no Disponible"
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
        
        modificar = objusuarios.modificarusuario(id, nombre, genero, nusuario, correo, contrasenia)

        if modificar is not False:
            return {
                "nombre":nombre,
                "genero":genero,
                "usuario":nusuario,
                "correo":correo,
                "contraseña":contrasenia    
            }
        return {
            "ERROR":"No se pudo modificar la información"
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

       type = request.json["type"]
       url = request.json["url"]
       date  = request.json["date"]
       category = request.json["category"]

       crearp = objpublicaciones.agregarpublicacion(type,url,date,category)

       if crearp is not False:

           return {
                "type": type,
                "url": url,
                "date": date,
                "category":category
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
