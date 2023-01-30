class Product:
    def __init__(self,id,name,price,category,ingredients,description):
        if id == None:
            self.__id = 0
        else:
            self.__id = id
        self.__name = name
        self.__price = price
        self.__category = category
        self.__ingredients = ingredients
        self.__description = description

    def getId(self):
        return self.__id

    def getName(self):
        return self.__name
    
    def getPrice(self):
        return self.__price

    def getCategory(self):
        return self.__category

    def getIngredients(self):
        return self.__ingredients

    def getDescription(self):
        return self.__description

    def setId(self,id):
        self.__id = id

    def setName(self,name):
        self.__name = name

    def setPrice(self,price):
        self.__price = price

    def setCategory(self,category):
        self.__category = category

    def setIngredients(self,ingredients):
        self.__ingredients = ingredients

    def setDescription(self,description):
        self.__description = description

    def toString(self):
        res = str(self.__id) + " " + self.__name + " " + str(self.__price) + " " + str(self.__category) + " " + str(self.__category) + " " + self.__description
        return res