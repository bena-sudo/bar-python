from controllerBar import ControllerBar
from order import Order
from ingredient import Ingredient
from category import Category
from product import Product


controller = ControllerBar()

def listCard():
    print("---- CARD ----")
    categorys = controller.getCategorys()
    for id,cate in categorys.items():
        print(cate.getName())
        print("----")
        products = controller.listProducts(cate.getName())
        for prod in products:
            print("\t",prod)
        print("----")
        
def listIngredients():
    controller.loadIngredients()
    lIng = controller.getIngredients()
    print("Ingredients list:")
    for id,ing in lIng.items():
        print("\t"+str(id) + " " + ing.getName())

def listCategory():
    controller.loadCategorys()
    lCat = controller.getCategorys()
    print("Category list:")
    for id,cat in lCat.items():
        print("\t"+str(id) + " " + cat.getName())

def listProducts():
    controller.loadProducts()
    lPro = controller.getProducts()
    print("Product list:")
    for id,pro in lPro.items():
        print("\t"+str(pro.getId()) + " " + pro.getName())

def menuOptions():
    print("0.- Finish day.")
    print("1.- Add order.")
    print("2.- Modify order.")
    print("3.- Finish order.")
    print("4.- Options administration.")
    print("------------------")

def menuAdministration():
    print("0.- Exit.")
    print("1.- Menu ingredient.")
    print("2.- Menu category.")
    print("3.- Menu product.")
    print("------------------")

def menuCRUD(option):
    print("0.- Exit.")
    print("1.- Add "+option+".")
    print("2.- Modify "+option+".")
    print("3.- Delete "+option+".")
    print("4.- List "+option+".")
    print("------------------")

controller.loadCategorys()
controller.loadProducts()
controller.loadIngredients()

while True:
    # SHOW MENU
    menuOptions()
    opc = int(input("Option: "))
    if opc == 0:
        # GET ALL ORDERS
        orders = controller.getOrders()
        # CALCULATE TOTAL PRICE OF THE DAY
        total = 0 
        for id,ord in orders.items():
            total += ord.getTprice()
        print("Total cash: ",total)
        break

    elif opc == 1:
        # SHOW CART
        listCard()
        # NUMBER TABLE
        table = input("Table: ")
        order = controller.findOrderByTable(table)
        if order == None:
            # NUMBER CLIENTS
            numclients = int(input("Number of clients: "))
            # NAME CLIENT
            client = input("Name of the client: ")
            # WAITER
            waiter = input("Name of the waiter: ")
            # PRODUCTS
            products = []
            while True:
                # NAME
                product = input("NameProduct (0 to end): ")
                if product == "0":
                        break
                # CUANTITY
                cuantity = int(input("Cuantity: "))
                # ADD PRODUCTS
                x = controller.getProduct(product)
                if x != None:
                    for j in range(0,cuantity):
                        products.append(x)
                else:
                    print("ERROR!")
            # ORDER
            order = Order(table,numclients,client,waiter,products)
            controller.addOrder(order)
        else:
            print("Table is exist.")
        
    elif opc == 2:
        # NUMBER TABLE
        table = input("Table: ")
        order = controller.findOrderByTable(table)
        if order == None:
            print("Table is not exist.")
        else:
            while True:
                # NAME
                product = input("NameProduct (0 to end): ")
                if product == "0":
                        break
                cuantity = int(input("Cuantity: "))
                # ADD PRODUCTS
                x = controller.getProduct(product)
                if x != None:
                    for j in range(0,cuantity):
                        products.append(x)
                else:
                    print("ERROR!")
        
    elif opc == 3:
        # NUMBER TABLE
        table = input("Table: ")
        # GET ORDER
        order = controller.findOrderByTable(table)
        if (order == None):
            print("Table is not exist.")
        else:
            order.getFinishOrder()

    elif opc == 4:
        while True:
            # SHOW MENU
            menuAdministration()
            opc = int(input("Option: "))
            # EXIT
            if opc == 0:
                break
            # INGREDIENT
            elif opc == 1:
                menuCRUD("Ingredient")
                while True:
                    opc = int(input("Option: "))
                    # EXIT
                    if opc == 0:
                        break
                    # ADD
                    elif opc == 1:
                        nameIng = input("Name: ")
                        descIng = input("Description: ")
                        prodIng = []
                        while(True):
                            opcIng = int(input("Id product (0 to end): "))
                            if opcIng == 0:
                                break
                            prodIng.append(opcIng)
                        ingredient = Ingredient(None,nameIng,prodIng,descIng)
                        controller.createIngredient(ingredient)
                    # MODIFY
                    elif opc == 2:
                        idIng = input("Ingredient id: ")
                        ing = controller.findIngredientById(idIng)
                        if ing == None:
                            print("Id not exist!")
                            break
                        # INFO
                        print("ID: "+ing.getId())
                        print("Name: "+ing.getName())
                        print("Products: "+str(ing.getProducts()))
                        print("Description: "+ing.getDescription())

                        nameIng = input("Ingredient name: ")
                        if nameIng != "":
                            ing.setName(nameIng)
                        descIng = input("Ingredient description: ")
                        if descIng != "":
                            ing.setDescription(descIng)
                        prodIng = []
                        listProducts()
                        while(True):
                            opcIng = int(input("Id product (0 to end / -1 to clean list): "))
                            if opcIng == 0:
                                break
                            elif opcIng ==1:
                                prodIng = []
                                break
                            prodIng.append(opcIng)
                        controller.updateIngredient(ing)
                    # DELETE
                    elif opc == 3:
                        id = input("Ingredient id: ")
                        controller.deleteIngredient(id)
                    # LIST
                    elif opc == 4:
                        listIngredients()
                    # DEFAULT
                    else:
                        print("Option incorrect!")
            # CATEGORY
            elif opc == 2:
                menuCRUD("Category")
            # PRODUCT
            elif opc == 3:
                menuCRUD("Product")

            # DEFAULT
            else:
                print("Option incorrect!")
