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