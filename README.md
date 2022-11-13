# Path-Tracer
Circular Path.py and EquiPolygon.py are separate files but uses similar logic.

**pyautogui** library is used to control mouse events and movements

`pip install pyautogui` to install pyautogui

The core of these two programmes is **mathematical equation** which gives the locus of the path.

For Circular Path.py

`x=r*cos(theta)+h`

`y=r*sin(theta)+h`

For EquiPolygon.py

`x=(z*cos(alpha/2)*cos(theta)) / ( (2-2*cos(alpha))^0.5 * cos((alpha/2)-mod(theta,alpha) )`

`y=(z*cos(alpha/2)*sin(theta)) / ( (2-2*cos(alpha))^0.5 * cos((alpha/2)-mod(theta,alpha) )`

In each iteration value of theta changes and ranges from 0 to 360 to give one complete revolution and traces the path 

*P.S: _angles are in degree_* 

