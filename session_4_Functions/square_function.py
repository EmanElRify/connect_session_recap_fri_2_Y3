import turtle
pen = turtle.Turtle()
# square("yellow", 20)

def square(color,length):
    turtle.color(color)
    for side in range(4):
        turtle.forward(length)
        turtle.right(90)
        
    

# square(20, "yellow") #TypeError
square("yellow", 20)
turtle.done()