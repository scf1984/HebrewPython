import turtle

sc = turtle.Screen()
sc.tracer(False)
batz = turtle.Turtle()

batz.penup()
batz.back(300)
batz.pendown()
batz.hideturtle()


def draw_koch(length, order):
    if order == 0:
        batz.forward(length)
    else:
        for angle in [60, -120, 60, 0]:
            draw_koch(length/3, order-1)
            batz.left(angle)
        
for _ in range(3):
    draw_koch(200, 5)
    batz.right(120)
sc.update()
