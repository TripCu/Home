import turtle
import random

# Set up the screen
screen = turtle.Screen()
screen.title("Pong")
screen.bgcolor("black")
screen.setup(width=800, height=600)


# Initialize scores
left_score = 0
right_score = 0

# Creates the left scoreboard
left_scoreboard = turtle.Turtle()
left_scoreboard.speed(0)
left_scoreboard.color("white")
left_scoreboard.penup()
left_scoreboard.hideturtle()
left_scoreboard.goto(-350, 270)

# Creates the right scoreboard
right_scoreboard = turtle.Turtle()
right_scoreboard.speed(0)
right_scoreboard.color("white")
right_scoreboard.penup()
right_scoreboard.hideturtle()
right_scoreboard.goto(350, 270)

# Creates the ball
ball = turtle.Turtle()
ball.shape("circle")
ball.color("white")
ball.shapesize(1, 1)
ball.penup()
ball.goto(0, 0)


#Generate random dy values between  1 and 5
ball.dx = (7)
ball.dy = random.uniform(1,5)


# Create the left paddle
left_paddle = turtle.Turtle()
left_paddle.shape("square")
left_paddle.color("white")
left_paddle.shapesize(5,1) # width = 5 and height = 1
left_paddle.penup()
left_paddle.goto(-375, 0)

# Create the right paddle
right_paddle = turtle.Turtle()
right_paddle.shape("square")
right_paddle.color("white")
right_paddle.shapesize(5,1) # width = 5 and height = 1
right_paddle.penup()
right_paddle.goto(375, 0)

#creates the verticle line 
dashed_line = turtle.Turtle()
dashed_line.color("white")
dashed_line.penup()
dashed_line.hideturtle() # hide turtle cursor
dashed_line.goto(0, -screen.window_height()/2)
dashed_line.pendown()
dashed_line.left(90) # rotate the turtle to point upwards

for i in range(-int(screen.window_height()/2), int(screen.window_height()/2), 30):
    dashed_line.forward(20)
    dashed_line.penup()
    dashed_line.forward(10)
    dashed_line.pendown()


def move_left_paddle_up():
    y = left_paddle.ycor()
    y += 50
    left_paddle.sety(y)

# Move the left paddle down
def move_left_paddle_down():
    y = left_paddle.ycor()
    y -= 50
    left_paddle.sety(y)

def move_right_paddle_up():
    y = right_paddle.ycor()
    y += 50
    right_paddle.sety(y)

# Move the right paddle down
def move_right_paddle_down():
    y = right_paddle.ycor()
    y -= 50
    right_paddle.sety(y)

# Bind the arrow keys to the paddle movement functions
screen.listen()
screen.onkeypress(move_left_paddle_up, "w")
screen.onkeypress(move_left_paddle_down, "s")
screen.onkeypress(move_right_paddle_up, "Up")
screen.onkeypress(move_right_paddle_down, "Down")


# Main game loop
while True:
#Move the ball by dx and dy
    ball.sety(ball.ycor() + ball.dy)
    ball.setx(ball.xcor() + ball.dx)

    #Check for collision with the top or bottom
    if ball.ycor() >= (screen.window_height() / 2) - 20 or ball.ycor() <= -(screen.window_height() / 2) + 20:
        if ball.xcor() > 0 and ball.xcor() < left_paddle.xcor() or ball.xcor() < 0 and ball.xcor() > right_paddle.xcor():
            ball.goto(0, 0)
            ball.dy *= -1
        else:
            ball.dy *= -1
    
    def update_scores():
        left_scoreboard.clear()
        right_scoreboard.clear()
        left_scoreboard.write("Left: {}".format(left_score), align="center", font=("Arial", 24, "normal"))
        right_scoreboard.write("Right: {}".format(right_score), align="center", font=("Arial", 24, "normal"))
    # Check for collision with the left or right

    if (ball.xcor() > (screen.window_width() / 2) - 20 or ball.xcor() < -(screen.window_width() / 2) + 20):
        ball.goto(0, 0)
        if ball.xcor() > 0:
            left_score += 1
        else:
            right_score += 1
        update_scores()
    #Check for collision with the left paddle
    if ball.xcor() < left_paddle.xcor() + 20 and ball.xcor() > left_paddle.xcor() - 20:
        if ball.ycor() < left_paddle.ycor() + 50 and ball.ycor() > left_paddle.ycor() - 50:
            ball.dx *= -1

    #Check for collision with the right paddle
    if ball.xcor() < right_paddle.xcor() + 20 and ball.xcor() > right_paddle.xcor() - 20:
        if ball.ycor() < right_paddle.ycor() + 50 and ball.ycor() > right_paddle.ycor() - 50:
         ball.dx *= -1
