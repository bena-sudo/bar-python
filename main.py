from controllerBar import ControllerBar
from order import Order
from ingredient import Ingredient
from category import Category


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

def menuOptions():
    print("0.- Finish day.")
    print("1.- Add order.")
    print("2.- Modify order.")
    print("3.- Finish order.")
    print("------------------")
    print("4.- Options administration.")

def menuAdministration():
    print("0.- Exit.")
    print("1.- Create ingredient.")
    print("2.- Modify ingredient.")
    print("3.- Delete ingredient.")
    print("4.- List ingredient.")
    print("------------------")
    print("5.- Create category.")
    print("6.- Modify category.")
    print("7.- Delete category.")
    print("8.- List category.")
    print("------------------")
    print("9.- Create product.")
    print("10.- Modify product.")
    print("11.- Delete product.")
    print("12.- List product.")
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
            if opc == 0:
                break

            elif opc == 1:
                nameIng = input("Ingredient name: ")
                descIng = input("Ingredient description: ")
                prodIng = []
                while(True):
                    opcIng = int(input("Id product (0 to end): "))
                    if opcIng == 0:
                        break
                    prodIng.append(opcIng)
                ingredient = Ingredient(None,nameIng,prodIng,descIng)
                controller.createIngredient(ingredient)

            elif opc == 2:
                idIng = int(input("Ingredient id: "))
                ing = controller.findIngredientById(id)
                if ing == None:
                    print("Id not exist!")
                    break
                nameIng = input("Ingredient name: ")
                if nameIng != "":
                    ing.setName(nameIng)
                descIng = input("Ingredient description: ")
                if descIng != "":
                    ing.setDescription(descIng)
                prodIng = []
                while(True):
                    opcIng = int(input("Id product (0 to end / -1 to clean list): "))
                    if opcIng == 0:
                        break
                    elif opcIng ==1:
                        prodIng = []
                        break
                    prodIng.append(opcIng)
                controller.updateIngredient(ing)

            elif opc == 3:
                id = input("Ingredient id: ")
                controller.deleteIngredient(id)

            elif opc == 4:
                listIngredients()
            
            elif opc == 5:
                nameCat = input("Category name: ")
                descCat = input("Category description: ")
                prodCat = []
                while(True):
                    opcCat = int(input("Id category (0 to end): "))
                    if opcCat == 0:
                        break
                    prodCat.append(opcCat)
                category = Category(None,nameCat,prodCat,descCat)
                controller.createCategory(category)

            elif opc == 6:
                idCat = int(input("Category id: "))
                cat = controller.findCategoryById(id)
                if cat == None:
                    print("Id not exist!")
                    break
                namCat = input("Category name: ")
                if namCat != "":
                    cat.setName(namCat)
                descCat = input("Category description: ")
                if descCat != "":
                    cat.setDescription(namCat)
                prodCat = []
                while(True):
                    opcCat = int(input("Id product (0 to end / -1 to clean list): "))
                    if opcCat == 0:
                        break
                    elif opcCat ==1:
                        prodCat = []
                        break
                    prodCat.append(opcIng)
                controller.updateCategory(ing)

            elif opc == 7:
                id = input("Category id: ")
                controller.deleteCategory(id)

            elif opc == 8:
                listCategory()

            else:
                print("Option incorrect.")

    else:
        print("Option incorrect.")

# TEST
orders = controller.getOrders()    
for id,ord in orders.items():
        print(id,ord.toString())