#Test para probar como se reproduce la canción.
from pygame import mixer  # Load the popular external library

mixer.init()
mixer.music.load('Ice Cream Cake.mp3')
mixer.music.play()

un_string = 'tuvieja.mp3'

print(un_string[-3:])