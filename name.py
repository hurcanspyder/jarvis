import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes 


listener = sr.Recognizer()
engine = pyttsx3.init()
engine.say('iam your jarvis what can i do for you')
engine.runAndWait()


def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'jarvis' in command:
                command=command.replace('jarvis','')
                print(command)

    except:
        pass 
    return command 
    


def run_jarvis():
    command=take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play','')
        talk('playing'+song)
        pywhatkit.playonyt(song)

    
    elif 'time' in command:
        time=datetime.datetime.now().strftime('%H:%M')
        talk('current time is'+time)
        print(time)
    elif 'who the heck is' in command:
        person=command.replace('who the heck is','')
        info = wikipedia.summary(person,1)
        print(info)
        talk(info)
    elif ' date'  in command:
        talk('sorry i have a headache')
    elif 'i love you ' in command:
        talk('i love you to ')
    elif 'jokes' in command:
        talk(pyjokes.get_joke())
    
    else :
        talk('please say command again')






run_jarvis()


