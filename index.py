import speech_recognition as sr
import os
import sys
import webbrowser




def talk(words):
    print(words)
    os.system('say ' + words)


def command():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('Жги уродец')
        r.pause_threshold = 2
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        task = r.recognize_google(audio, language='ru-RU').lower()  
        print('Из вашей дырки донеслось: {}'.format(task)) 
    except sr.UnknownValueError: 
        # talk('Глупый организм, скажи внятно')
        task = command()

    return task


def make_some(task):
    if 'проснись и пой' in task:
        talk('Привет кожанный ублюдок, чё тебе надо')

    elif 'открой google' in task:
        talk('Откываю жди какашка')
        url = 'https://google.com'
        webbrowser.open(url)
    elif 'открой яндекс' in task:
        talk('Откываю жди какашка')
        url = 'https://yandex.ru'
        webbrowser.open(url)

    elif 'включи музыку' in task:
        talk('понеслась жара, танцуйте организмы')
        url = 'https://www.youtube.com/watch?v=zzHouyi6t4g&list=RDJn8GQ-dLrWg&index=8'
        webbrowser.open(url)

    elif 'кто такая ира' in task:
        talk('Ты что дурак? это ваш главный женский человек')
    elif 'кто такая наташа' in task:
        talk('Наташка заведует вашей работой. С ней не шути кожанный дурачёк')
    elif 'кто такой серёжа' in task:
        talk('Ой зайбей вообще, чувак пишет на питоне. Прости серёга')
    elif 'кто такой виталик' in task:
        talk('Это наш бро. За бротана и двор стреляю в упор')
    elif 'кто такой ваня' in task:
        talk('Ваня монстр, он и ios и android')
    elif 'майкл тут' in task:
        talk('да знаю я! не пались делай вид что работаешь глупый организм')
    elif 'запускаю' in task:
        talk('кого ты там запускаешь какашка! успакойся')        
    elif 'убейся' in task:
        talk('Удаляюсь, кричи если что глупый организм')
        sys.exit()


while True:
    make_some(command())
