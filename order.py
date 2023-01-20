from datetime import datetime

class Order:
    def __init__(self,order,table,lines,state):
        self.__order = order
        self.__table = table
        self.__creationdate = datetime.now()
        self.__lines = lines
        self.__tprice = 0
        self.__state = state

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