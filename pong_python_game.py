import turtle

wn = turtle.Screen()
wn.title("PING PONG by Bobin")
wn.bgcolor("black")
wn.setup(width=800, height=600)
# wn.tracer(0)


# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(0, 0)
ball.dx = 3
ball.dy = 3


# Function
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)


# Keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")

wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

# Score
score_a = 0
score_b = 0

# Score Board
board = turtle.Turtle()
board.speed(0)
board.color("White")
board.penup()
board.hideturtle()
board.goto(0, 260)
board.write("Player A : 0     Player B : 0", align="Center", font=("Ariel", 15, "normal"))

# For closing screen on clicking close button
canvas = wn.getcanvas()
root = canvas.winfo_toplevel()  # for getting top level widget


def on_close():
    global running
    running = False


root.protocol("WM_DELETE_WINDOW", on_close)

running = True

# Main game loop
while running:  # similar to while True:
    # wn.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 280:
        ball.sety(280)
        ball.dy += -5

    if ball.ycor() < -280:
        ball.sety(-280)
        ball.dy += 5

    if ball.xcor() > 380:
        ball.goto(0, 0)
        ball.dx += -5
        score_a += 1
        board.clear()
        board.write("Player A : {}     Player B : {}".format(score_a, score_b), align="Center",
                    font=("Ariel", 15, "normal"))

    if ball.xcor() < -380:
        ball.goto(0, 0)
        ball.dx += 5
        score_b += 1
        board.clear()
        board.write("Player A : {}     Player B : {}".format(score_a, score_b), align="Center",
                    font=("Ariel", 15, "normal"))

    # Paddle and ball collisions
    if (330 < ball.xcor() < 340) and (
            paddle_b.ycor() + 50 > ball.ycor() > paddle_b.ycor() - 50):
        ball.setx(330)
        ball.dx += -5

    if (-330 > ball.xcor() > -340) and (
            paddle_a.ycor() + 50 > ball.ycor() > paddle_a.ycor() - 50):
        ball.setx(-330)
        ball.dx += 5

