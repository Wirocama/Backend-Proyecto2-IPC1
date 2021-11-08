class usuarios:
    def __init__(self, id, nombre, genero, nusuario,correo,contrasenia,tipousuario): 
        self.id=id
        self.nombre=nombre
        self.genero=genero
        self.nusuario=nusuario
        self.correo=correo
        self.contrasenia=contrasenia
        self.tipousuario=tipousuario


    #METODOS GET 
    def getid(self):
        return self.id
    
    def getnombre(self):
        return self.nombre

    def getgenero(self):
        return self.genero

    def getusuario(self):
        return self.nusuario
    
    def getcorreo(self):
        return self.correo
    
    def getcontrasenia(self):
        return self.contrasenia

    def gettipousuario(self):
        return self.tipousuario


    #METODOS SET 
    def setid(self,id):
        self.id=id
    
    def setnombre(self,nombre):
        self.nombre=nombre

    def setgenero(self,genero):
        self.genero=genero

    def setnusuario(self,nusuario):
        self.nusuario=nusuario

    def setcorreo(self,correo):
        self.correo=correo

    def setcontrasenia(self,contrasenia):
        self.contrasenia=contrasenia
    
    def settipousuario(self,tipousuario):
        self.tipousuario=tipousuario

    #METODO DE INFORMACION
    def infousuario(self):
        return{
            "id":self.id,
            "nombre":self.nombre,
            "genero":self.genero,
            "nusuario":self.nusuario,
            "correo":self.correo,
            "tipousuario":self.tipousuario
        }