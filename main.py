import turtle
import winsound
import time

turtle.register_shape("PlayerRight.png")
turtle.register_shape("PlayerLeft.png")
turtle.register_shape("slab.png")
turtle.register_shape("ground.png")
turtle.register_shape("Player2Right.png")
turtle.register_shape("Player2Left.png")
turtle.register_shape("1Heart.png")
turtle.register_shape("2Hearts.png")
turtle.register_shape("3Hearts.png")
turtle.register_shape("4Hearts.png")

wn = turtle.Screen()
wn.bgcolor("black")
wn.setup(height=600, width=1000)
wn.tracer(0)
wn.title("Two Player Shooter Game by @TurboRacecar")



player = turtle.Turtle()
player.color("cyan")
player.speed(0)
player.shape("PlayerRight.png")
player.penup()
player.goto(-400, -240)
player.state = "ready"
player.facing = "right"
player.dx = 0
player.dy = 0

player2 = turtle.Turtle()
player2.color("cyan")
player2.speed(0)
player2.shape("Player2Left.png")
player2.penup()
player2.goto(400, -240)
player2.state = "ready"
player2.health = 4
player2.dx = 0
player2.dy = 0


slab1 = turtle.Turtle()
slab1.color("lime")
slab1.speed(0)
slab1.shape("slab.png")
slab1.penup()
slab1.goto(300, -180)
slab1.shapesize(stretch_wid=1, stretch_len=10)

slab2 = turtle.Turtle()
slab2.color("lime")
slab2.speed(0)
slab2.shape("slab.png")
slab2.penup()
slab2.goto(0, -130)
slab2.shapesize(stretch_wid=1, stretch_len=10)

slab3 = turtle.Turtle()
slab3.color("lime")
slab3.speed(0)
slab3.shape("slab.png")
slab3.penup()
slab3.goto(-300, -80)
slab3.shapesize(stretch_wid=1, stretch_len=10)

slab4 = turtle.Turtle()
slab4.color("lime")
slab4.speed(0)
slab4.shape("slab.png")
slab4.penup()
slab4.goto(20, 34)
slab4.shapesize(stretch_wid=1, stretch_len=10)

ground = turtle.Turtle()
ground.color("lime")
ground.speed(0)
ground.shape("ground.png")
ground.penup()
ground.goto(0, -270)
ground.shapesize(stretch_len=50, stretch_wid=1)

bullet = turtle.Turtle()
bullet.color("gold")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.shapesize(stretch_len=0.4, stretch_wid=0.2)
bullet.hideturtle()
bullet.goto(400, 400)

bullet1 = turtle.Turtle()
bullet1.color("yellow")
bullet1.shape("triangle")
bullet1.penup()
bullet1.speed(0)
bullet1.shapesize(stretch_len=0.4, stretch_wid=0.2)
bullet1.hideturtle()
bullet1.goto(400, 400)

bullet2 = turtle.Turtle()
bullet2.color("yellow")
bullet2.shape("triangle")
bullet2.penup()
bullet2.speed(0)
bullet2.hideturtle()
bullet2.shapesize(stretch_len=0.4, stretch_wid=0.2)
bullet2.goto(400, 400)

bullet3 = turtle.Turtle()
bullet3.color("gold")
bullet3.shape("triangle")
bullet3.penup()
bullet3.speed(0)
bullet3.hideturtle()
bullet3.shapesize(stretch_len=0.4, stretch_wid=0.2)
bullet3.goto(400, 400)

bullet4 = turtle.Turtle()
bullet4.color("gold")
bullet4.shape("triangle")
bullet4.penup()
bullet4.speed(0)
bullet4.shapesize(stretch_len=0.4, stretch_wid=0.2)
bullet4.hideturtle()
bullet4.goto(400, 400)

bullet5 = turtle.Turtle()
bullet5.color("gold")
bullet5.shape("triangle")
bullet5.penup()
bullet5.speed(0)
bullet5.shapesize(stretch_len=0.4, stretch_wid=0.2)
bullet5.hideturtle()
bullet5.goto(400, 400)

bullet6 = turtle.Turtle()
bullet6.color("yellow")
bullet6.shape("triangle")
bullet6.penup()
bullet6.speed(0)
bullet6.hideturtle()
bullet6.shapesize(stretch_len=0.4, stretch_wid=0.2)
bullet6.goto(400, 400)

