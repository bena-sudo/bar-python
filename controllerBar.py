from product import Product
from category import Category
from ingredient import Ingredient
import requests
import json

class ControllerBar():
    def __init__(self):
        self.__categorys = {}
        self.__products = {}
        self.__orders = {}
        self.__ingredients = {}
        self.__con = 0

    # LOAD 
    def loadCategorys(self):
        self.__categorys = {}
        url = "http://localhost:8069/bar_app/getAllCategorys"
        response = requests.request("GET", url)
        data = response.json()

        categorys = data["data"]
        for x in categorys:
            self.__categorys[x["id"]] = Category(x["id"],x["name"],x["product"],x["description"])

    def loadProducts(self):
        self.__products = {}
        url = "http://localhost:8069/bar_app/getAllProducts"
        response = requests.request("GET", url)
        data = response.json()

        products = data["data"]
        for x in products:
            id = x["id"]
            name = x["name"]
            price = x["price"]
            category = x["category"]
            ingredients = x["ingredients"]
            description = x["description"]
            self.__products[name] = Product(id,name,price,category,ingredients,description)

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

    # GET
    def getProducts(self):
        return self.__products

    def getCategorys(self):
        return self.__categorys

    def getIngredients(self):
        return self.__ingredients

    # OTROS
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


    # BUSCAR
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

    # FIND
    def findIngredientById(self,idd):
        self.__ingredients = {}
        url = "http://localhost:8069/bar_app/getIngredient/"+str(idd)
        response = requests.request("GET", url)
        if response.status_code == 200:
            jsondata = response.json()
        else:
            print("Error GET")
            return None
        data = jsondata["data"]    
        ingredient = Ingredient(data["id"],data["name"],data["products"],data["description"])
        return ingredient

    def findCategoryById(self,id):
        self.__categorys = {}
        url = "http://localhost:8069/bar_app/getCategory/"+str(id)
        response = requests.request("GET", url)
        datajson = response.json()
        data = datajson["data"] 

        for x in data:
            cat = Category(x["id"],x["name"],x["product"],x["description"]) 
        return cat

    def findProductById(self,id):
        self.__products = {}
        url = "http://localhost:8069/bar_app/getProduct/"+str(id)
        response = requests.request("GET", url)
        datajson = response.json()
        data = datajson["data"]    
        return Product(data["id"],data["name"],data["price"],data["category"],data["ingredients"],data["description"])

    # CREATE
    def createIngredient(self,ingredient):
        url = "http://localhost:8069/bar_app/addIngredient"

        querystring = {
            "name":ingredient.getName(),
            "description":ingredient.getDescription(),
            "products":ingredient.getProducts()
        }
        response = requests.request("POST",url=url,json=querystring)

        if response.status_code == 200:
            print("Correct, ingredient created!")
        else:
            print(response.status_code)
            print("Error!")

    def createCategory(self,category):
        url = "http://localhost:8069/bar_app/addCategory"

        querystring = {
            "name":category.getName(),
            "description":category.getDescription(),
            "product":category.getProducts()
        }
        response = requests.request("POST",url=url,json=querystring)

        if response.status_code == 200:
            print("Correct, ingredient created!")
        else:
            print(response.status_code)
            print("Error!")

    def createProduct(self,product):
        url = "http://localhost:8069/bar_app/addProduct"

        querystring = {
            "name":product.getName(),
            "price":product.getPrice(),
            "category":product.getCategory(),
            "ingredients":product.getIngredients(),
            "description":product.getDescription()
        }
        response = requests.request("POST",url=url,json=querystring)

        if response.status_code == 200:
            print("Correct, product created!")
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
            print("Correct, category update!")
        else:
            print("Error!")

    def updateCategory(self,category):
        url = "http://localhost:8069/bar_app/updateCategory"

        querystring = {
            "id":category.getId(),
            "name":category.getName(),
            "description":category.getDescription(),
            "product":category.getProducts()
        }
        response = requests.request("PUT",url=url,json=querystring)

        if response.status_code == 200:
            print("Correct, category update!")
        else:
            print("Error!")

    def updateProduct(self,product):
        url = "http://localhost:8069/bar_app/updateProduct"

        querystring = {
            "name":product.getName(),
            "price":product.getPrice(),
            "category":product.getCategory(),
            "ingredients":product.getIngredients(),
            "description":product.getDescription()
        }
        response = requests.request("PUT",url=url,json=querystring)

        if response.status_code == 200:
            print("Correct, product update!")
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