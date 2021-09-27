import time
import speech_recognition as sr
import pyttsx3
import threading
import sys
import re

#User's modules
import modules.logic.conversation.os.const as constant
import modules.logic.conversation.os.index as os_user

import os

import main

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
    request = rec.recognize_google(audio, language = 'ru-RU').lower()
    print(request)

    print("Converting Speech to Text...")
    if request == 'привет':
        speak("Приветствую, мастер. Я вас внимательно слушаю!")

    elif request == 'выключить систему':
        os_user.SYSTEM__OFF()

    elif 'создай директорию' in request:
        dir_name = re.sub('создай директорию ', '', request)
        speak(f"Создаю директорию с именем {dir_name}.")
        os_user.CREATE__DIR(dir_name)
    
    elif 'удали директорию' in request:
        dir_name = re.sub('удали директорию ', '', request)
        speak(f"Удаляю директорию с именем {dir_name}.")
        response = os_user.REMOVE__DIR(dir_name)
        speak(response)
    
    elif 'запусти браузер' in request:
        browser_name = re.sub('запусти браузер ', '', request)
        speak(f"Запускаю {browser_name}.")
        response = os_user.START__BROWSER(browser_name)
        speak(response)

    elif request == 'отключись':
        speak("Вас поняла. Отключаю все свои процессы.")
    # elif request == 'перезапуск': 
    #     os.startfile('__init__.py')
    else:
        speak("Запрос не понят. Пожалуйста, повторите ещё раз или перефразируйте.")

#Config

tts.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\TokenEnums\RHVoice\Victoria') 
tts.setProperty('rate', 220) 

rec = sr.Recognizer()

#Start
speak(f"Приветствую, мастер. Запуск всех систем. Рабочая директория: {constant.dir_path_core}")


while True:
    with mic as audio_file:
        rec.adjust_for_ambient_noise(audio_file)


        print("Пожалуйста, говорите.")
        audio = rec.listen(audio_file)

        try:
            callback(rec, audio)
        except sr.UnknownValueError:
            print(Exception)

                
# speech_thread = threading.Thread(target=speech)
# speech_thread.start()