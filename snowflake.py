import turtle
batz = turtle.Turtle()
batz.pencolor(0, 0, 1.0)
batz.pensize(10)

def draw_arm():
    batz.forward(100)
    
    batz.right(30)
    batz.forward(50)
    batz.back(50)
    
    batz.left(30)
    batz.forward(50)
    batz.back(50)
    
    batz.left(30)
    batz.forward(50)
    batz.back(50)

    batz.right(30)
    batz.back(100)

for _ in range(6):
    draw_arm()
    batz.right(60)
    
