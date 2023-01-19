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
    if opc == 1:
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
        id = input("Order id:")
        controller.confirmOrder(id)

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
                while True:
                    menuCRUD("Ingredient")
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
                            opcIng = int(input("Id product (0 to end): "))
                            if opcIng == 0:
                                break
                            else:
                                prodIng.append(opcIng)
                        ing.setProducts(prodIng)
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
                while True:
                    menuCRUD("Category")
                    opc = int(input("Option: "))
                    # EXIT
                    if opc == 0:
                        break
                    # ADD
                    elif opc == 1:
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
                    # MODIFY
                    elif opc == 2:
                        idCat = int(input("Category id: "))
                        cat = controller.findCategoryById(idCat)
                        if cat == None:
                            print("Id not exist!")
                            break
                        # INFO
                        print("Name: "+cat.getName())
                        print("Products: "+str(cat.getProducts()))
                        print("Description: "+cat.getDescription())

                        namCat = input("Category name: ")
                        if namCat != "":
                            cat.setName(namCat)
                        descCat = input("Category description: ")
                        if descCat != "":
                            cat.setDescription(descCat)
                        prodCat = []
                        listProducts()
                        while(True):
                            opcCat = int(input("Id product (0 to end): "))
                            if opcCat == 0:
                                break
                            prodCat.append(opcCat)
                        cat.setProducts(prodCat)
                        controller.updateCategory(cat)
                    # DELETE
                    elif opc == 3:
                        id = input("Category id: ")
                        controller.deleteCategory(id)
                    # LIST
                    elif opc == 4:
                        listCategory()
                    # DEFAULT
                    else:
                        print("Option incorrect!")
            # PRODUCT
            elif opc == 3:
                while True:
                    menuCRUD("Product")
                    opc = int(input("Option: "))
                    # EXIT
                    if opc == 0:
                        break
                    # ADD
                    elif opc == 1:
                        namePro = input("Product name: ")
                        pricePro = input("Product price: ")
                        descCat = input("Product description: ")
                        ingCat = []
                        while(True):
                            opcPro = int(input("Id ingredient (0 to end): "))
                            if opcPro == 0:
                                break
                            ingCat.append(opcPro)
                        product = Product(None,namePro,pricePro,catPro,ingCat,descCat)
                        controller.createProduct(product)
                    # MODIFY
                    elif opc == 2:
                        idPro = int(input("Product id: "))
                        pro = controller.findProductById(idPro)
                        if pro == None:
                            print("Id not exist!")
                            break
                        print("Name: "+pro.getName())
                        print("Price: "+str(pro.getPrice()))
                        print("Category: "+str(pro.getCategory()))
                        print("Ingredient: "+str(pro.getIngredients()))
                        print("Description: "+pro.getDescription())

                        namePro = input("Product name: ")
                        if namePro != "":
                            pro.setName(namePro)
                        pricePro = float(input("Product price: (0 para no cambiar)"))
                        if pricePro != 0:
                            pro.setPrice(pricePro)
                        descPro = input("Category description: ")
                        if descPro != "":
                            pro.setDescription(descPro)
                        ingPro = []
                        listIngredients()
                        while(True):
                            opcIng = int(input("Id product (0 to end): "))
                            if opcIng == 0:
                                break
                            ingPro.append(opcIng)
                        pro.setIngredients(ingPro)
                        controller.updateProduct(pro)

                    # DELETE
                    elif opc == 3:
                        id = input("Product id: ")
                        controller.deleteProduct(id)
                    # LIST
                    elif opc == 4:
                        listProducts()
                    # DEFAULT
                    else:
                        print("Option incorrect!")
            # DEFAULT
            else:
                print("Option incorrect!")