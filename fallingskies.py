import turtle
import time
import random

delay = 0.025

score = 0
lives = 3

# Set up the screen
wn = turtle.Screen()
wn.title("Falling Skies Game")
wn.bgcolor("black")
wn.bgpic("forest.gif")
wn.setup(width=800, height=600)
wn.tracer(0)

wn.register_shape("squirrel.gif")
wn.register_shape("nut.gif")
wn.register_shape("poison.gif")

# Add the player
player = turtle.Turtle()
player.speed(0)
player.shape("squirrel.gif")
player.penup()
player.goto(0, -250)
player.direction = "stop"

#create a list of a good_guys
good_guys =[]

# Add the good_guys
for _ in range(10):
    good_guy = turtle.Turtle()
    good_guy.speed(0)
    good_guy.shape("nut.gif")
    good_guy.penup()
    good_guy.goto(-100, 250)
    good_guy.speed = random.randint(1, 4)
    good_guys.append(good_guy) #add more good_guy

#create a list of a bad_guys
bad_guys =[]

# Add the bad_guys
for _ in range(10):
    bad_guy = turtle.Turtle()
    bad_guy.speed(0)
    bad_guy.shape("poison.gif")
    bad_guy.penup()
    bad_guy.goto(100, 250)
    bad_guy.speed = random.randint(1, 4)
    bad_guys.append(bad_guy) #add more bad_guy

#Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: {}  Lives: {}".format(score, lives), align="center", font=("Courier", 24, "bold"))

#functions
def go_left():
    player.direction = "left"

def go_right():
    player.direction = "right"

#key binding
wn.listen()
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "Right")

#Main loop game
while True:
    wn.update()

    #Move the player
    if player.direction == "left":
        player.setx(player.xcor() - 3)

    if player.direction == "right":
        player.setx(player.xcor() + 3)

    #Move the good_guys
    for good_guy in good_guys:
        y = good_guy.ycor()
        y -= good_guy.speed
        good_guy.sety(y)
    
        #Check if off the screen
        if y < -300:
            x = random.randint(-380,380)
            y = random.randint(-300,400)
            good_guy.goto(x, y)

        #Check for the collision with the player
        if good_guy.distance(player) < 35:
            x = random.randint(-380,380)
            y = random.randint(-300,400)
            good_guy.goto(x, y)

            #Increase the score
            score += 10

            pen.clear()
            pen.write("Score: {}  Lives: {}".format(score, lives), align="center", font=("Courier", 24, "bold"))

    #Move the bad_guys
    for bad_guy in bad_guys:
        y = bad_guy.ycor()
        y -= bad_guy.speed
        bad_guy.sety(y)
    
        #Check if off the screen
        if y < -300:
            x = random.randint(-380,380)
            y = random.randint(-300,400)
            bad_guy.goto(x, y)

        #Check for the collision with the player
        if bad_guy.distance(player) < 35:
            x = random.randint(-380,380)
            y = random.randint(-300,400)
            bad_guy.goto(x, y)

            #Increase the score
            score -= 10
            lives -= 1

            pen.clear()
            pen.write("Score: {}  Lives: {}".format(score, lives), align="center", font=("Courier", 24, "bold"))
    
    time.sleep(delay)

wn.mainloop()