# CircuitPython
 The follwing files are my first foray into CircuitPython.
## Table of Contents
* [Table of Contents](#TableOfContents)
* [Hello_CircuitPython](#Hello_CircuitPython)
* [CircuitPython_Servo](#CircuitPython_Servo)
* [CircuitPython Servo Touch](#CircuitPython_Servo_Touch)
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


### Evidence

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
This is the websites that I used to get the code for my servo.

[The code and wiring for servo ](https://www.makerguides.com/servo-arduino-tutorial/)

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
I used Mr. H code for this assignments. 

[This is Mr H servo Touch code](https://github.com/Helmstk1/CircuitPython/blob/master/files/touchTheWireServo.py)

### Images
<img src="https://github.com/msadat50/CircuitPython/blob/main/Pictures/The%20touch%20servo%20wiring%20.png?raw=true" width="400">

### Reflection
Doing this was good. I had some troubles getting the servo work. At the beginning the servo was working but than after a few minutes the servo wasn't working. I checked the wiring like 3 times to see if I had the wire in the wrong place, but the wiring seems good to me. After that I asked MR. H for help to see what could have gone wrong he checked the code everything looked good expect one part wasn't the same so we fix it. After that I uploded the code to see if the servo is working So I did but still the servo wasn't working. So the next day I checked the wiring again, the wiring was good I asked Mr. Dierolf for help. 
He checked my code the code was good, than he checked the wiring at first when he see it the wiring was good, so we didn't know what I have done wrong. Than he said that I had one wiring putting in the wrong place, and I was using the wrong servo, so I changed the servo but than the servo worked. Thanks to Mr Dierolf he helped me fix it. 

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
