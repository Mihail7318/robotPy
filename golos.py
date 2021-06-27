import pyttsx3


def go(text):
    tts = pyttsx3.init()
    voices = tts.getProperty('voices')
    tts.setProperty('voice', 'ru')
    for voice in voices:

        if voice.name == 'Mandy':
            tts.setProperty('voice', voice.id)
    print(text)
    tts.say(text)

    tts.runAndWait()