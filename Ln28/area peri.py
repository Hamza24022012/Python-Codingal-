class circle:
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        print("Area=",3.142*self.radius*self.radius)
    def perimeter(self):
        print("Perimeter=",2*3.142*self.radius)
r1=circle(2)
r2=circle(3)
r1.area()
r1.perimeter()
r2.area()
r2.perimeter()