


class Call(object):
    def __init__(self,name,number,calltime,reason):
        self.id = ".join(random.choice(string.ascii_uppercase + string.digits) for _ in range(12))"
        self.name = name
        self.number = number
        self.calltime = calltime
        self.reason = reason

    def displayinfo(self):
        print '{} {} {} {} {}'.format(self.id, self.name, self.number,self.calltime,self.reason)

class CallCenter(object):
    def __init__(self):
        self.calls = []
        self.qsize =  0


    def add(self, x):
        self.qsize = self.qsize + 1
        self.calls.append(x)
        return self
    def remove(self, y):
        self.qsize = self.qsize - 1
        self.calls.append(y)
        return self

    def info(self):










caller = Call(23445, "Jonathan", "434-3333", "12:00 PM", "Reasons")
animal1.walk().walk().walk().run().run().displayHealth()
