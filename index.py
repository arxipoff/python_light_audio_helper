import speech_recognition as sr
import os
import sys
import webbrowser

def talk (words):
    print(words)
    os.system('say ' + words)

talk('Привет кожанный ублюдок, чё тебе надо')


def command():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('Жги уродец')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try: 
        task = r.recognize_google(audio, language='ru-RU').lower()  
        print('Из вашей дырки донеслось: {}'.format(task)) 
    except sr.UnknownValueError: 
        talk('Глупый организм, скажи внятно') 
        task = command()

    return task


def makeSome(task):
    if 'открыть сайт' in task:
        talk('Откываю жди какашка')
        url = 'https://google.com'
        webbrowser.open(url)
    elif 'кто такая ира' in task:
        talk('Ты что дурак? это ваш главнй женский человек')
    elif 'кто такая наташа' in task:
        talk('Наташка заведует вашей работой. С ней не шути кожанный дурачёк')
    elif 'кто такой серёжа' in task:
        talk('Ой зайбей вообще, чувак пишет на питоне. Прости серёга')
    elif 'убейся' in task:
        talk('Удаляюсь, кричи если что глупый организм')
        sys.exit()


while True:
    makeSome(command())   