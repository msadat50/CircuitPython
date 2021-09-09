# Write your code here :-)
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
