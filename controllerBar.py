from product import Product
from category import Category
import requests

class ControllerBar():
    def __init__(self):
        self.__categorys = {}
        self.__products = {}
        self.__orders = {}
        self.__con = 1
        
    def loadCategorys(self):
        url = "http://localhost:8069/bar_app/category"

        response = requests.request("GET", url)
        data = response.json()

        categorys = data["data"]
        for x in categorys:
            self.__categorys[x["id"]] = Category(x["name"],x["product"],x["description"])

    def getCategorys(self):
        return self.__categorys

    def loadProducts(self):
        url = "http://localhost:8069/bar_app/product"

        response = requests.request("GET", url)
        data = response.json()

        products = data["data"]
        for x in products:
            name = x["name"]
            price = x["price"]
            category = x["category"]
            ingredients = x["ingredients"]
            description = x["description"]
            self.__products[name] = Product(name,price,category,ingredients,description)

    def getProducts(self):
        return self.__products

    def listProducts(self,category):
        products = []
        for name,prod in self.__products.items():
            cate = prod.getCategory()
            if cate[1] == category:
                products.append(prod.getName())
        return products

    def getProduct(self,nameProduct):
        for name,prod in self.__products.items():
            if (prod.getName()==nameProduct):
                return prod
        return None

    def addOrder(self,order):
        self.__orders[self.__con] = order
        self.__con += 1

    def getOrders(self):
        return self.__orders