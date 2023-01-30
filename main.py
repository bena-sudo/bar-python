from controllerBar import ControllerBar
from order import Order
from ingredient import Ingredient
from category import Category
from product import Product
from table import Table
controller = ControllerBar()


def menuCard():
    controller.loadIngredients()
    controller.loadCategorys()
    controller.loadProducts()

    print("---- CARD ----")
    categorys = controller.getCategorys()
    for id,cate in categorys.items():
        if cate.getParent() == False:
            print(cate.getName())
            print("----")
            for id,cate2 in categorys.items():
                x = cate2.getParent()
                if x != False:
                    if x[1] == cate.getName():
                        print("\t",cate2.getName())
                        print("\t----")
                        products = controller.listProducts(cate2.getId())
                        for prod in products:
                            print("\t\t",prod)
"""
def menuCardrecursive():
    controller.loadIngredients()
    controller.loadCategorys()
    controller.loadProducts()

    categorys = controller.getCategorys
    products = controller.getProducts
    for id,cate in categorys.items():
        if cate.getParent() == False:
            pass
        
def printCategory(categorys,products,cat):
    for id,cate in categorys.items():
        x = cate.getParent()
        if x != False:
            if x[1] == cate.getName():
                printCategory()"""

def menuOptions():
    print("0.- FINISH")
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

while True:
    # SHOW MENU
    menuOptions()
    opc = int(input("Option: "))
    if opc == 0:
        print("ADEU")
        break
    elif opc == 1:
        #menuCard()
        tableName = input("Table: ") # NUMBER TABLE
        numclients = int(input("Number of clients: ")) # NUMBER CLIENTS
        client = input("Name of the client: ") # NAME CLIENT
        waiter = input("Name of the waiter: ") # WAITER
        description = input("Description of the table: ") # DESCRIPTION
        products = [] # PRODUCTS
        
        """
        while True:
            product = input("NameProduct (0 to end): ") # NAME
            if product == "0":
                break
            cuantity = int(input("Cuantity: ")) # CUANTITY
            x = controller.getProduct(product) # ADD PRODUCTS
            if x != None:
                for j in range(0,cuantity):
                    products.append(x)
            else:
                print("ERROR!")
        """

        table = Table(None,tableName,numclients,client,waiter,None,description) # TABLE
        controller.createTable(table)
        order = Order(None,table.getId(),None,False) # ORDER
        controller.createOrder(order)
        
    elif opc == 2:
        print("")
        
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
                        controller.loadIngredients()
                        lIng = controller.getIngredients()
                        print("Ingredients list:")
                        for id,ing in lIng.items():
                            print("\t"+ing.toString())
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
                        nameCat = input("Category name: ") # NAME
                        descCat = input("Category description: ") # DESCRIPTION
                        listCategory()
                        parCat = int(input("Category parent: ")) # PARENT
                        listProducts()
                        prodCat = []
                        while(True):
                            opcCat = int(input("Id product (0 to end): ")) # ADD PRODUCT
                            if opcCat == 0:
                                break
                            prodCat.append(opcCat)
                        if parCat == 0:
                            parCat = False
                        category = Category(None,nameCat,prodCat,descCat,parCat)
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
                        print("Category parent: "+str(cat.getParent()))

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

                        listCategory()
                        parCat = int(input("Category id (0 to none): ")) # CATEGORY
                        if parCat == 0:
                            parCat = False
                        cat.setParent(parCat)
                        
                        controller.updateCategory(cat)
                    # DELETE
                    elif opc == 3:
                        id = input("Category id: ")
                        controller.deleteCategory(id)
                    # LIST
                    elif opc == 4:
                        controller.loadCategorys()
                        lCat = controller.getCategorys()
                        print("Category list:")
                        for id,cat in lCat.items():
                            print("\t"+cat.toString())
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
                        namePro = input("Product name: ") # NAME
                        pricePro = input("Product price: ") # PRICE
                        descPro = input("Product description: ") # DESCRIPTION

                        listCategory() # SHOW CATEGORY
                        catPro = []
                        while(True):
                            opcCat = int(input("Id category (0 to end): ")) # ADD CATEGORY
                            if opcCat == 0:
                                break
                            catPro.append(opcCat)

                        listIngredients() # SHOW INGREDIENTS
                        ingPro = []
                        while(True):
                            opcIng = int(input("Id product (0 to end): ")) # ADD INGREDIENT
                            if opcIng == 0:
                                break
                            ingPro.append(opcIng)

                        product = Product(None,namePro,pricePro,catPro,ingPro,descPro)
                        controller.createProduct(product)
                    # MODIFY
                    elif opc == 2:
                        listProducts() # SHOW PRODUCTS
                        idPro = int(input("Product id: ")) # ID
                        pro = controller.findProductById(idPro) # GET PRODUCT
                        if pro == None:
                            print("Id not exist!")
                            break

                        print("Name: "+pro.getName())
                        print("Price: "+str(pro.getPrice()))
                        print("Category: "+str(pro.getCategory()))
                        print("Ingredient: "+str(pro.getIngredients()))
                        print("Description: "+pro.getDescription())

                        namePro = input("Product name: ") # NAME
                        if namePro != "":
                            pro.setName(namePro)
                        pricePro = float(input("Product price: (0 not to change): ")) # PRICE
                        if pricePro != 0:
                            pro.setPrice(pricePro)
                        descPro = input("Product description: ") # DESCRIPTION
                        if descPro != "":
                            pro.setDescription(descPro)
                        
                        listCategory() # SHOW CATEGORY
                        catPro = []
                        while(True):
                            opcCat = int(input("Id category (0 to end): ")) # ADD CATEGORY
                            if opcCat == 0:
                                break
                            catPro.append(opcCat)
                        pro.setCategory(catPro)

                        listIngredients() # SHOW INGREDIENTS
                        ingPro = []
                        while(True):
                            opcIng = int(input("Id product (0 to end): ")) # ADD INGREDIENT
                            if opcIng == 0:
                                break
                            ingPro.append(opcIng)
                        pro.setIngredients(ingPro)
                        controller.updateProduct(pro) # CONTROLLER
                    # DELETE
                    elif opc == 3:
                        id = input("Product id: ")
                        controller.deleteProduct(id)
                    # LIST
                    elif opc == 4:
                        controller.loadProducts()
                        lPro = controller.getProducts()
                        print("Product list:")
                        for id,pro in lPro.items():
                            print("\t"+pro.toString())
                    # DEFAULT
                    else:
                        print("Option incorrect!")
            # DEFAULT
            else:
                print("Option incorrect!")