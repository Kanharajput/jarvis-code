from pygame import *
mixer.init()
mixer.music.load("pehli.wav")
mixer.music.play()
while mixer.music.get_busy():
    time.Clock().tick(10)


