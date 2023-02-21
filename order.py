from datetime import datetime

class Order:
    def __init__(self,id,order,table,numclients,client,waiter,creationdate,lines,state):
        if id == None:
            self.__id = 0
        else:
            self.__id = id
        if order == None:
            self.__order = 0
        else:
            self.__order = order
        self.__table = table
        self.__numclients = numclients
        self.__client = client
        self.__waiter = waiter
        if creationdate == None:
            self.__creationdate = datetime.now()
        else:
            self.__creationdate = creationdate
        self.__lines = lines
        self.__tprice = 0
        self.__state = state

    def getId(self):
        return self.__id
    
    def getOrder(self):
        return self.__order
    
    def getTable(self):
        return self.__table
    
    def getCreationdate(self):
        return self.__creationdate

    def getLines(self):
        return self.__lines

    def getTprice(self):
        return self.__tprice

    def getState(self):
        return self.__state

    def getClient(self):
        return self.__client

    def getNumberclients(self):
        return self.__numclients

    def getWaiter(self):
        return self.__waiter

    def setId(self,id):
        self.__id = id