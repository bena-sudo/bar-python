class Invoice:
    def __init__(self,reference,client,creationdate,lines,bprice,vat,tprice,state):
        if reference == None:
            self.__reference = 0
        else:
            self.__reference = reference
        self.__client = client
        self.__creationdate = creationdate
        self.__lines = lines
        self.__bprice = bprice
        self.__vat = vat
        self.__tprice = tprice
        self.__state = state

    def getReference(self):
        return self.__reference

    def getClient(self):
        return self.__client

    def getCreationdate(self):
        return self.__creationdate

    def getLines(self):
        return self.__lines

    def getBprice(self):
        return self.__bprice

    def getVat(self):
        return self.__vat

    def getTprice(self):
        return self.__tprice
    
    def getState(self):
        return self.__state