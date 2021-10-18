# CircuitPython
 The follwing files are my first foray into CircuitPython.
## Table of Contents
* [Table of Contents](#TableOfContents)
* [Hello_CircuitPython](#Hello_CircuitPython)
* [CircuitPython_Servo](#CircuitPython_Servo)
* [CircuitPython Servo Touch](#CircuitPython_Servo_Touch)
* [CircuitPython Distance Sensor](#CircuitPython_Distance_Sensor)
* [CircuitPython Photointerrupters](#CircuitPython_Photointerrupter)
* [CircuitPython_LCD](#CircuitPython_LCD)
* [NextAssignmentGoesHere](#NextAssignment)
---

## Hello_CircuitPython

### Description & Code
This is the code for circuit python.

```python
import board
import neopixel
import sleep

dot = neopixel.NeoPixel(board.NEOPIXEL, 1)
dot.brightness = 0.5 

print("Make it red!")

while True:
    dot.fill((0, 0, 255))
    time.sleep
    print("Make it yellow!")
    dot.fill((51, 204, 51))
    time.sleep
    

```


### Images
<img src="https://github.com/msadat50/CircuitPython/blob/main/Pictures/changing%20color%202.png?raw=true" width="200">
<img src="https://github.com/msadat50/CircuitPython/blob/main/Pictures/changing%20color.png?raw=true" width="200">


### Reflection
Doing this was easy. The only promble was that I had the code written but when I was trying to uploaded it wasn't working like the light was changing, but one of my classmate help me out. The promble was that I had to uploade something in my folder first after doing that it worked. 




## CircuitPython_Servo

### Description & Code
This is the code for making a servo trun. 
```python
# Write your code here :-)
import board
import pwmio
import servo

# create a PWMOut object on Pin A2.
pwm = pwmio.PWMOut(board.A2, duty_cycle=2 ** 15, frequency=50)

# Create a servo object, my_servo.
my_servo = servo.Servo(pwm)

while True:
    for angle in range(0, 180, 5):  # 0 - 180 degrees, 5 degrees at a time.
        my_servo.angle = angle
        time.sleep(0.05)
    for angle in range(180, 0, -5): # 180 - 0 degrees, 5 degrees at a time.
        my_servo.angle = angle
        time.sleep(0.05)
```

### Evidence
The servo moved something like this:

<img src="https://media.giphy.com/media/4EFCiAOcusZ2OOTi3X/giphy.gif" width="400">

[Image credit goes to electronics-lab.com](https://www.electronics-lab.com/project/using-sg90-servo-motor-arduino/)

[This is the websites that I used to get the code for my servo.](https://www.makerguides.com/servo-arduino-tutorial/)

### Images
<img src="https://github.com/msadat50/CircuitPython/blob/main/Pictures/Screenshot%202021-09-13%203.05.01%20PM.png?raw=true" width="400">

### Reflection
Doing this was easy. I had one wiring putting in the wrong place, which was the A1 Thanks to Mr. H he helped me correct it and he help me put the code into the in github. 


## CircuitPythoin_Servo_Touch

### Description & Code 
This is the code for servo touch.


```python
import time
import board
import pwmio
import touchio
import servo

# create a PWMOut object on Pin A2.
pwm = pwmio.PWMOut(board.A2, duty_cycle=2 ** 15, frequency=50)

# Create a servo object, my_servo.
my_servo = servo.Servo(pwm)

touch_pad1 = board.A0  # Will not work for Circuit Playground Express!
touch1 = touchio.TouchIn(touch_pad1)
touch_pad2 = board.A5  # Will not work for Circuit Playground Express!
touch2 = touchio.TouchIn(touch_pad2)

while True:

    if touch1.value:
        print("Touched the White Wire!")
        for angle in range(0, 180, 5):  # 0 - 180 degrees, 5 degrees at a time.
            my_servo.angle = angle
            print(angle)
            time.sleep(0.05)
    if touch2.value:
        print("Touched the Green Wire!")
        for angle in range(180, 0, -5):  # 180 - 0 degrees, 5 degrees at a time
            my_servo.angle = angle
            time.sleep(0.05)
    time.sleep(0.05)
    print("end of loop!")
    
```
## Evidence
The touch servo moved something like this:

<img src="https://projects-static.raspberrypi.org/projects/getting-started-crumble/0df4d240330dcb842375927e100ab166c46a5cb8/en/images/servo_movement_0.gif" width="400">

[Image credit goes to projects.raspberrypi.org](https://projects.raspberrypi.org/en/projects/getting-started-crumble/6)



I used Mr. H code for this assignments. 

[This is Mr. H code link that I used for servo Touch assignment](https://github.com/Helmstk1/CircuitPython/blob/master/files/touchTheWireServo.py)

### Images
<img src="https://github.com/msadat50/CircuitPython/blob/main/Pictures/The%20touch%20servo%20wiring%20.png?raw=true" width="400">

### Reflection
Doing this was good. I had some troubles getting the servo work. At the beginning the servo was working but than after a few minutes the servo wasn't working. I checked the wiring like 3 times to see if I had the wire in the wrong place, but the wiring seems good to me. After that I asked MR. H for help to see what could have gone wrong he checked the code everything looked good expect one part wasn't the same so we fix it. After that I uploded the code to see if the servo is working So I did but still the servo wasn't working. So the next day I checked the wiring again, the wiring was good I asked Mr. Dierolf for help. 
He checked my code the code was good, than he checked the wiring at first when he see it the wiring was good, so we didn't know what I have done wrong. Than he said that I had one wiring putting in the wrong place, and I was using the wrong servo, so I changed the servo but than the servo worked. Thanks to Mr Dierolf he helped me fix it. 

## CircuitPython_Distance sensor

### Description & Code 

```python

import time
import board
import neopixel
import simpleio
import adafruit_hcsr04

sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D5, echo_pin=board.D6)
dot = neopixel.NeoPixel(board.NEOPIXEL, 1)
r=0
g=0
b=0

cm = 0
while True:
    try:
        cm = sonar.distance
        print((cm))
        if cm < 5:
            r=255
            g=0
            b=0
            print("red!")
        elif cm < 20:
            print("red or blue!")
            r = simpleio.map_range(cm, 5, 20, 255, 0)
            g = 0
            b = simpleio.map_range(cm, 5, 20, 0, 255)


        elif cm < 35:
            print("blue or green!")
            r = 0
            g = simpleio.map_range(cm, 20, 35, 0, 255)
            b = simpleio.map_range(cm, 20, 35, 255, 0)

        else:
            print("green")
        dot.fill((int(r), int(g), int(b)))

    except RuntimeError:
        print("Retrying!")
    time.sleep(0.1)


```

### Image/video
 The video credit goes to Quinn for helping me.

<img src="the distance sensor.gif" width="400">


### Reflection
Doing this was hard for me in the beginning and confusing. There was a link to the assignment that would take you to this very long confusing code when I saw that code I didn't know which part of the code we should copy, so I just copied the whole code and put it in Mu. After that I didn't even know what to do so I used the hint to help me when I clicked on it there was all variable iut made it even more confusing this time I asked Mr. H for help He helped me find the correct code and than explained it to me I understanded it better than it was easy and he did the first part of the code for me to understand it better. After that I knew what to do.

### Evidence
[This is Dylan Herrada code link that I used for Distance Sensor assignment](https://github.com/adafruit/Adafruit_CircuitPython_HCSR04/blob/main/examples/hcsr04_simpletest.py)

[This was the Dylan Herrada long confusing code for distance sensor assignment](https://github.com/adafruit/Adafruit_CircuitPython_HCSR04/blob/main/adafruit_hcsr04.py)

[This is the hint link for distance sensor assignment thjat I used](https://docs.google.com/spreadsheets/d/e/2PACX-1vRzoIejkQqugrDoWHBw14qTI0HifXba92WiyQ24whEnzWcCUaCDYu6ifMQKK5O5Ilkxrd7UKIxPLBCW/pubhtml)

[This is the link for how to use simpleip for distance sensor assignment](https://circuitpython.readthedocs.io/projects/simpleio/en/latest/api.html#simpleio.map_range)





## CircuitPython_LCD

### Description & Code 

### Evidence

### Images

### Reflection





## NextAssignment

### Description & Code

```python
Code goes here

```

### Evidence

### Images

### Reflection
