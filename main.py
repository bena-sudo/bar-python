from controllerBar import ControllerBar
from order import Order


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
        
def menuOptions():
    print("0.- Finish day.")
    print("1.- Add order.")
    print("2.- Modify order.")
    print("3.- Finish order.")

controller.loadCategorys()
controller.loadProducts()

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
            # ADD PRODUCTS
            x = controller.getProduct(product)
            if x != None:
                products.append(x)
            else:
                print("ERROR!")
        # ORDER
        order = Order(table,numclients,client,waiter,products)
        controller.addOrder(order)

    elif opc == 2:
        # NUMBER TABLE
        table = input("Table: ")
        order = controller.getOrderByTable(table)
        while True:
            # NAME
            product = input("NameProduct (0 to end): ")
            if product == "0":
                    break
            # ADD PRODUCTS
            x = controller.getProduct(product)
            if x != None:
                order.addProduct(x)
            else:
                print("ERROR!")
    
    elif opc == 3:
        # NUMBER TABLE
        table = input("Table: ")
        # GET ORDER
        order = controller.getOrderByTable(table)
        order.getFinishOrder()
    
    else:
        print("Option incorrect")

# TEST
orders = controller.getOrders()    
for id,ord in orders.items():
        print(id,ord.toString())