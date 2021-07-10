from gtts import *
import pygame, mutagen.mp3
import os

tts = gTTS('Доброго времени суток мои родные', lang='ru')

tts.save('tts_output.mp3')

mp3 = mutagen.mp3.MP3("tts_output.mp3")
pygame.mixer.init(frequency=mp3.info.sample_rate)
pygame.mixer.music.load("tts_output.mp3")
pygame.mixer.music.play()
while pygame.mixer.music.get_busy() == True:
     continue