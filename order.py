from datetime import datetime

class Order:
    def __init__(self,table,products):
        self.__table = table
        self.__products = products
        self.__date = datetime.now()
        self.__tprice = 0.0

    def getTabla(self):
        return self.__table

    def getProducts(self):
        return self.__products

    def getDate(self):
        return self.__date

    def getTprice(self):
        return self.__tprice

    def getTprice(self):
        products = self.__products
        for x in products:
            self.__tprice += x.getPrice()
        return self.__tprice

    def toString(self):
        price = self.getTprice()
        products = ""
        produ = self.__products
        for x in produ:
            products += x.getName() + " "
        result = "Table: " + str(self.__table)+" / Date: "+str(self.__date)+" / Products: "+str(products)+" / Total price: "+str(price)
        return result
