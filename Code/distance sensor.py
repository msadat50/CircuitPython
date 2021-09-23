# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

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