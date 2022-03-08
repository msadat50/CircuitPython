# CircuitPython
 The follwing files are my first foray into CircuitPython.
## Table of Contents
* [Table of Contents](#TableOfContents)
* [Hello_CircuitPython](#Hello_CircuitPython)
* [CircuitPython_Servo](#CircuitPython_Servo)
* [Servo Touch CircuitPython](#CircuitPython_Servo_Touch)
* [CircuitPython Distance Sensor](#CircuitPython_Distance_Sensor)
* [CircuitPython Photointerrupters](#CircuitPython_Photointerrupter)
* [CircuitPython_LCD Touch](#CircuitPython_LCD_Touch)
* [NextAssignmentGoesHere](#NextAssignment)
---

## Hello_CircuitPython

### Description & Code
The purpose of Hello CP was to make the onboard RGB LED change colours, which I achieved by using the neopixel library commands.
This is the code for circuit python.


```python
import board
import neopixel
import sleep

dot = neopixel.NeoPixel(board.NEOPIXEL, 1)
dot.brightness = 0.5     # the brightness

print("Make it red!")       

while True:  # helps the loop runs forever 
    dot.fill((0, 0, 255))         # the red color value that starts from zero than it goes higher  
    time.sleep        #setting up a reset before it repeats the loop 
    print("Make it yellow!")       
    dot.fill((51, 204, 51))       # the yellow color value number that starts from an avarge number then it goes to a higher number
    time.sleep                    # stop it
    

```


### Images
<img src="https://github.com/msadat50/CircuitPython/blob/main/Pictures/changing%20color%202.png?raw=true" width="200">
<img src="https://github.com/msadat50/CircuitPython/blob/main/Pictures/changing%20color.png?raw=true" width="200">


### Reflection
Doing this was easy. The only problem was that I had the code written but when I was trying to uploaded it wasn't working like the light was changing, but one of my classmate help me out. The problem was that I had to uploade something in my folder first after doing that it worked. 




## CircuitPython_Servo

### Description & Code
The purpose of this assignment was to turn an 90 degree servo, I achived my goal by using the PWMOut library commands. 
This is the code for making a servo trun. 

```python
# Write your code here :-)
import board
import pwmio
import servo

# create a PWMOut object on Pin A2. 
pwm = pwmio.PWMOut(board.A2, duty_cycle=2 ** 15, frequency=50) # setting up the servo rotation 

# Create a servo object, my_servo.
my_servo = servo.Servo(pwm)

while True:
    for angle in range(0, 180, 5):  # 0 - 180 degrees, 5 degrees at a time
        my_servo.angle = angle  # the servo angle command 
        time.sleep(0.05) #setting up a reset before it repeats the loop 
    for angle in range(180, 0, -5): # 180 - 0 degrees, 5 degrees at a time
        my_servo.angle = angle  # the servo angle command 
        time.sleep(0.05)     #setting up a reset before it repeats the loop 
```

The servo moved something like this:

<img src="https://media.giphy.com/media/4EFCiAOcusZ2OOTi3X/giphy.gif" width="400">

[Image credit goes to electronics-lab.com](https://www.electronics-lab.com/project/using-sg90-servo-motor-arduino/)

[This is the websites that I used to get the code for my servo.](https://www.makerguides.com/servo-arduino-tutorial/)


### Images
<img src="https://github.com/msadat50/CircuitPython/blob/main/Pictures/Screenshot%202021-09-13%203.05.01%20PM.png?raw=true" width="400">

### Reflection
Doing this was easy. I had one wiring putting in the wrong place, which was the A1 Thanks to Mr. H he helped me correct it and he help me put the code into the in github. 


## CircuitPython_Servo_Touch

### Description & Code 
The purpose of CircuitPython servo Touch was to make a servo turn by touching the wires, which I achive by using the PWMOut library.  
This is the code for servo touch.


```python
import time
import board
import pwmio
import touchio
import servo

# create a PWMOut object on Pin A2.
pwm = pwmio.PWMOut(board.A2, duty_cycle=2 ** 15, frequency=50)   # setting up the servo rotation 

# Create a servo object, my_servo.
my_servo = servo.Servo(pwm) 

touch_pad1 = board.A0   # the first touch wire vaule in the board 
touch1 = touchio.TouchIn(touch_pad1)   # the touch command in order to make the servo touch work 
touch_pad2 = board.A5    # the 2nd wire touch vaule in the board that shows where the 2nd wire suppose to be in the board 
touch2 = touchio.TouchIn(touch_pad2) # the basic command for servo touch 

while True:  # helps run this loop forever

    if touch1.value:  # the funcation touch value command that helps the servo turn left 
        print("Touched the White Wire!")
        for angle in range(0, 180, 5):  # 0 - 180 degrees, 5 degrees at a time.
            my_servo.angle = angle # setting up the angle of the servo 
            print(angle)  # telling the angle vaule in serial monitor
            time.sleep(0.05) # a reset before it repeats the loop 
    if touch2.value:   #the 2nd wire touch that helps turn right 
        print("Touched the Green Wire!")
        for angle in range(180, 0, -5):  # 180 - 0 degrees, 5 degrees at a time
            my_servo.angle = angle  # setting up the angle of the servo 
            time.sleep(0.05)    # a reset before it repeats the loop 
    time.sleep(0.05)   # a reset before it repeats the loop 
    print("end of loop!") # when no one touchs the wires it's printing the end of the loop
    
```

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


## CircuitPython_Distance_Sensor

### Description & Code 
The purpose of this assingment was to measure the distance by using sensors. I achive my goal by using neopixel library and using an HCSR04 sensor. 
This is the code for the distance sensor.
```python

import time
import board
import neopixel
import simpleio
import adafruit_hcsr04

sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D5, echo_pin=board.D6)  # setting up the sensor pins 
dot = neopixel.NeoPixel(board.NEOPIXEL, 1)

r=0  
g=0        # these are the start values of each color 
b=0

cm = 0
while True:    # helps run this loop forever
    try:
        cm = sonar.distance  # the distance number that sends back to the sensor in cm 
        print((cm))    # printing numbers in cm
        if cm < 5:    # the command funcation that if the distance vaule is less than 5cm it should be red
            r=255   # the vaules that we are staring with is red 
            g=0     # these are the values where one value start first while other ones are off
            b=0
            print("red!")   # it's gonna print red in serial monitor  
        elif cm < 20:         # if the distance is less then 20cm it should be 2 colors 
            print("red or blue!")  # the serial monitor that prints red or blue so we could see that it's less than 20cm
            r = simpleio.map_range(cm, 5, 20, 255, 0)  #Maps out the values of red that the led moves between
            g = 0        # green vaule is off because it's less than 20cm
            b = simpleio.map_range(cm, 5, 20, 0, 255)  #Maps out the values of blue that the led moves between


        elif cm < 35:   # if it's less then 35 
            print("blue or green!")  # the serial monitor should print blue or green so we know it's less than 35cm
            r = 0    # the red value is off because it's less than 35cm
            g = simpleio.map_range(cm, 20, 35, 0, 255)  #Maps out the values of green that the led moves between
            b = simpleio.map_range(cm, 20, 35, 255, 0)  #Maps out the values of blue that the led moves between

        else:             # otherwise 
            print("green") # it should be printing green
        dot.fill((int(r), int(g), int(b)))  # the color values integer that the led moves should be moving equaly

    except RuntimeError: # the error command that when something went wrong 
        print("Retrying!") # if something goes wrong print retrying 
    time.sleep(0.1)       # a reset before it repeats the loop 


```

[This is Dylan Herrada code link that I used for Distance Sensor assignment](https://github.com/adafruit/Adafruit_CircuitPython_HCSR04/blob/main/examples/hcsr04_simpletest.py)

[This was the Dylan Herrada long confusing code for distance sensor assignment](https://github.com/adafruit/Adafruit_CircuitPython_HCSR04/blob/main/adafruit_hcsr04.py)

[This is the hint link for distance sensor assignment thjat I used](https://docs.google.com/spreadsheets/d/e/2PACX-1vRzoIejkQqugrDoWHBw14qTI0HifXba92WiyQ24whEnzWcCUaCDYu6ifMQKK5O5Ilkxrd7UKIxPLBCW/pubhtml)

[This is the link for how to use simpleip for distance sensor assignment](https://circuitpython.readthedocs.io/projects/simpleio/en/latest/api.html#simpleio.map_range)


### Image/video
 The video credit goes to [Quinn](https://github.com/qragsda80/CircuitPython1) for helping me.

<img src="the distance sensor.gif" width="300">

<img src="https://github.com/msadat50/CircuitPython/blob/main/Pictures/Distance%20sensor%20picture.png?raw=true" width="400">


### Reflection
Doing this was hard for me in the beginning and confusing. There was a link to the assignment that would take you to this very long confusing code when I saw that code I didn't know which part of the code we should copy, so I just copied the whole code and put it in Mu. After that I didn't even know what to do so I used the hint to help me when I clicked on it there was all variable iut made it even more confusing. This time I asked Mr. H for help He helped me find the correct code and than explained it to me I understanded it better than it was easy and he did the first part of the code for me to understand it better. After that I knew what to do.


## CircuitPython_Photointerrupter

### Description & Code 
The purpose of this assignment was to get an photointerruper work that counts, which I achieved by using DigitalInOut library command. 
This is the code for the photointerrupter

```python

# Write your code here :-)
from digitalio import DigitalInOut, Direction, Pull
import time
import board

interrupter = DigitalInOut(board.D11)  # sets the digital number in the board 
interrupter.direction = Direction.INPUT  # sets up the input direction of the board 
interrupter.pull = Pull.UP  

counter = 0   

photo = False  # the false statement
state = False

max = 4  # the max time is 4
start = time.time()  # starting the time 
while True: # helps run this loop forever 

    now = time.monotonic()  # starts timing the monotonic

    photo = interrupter.value  # the photo interrupter value 
    if photo and not state:  # the photo interrupter if statement
            counter += 1  # add 1 to the counter statement vaule 
    state = photo

    remaining = max - time.time() # the remaining max time 

    if remaining <= 0:    #if the remaining is less than 0
        print("Interrupts:", str(counter))    # the serial monitor should print interrupts 
        max = time.time() + 4    # add 4 to the max time 
        counter = 0            # the counter statement drops down to zero
        
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
The purpose of this assignment was to print numbers using an LCD and 2 wires, which I achieved by using an LCD.  
This is the code for the LCD touch 

```python
import board
import time
from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface
import touchio

# get and i2c object
i2c = board.I2C()
# some LCDs are 0x3f... some are 0x27.
lcd = LCD(I2CPCF8574Interface(i2c, 0x3f), num_rows=2, num_cols=16)  # sets the board pins

touch_A0 = touchio.TouchIn(board.A0)   # the touch 1 wire pin in the board 
touch_A5 = touchio.TouchIn(board.A5)   # the touch 2 wire pin in the board 

counter = 0  # the counter statement 
lcd.print("Hello, Engineer!")   # when the wires are touched the serial monitor should print Hello Engineer
time.sleep(3)    # a reset before it repeats the loop 
lcd.clear()    # afte the reset the LCD is clear 

while True:   # helps run the loop forever  
    if touch_A0.value:  # giving the statement a command 
        counter += 1    # when touching the object the counter statement adds to the value
        lcd.set_cursor_pos(0, 0)  # setting up the cursor pos value 
        lcd.print(str(counter))  # printing the counter statement
        print(" Green wire touched ")  # the serial monitor will print Green wire touched 

    if touch_A5.value: 
        counter += 1   # when touching the object the counter statement adds to the value
        lcd.set_cursor_pos(1, 4) # setting up the cursor pos value 
        lcd.print(str(counter)) # printing the counter statement
        print(" Yellow wire touched ") # the serial monitor will print Yellow wire touched 
        
    else:
        counter = counter # counting the object vaule 
        time.sleep(0.1)  # a reset before it repeats the loop 
        
   ```     

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
The class code

```python

# These are the libraries needed to fade an LED, even if you imported elsewhere
import time
import pwmio

class RGB(object):

    full = 65535

class LED:
        # It's propper coding to always write a line explaining a class
        # with a "docstring."   Like this:
    '''LED is a class designed for a single color LED to fade in and out'''

    def __init__(self, ledpin):

        self.led = pwmio.PWMOut(ledpin, frequency=5000, duty_cycle=0)

        # init is like void Setup() from arduino.  Initialize your pins here
        # start each object with "self.object"

    def fade(self):
        for i in range(100):
            # PWM LED up and down
            if i < 50:
                self.led.duty_cycle = int(i * 2 * 65535 / 100)  # Up
            else:
                self.led.duty_cycle = 65535 - int((i - 50) * 2 * 65535 / 100)   # Down
            print(self.led.duty_cycle)
            time.sleep(0.03)

```

The main code

```python
''' This file is the class-based version of making a single LED fade'''
import time
import board
from rgb import LED   # import the LED class from the rgb module

blueLEDPin = board.D9
greenLEDPin = board.D8
redLEDPin = board.D10

myBlueLED = LED(blueLEDPin)
myGreenLED = LED(greenLEDPin)
myRedLED = LED(redLEDPin)

while True:
    myBlueLED.fade()
    time.sleep(1)
    myGreenLED.fade()
    time.sleep(1)
    myRedLED.fade()
    time.sleep(1)
    
```


### Evidence

### Images
<imag src="![RGB LED wiring](https://user-images.githubusercontent.com/71345399/157266888-ebdef9a3-3b08-41ae-a776-35457f1dee77.PNG)>"

### Reflection
