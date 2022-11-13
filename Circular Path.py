# Objective: Objective of this project is move mouse in a circular path and that's it
import pyautogui as auto
import time
import math
global r, pi
r=int(input("Enter the radius: "))
def open_mspaint():
    auto.hotkey("win","r")
    auto.write("mspaint")
    auto.press("enter")
    time.sleep(3)
open_mspaint()
pi=math.pi
def x(theta):
    x_position=r*math.cos(pi*theta/180)
    return x_position
def y(theta):
    y_position=r*math.sin(pi*theta/180)
    return y_position
centre=[674, 384] # Centre of the circle
#now we need to move the mouse in a circular path
# the locus of the mouse for circular moverment will be (rcos(theta)+h,rsin(theta)+k) where (h,k) is the centre of the circle and r is radius
theta=0
auto.mouseDown(x(theta)+centre[0], y(theta)+centre[1], button="left")
while theta>-370:
    auto.moveTo(x(theta)+centre[0],y(theta)+centre[1],0)
    theta-=3
auto.mouseUp()
position=auto.position()
auto.click(position.x, position.y, 1, 0.1, button="left")
exit()
