from product import Product
from category import Category
from ingredient import Ingredient
import requests

class ControllerBar():
    def __init__(self):
        self.__categorys = {}
        self.__products = {}
        self.__orders = {}
        self.__ingredients = {}
        self.__con = 0
        
    def loadCategorys(self):
        self.__categorys = {}
        url = "http://localhost:8069/bar_app/getAllCategorys"
        response = requests.request("GET", url)
        data = response.json()

        categorys = data["data"]
        for x in categorys:
            self.__categorys[x["id"]] = Category(x["name"],x["product"],x["description"])

    def getCategorys(self):
        return self.__categorys

    def loadProducts(self):
        self.__products = {}
        url = "http://localhost:8069/bar_app/getAllProducts"
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

    def loadIngredients(self):
        self.__ingredients = {}
        url = "http://localhost:8069/bar_app/getAllIngredients"
        response = requests.request("GET", url)
        data = response.json()
        
        categorys = data["data"]
        for x in categorys:
            self.__ingredients[x["id"]] = Ingredient(x["id"],x["name"],x["products"],x["description"])
    
    def loadIngredients(self):
        self.__ingredients = {}
        url = "http://localhost:8069/bar_app/getAllIngredients"
        response = requests.request("GET", url)
        data = response.json()
        
        categorys = data["data"]
        for x in categorys:
            self.__ingredients[x["id"]] = Ingredient(x["id"],x["name"],x["products"],x["description"])

    def getIngredients(self):
        return self.__ingredients

    def findIngredientById(self,id):
        self.__ingredients = {}
        url = "http://localhost:8069/bar_app/getIngredient/"+str(id)
        response = requests.request("GET", url=url)
        datajson = response.json()
        data = datajson["data"]    
        return Ingredient(data["id"],data["name"],data["products"],data["description"])

    #######
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
        self.__con += 1
        self.__orders[self.__con] = order

    def getOrders(self):
        return self.__orders


    # FIND

    def getOrderByTable(self,table):
        for name,ord in self.__orders.items():
            if (ord.getTable()==table):
                if (ord.getFinish()==True):
                    return ord
        return None

    def findOrderByTable(self,table):
        for name,ord in self.__orders.items():
            if (ord.getTable()==table):    
                if (ord.getFinish()==False):
                    return ord
        return None

    # CREATE

    def createIngredient(self,ingredient):
        url = "http://localhost:8069/bar_app/addIngredient"

        querystring = {
            "name":ingredient.getName(),
            "description":ingredient.getDescription(),
            "products":ingredient.getProducts()
        }
        response = requests.request("POST",url=url,json=querystring)

        if response.status_code == 201:
            print("Correct, ingredient created!")
        else:
            print(response.status_code)
            print("Error!")


    # UPDATE

    def updateIngredient(self,ingredient):
        url = "http://localhost:8069/bar_app/updateIngredient"

        querystring = {
            "id":ingredient.getId(),
            "name":ingredient.getName(),
            "description":ingredient.getDescription(),
            "products":ingredient.getProducts()
        }
        response = requests.request("PUT",url=url,json=querystring)

        if response.status_code == 200:
            print("Correct, ingredient update!")
        else:
            print("Error!")

    # DELETE

    def deleteIngredient(self,id):
        url = "http://localhost:8069/bar_app/deleteIngredient"

        querystring = {"id":id}

        response = requests.request("DELETE",url=url,json=querystring)

        if response.status_code == 200:
            print("Correct, ingredient deleted!")
        else:
            print("Error!")

    def deleteCategory(self,id):
        url = "http://localhost:8069/bar_app/deleteCategory"

        querystring = {"id":id}

        response = requests.request("DELETE",url=url,json=querystring)

        if response.status_code == 200:
            print("Correct, category deleted!")
        else:
            print("Error!")

    def deleteProduct(self,id):
        url = "http://localhost:8069/bar_app/deleteProduct"

        querystring = {"id":id}

        response = requests.request("DELETE",url=url,json=querystring)

        if response.status_code == 200:
            print("Correct, product deleted!")
        else:
            print("Error!")