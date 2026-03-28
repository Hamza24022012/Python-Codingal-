from abc import ABC,abstractmethod

class animal(ABC):
    def move(self):
        pass

class human(animal):
    def move(self):
        print("I can walk & run")

class dog(animal):
    def move(self):
        print("I can walk & run")


class snake(animal):
    def move(self):
        print("I can slither")

class lion(animal):
    def move(self):
        print("I can walk & run")

a=human()
a.move()
b=snake()
b.move()
c=dog()
c.move()
d=lion()
d.move()