import turtle

pantalla = turtle.Screen()
pantalla.title("Ping Pong")
pantalla.bgcolor("black")
pantalla.setup(width=800, height=600)
pantalla.tracer(0)
#
paleta_1 = turtle.Turtle()
paleta_1.speed(0)
paleta_1.shape("square")
paleta_1.color("white")
paleta_1.shapesize(stretch_wid=5, stretch_len=1)
paleta_1.penup()
paleta_1.goto(-350, 0)
#
paleta_2 = turtle.Turtle()
paleta_2.speed(0)
paleta_2.shape("square")
paleta_2.color("white")
paleta_2.shapesize(stretch_wid=5, stretch_len=1)
paleta_2.penup()
paleta_2.goto(350, 0)
#
pelota = turtle.Turtle()
pelota.speed(0)
pelota.shape("circle")
pelota.color("red")
pelota.penup()
pelota.goto(0, 0)
pelota.dx = 0.3
pelota.dy = 0.3
#
puntaje_1 = 0
puntaje_2 = 0
puntaje = turtle.Turtle()
puntaje.speed(0)
puntaje.color("white")
puntaje.penup()
puntaje.hideturtle()
puntaje.goto(0, 260)

def marcador(marcador_1, marcador_2):
    puntaje.clear()
    puntaje.write("Jugador 1: {}  Jugador 2: {}".format(marcador_1, marcador_2), align="center", font=("Courier", 20, "normal"))

marcador(puntaje_1, puntaje_2)

# mover paletas
def paleta_1_up():
    y = paleta_1.ycor()
    y += 20
    paleta_1.sety(y)

def paleta_1_down():
    y = paleta_1.ycor()
    y -= 20
    paleta_1.sety(y)


def paleta_2_up():
    y = paleta_2.ycor()
    y += 20
    paleta_2.sety(y)

def paleta_2_down():
    y = paleta_2.ycor()
    y -= 20
    paleta_2.sety(y)


# teclas
pantalla.listen()
pantalla.onkeypress(paleta_1_up, "w")
pantalla.onkeypress(paleta_1_down, "s")
pantalla.onkeypress(paleta_2_up, "Up")
pantalla.onkeypress(paleta_2_down, "Down")

while True:
    pantalla.update()

    #mover pelota
    pelota.setx(pelota.xcor() + pelota.dx)
    pelota.sety(pelota.ycor() + pelota.dy)

    if pelota.ycor() > 290:
        pelota.sety(290)
        pelota.dy /= -1

    if pelota.ycor() < -290:
        pelota.sety(-290)
        pelota.dy *= -1

    if pelota.xcor() > 390:
        pelota.goto(0, 0)
        pelota.dx *= -1
        puntaje_1 += 1
        marcador(puntaje_1, puntaje_2)

    if pelota.xcor() < -390:
        pelota.goto(0, 0)
        pelota.dx *= -1
        puntaje_2 += 1
        marcador(puntaje_1, puntaje_2)

    # golpe paleta
    if (pelota.xcor() > 340 and pelota.xcor() < 350) and (pelota.ycor() < paleta_2.ycor() + 40 and pelota.ycor() > paleta_2.ycor() - 40):
        pelota.setx(340)
        pelota.dx *= -1


    if (pelota.xcor() < -340 and pelota.xcor() > -350) and (pelota.ycor() < paleta_1.ycor() + 40 and pelota.ycor() > paleta_1.ycor() - 40):
        pelota.setx(-340)
        pelota.dx *= -1