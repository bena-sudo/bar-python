from datetime import datetime

class Order:
    def __init__(self,table,numclients,client,waiter,products):
        self.__table = table
        self.__numClients = numclients
        self.__client = client
        self.__waiter = waiter
        self.__products = products
        self.__date = datetime.now()
        self.__tprice = 0.0
        self.__finish = False

    def getTable(self):
        return self.__table
    
    def getNumClients(self):
        return self.__numClients
    
    def getClient(self):
        return self.__client

    def getWaiter(self):
        return self.__waiter

    def getProducts(self):
        return self.__products

    def getDate(self):
        return self.__date

    def getTprice(self):
        return self.__tprice

    def getFinish(self):
        return self.__finish

    def addProduct(self,product):
        self.__products.append(product)

    def getFinishOrder(self):
        self.__finish = True
        products = self.__products
        for x in products:
            self.__tprice += x.getPrice()
        return self.__tprice

    def toString(self):
        products = ""
        produ = self.__products
        for x in produ:
            products += x.getName() + ", "
        result = "Table: " + str(self.__table)+ " / Finish: " + str(self.__finish) + " / Num clientes: " + str(self.__numClients)+ " / Client: "+ str(self.__client) + " / Waiter: "+ str(self.__waiter) +" / Date: "+str(self.__date)+" / Products: "+str(products)+" / Total price: "+str(self.__tprice)
        return result
