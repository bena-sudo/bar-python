class Ingredient:
    def __init__(self,id,name,products,description):
        if id == None:
            self.__id = 0
        else:
            self.__id = id
        self.__name = name
        self.__products = products
        self.__description = description

    def getId(self):
        return self.__id

    def getName(self):
        return self.__name
    
    def getProducts(self):
        return self.__products
    
    def getDescription(self):
        return self.__description

    def setId(self,id):
        self.__id = id

    def setName(self,name):
        self.__name = name

    def setProducts(self,products):
        self.__products = products

    def setDescription(self,description):
        self.__description = description