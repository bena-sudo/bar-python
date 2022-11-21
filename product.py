class Product:
    def __init__(self,name,price,category,ingredients,description):
        self.__name = name
        self.__price = price
        self.__category = category
        self.__ingredients = ingredients
        self.__description = description

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