bullet7 = turtle.Turtle()
bullet7.color("yellow")
bullet7.shape("triangle")
bullet7.penup()
bullet7.speed(0)
bullet7.shapesize(stretch_len=0.4, stretch_wid=0.2)
bullet7.hideturtle()
bullet7.goto(400, 400)

bullet8 = turtle.Turtle()
bullet8.color("yellow")
bullet8.shape("triangle")
bullet8.penup()
bullet8.speed(0)
bullet8.shapesize(stretch_len=0.4, stretch_wid=0.2)
bullet8.hideturtle()
bullet8.goto(400, 400)

bullet9 = turtle.Turtle()
bullet9.color("yellow")
bullet9.shape("triangle")
bullet9.penup()
bullet9.speed(0)
bullet9.shapesize(stretch_len=0.4, stretch_wid=0.2)
bullet9.hideturtle()
bullet9.goto(400, 400)

bullet10 = turtle.Turtle()
bullet10.color("yellow")
bullet10.shape("triangle")
bullet10.penup()
bullet10.speed(0)
bullet10.shapesize(stretch_len=0.4, stretch_wid=0.2)
bullet10.hideturtle()
bullet10.goto(400, 400)

HitPoints = turtle.Turtle()
HitPoints.penup()
HitPoints.goto(-300, 200)
HitPoints.shape("4Hearts.png")


hearts = turtle.Turtle()
hearts.penup()
hearts.goto(300, 200)
hearts.shape("4Hearts.png")



bulletspeed = 16

bulletstate = "ready"

bullet1state = "ready"

bullet2state = "ready"

bullet3state = "ready"

bullet4state = "ready"

bullet5state = "ready"

bullet6state = "ready"

bullet7state = "ready"

bullet8state = "ready"

bullet9state = "ready"

bullet10state = "ready"

pen = turtle.Turtle()
pen.color("white")
pen.hideturtle()
pen.penup()
pen.goto(496, 300)
pen.pendown()
pen.pensize(8)
pen.goto(496, -300)
pen.goto(-500, -300)
pen.goto(-500, 300)
pen.goto(496, 300)
pen.penup()
del(pen)


gravity = -0.0124

def fire_bullet():

    global bulletstate
    global bullet1state
    global bullet2state
    global bullet3state
    global bullet4state
    global bullet5state
    global bullet6state
    global bullet7state
    global bullet8state
    global bullet9state
    global bullet10state
    global bullet11state
    winsound.PlaySound("audio_explosion.wav", 1)
    if bulletstate == "ready":
        bulletstate = "fire"
        x = player.xcor()
        y = player.ycor()
        bullet.goto(x, y + 10)
        bullet.showturtle()
    elif bullet1state == "ready":
        bullet1state = "fire"
        x = player.xcor()
        y = player.ycor()
        bullet1.goto(x, y + 10)
        bullet1.showturtle()
    elif bullet2state == "ready":
        bullet2state = "fire"
        x = player.xcor()
        y = player.ycor()
        bullet2.goto(x, y + 10)
        bullet2.showturtle()
    elif bullet3state == "ready":
        bullet3state = "fire"
        x = player.xcor()
        y = player.ycor()
        bullet3.goto(x, y + 10)
        bullet3.showturtle()
    elif bullet4state == "ready":
        bullet4state = "fire"
        x = player.xcor()
        y = player.ycor()
        bullet4.goto(x, y + 10)
        bullet4.showturtle()
    elif bullet5state == "ready":
        bullet5state = "fire"
        x = player.xcor()
        y = player.ycor()
        bullet5.goto(x, y + 10)
        bullet5.showturtle()
    elif bullet6state == "ready":
        bullet6state = "fire"
        x = player.xcor()
        y = player.ycor()
        bullet6.goto(x, y + 10)
        bullet6.showturtle()
    elif bullet7state == "ready":
        bullet7state = "fire"
        x = player.xcor()
        y = player.ycor()
        bullet7.goto(x, y + 10)
        bullet7.showturtle()
    elif bullet8state == "ready":
        bullet8state = "fire"
        x = player.xcor()
        y = player.ycor()
        bullet8.goto(x, y + 10)
        bullet8.showturtle()
    elif bullet9state == "ready":
        bullet9state = "fire"
        x = player.xcor()
        y = player.ycor()
        bullet9.goto(x, y + 10)
        bullet9.showturtle()
    elif bullet10state == "ready":
        bullet10state = "fire"
        x = player.xcor()
        y = player.ycor()
        bullet10.goto(x, y + 10)
        bullet10.showturtle()

