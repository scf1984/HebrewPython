##sentence = 'A'
##
##rules = {
##    'A': 'AB',
##    'B': 'A'
##}

##sentence = '0'
##rules = {
##    '1': '11',
##    '0': '1[0]0'
##}

sentence = 'X'
rules = {
    'X': 'F+[[X]-X]-F[-FX]+X',
    'F': 'FF'
}

generations = 6

for _ in range(generations):
    sentence = ''.join([rules[c] if c in rules else c for c in sentence])


import turtle
batz = turtle.Turtle()
sc = turtle.Screen()
sc.tracer(False)
batz.left(90)

state = []

for c in sentence:
    if c == 'F':
        batz.forward(2)
    if c == 'X':
        pass
    if c == '+':
        batz.right(25)
    if c == '-':
        batz.left(25)
    if c == '[':
        state.append(batz.position())
        state.append(batz.heading())
    if c == ']':
        batz.penup()
        batz.setheading(state.pop())
        batz.setposition(state.pop())
        batz.pendown()

sc.update()












