from controllerBar import ControllerBar
from order import Order


controller = ControllerBar()

def listCategory():
    print("---- MENU ----")
    categorys = controller.getCategorys()
    for id,cate in categorys.items():
        print(cate.getName())
        print("----")
        products = controller.listProducts(cate.getName())
        for prod in products:
            print("\t",prod)
        print("----")
        
controller.loadCategorys()
controller.loadProducts()

while True:
    listCategory()
    table = input("Table: ")
    if table == "0":
        break
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
    
orders = controller.getOrders()    
for id,ord in orders.items():
        print(id,ord.toString())