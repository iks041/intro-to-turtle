import turtle

turtle.Screen().bgcolor("Orange")

sc = turtle.Screen()
sc.setup(400, 200)

turtle.title("Welcome to turtle's window")

board = turtle.Turtle()

for i in range(4):
    board.forward(100)
    board.left(90)
    i = i+1

turtle.done()