def jump():
    if player.state == "ready":
        player.dy = 1.68
        player.state = "jumping"


def jump1():
    if player2.state == "ready":
        player2.dy = 1.68
        player2.state = "jumping"


def right():
    if player.state == "ready":
        player.dx = 0.32
        player.shape("PlayerRight.png")
        player.facing = "right"
    else:
        player.shape("PlayerRight.png")
        player.facing = "right"


def left():
    if player.state == "ready":
        player.dx = -0.32
        player.shape("PlayerLeft.png")
        player.facing = "left"
    else:
        player.shape("PlayerLeft.png")
        player.facing = "left"


def stop():
    if player.state == "ready":
        player.dx = 0


def right1():
    if player2.state == "ready":
        player2.dx = 0.32
        player2.shape("Player2Right.png")
    else:
        player2.shape("Player2Right.png")


def left1():
    if player2.state == "ready":
        player2.dx = -0.32
        player2.shape("Player2Left.png")
    else:
        player2.shape("Player2Left.png")


def stop1():
    if player2.state == "ready":
        player2.dx = 0


wn.listen()
wn.onkeypress(jump, "space")
wn.onkeypress(jump, "Up")
wn.onkeypress(right, "Right")
wn.onkeypress(left, "Left")
wn.onkeypress(stop, "Down")
wn.onkeypress(jump1, "w")
wn.onkeypress(right1, "d")
wn.onkeypress(left1, "a")
wn.onkeypress(stop1, "s")
wn.onkeypress(fire_bullet, ".")

