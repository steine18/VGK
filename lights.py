import time
from neopixel import *

def all_color(strip, color):
    for p in range(strip.numPixels()):
        strip.setPixelColor(p, color)
    strip.show()
    
def all_off(strip):
    for p in range(strip.numPixels()):
        strip.setPixelColor(p, Color(0,0,0))
    strip.show()
    
def alternate_zones(strip, zone1, color1, color2, frequency):
    for p in range(strip.numPixels()):
        if p in zone1:
            strip.setPixelColor(p, color1)
        else:
            strip.setPixelColor(p, color2)
    strip.show()
    time.sleep(1/frequency)
    for p in range(strip.numPixels()):
        if p in zone1:
            strip.setPixelColor(p, color2)
        else:
            strip.setPixelColor(p, color1)
    strip.show()
    time.sleep(1/frequency)
