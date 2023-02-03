
class Table:
    def __init__(self,id,table,orders,description):
        if id == None:
            self.__id = 0
        else:
            self.__id = id
        self.__table = table
        
        if orders == None:
            self.__orders = None
        else:
            self.__orders = orders
        self.__description = description

    def getId(self):
        return self.__id

    def getTable(self):
        return self.__table
    
    def getOrders(self):
        return self.__orders

    def getDescription(self):
        return self.__description
    
    def setId(self,id):
        self.__id = id