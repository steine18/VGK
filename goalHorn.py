import simpleaudio as sa
from time import sleep
import time
from neopixel import *
from lights import *
from sys import argv

def play_song(song):
    wave_obj = sa.WaveObject.from_wave_file(song)
    play_obj = wave_obj.play()
    return play_obj

# Make a dictionary with song file locations, duration, and animation function?
songs = {'viva' : "/home/pi/python_projects/VGK/Music/Viva Las Vegas.wav",
         'start': "/home/pi/python_projects/VGK/Music/Le Castle Vania - John Wick Mode (John Wick Chapter 2 Club Scene Music) Official.wav",
         'goal' : "/home/pi/python_projects/VGK/Music/Vegas Golden Knights 2018 Playoffs Goal Horn"}


strip = Adafruit_NeoPixel(31, 12, 800000, 5, False)

def lights(strip, song):
    music = play_song(song)
    start = time.time()
    while time.time()-start < 30:
            alternate_zones(strip, range(16), Color(255,255,0), Color(0,255,0),2)
    music.stop()
    all_off(strip)

if __name__ == "__main__":
    strip = Adafruit_NeoPixel(31, 12, 800000, 5, False)
    strip.begin()
    song = play_song(songs[argv[1]])
    start = time.time()
    while time.time()-start <30:
        alternate_zones(strip, range(int(strip.numPixels()/2)), Color(69, 139, 19), Color(255,255,0),3)
    song.stop()
    all_off(strip)
