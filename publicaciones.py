class publicaciones:
    def __init__(self, id, type, url, date, category, like): 
        self.id = id
        self.type=type
        self.url=url
        self.date=date
        self.category=category
        self.like = like

    #METODOS GET 
    def getid(self):
        return self.id

    def gettype(self):
        return self.type
    
    def geturl(self):
        return self.url

    def getdate(self):
        return self.date

    def getcategory(self):
        return self.category

    def getlikes(self):
        return self.like    

    #METODOS SET
    def settype(self,id):
            self.id=id 

    def settype(self,type):
        self.type=type
    
    def seturl(self,url):
        self.url=url

    def setdate(self,date):
        self.date=date

    def setcategory(self,category):
        self.category=category

    def setlikes(self):
        self.like=self.like + 1    
 
    #METODO DE INFORMACION
    def infopublicacion(self):
        return{
            "type":self.type,
            "url":self.url,
            "date":self.date,
            "category":self.category,
            "likes":self.likes    
        }