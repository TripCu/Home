import turtle

# Set up the screen
screen = turtle.Screen()
screen.title("Pong")
screen.bgcolor("black")
screen.setup(width=800, height=600)
# Create the left score
left_score = turtle.Turtle()
left_score.color("white")
left_score.penup()
left_score.hideturtle()
left_score.goto(-350, 260)
left_score.score = 0

# Create the right score
right_score = turtle.Turtle()
right_score.color("white")
right_score.penup()
right_score.hideturtle()
right_score.goto(350, 260)
right_score.score = 0

# Function to update the scores
def update_score(turtle):
    turtle.clear()
    turtle.write(turtle.score, align="center", font=("Arial", 24, "normal"))

# Increase the left score
def increase_left_score():
    left_score.score += 1
    update_score(left_score)

# Increase the right score
def increase_right_score():
    right_score.score += 1
    update_score(right_score)

#Test Keyboard bindings
screen.listen()
screen.onkeypress(increase_left_score, "1")
screen.onkeypress(increase_right_score, "2")

# Create the ball
ball = turtle.Turtle()
ball.shape("circle")
ball.color("white")
ball.shapesize(1, 1)
ball.penup()
ball.goto(0, 0)
ball.dy = 3
ball.dx = 3

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

def move_left_paddle_up():
    y = left_paddle.ycor()
    y += 20
    left_paddle.sety(y)

# Move the left paddle down
def move_left_paddle_down():
    y = left_paddle.ycor()
    y -= 20
    left_paddle.sety(y)

def move_right_paddle_up():
    y = right_paddle.ycor()
    y += 20
    right_paddle.sety(y)

# Move the right paddle down
def move_right_paddle_down():
    y = right_paddle.ycor()
    y -= 20
    right_paddle.sety(y)

# Bind the arrow keys to the paddle movement functions
screen.listen()
screen.onkeypress(move_left_paddle_up, "Up")
screen.onkeypress(move_left_paddle_down, "Down")
screen.onkeypress(move_right_paddle_up, "w")
screen.onkeypress(move_right_paddle_down, "s")

# Main game loop
while True:
    # Move the ball
    ball.sety(ball.ycor() + ball.dy)
    ball.setx(ball.xcor() + ball.dx)
    
    if ball.xcor() > 390 or ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dy *= -1

    # Check for collision with the top or bottom
    if ball.ycor() >= (screen.window_height() / 2) - 20 or ball.ycor() <= -(screen.window_height() / 2) + 20:
        if ball.xcor() > 0 and ball.xcor() < left_paddle.xcor() or ball.xcor() < 0 and ball.xcor() > right_paddle.xcor():
            ball.goto(0, 0)
            ball.dy *= -1
        else:
            ball.dy *= -1
    

    # Check for collision with the left or right
    if (ball.xcor() > (screen.window_width() / 2) - 20 or ball.xcor() < -(screen.window_width() / 2) + 20):
        if (ball.ycor() < left_paddle.ycor() + 50 and ball.ycor() > left_paddle.ycor() - 50) or (ball.ycor() < right_paddle.ycor() + 50 and ball.ycor() > right_paddle.ycor() - 50):
            ball.goto(0, 0)
        else:
            ball.dx *= -1


   # Check for collision with the left paddle
    if ball.xcor() < left_paddle.xcor() + 20 and ball.xcor() > left_paddle.xcor() - 20:
        if ball.ycor() < left_paddle.ycor() + 50 and ball.ycor() > left_paddle.ycor() - 50:
            ball.dx *= -1

# Check for collision with the right paddle
    if ball.xcor() < right_paddle.xcor() + 20 and ball.xcor() > right_paddle.xcor() - 20:
        if ball.ycor() < right_paddle.ycor() + 50 and ball.ycor() > right_paddle.ycor() - 50:
            ball.dx *= -1
