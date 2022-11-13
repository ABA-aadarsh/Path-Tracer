#Objective: Move mouse in a locus of equi_polygon with 'n' number of sides and length 'l'
import pyautogui as auto
import time
import math
def open_mspaint():
    auto.hotkey("win","r")
    auto.write("mspaint")
    auto.press("enter")
    time.sleep(3)
global pi, n, z 
pi=math.pi
def sin(theta):
    return(math.sin(theta*pi/180))
def cos(theta):
    return(math.cos(theta*pi/180))
def x(theta):
    x_position=(z*cos(alpha/2)*cos(theta))/(pow(2*(1-cos(alpha)),0.5)*cos((alpha/2)-theta%alpha))
    return x_position
def y(theta):
    y_position=(z*cos(alpha/2)*sin(theta))/(pow(2*(1-cos(alpha)),0.5)*cos((alpha/2)-theta%alpha))
    return y_position
centre=[674,384]
n=int(input("Enter the number of sides: "))
z=int(input("Enter the length of side: "))
open_mspaint()
alpha=360/n 
theta=0
auto.mouseDown(x(theta)+centre[0],y(theta)+centre[1],button="left")
while(theta>-370):
    auto.moveTo(x(theta)+centre[0],y(theta)+centre[1],0)
    theta-=1
auto.mouseUp()
position=auto.position()
auto.click(position.x, position.y, 1, 0., button="left")
exit()