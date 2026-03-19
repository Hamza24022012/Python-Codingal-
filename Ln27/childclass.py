class vehicle:
    def __init__(self,fare):
       
        self.fare=fare
class bus(vehicle):
    def __init__(self,fare,count):
        self.count=count
        super().__init__(fare)
    def fare(self):
        print("fare is",self.count*self.fare)
f=bus(10,5)
f.fare()
