class parrot:
    species="bird"
    def __init__(self,name,age):
        self.name=name
        self.age=age
species1=parrot("S1",3)
species2=parrot("S2",3)
print("Name of species1 is",species1.name,"& age is ",species1.age)
print("Name of species2 is",species2.name,"& age is ",species2.age)
print(species1.species)
print(species2.species)