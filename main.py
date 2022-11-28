from controllerBar import ControllerBar
from order import Order


controller = ControllerBar()

def listCategory():
    print("---- CARTA ----")
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
    menuOptions()
    opc = int(input("Oprtion: "))
    if opc == 0:
        orders = controller.getOrders()
        total = 0    
        for id,ord in orders.items():
            total += ord.getTprice()
        print("Total cash: ",total)
        break
    elif opc == 1:
        listCategory()
        table = input("Table: ")
        products = []
        while True:
            product = input("NameProduct: ")
            if product == "0":
                    break
            x = controller.getProduct(product)
            if x != None:
                products.append(x)
            else:
                print("ERROR!")
        order = Order(table,products)
        controller.addOrder(order)
    elif opc == 2:
        table = input("Table: ")
        products = []
        while True:
            product = input("NameProduct: ")
            if product == "0":
                    break
            x = controller.getProduct(product)
            if x != None:
                products.append(x)
            else:
                print("ERROR!")



orders = controller.getOrders()    
for id,ord in orders.items():
        print(id,ord.toString())