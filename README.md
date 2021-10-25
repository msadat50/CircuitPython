# CircuitPython
 The follwing files are my first foray into CircuitPython.
## Table of Contents
* [Table of Contents](#TableOfContents)
* [Hello_CircuitPython](#Hello_CircuitPython)
* [CircuitPython_Servo](#CircuitPython_Servo)
* [Servo Touch CircuitPython](#CircuitPythoin_Servo_Touch)
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
Doing this was easy. The only problem was that I had the code written but when I was trying to uploaded it wasn't working like the light was changing, but one of my classmate help me out. The problem was that I had to uploade something in my folder first after doing that it worked. 




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
Doing this was good. I had some troubles getting the servo work. At the beginning the servo was working but than after a few minutes the servo wasn't working. I checked the wiring like 3 times to see if I had the wire in the wrong place, but the wiring seems good to me. After that I asked MR. H for help to see what could have gone wrong he checked the code everything looked good expect one part wasn't the same so we fix it. After that I uploded the code to see if the servo was working, but tha the servo wasn't working. So the next day I checked the wiring again, the wiring was good I asked Mr. Dierolf for help. 
He checked my code the code was good, than he checked the wiring at first when he see it the wiring was good, so we didn't know what I have done wrong. Than he said that I was putting one wire in the wrong place, and I was using the wrong servo, so I changed the servo but than the servo worked. Thanks to Mr Dierolf he helped me fix it. 

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

<img src="the distance sensor.gif" width="300">

<img src="https://github.com/msadat50/CircuitPython/blob/main/Pictures/Distance%20sensor%20picture.png?raw=true" width="400">


### Reflection
Doing this was hard for me in the beginning and confusing. There was a link to the assignment that would take you to this very long confusing code when I saw that code I didn't know which part of the code we should copy, so I just copied the whole code and put it in Mu. After that I didn't even know what to do so I used the hint to help me when I clicked on it there was all variable iut made it even more confusing. This time I asked Mr. H for help He helped me find the correct code and than explained it to me I understanded it better than it was easy and he did the first part of the code for me to understand it better. After that I knew what to do.

### Evidence
[This is Dylan Herrada code link that I used for Distance Sensor assignment](https://github.com/adafruit/Adafruit_CircuitPython_HCSR04/blob/main/examples/hcsr04_simpletest.py)

[This was the Dylan Herrada long confusing code for distance sensor assignment](https://github.com/adafruit/Adafruit_CircuitPython_HCSR04/blob/main/adafruit_hcsr04.py)

[This is the hint link for distance sensor assignment thjat I used](https://docs.google.com/spreadsheets/d/e/2PACX-1vRzoIejkQqugrDoWHBw14qTI0HifXba92WiyQ24whEnzWcCUaCDYu6ifMQKK5O5Ilkxrd7UKIxPLBCW/pubhtml)

[This is the link for how to use simpleip for distance sensor assignment](https://circuitpython.readthedocs.io/projects/simpleio/en/latest/api.html#simpleio.map_range)




## Photointerrupters

### Description & Code 

```python

# Write your code here :-)
from digitalio import DigitalInOut, Direction, Pull
import time
import board

interrupter = DigitalInOut(board.D11)
interrupter.direction = Direction.INPUT
interrupter.pull = Pull.UP

counter = 0

photo = False
state = False

max = 4
start = time.time()
while True:

    now = time.monotonic()

    photo = interrupter.value
    if photo and not state:
            counter += 1
    state = photo

    remaining = max - time.time()

    if remaining <= 0:
        print("Interrupts:", str(counter))
        max = time.time() + 4
        counter = 0
        
  ```
        

### Evidence
[This is Gventre code link that I used for PhotoInterrupter assignment](https://github.com/gventre04/CircuitPython/blob/master/photointerrupter.py)

[The picture credit goes to Gventre](https://github.com/gventre04/CircuitPython/raw/master/media/PhotoInterrupter.png)


### Images

<img src="https://github.com/gventre04/CircuitPython/raw/master/media/PhotoInterrupter.png" width="400">

### Reflection
Doing this assignment was easy I just had to copy the code, understand it, and know how to work it. It wasn't harder than the other assignments and it wasn't as confusing as the other assignments. 



## CircuitPython_LCD_Touch

### Description & Code 

```python
import board
import time
from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface
import touchio

# get and i2c object
i2c = board.I2C()
# some LCDs are 0x3f... some are 0x27.
lcd = LCD(I2CPCF8574Interface(i2c, 0x3f), num_rows=2, num_cols=16)

touch_A0 = touchio.TouchIn(board.A0)
touch_A5 = touchio.TouchIn(board.A5)

counter = 0
lcd.print("Hello, Engineer!")
time.sleep(3)
lcd.clear()

while True:
    if touch_A0.value:
        counter += 1
        lcd.set_cursor_pos(0, 0)
        lcd.print(str(counter))
        print(" Green wire touched ")

    if touch_A5.value:
        counter += 1
        lcd.set_cursor_pos(1, 4)
        lcd.print(str(counter))
        print(" Yellow wire touched ")

    else:
        counter = counter
        time.sleep(0.1)
        
   ```     

### Evidence
[This is Gventre code link that I used for LCD touch assignment](https://github.com/gventre04/CircuitPython/blob/master/lcd_button.py)

[This is the link from Gventre github page that helped me understand the code better](https://learn.adafruit.com/sensor-plotting-with-mu-and-circuitpython/buttons-and-switch)


### Images
The Touch LCD moved something like this. 

<img src="https://assets.website-files.com/5beab1239ac8840644a660b4/5c2f6a0da059f38a075fe012_5c1ca503edf0cc792c36e658_counter-gif.gif" width="400">

[Image credit goes to flowbase.co](https://www.flowbase.co/blog/guide-counter-interaction)

<img src="https://github.com/msadat50/CircuitPython/blob/main/Pictures/lcd%201.jpg?raw=true" width= "300">
<img src="https://github.com/msadat50/CircuitPython/blob/main/Pictures/lcd%202.jpg?raw=true" width= "300"> 

The green and yellow color wire are the touch wires.



### Reflection
Doing this assignment was pretty easy. I kind of hard trouble finding the code for this assignment I didn't know where to start or where to get the code from, so I went and did some reasearch to find the correct code for this but than I found one of Mr. H student from last year GirHub notebook. I went there and saw the code for this assignment his code was kind of different from mine but it helped me a lot and it helped me to understand the code better. So the full credit to Gventre. 



## NextAssignment

### Description & Code

```python
Code goes here

```

### Evidence

### Images

### Reflection
