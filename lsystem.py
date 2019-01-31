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

def forward():
    batz.forward(2)
def plus():
    batz.right(25)
def minus():
    batz.left(25)
def save_state():
    state.append(batz.position())
    state.append(batz.heading())
def load_state():
    batz.penup()
    batz.setheading(state.pop())
    batz.setposition(state.pop())
    batz.pendown()
def nothing():
    pass
    
functions = {
    'F': forward,
    'X': nothing,
    '+': plus,
    '-': minus,
    '[': save_state,
    ']': load_state
}
for c in sentence:
    functions[c]()

        
sc.update()












