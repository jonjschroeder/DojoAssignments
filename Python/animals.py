class Animal(object):
    def __init__(self, name):
        self.name = name
        self.health = 100



    def walk(self):
        self.health = self.health - 1
        return self
    def run(self):
        self.health = self.health -5
        return self
    def displayHealth(self):
        print self.name
        print self.health
        return self

class Dog(object):
    def __init__(self, name):
        super(Dog, self).__init__(name)
        self.health = 150
    def pet(self):
        self.health = self.health + 5

class Dragon(object):
    def __init__(self, name):
        super(Dragon, self).__init__(name)
        self.health = 170
    def fly(self):
        self.health = self.health - 10
        return self
    def displayHealth(self):
        print "This is a dragon"
        super(Dragon,self).displayHealth()
        return self

animal1 = Animal('Sandy')
animal1.walk().walk().walk().run().run().displayHealth()
