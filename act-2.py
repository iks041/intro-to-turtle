import turtle

turtle.Screen().bgcolor("Red")

sc = turtle.Screen()
sc.setup(500, 250)

turtle.title("welcome")

board = turtle.Turtle()

for i in range(6):
    board.forward(200)
    board.left(60)
    i = i+1

turtle.done()