while True:
    wn.update()
    if player2.health == 0:
        player2.hideturtle()
        player2.goto(1000, 1000)
        hearts.hideturtle()
        hearts.goto(1000, 1000)

        player2.goto(400, -236)
        hearts.goto(300, 200)
        player2.showturtle()
        time.sleep(0.6)
        player2.hideturtle()
        player2.goto(1000, 1000)

        player2.goto(400, -236)
        player2.showturtle()
        player2.health = 4
        hearts.shape("4Hearts.png")
        hearts.showturtle()
    if player.facing == "right":
        if bulletstate == "ready":
            bullet.setheading(0)
        if bullet1state == "ready":
            bullet1.setheading(0)
        if bullet2state == "ready":
            bullet2.setheading(0)
        if bullet3state == "ready":
            bullet3.setheading(0)
        if bullet4state == "ready":
            bullet4.setheading(0)
        if bullet5state == "ready":
            bullet5.setheading(0)
        if bullet6state == "ready":
            bullet6.setheading(0)
        if bullet7state == "ready":
            bullet7.setheading(0)
        if bullet8state == "ready":
            bullet8.setheading(0)
        if bullet9state == "ready":
            bullet9.setheading(0)
        if bullet10state == "ready":
            bullet10.setheading(0)

    if player.facing == "left":
        if bulletstate == "ready":
            bullet.setheading(180)
        if bullet1state == "ready":
            bullet1.setheading(180)
        if bullet2state == "ready":
            bullet2.setheading(180)
        if bullet3state == "ready":
            bullet3.setheading(180)
        if bullet4state == "ready":
            bullet4.setheading(180)
        if bullet5state == "ready":
            bullet5.setheading(180)
        if bullet6state == "ready":
            bullet6.setheading(180)
        if bullet7state == "ready":
            bullet7.setheading(180)
        if bullet8state == "ready":
            bullet8.setheading(180)
        if bullet9state == "ready":
            bullet9.setheading(180)
        if bullet10state == "ready":
            bullet10.setheading(180)

    if bulletstate == "fire":
        bullet.fd(bulletspeed)
        if bullet.xcor() > 500:
            bullet.hideturtle()
            bulletstate = "ready"
        if bullet.xcor() < -500:
            bullet.hideturtle()
            bulletstate = "ready"
        if bullet.distance(player2) < 46:
            player2.health -= 1
            if player2.health == 3:
                hearts.shape("3Hearts.png")
            if player2.health == 2:
                hearts.shape("2Hearts.png")
            if player2.health == 1:
                hearts.shape("1Heart.png")
            bullet.hideturtle()
            bullet.goto(0, 200)
            bulletstate = "fire"
    if bullet1state == "fire":
        bullet1.fd(bulletspeed)
        if bullet1.xcor() > 500:
            bullet1.hideturtle()
            bullet1state = "ready"
        if bullet1.xcor() < -500:
            bullet1.hideturtle()
            bullet1state = "ready"
        if bullet1.distance(player2) < 46:
            player2.health -= 1
            if player2.health == 3:
                hearts.shape("3Hearts.png")
            if player2.health == 2:
                hearts.shape("2Hearts.png")
            if player2.health == 1:
                hearts.shape("1Heart.png")
            bullet1.goto(0, 200)
            bullet1.hideturtle()
            bullet1state = "fire"
    if bullet2state == "fire":
        bullet2.fd(bulletspeed)
        if bullet2.xcor() > 500:
            bullet2.hideturtle()
            bullet2state = "ready"
        if bullet2.xcor() < -500:
            bullet2.hideturtle()
            bullet2state = "ready"
        if bullet2.distance(player2) < 46:
            player2.health -= 1
            if player2.health == 3:
                hearts.shape("3Hearts.png")
            if player2.health == 2:
                hearts.shape("2Hearts.png")
            if player2.health == 1:
                hearts.shape("1Heart.png")
            bullet2.goto(0, 200)
            bullet2.hideturtle()
            bullet2state = "fire"
    if bullet3state == "fire":
        bullet3.fd(bulletspeed)
        if bullet3.xcor() > 500:
            bullet3.hideturtle()
            bullet3state = "ready"
        if bullet3.xcor() < -500:
            bullet3.hideturtle()
            bullet3state = "ready"
        if bullet3.distance(player2) < 46:
            player2.health -= 1
            if player2.health == 3:
                hearts.shape("3Hearts.png")
            if player2.health == 2:
                hearts.shape("2Hearts.png")
            if player2.health == 1:
                hearts.shape("1Heart.png")
            bullet3.hideturtle()
            bullet3state = "ready"
    if bullet4state == "fire":
        bullet4.fd(bulletspeed)
        if bullet4.xcor() > 500:
            bullet4.hideturtle()
            bullet4state = "ready"
        if bullet4.distance(player2) < 46:
            player2.health -= 1
            bullet4.hideturtle()
            if player2.health == 3:
                hearts.shape("3Hearts.png")
            if player2.health == 2:
                hearts.shape("2Hearts.png")
            if player2.health == 1:
                hearts.shape("1Heart.png")
            bullet4state = "ready"
    if bullet5state == "fire":
        bullet5.fd(bulletspeed)
        if bullet5.xcor() > 500:
            bullet5.hideturtle()
            bullet5state = "ready"
        if bullet5.distance(player2) < 46:
            player2.health -= 1
            bullet5.hideturtle()
            if player2.health == 3:
                hearts.shape("3Hearts.png")
            if player2.health == 2:
                hearts.shape("2Hearts.png")
            if player2.health == 1:
                hearts.shape("1Heart.png")
            bullet5state = "ready"
    if bullet6state == "fire":
        bullet6.fd(bulletspeed)
        if bullet6.xcor() > 500:
            bullet6.hideturtle()
            bullet6state = "ready"
            if bullet6.distance(player2) < 46:
                player2.health -= 1
                bullet6.hideturtle()
                if player2.health == 3:
                    hearts.shape("3Hearts.png")
                if player2.health == 2:
                    hearts.shape("2Hearts.png")
                if player2.health == 1:
                    hearts.shape("1Heart.png")
                bullet6state = "ready"
        if bullet7state == "fire":
            bullet7.fd(bulletspeed)
        if bullet7.xcor() > 500:
            bullet7.hideturtle()
            bullet7state = "ready"
        if bullet7.distance(player2) < 46:
            player2.health -= 1
            bullet6.hideturtle()
            if player2.health == 3:
                hearts.shape("3Hearts.png")
            if player2.health == 2:
                hearts.shape("2Hearts.png")
            if player2.health == 1:
                hearts.shape("1Heart.png")
            bullet6state = "ready"
    if bullet8state == "fire":
        bullet8.fd(bulletspeed)
        if bullet8.xcor() > 500:
            bullet8.hideturtle()
            bullet8state = "ready"
        if bullet8.distance(player2) < 46:
            player2.hideturtle()
    if bullet9state == "fire":
        bullet9.fd(bulletspeed)
    if bullet9.xcor() > 500:
        bullet9.hideturtle()
        bullet9state = "ready"
    if bullet9.distance(player2) < 46:
        player2.hideturtle()
    if bullet10state == "fire":
        bullet10.fd(bulletspeed)
    if bullet10.xcor() > 500:
        bullet10.hideturtle()
        bullet10state = "ready"
    if bullet10.distance(player2) < 46:
        player2.hideturtle()

    player.dy += gravity
    player2.dy += gravity

    y = player.ycor()
    y += player.dy
    player.sety(y)
    player.state = "jumping"

    y = player2.ycor()
    y += player2.dy
    player2.sety(y)
    player2.state = "jumping"

    x = player.xcor()
    x += player.dx
    player.setx(x)

    x = player2.xcor()
    x += player2.dx
    player2.setx(x)

    if player.dx < 0:
        if player.dx > -1.2:
            player.dx -= 0.02

    if player.dx > 0:
        if player.dx < 1.2:
            player.dx += 0.02

    if player2.dx < 0:
        if player2.dx > -1.2:
            player2.dx -= 0.02

    if player2.dx > 0:
        if player2.dx < 1.2:
            player2.dx += 0.02

    if player.ycor() < -244:
        player.sety(-244)
        player.state = "ready"
        player.dy = 0

    if player.xcor() < -486:
        player.setx(-486)
        player.dx = 0

    if player.xcor() > 486:
        player.setx(486)
        player.dx = 0

    if player2.ycor() < -244:
        player2.sety(-244)
        player2.state = "ready"
        player2.dy = 0

    if player2.xcor() < -486:
        player2.setx(-486)
        player2.dx = 0

    if player2.xcor() > 486:
        player2.setx(486)
        player2.dx = 0

    if (player.xcor() < 402) and (player.xcor() > 200):
        if (player.ycor() > -164) and (player.ycor() < -154):
            player.sety(-154)
            player.dy = 0
            player.state = "ready"

    if (player.ycor() > -190) and (player.ycor() < -170):
        if (player.xcor() < 200) and (player.xcor() > 190):
            player.setx(190)
            player.dx = 0
            player.dy = -0.1
            player.state = "jumping"

    if (player.ycor() > -190) and (player.ycor() < -170):
        if (player.xcor() < 410) and (player.xcor() > 390):
            player.setx(410)
            player.dx = 0
            player.dy = -0.1
            player.state = "jumping"

    if (player.xcor() < 402) and (player.xcor() > 200):
        if (player.ycor() > -200) and (player.ycor() < -170):
            player.sety(-200)
            player.dy = -0.6
            player.state = "jumping"
            # from here

    if (player.xcor() < 110) and (player.xcor() > -100):
        if (player.ycor() > -114) and (player.ycor() < -104):
            player.sety(-104)
            player.dy = 0
            player.state = "ready"

    if (player.ycor() > -140) and (player.ycor() < -120):
        if (player.xcor() < -100) and (player.xcor() > -110):
            player.setx(-110)
            player.dx = 0
            player.dy = -0.08
            player.state = "jumping"

    if (player.ycor() > -150) and (player.ycor() < -120):
        if (player.xcor() < 110) and (player.xcor() > 100):
            player.setx(110)
            player.dx = 0
            player.dy = -0.08
            player.state = "jumping"

    if (player.xcor() < 110) and (player.xcor() > -100):
        if (player.ycor() > -150) and (player.ycor() < -120):
            player.sety(-150)
            player.dy = -0.4
            player.state = "jumping"
            # from here

    if (player.xcor() < -190) and (player.xcor() > -400):
        if (player.ycor() > -64) and (player.ycor() < -54):
            player.sety(-54)
            player.dy = 0
            player.state = "ready"

    if (player.ycor() > -90) and (player.ycor() < -70):
        if (player.xcor() < -400) and (player.xcor() > -410):
            player.setx(-410)
            player.dx = 0
            player.dy = -0.04
            player.state = "jumping"

    if (player.ycor() > -100) and (player.ycor() < -70):
        if (player.xcor() < -190) and (player.xcor() > -200):
            player.setx(-190)
            player.dx = 0
            player.dy = -0.04
            player.state = "jumping"

    if (player.xcor() < -190) and (player.xcor() > -400):
        if (player.ycor() > -100) and (player.ycor() < -70):
            player.sety(-100)
            player.dy = -0.4
            player.state = "jumping"
            # from here

    if (player.xcor() < 130) and (player.xcor() > -80):
        if (player.ycor() > 50) and (player.ycor() < 60):
            player.sety(60)
            player.dy = 0
            player.state = "ready"

    if (player.ycor() > 30) and (player.ycor() < 50):
        if (player.xcor() < -80) and (player.xcor() > -90):
            player.setx(-90)
            player.dx = 0
            player.dy = -0.04
            player.state = "jumping"

    if (player.ycor() > 20) and (player.ycor() < 50):
        if (player.xcor() < 130) and (player.xcor() > 120):
            player.setx(130)
            player.dx = 0
            player.dy = -0.04
            player.state = "jumping"

    if (player.xcor() < 130) and (player.xcor() > -80):
        if (player.ycor() > 20) and (player.ycor() < 50):
            player.sety(20)
            player.dy = -0.4
            player.state = "jumping"
            # from here

    if (player2.xcor() < 402) and (player2.xcor() > 200):
        if (player2.ycor() > -164) and (player2.ycor() < -154):
            player2.sety(-154)
            player2.dy = 0
            player2.state = "ready"

    if (player2.ycor() > -190) and (player2.ycor() < -170):
        if (player2.xcor() < 200) and (player2.xcor() > 190):
            player2.setx(190)
            player2.dx = 0
            player2.dy = -0.1
            player2.state = "jumping"

    if (player2.ycor() > -190) and (player2.ycor() < -170):
        if (player2.xcor() < 410) and (player2.xcor() > 390):
            player2.setx(410)
            player2.dx = 0
            player2.dy = -0.1
            player2.state = "jumping"

    if (player2.xcor() < 402) and (player2.xcor() > 200):
        if (player2.ycor() > -200) and (player2.ycor() < -170):
            player2.sety(-200)
            player2.dy = -0.6
            player2.state = "jumping"
            # from here

    if (player2.xcor() < 110) and (player2.xcor() > -100):
        if (player2.ycor() > -114) and (player2.ycor() < -104):
            player2.sety(-104)
            player2.dy = 0
            player2.state = "ready"

    if (player2.ycor() > -140) and (player2.ycor() < -120):
        if (player2.xcor() < -100) and (player2.xcor() > -110):
            player2.setx(-110)
            player2.dx = 0
            player2.dy = -0.08
            player2.state = "jumping"

    if (player2.ycor() > -150) and (player2.ycor() < -120):
        if (player2.xcor() < 110) and (player2.xcor() > 100):
            player2.setx(110)
            player2.dx = 0
            player2.dy = -0.08
            player2.state = "jumping"

    if (player2.xcor() < 110) and (player2.xcor() > -100):
        if (player2.ycor() > -150) and (player2.ycor() < -120):
            player2.sety(-150)
            player2.dy = -0.4
            player2.state = "jumping"
            # from here

    if (player2.xcor() < -190) and (player2.xcor() > -400):
        if (player2.ycor() > -64) and (player2.ycor() < -54):
            player2.sety(-54)
            player2.dy = 0
            player2.state = "ready"

    if (player2.ycor() > -90) and (player2.ycor() < -70):
        if (player2.xcor() < -400) and (player2.xcor() > -410):
            player2.setx(-410)
            player2.dx = 0
            player2.dy = -0.04
            player2.state = "jumping"

    if (player2.ycor() > -100) and (player2.ycor() < -70):
        if (player2.xcor() < -190) and (player2.xcor() > -200):
            player2.setx(-190)
            player2.dx = 0
            player2.dy = -0.04
            player2.state = "jumping"

    if (player2.xcor() < -190) and (player2.xcor() > -400):
        if (player2.ycor() > -100) and (player2.ycor() < -70):
            player2.sety(-100)
            player2.dy = -0.4
            player2.state = "jumping"
            # from here

    if (player2.xcor() < 130) and (player2.xcor() > -80):
        if (player2.ycor() > 50) and (player2.ycor() < 60):
            player2.sety(60)
            player2.dy = 0
            player2.state = "ready"

    if (player2.ycor() > 30) and (player2.ycor() < 50):
        if (player2.xcor() < -80) and (player2.xcor() > -90):
            player2.setx(-90)
            player2.dx = 0
            player2.dy = -0.04
            player2.state = "jumping"

    if (player2.ycor() > 20) and (player2.ycor() < 50):
        if (player2.xcor() < 130) and (player2.xcor() > 120):
            player2.setx(130)
            player2.dx = 0
            player2.dy = -0.04
            player2.state = "jumping"

    if (player2.xcor() < 130) and (player2.xcor() > -80):
        if (player2.ycor() > 20) and (player2.ycor() < 50):
            player2.sety(20)
            player2.dy = -0.4
            player2.state = "jumping"
            # from here
