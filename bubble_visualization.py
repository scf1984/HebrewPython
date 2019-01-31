import tkinter
from random import shuffle
from time import sleep

window_size = 500
canvas_size = 500
gui = tkinter.Tk()
gui.geometry(f'{500}x{500}')
gui.title('Bubble sort')
c = tkinter.Canvas(gui, width=canvas_size, height=canvas_size, bg='black')
c.pack()

def draw_rects(array):
    square_size = canvas_size / len(array)
    c.delete(tkinter.ALL)
    for i, item in enumerate(array):
        coords = [
            i * square_size,
            canvas_size,
            (i + 1) * square_size,
            canvas_size - item * square_size
        ]
        c.create_rectangle(*coords, fill='red')
    gui.update()

def bubble_sort(array):
    tmp = list(array)
    for _ in range(len(tmp) - 1):
        for i in range(0, len(tmp) - _ - 1):
            if tmp[i] > tmp[i + 1]:
                tmp[i], tmp[i + 1] = tmp[i + 1], tmp[i]
        draw_rects(tmp)
##        sleep(0.05)

    return tmp

arr = list(range(1, 250))
shuffle(arr)

bubble_sort(arr)

