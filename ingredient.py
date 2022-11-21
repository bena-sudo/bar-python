class Ingredient:
    def __init__(self,name,product,description):
        self.__name = name
        self.__product = product
        self.__description = description

    def getName(self):
        self.__name
    
    def getProduct(self):
        self.__product
    
    def getDescription(self):
        self.__description