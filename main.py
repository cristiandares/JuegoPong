import turtle

#ventana
ventana = turtle.Screen()
ventana.title("Pong")
ventana.bgcolor("black")
ventana.setup(width = 800, height = 600)
ventana.tracer(0)

#Marcador
marcadorA = 0
marcadorB = 0

#JugadorA
jugadorA = turtle.Turtle()
jugadorA.speed(0)
jugadorA.shape("square")
jugadorA.color("white")
jugadorA.penup() #este metodo evita que deje una linea desde el punto 0,0 hasta el nuevo sitio asignado
jugadorA.goto(-350,0)
jugadorA.shapesize(stretch_wid = 5, stretch_len = 1)

#JugadorB
jugadorB = turtle.Turtle()
jugadorB.speed(0)
jugadorB.shape("square")
jugadorB.color("white")
jugadorB.penup()
jugadorB.goto(350,0)
jugadorB.shapesize(stretch_wid = 5, stretch_len = 1)

#Pelota
pelota = turtle.Turtle()
pelota.speed(0)
pelota.shape("square")
pelota.color("white")
pelota.penup()
pelota.goto(0,0)
pelota.dx = 0.3 #movemos la pelota cada 3 pixeles
pelota.dy = 0.3

#Linea Division
division = turtle.Turtle()
division.color("white")
division.goto(0,400)
division.goto(0,-400)

#Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("JugadorA: 0              JugadorB: 0", align = "center", font = ("Curier", 24, "normal"))

#Funciones
def jugadorA_up():
    y = jugadorA.ycor()
    y += 40
    jugadorA.sety(y)

def jugadorA_down():
    y = jugadorA.ycor()
    y -= 40
    jugadorA.sety(y)

def jugadorB_up():
    y = jugadorB.ycor()
    y += 40
    jugadorB.sety(y)

def jugadorB_down():
    y = jugadorB.ycor()
    y -= 40
    jugadorB.sety(y)

#Teclado
ventana.listen()
ventana.onkeypress(jugadorA_up, "w")
ventana.onkeypress(jugadorA_down, "s")

ventana.onkeypress(jugadorB_up, "Up")
ventana.onkeypress(jugadorB_down, "Down")

while True:
    ventana.update()
    pelota.setx(pelota.xcor() + pelota.dx)
    pelota.sety(pelota.ycor() + pelota.dy)

    #Bordes arriba - abajo
    if pelota.ycor() > 290:
        pelota.dy *= -1
    if pelota.ycor() < -290:
        pelota.dy *= -1
    
    #Bordes derecha - izquierda
    if pelota.xcor() > 390:
        pelota.goto(0,0)
        pelota.dx *= -1
        marcadorA += 1
        pen.clear()
        pen.write("JugadorA: {}              JugadorB: {}".format(marcadorA, marcadorB), align = "center", font = ("Curier", 24, "normal"))
    if pelota.xcor() < -390:
        pelota.goto(0,0)
        pelota.dx *= -1
        marcadorB += 1
        pen.clear()
        pen.write("JugadorA: {}              JugadorB: {}".format(marcadorA, marcadorB), align = "center", font = ("Curier", 24, "normal"))
    
    #colisiones, cuando un jugador devuelve la pelota
    #colisiones jugadorB
    if ((pelota.xcor() > 340 and pelota.xcor() < 350)
            and (pelota.ycor() < jugadorB.ycor() + 50
            and pelota.ycor() > jugadorB.ycor() - 50)):
        pelota.dx *= -1
    #colisiones jugadorA
    if ((pelota.xcor() < -340 and pelota.xcor() > -350)
            and (pelota.ycor() < jugadorA.ycor() + 50
            and pelota.ycor() > jugadorA.ycor() - 50)):
        pelota.dx *= -1