import speech_recognition as sr
import os
import sys
import webbrowser
import golos

def go():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        golos.go("Здраствуйте как вас зовут?")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
    try:
        zadanie = r.recognize_google(audio, language="ru-RU").lower()
        print("Вы сказали: " + zadanie)
    except sr.UnknownValueError:
        golos.go("Я вас не поняла")
    return zadanie

