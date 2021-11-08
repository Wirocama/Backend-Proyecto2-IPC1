class publicaciones:
    def __init__(self, id, tipo, url, date, category, likes, idU, usuario): 
        self.id = id
        self.tipo = tipo
        self.url=url
        self.date=date
        self.category=category
        self.likes = likes
        self.idU = idU
        self.usuario = usuario

    #METODOS GET 
    def getid(self):
        return self.id

    def gettipo(self):
        return self.tipo
    
    def geturl(self):
        return self.url

    def getdate(self):
        return self.date

    def getcategory(self):
        return self.category

    def getlikes(self):
        return self.likes 

    def getidU(self):
        return self.idU

    def getusuario(self):
        return self.usuario          

    #METODOS SET
    def setid(self,id):
            self.id=id 

    def settipo(self,tipo):
        self.tipo=tipo
    
    def seturl(self,url):
        self.url=url

    def setdate(self,date):
        self.date=date

    def setcategory(self,category):
        self.category=category

    def setlikes(self, likes):
        self.likes=self.likes + 1

    def setidU(self,idU):
            self.idU=idU

    def setusuario(self,usuario):
            self.usuario=usuario                  
 
    #METODO DE INFORMACION
    def infopublicacion(self):
        return{
            "id":self.id,
            "tipo":self.tipo,
            "url":self.url,
            "date":self.date,
            "category":self.category,
            "likes":self.likes,
            "idUsuario":self.idU,
            "usuario": self.usuario    
        }