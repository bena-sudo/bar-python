class Category:
    def __init__(self,id,name,products,description,parent):
        if id == None:
            self.__id = 0
        else:
            self.__id = id
        self.__name = name
        self.__products = products
        self.__description = description
        self.__parent = parent
          
    def getId(self):
        return self.__id

    def getName(self):
        return self.__name
    
    def getProducts(self):
        return self.__products
    
    def getDescription(self):
        return self.__description

    def getParent(self):
        return self.__parent
    
    def setId(self,id):
        self.__id = id

    def setName(self,name):
        self.__name = name

    def setProducts(self,products):
        self.__products = products

    def setDescription(self,description):
        self.__description = description

    def setParent(self,parent):
        self.__parent = parent

    def toString(self):
        res = str(self.__id)+ " / Name: " + self.__name + " / Products: " + str(self.__products) + " / Category parent: " + str(self.__parent) + " / Description: " + str(self.__description)
        return res