import pyaudio
import speech_recognition as sr
import golos

def go():
    r = sr.Recognizer()
    r.energy_threshold=4000
    golos.go("Здраствуйте, как вас зовут?")
    with sr.Microphone(device_index = 2, sample_rate = 44100, chunk_size = 512) as source:
        print ("listening")
        audio = r.listen(source)
        print ("processing")

    try:
        message = (r.recognize_google(audio, language = 'ru', show_all=False))
        print(message)
    except:
        print("что то не так")
    return message