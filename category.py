class Category:
    def __init__(self,name,products,description):
        self.__name = name
        self.__products = products
        self.__description = description

    def getName(self):
        return self.__name
    
    def getProducts(self):
        return self.__products
    
    def getDescription(self):
        return self.__description