from machine import Pin, I2C
from lib.ssd1306 import SSD1306_I2C
import time

# Opzetten I2C protocol op pinnen
oled_i2c = I2C(0, sda=Pin(8), scl=Pin(9))

# Check of via i2c een chip te vinden is
print(oled_i2c.scan())

# I2C configureren voor ssd1306 display
oled = SSD1306_I2C(width=128, height=32, i2c=oled_i2c, addr=0x3D)

# Print iets op het scherm
oled.fill(0)
oled.text('Hello', 0, 0, 0xffff)
oled.text('MicroPython!', 0, 10, 0xffff)
oled.hline(0, 20, 95, 0xffff)
oled.show()

time.sleep(2.)

teller = 0

while True:
    oled.fill(0)
    oled.text('Test program', 0, 0, 0xffff)
    oled.text(f'Teller = {teller}', 0, 10, 0xffff)
    oled.show()

    time.sleep(.5)

