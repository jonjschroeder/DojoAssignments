class Bike(object):
    def __init__(self, price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0

    def displayInfo(self):
        print '{} {} {}'.format(self.price,self.max_speed,self.miles)
        return self
    def ride(self):
        self.miles += 10
        print "Riding" + str(self.miles)
        return self
    def reverse(self):
        if self.miles>4:
            self.miles -= 5
        print self.miles
        return self


bike1 = Bike(200, "25mph")
bike1.ride().ride().ride().reverse().displayInfo()
#.ride().reverse().displayInfo()
