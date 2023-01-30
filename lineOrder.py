class LineOrder:
    def __init__(self,id,order,cuantity,product,description):
        if id == None:
            self.__id = 0
        else:
            self.__id = id
        self.__order = order
        self.__cuantity = cuantity
        self.__product = product
        self.__description = description

    def getId(self):
        return self.__id

    def getOrder(self):
        return self.__order
    
    def getCuantitity(self):
        return self.__cuantity

    def getProduct(self):
        return self.__product

    def getDescription(self):
        return self.__description