# py -m pip install opencv-python
# py -m pip install Pillow

import tkinter
import time

import cv2
from PIL import ImageTk, Image

root = tkinter.Tk()
label = tkinter.Label(root)
label.pack()

vidcap = cv2.VideoCapture('sample.mp4')

start_time = time.time()
dt = 1/vidcap.get(cv2.CAP_PROP_FPS)

while True:        
    valid, img = vidcap.read()
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    if valid:
        frame = Image.fromarray(img)
        label.image = ImageTk.PhotoImage(frame)
        label['image'] = label.image
        root.update()
        time.sleep(dt - (time.time() - start_time) % dt)
    else:
        print('Corrupted frame')
        break    
vidcap.release()