"""
            
            
            elif opc == 5:
                nameCat = input("Category name: ")
                descCat = input("Category description: ")
                prodCat = []
                while(True):
                    opcCat = int(input("Id product (0 to end): "))
                    if opcCat == 0:
                        break
                    prodCat.append(opcCat)
                category = Category(None,nameCat,prodCat,descCat)
                controller.createCategory(category)

            elif opc == 6:
                idCat = int(input("Category id: "))
                cat = controller.findCategoryById(idCat)
                if cat == None:
                    print("Id not exist!")
                    break
                namCat = input("Category name: ")
                if namCat != "":
                    cat.setName(namCat)
                descCat = input("Category description: ")
                if descCat != "":
                    cat.setDescription(descCat)
                prodCat = []
                listProducts()
                while(True):
                    opcCat = int(input("Id product (0 to end / -1 to clean list): "))
                    if opcCat == 0:
                        break
                    elif opcCat ==1:
                        prodCat = []
                        break
                    prodCat.append(opcCat)
                controller.updateCategory(cat)

            elif opc == 7:
                id = input("Category id: ")
                controller.deleteCategory(id)

            elif opc == 8:
                listCategory()


            elif opc == 9:
                namePro = input("Product name: ")
                pricePro = input("Product price: ")
                catPro = input("Product category id: (0 to null) ")
                if catPro == "0":
                    catPro = ""
                descCat = input("Product description: ")
                ingCat = []
                while(True):
                    opcPro = int(input("Id ingredient (0 to end): "))
                    if opcPro == 0:
                        break
                    ingCat.append(opcPro)
                product = Product(None,namePro,pricePro,catPro,ingCat,descCat)
                controller.createProduct(product)

            elif opc == 10:
                idPro = int(input("Product id: "))
                pro = controller.findProductById(id)
                if pro == None:
                    print("Id not exist!")
                    break
                namePro = input("Product name: ")
                if namePro != "":
                    pro.setName(namePro)
                pricePro = float(input("Product price: (0 para no cambiar)"))
                if pricePro != 0:
                    pro.setPrice(pricePro)
                catPro = input("Category id: ")
                if catPro != "":
                    pro.setCategory(catPro)
                descPro = input("Category description: ")
                if descPro != "":
                    pro.setDescription(descPro)
                ingPro = []
                listIngredients()
                while(True):
                    opcIng = int(input("Id product (0 to end / -1 to clean list): "))
                    if opcIng == 0:
                        break
                    elif opcIng == 1:
                        ingPro = []
                        break
                    ingPro.append(opcIng)
                controller.updateProduct(pro)

            elif opc == 11:
                id = input("Product id: ")
                controller.deleteProduct(id)

            elif opc == 12:
                listProducts()
"""

# TEST
orders = controller.getOrders()    
for id,ord in orders.items():
        print(id,ord.toString())