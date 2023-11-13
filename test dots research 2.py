from math import *
from random import random
from tkinter import *
import time

FPS = 60
MS_PER_FRAME = int(1000 / FPS)

tk = Tk()
canvas = Canvas(height=800, width=800, bg='black')
canvas.pack()



start_time=time.time()

circleX= random()*600+100
circleY = random()*600+100
size=40
miss=size/2


def time_convert(sec):
  mins = sec // 60
  sec = sec % 60
  hours = mins // 60
  mins = mins % 60
  print("Time Lapsed = {0}:{1}:{2}".format(int(hours),int(mins),sec)) 

def draw():
    circleX= random()*600+100
    circleY = random()*600+100
    size=50*random()
    miss=size/2
    canvas.create_oval(circleX,circleY, circleX+size, circleY+size, fill='white')


    
print(size)
draw()

def getxy(event):
    global circleX, circleY, size
    clickX=event.x
    clickY=event.y
    end_time = time.time()
    check(clickX,clickY, circleX, circleY,end_time)
    

def check(clickX,clickY, circleX, circleY, end_time):
    global size, miss, start_time
    centerX=circleX+25
    centerY=circleY+25
    time_lapsed = end_time - start_time*2
    time_convert(time_lapsed)
    if abs(clickX-centerX)<=20 and abs(clickY-centerY)<=20:
        print("got it!")
        
        update()
    else:
        print("Missed it!")
        update()
        
        
def update():
        canvas.delete('all')
        draw()
    

update()
canvas.bind('<Button-1>', getxy)
tk.mainloop()
