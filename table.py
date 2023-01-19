
class Table:
    def __init__(self,table,numclients,client,waiter,orders,description):
        self.__table = table
        self.__numclients = numclients
        self.__client = client
        self.__waiter = waiter
        self.__orders = orders
        self.__description = description

    def getTable(self):
        return self.__table

    def getClient(self):
        return self.__client

    def getNumberclients(self):
        return self.__numclients

    def getWaiter(self):
        return self.__waiter
    
    def getOrders(self):
        return self.__orders

    def getDescription(self):
        return self.__description