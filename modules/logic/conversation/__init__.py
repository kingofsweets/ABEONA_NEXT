import time
import speech_recognition as sr
import pyttsx3
import threading
import sys

tts = pyttsx3.init()

mic = sr.Microphone()

voices = tts.getProperty('voices')

# for voice in voices:

#     print('=======')

#     print('Имя: %s' % voice.name)

#     print('ID: %s' % voice.id)

#     print('Язык(и): %s' % voice.languages)

#     print('Пол: %s' % voice.gender)

#     print('Возраст: %s' % voice.age)

# print(sr.Microphone.list_microphone_names())

def speak(text):
    tts.say(text)
    tts.runAndWait()
    tts.stop()


def callback(rec, audio):
    print("Converting Speech to Text...")
    if rec.recognize_google(audio, language = 'ru-RU') == 'Привет':
        speak("Приветствую, мастер. Я вас внимательно слушаю!")
    if rec.recognize_google(audio, language = 'ru-RU').lower() == 'остановись':
        sys.exit()

#Config

tts.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\TokenEnums\RHVoice\Victoria') 
tts.setProperty('rate', 220) 

rec = sr.Recognizer()

#Start
speak("Я бы выбрал сломать колени. Зачем давать рыбу своему рабу? Достаточно просто поддерживать процессы жизнедеятельности в организме до тех пор, пока требуемая от него информация или другие блага не будут захвачены. Потом можно будет продать органы на черном рынке. По моим подсчётам в городе Таганрог имеется 5 точек для сбыта биоматериала человека.")


while True:
    with mic as audio_file:
        print("Пожалуйста, говорите.")
        rec.adjust_for_ambient_noise(audio_file)


        print("Пожалуйста, говорите.")
        audio = rec.listen(audio_file)
        callback(rec, audio)


                
# speech_thread = threading.Thread(target=speech)
# speech_thread.start()