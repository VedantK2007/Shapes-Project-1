import turtle
turtle = turtle.Turtle()

def triangle(length, color):
  turtle.fillcolor(color)
  turtle.begin_fill()
  turtle.forward(int(length))
  turtle.left(120)
  turtle.forward(int(length))
  turtle.left(120)
  turtle.forward(int(length))
  turtle.end_fill()



def square(length, color):
  turtle.fillcolor(color)
  turtle.begin_fill()
  turtle.forward(int(length))
  turtle.left(90)
  turtle.forward(int(length))
  turtle.left(90)
  turtle.forward(int(length))
  turtle.left(90)
  turtle.forward(int(length))
  turtle.end_fill()


def circle(length, color):
  turtle.fillcolor(color)
  turtle.begin_fill()
  turtle.circle(length)
  turtle.end_fill()



userShape = input("What shape do you want to draw?")
userShape1 = input("What is the length of your shape?")
userShape2 = input("What is the color of your shape?")

if userShape == "triangle":
  triangle(userShape1, userShape2)
elif userShape == "square":
  square(userShape1, userShape2)
elif userShape == "circle":
  circle(userShape1, userShape2)

