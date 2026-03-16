class vehicle:
    def __init__(self,max_speed,mileage):
        self.max_speed=max_speed
        self.mileage=mileage
model1= vehicle(160,20)
model2= vehicle(210,40)

print("model1 max speed",model1.max_speed)
print("model1 mileage",model1.mileage)

print("model2 max speed",model2.max_speed)
print("model2 mileage",model2.mileage)
