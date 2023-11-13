from math import *
from random import random
from tkinter import *
import time

FPS = 60
MS_PER_FRAME = int(1000 / FPS)

tk = Tk()
canvas = Canvas(height=800, width=1600, bg='black')
canvas.pack()



start_time=time.time()



def time_convert(sec):
  mins = sec // 60
  sec = sec % 60
  hours = mins // 60
  mins = mins % 60
  print("Time Lapsed = {0}:{1}:{2}".format(int(hours),int(mins),sec)) 

def draw():
    circleX= random()*1400+100
    circleY = random()*600+100
    size=10+30*random()
    miss=size/2
    canvas.create_oval(circleX,circleY, circleX+size, circleY+size, fill='white')
    return circleX, circleY  # return these values so function getxy(event) can use it. It is not possible to command getxy(circleX, circleY, event)  from the function draw() because
  #its a special Event function that can only take (event) as an argument. 


    


def getxy(event):
    global circleX, circleY, size #get these values here, when a new 
    clickX=event.x
    clickY=event.y
    update()
    end_time = time.time()
    check(clickX,clickY, circleX, circleY,end_time) #this doesnt work because we arent getting the values from draw()
    

def check(clickX,clickY, circleX, circleY, end_time): #checks if user clicked on the circle
    global size, miss, start_time #also here
    centerX=circleX+25
    centerY=circleY+25
    time_lapsed = end_time - start_time*2
    time_convert(time_lapsed)
    if abs(clickX-centerX)<=20 and abs(clickY-centerY)<=20:
        print("Got it!")
        
        update()
    else:
        print("Missed it!")
        update()
        
        
def update():
        canvas.delete('all')
        draw()
    
draw() #timer starts
update()
canvas.bind('<Button-1>', getxy)
tk.mainloop()
