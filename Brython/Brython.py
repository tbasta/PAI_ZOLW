from browser import document, alert
from turtle import restart
import turtle

restart()

turtle.set_defaults(turtle_canvas_wrapper = document['lowerContainer'], canvwidth = 1000, canvheight = 800)
t = turtle.Turtle()
t.penup()
t.goto(0, 0)
t.width(5)
t.pendown()

try:
    _code
    turtle.done()
except:
    try:
        traceback.print_exc()
        alert("Nieprawidłowy kod!")
    except:
        alert("Nie można wykonać kodu")

document["mybutton"].bind("click", runcode)