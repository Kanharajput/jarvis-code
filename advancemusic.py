import random
from pygame import *
while True:

      songs=["kanha.wav","jogi.wav","river.wav","pehli.wav"]
      file=(random.choice(songs))
      mixer.init()
      mixer.music.load(file)
      mixer.music.play()
      while mixer.music.get_busy:
          time.Clock().tick(10)

