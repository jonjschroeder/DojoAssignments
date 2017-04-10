class Car(object):
    def __init__(self, price,speed,fuel,mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage


    def tx(self):
        if self.price>10000:
            self.price = self.price + self.price*0.15
        else:
            self.price = self.price + self.price*0.12
        return self.price
        #return self
    def displayInfo(self):
        print '{} {} {} {}'.format(self.price,self.speed,self.fuel,self.mileage)
        return self
car1 = Car(11000,35,1,17)
car2 = Car(13000,35,"Full",17)
car3 = Car(8000,35,"Empty",17)
car4 = Car(5000,35,"Full",17)
car5 = Car(55000,35,"No Tank",17)
car6 = Car(22000,35,"Full",17)

#"""car1.tx()
car1.displayInfo()
car2.tx()
car2.displayInfo()
car3.tx()
car3.displayInfo()
car4.tx()
car4.displayInfo()
car5.tx()
car5.displayInfo()
car6.tx()
car6.displayInfo()
#.displayInfo()"""
