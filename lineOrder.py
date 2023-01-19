class LineOrder:
    def __init__(self,order,cuantity,product,description):
        self.__order = order
        self.__cuantity = cuantity
        self.__product = product
        self.__description = description

    def getOrder(self):
        return self.__order
    
    def getCuantitity(self):
        return self.__cuantity

    def getProduct(self):
        return self.__product

    def getDescription(self):
        return self.__description