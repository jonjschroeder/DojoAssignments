class Product(object):
    def __init__(self, price, item_name, weight, brand, cost):
        self.price = price
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.cost = cost
        self.status = "for sale"

    def sold(self):
        self.status = "Sold"
        return self
    def tx(self, x):
        self.price = self.price + self.price*(x)
        return self
    def ret(self, y):
        if y == "defective":
            self.price = 0
        if y == "like new":
            self.status = "for sale"
        if y == "opened":
            self.price = self.price - self.price*(0.20)
        return self
    def displayinfo(self):
        print '{} {} {} {} {}'.format(self.price, self.item_name, self.weight, self.brand, self.cost)





product1=Product(100,"White Album LP",1,"Apple",100)
product1.ret('opened').displayinfo()
