#Tähtikirkas yö (sivu 90)
import turtle as t
from random import randint, random
def draw_star (points, size, col, x, y):
    t.penup ()
    t.goto (x, y)
    t.pendown
    angle = 180 - (180 points) 
    t.color (col)
    t.begin_fill ()
    print (x, y)
    for i in range (points):
        t.forward (size)
        t.right (angle)
    t.end_fill()
    
#Pääohjelma
t.Screen ().bgcolor ('dark blue')
while True:
    ranPts = randint (2, 5) * 2 + 1
    ranSize = randint (10, 50)
    ranCol = (random(), random (), random())
    ranX =  randint (-350, 300)
    rany = randint (-250, 250)
    draw_star (ranPts, ranSize, ranCol, ranX, ranY)