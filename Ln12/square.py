import turtle
turtle.Screen().bgcolor("blue")
turtle.Screen().setup(300,400)
polygon=turtle.Turtle()
num_sides=4
side_lenght=70
angle=360/num_sides
for i in range(num_sides):
    polygon.forward(side_lenght)
    polygon.right(angle)
turtle.done()